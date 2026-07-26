from dataclasses import dataclass


@dataclass(slots=True)
class Product1C:
    article: str
    name: str
    cost: float | None


from dataclasses import dataclass


@dataclass(slots=True)
class MarketplaceProduct:
    seller_article: str
    sku: str
    name: str

    commission: float

    handling: float

    logistics_min: float
    logistics_max: float

    delivery: float


from dataclasses import dataclass

from app.domain.enums import MatchingStatus


@dataclass(slots=True)
class MatchedProduct:
    source: Product1C

    marketplace: MarketplaceProduct | None

    status: MatchingStatus

    min_price: float | None = None
