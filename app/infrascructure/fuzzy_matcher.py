from rapidfuzz import fuzz

from app.domain.enums import MatchingStatus
from app.domain.matcher import ProductMatcher
from app.domain.models import (
    MarketplaceProduct,
    MatchedProduct,
    Product1C,
)

from app.infrascructure.utils import normalize


class FuzzyMatcher(ProductMatcher):

    MATCH_THRESHOLD = 95
    REVIEW_THRESHOLD = 85

    def match(
        self,
        product: Product1C,
        marketplace_products: list[MarketplaceProduct],
    ) -> MatchedProduct:

        if product.cost is None:
            return MatchedProduct(
                source=product,
                marketplace=None,
                status=MatchingStatus.NO_COST,
            )

        normalized_article = normalize(product.article)

        # 1. Поиск по артикулу
        for marketplace in marketplace_products:
            if normalize(marketplace.seller_article) == normalized_article:
                return MatchedProduct(
                    source=product,
                    marketplace=marketplace,
                    status=MatchingStatus.MATCHED,
                )

        # 2. Поиск по названию
        best_match = None
        best_score = 0

        for marketplace in marketplace_products:

            score = fuzz.token_sort_ratio(
                normalize(product.name),
                normalize(marketplace.name),
            )

            if score > best_score:
                best_score = score
                best_match = marketplace

        if best_match is None:
            return MatchedProduct(
                source=product,
                marketplace=None,
                status=MatchingStatus.NOT_FOUND,
            )

        if best_score >= self.MATCH_THRESHOLD:
            status = MatchingStatus.MATCHED
        elif best_score >= self.REVIEW_THRESHOLD:
            status = MatchingStatus.MANUAL_REVIEW
        else:
            status = MatchingStatus.NOT_FOUND
            best_match = None

        return MatchedProduct(
            source=product,
            marketplace=best_match,
            status=status,
        )