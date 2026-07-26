from abc import ABC, abstractmethod

from app.domain.models import MatchedProduct


class PricingCalculator(ABC):
    @abstractmethod
    def calculate(self, product: MatchedProduct) -> float | None: ...
