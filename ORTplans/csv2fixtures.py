import csv
import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent


def read_csv_to_fixtures(file_path, model):
    # model = model.lower()
    try:
        with open(file_path, mode="r", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            fixtures = []
            for id, row in enumerate(reader):
                fields = {}
                for i, header in enumerate(headers):
                    fields[header] = row[i]
                fixture = {
                    "model": model,
                    "pk": id + 1,
                    "fields": fields,
                }
                fixtures.append(fixture)
            return fixtures
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
        return []
    except Exception as e:
        print(f"读取文件 {file_path} 时发生错误: {e}")
        return []


custcode_file = ROOT_DIR.joinpath("static/data/custcode.csv")
producttype_file = ROOT_DIR.joinpath("static/data/producttype.csv")

customer = read_csv_to_fixtures(custcode_file, "ORTplans.tcustcode")
producttype = read_csv_to_fixtures(producttype_file, "ORTplans.tproducttype")

if __name__ == "__main__":
    # print(customer)
    # print(producttype)
    with open(ROOT_DIR.joinpath("fixtures/customer.json"), "w", encoding="utf-8") as f:
        json.dump(customer, f, ensure_ascii=False, indent=4)
    with open(
        ROOT_DIR.joinpath("fixtures/producttype.json"), "w", encoding="utf-8"
    ) as f:
        json.dump(producttype, f, ensure_ascii=False, indent=4)
