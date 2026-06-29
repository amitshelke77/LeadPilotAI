from pathlib import Path
import pandas as pd


EXPORT_FOLDER = Path("exports")
EXPORT_FOLDER.mkdir(exist_ok=True)


def export_to_excel(df: pd.DataFrame, filename: str = "companies.xlsx"):
    filepath = EXPORT_FOLDER / filename
    df.to_excel(filepath, index=False)
    return filepath