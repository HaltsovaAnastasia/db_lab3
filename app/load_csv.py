from pathlib import Path
import pandas as pd


def main():
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "GlobalWeatherRepository.csv"

    print(f"Looking for csv file: {csv_path}")

    if not csv_path.exists():
        print(f"File wasn't found': {csv_path}")
        return

    df = pd.read_csv(csv_path)

    print("CSV uploaded.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    print("\Names of columns:")
    for column in df.columns:
        print(f"- {column}")

    print("\First 5:")
    print(df.head())


if __name__ == "__main__":
    main()
