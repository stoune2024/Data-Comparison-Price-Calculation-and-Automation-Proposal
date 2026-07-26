from pathlib import Path

import pandas as pd

from app.domain.models import MatchedProduct


class ExcelWriter:
    def write(
        self,
        products: list[MatchedProduct],
        output_path: str | Path,
    ) -> None:

        rows = []

        for product in products:
            marketplace = product.marketplace

            rows.append(
                {
                    "Артикул 1С": product.source.article,
                    "Наименование": product.source.name,
                    "Себестоимость": product.source.cost,
                    "Артикул продавца": marketplace.seller_article
                    if marketplace
                    else None,
                    "SKU": marketplace.sku if marketplace else None,
                    "Название товара": marketplace.name if marketplace else None,
                    "Комиссия": marketplace.commission if marketplace else None,
                    "Обработка": marketplace.handling if marketplace else None,
                    "Мин. логистика": marketplace.logistics_min
                    if marketplace
                    else None,
                    "Макс. логистика": marketplace.logistics_max
                    if marketplace
                    else None,
                    "Доставка": marketplace.delivery if marketplace else None,
                    "Статус": product.status,
                    "Минимальная цена": product.min_price,
                }
            )

        df = pd.DataFrame(rows)

        df.to_excel(output_path, index=False)
