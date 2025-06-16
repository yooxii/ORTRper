import csv
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent


def read_csv_to_unique_tuples(file_path):
    try:
        with open(file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip headers
            seen = set()
            unique_data = []
            for i, row in enumerate(reader):
                if row[1] not in seen:
                    seen.add(row[1])
                    unique_data.append((i, row[1]))
            unique_data.insert(0, (0, "NA"))  # Insert (0, "NA") at the beginning
            return tuple(unique_data)
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
        return ()
    except Exception as e:
        print(f"读取文件 {file_path} 时发生错误: {e}")
        return ()


custcode_file = ROOT_DIR.joinpath("static/data/custcode.csv")
producttype_file = ROOT_DIR.joinpath("static/data/producttype.csv")

customer = read_csv_to_unique_tuples(custcode_file)
producttype = read_csv_to_unique_tuples(producttype_file)

if __name__ == "__main__":
    print(customer)
    print(producttype)
