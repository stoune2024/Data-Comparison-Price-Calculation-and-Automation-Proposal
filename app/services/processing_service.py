from pathlib import Path

from app.domain.matcher import ProductMatcher
from app.domain.models import MatchedProduct
from app.domain.pricing import PricingCalculator
from app.infrascructure.excel_reader import ExcelReader
from app.infrascructure.excel_writer import ExcelWriter


class ProcessingService:
    def __init__(
        self,
        writer: ExcelWriter,
        matcher: ProductMatcher,
        pricing: PricingCalculator,
    ):
        self._writer = writer
        self._matcher = matcher
        self._pricing = pricing

    def process(self, input_path: str | Path, output_path: str | Path) -> None:
        reader = ExcelReader(input_path)

        products_1c = reader.read_products_1c()

        marketplace_products = reader.read_marketplace_products()

        result: list[MatchedProduct] = []

        for product in products_1c:
            matched = self._matcher.match(
                product,
                marketplace_products,
            )

            matched.min_price = self._pricing.calculate(
                matched,
            )

            result.append(matched)

        self._writer.write(
            products=result,
            output_path=output_path,
        )
