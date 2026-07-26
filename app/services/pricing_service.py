import math

from app.domain.enums import MatchingStatus
from app.domain.models import MatchedProduct
from app.domain.pricing import PricingCalculator


class PricingService(PricingCalculator):
    def calculate(self, product: MatchedProduct) -> float | None:

        if product.status != MatchingStatus.MATCHED:
            return None

        marketplace = product.marketplace

        if (
            product.source.cost is None
            or marketplace is None
            or marketplace.commission is None
            or marketplace.handling is None
            or marketplace.logistics_min is None
            or marketplace.delivery is None
        ):
            return None

        cost = product.source.cost

        commission = marketplace.commission / 100

        expenses = (
            marketplace.handling + marketplace.logistics_min + marketplace.delivery
        )

        denominator = 1 - commission

        if denominator <= 0:
            return None

        price = (1.3 * cost + expenses) / denominator

        return math.ceil(price)
