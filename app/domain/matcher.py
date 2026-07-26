from abc import ABC, abstractmethod

from app.domain.models import (
    MarketplaceProduct,
    MatchedProduct,
    Product1C,
)


class ProductMatcher(ABC):
    @abstractmethod
    def match(
        self,
        product: Product1C,
        marketplace_products: list[MarketplaceProduct],
    ) -> MatchedProduct: ...
