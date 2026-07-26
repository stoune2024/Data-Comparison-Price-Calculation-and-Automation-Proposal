from pathlib import Path

import pandas as pd


class ExcelWriter:
    def write(
        self,
        dataframe: pd.DataFrame,
        output_path: str | Path,
    ) -> None:
        dataframe.to_excel(output_path, index=False)
