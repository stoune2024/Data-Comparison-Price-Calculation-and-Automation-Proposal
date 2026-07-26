from pathlib import Path

import pandas as pd

from app.domain.models import MarketplaceProduct, Product1C


class ExcelReader:
    def __init__(self, file_path: str | Path):
        self._file_path = Path(file_path)

    @staticmethod
    def _to_float(value) -> float | None:
        if pd.isna(value):
            return None

        if isinstance(value, str):
            value = value.replace("%", "").replace(",", ".").strip()

            if value == "":
                return None

        return float(value)

    def read_products_1c(self) -> list[Product1C]:
        df = pd.read_excel(
            self._file_path,
            sheet_name="Данные из 1С",
        )

        products = []

        for _, row in df.iterrows():
            products.append(
                Product1C(
                    article=str(row["Артикул 1С"]).strip(),
                    name=str(row["Наименование"]).strip(),
                    cost=self._to_float(row["Себестоимость"]),
                )
            )

        return products

    def read_marketplace_products(self) -> list[MarketplaceProduct]:

        df = pd.read_excel(
            self._file_path,
            sheet_name="Данные с маркетплейса",
        )

        products = []

        for _, row in df.iterrows():
            products.append(
                MarketplaceProduct(
                    seller_article=str(row["Артикул продавца"]).strip(),
                    sku=str(row["SKU"]).strip(),
                    name=str(row["Название товара"]).strip(),
                    commission=self._to_float(row["Комиссия маркетплейса"]),
                    handling=self._to_float(row["Обработка нестандартного товара"]),
                    logistics_min=self._to_float(
                        row["Минимальная стоимость логистики"]
                    ),
                    logistics_max=self._to_float(
                        row["Максимальная стоимость логистики"]
                    ),
                    delivery=self._to_float(row["Доставка до места выдачи"]),
                )
            )

        return products
