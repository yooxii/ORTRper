import win32com.client as win32
import openpyxl as xl
import os
import shutil

STANDARD_TEMPLATE_DIR = ".\\DataFiles\\report_templates\\# ORT Test Report (WK#)_#"
ORTPLAN_DIR = ".\\DataFiles\\ORTplans"
TEMP_DIR = ".\\DataFiles\\Temp"


def convert_to_xlsx(file_path):
    """
    将xls文件转换为xlsx格式
    """
    if file_path.endswith(".xls"):
        # 启动Excel应用程序
        excel = win32.gencache.EnsureDispatch("Excel.Application")
        excel.Visible = False

        try:
            # 打开xls文件
            wb = excel.Workbooks.Open(file_path)
            # 生成新的xlsx文件路径
            xlsx_path = file_path.replace(".xls", ".xlsx")
            # 保存为xlsx格式
            wb.SaveAs(xlsx_path, FileFormat=51)  # 51代表xlsx格式
            wb.Close()
            return xlsx_path
        except Exception as e:
            print(f"转换文件时出错: {e}")
            return None
        finally:
            excel.Quit()
    elif file_path.endswith(".xlsx"):
        return file_path
    else:
        return None


def extract_ortplan(file_path: str):
    """
    处理模板文件：提取 ORT Plan 表格。
    """
    if not file_path.endswith(".xlsx"):  # 仅处理xlsx文件
        return None, None
    wb = xl.load_workbook(file_path)
    sheetnames = wb.sheetnames
    if "ORT Plan" in sheetnames:
        sheetnames.remove("ORT Plan")
    else:
        return None, None

    for st in sheetnames:
        wb.remove(wb[st])

    file_name = file_path.split("\\")[-1]
    uut_name = file_name.split(" ")[0]
    date = file_name[file_name.find("WK") : -6]
    save_path = os.path.join(ORTPLAN_DIR, f"{uut_name}_{date}.xlsx")
    wb.save(save_path)
    return save_path, wb[wb.sheetnames[0]]


def make_template(file_path: str):
    import json

    if not file_path.endswith(".xlsx"):  # 仅处理xlsx文件
        return None
    plan_path, st_plan = extract_ortplan(file_path)
    wb = xl.load_workbook(
        os.path.join(STANDARD_TEMPLATE_DIR, "# ORT Test Report(WK#).xlsx")
    )

    with open(os.path.join(STANDARD_TEMPLATE_DIR, "setup_info.json"), "r") as json_file:
        info = json.loads(json_file.read())
    print(info)


def process_directory(source_dir, target_dir):
    """
    处理目录，并将处理完成的文件保存到目标目录下
    """

    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

    source_name = source_dir.split("\\")[-1]  # 源文件夹名称
    # 确保目标目录存在
    if not os.path.exists(os.path.join(target_dir, source_name)):
        os.makedirs(os.path.join(target_dir, source_name))

    # 遍历目标目录
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)
        source_path = os.path.abspath(source_path)

        if filename.endswith(".xls") or filename.endswith(".xlsx"):
            xlsx_path = convert_to_xlsx(source_path)
            report_path = make_template(xlsx_path)
            break


def main():
    """
    主函数：制作模板文件夹
    """
    # 设置源目录和目标目录
    source_directory = input("请输入源文件夹路径: ")
    target_directory = input("请输入目标模板文件夹路径: ")

    if not os.path.exists(source_directory):
        print("源文件夹不存在!")
        return

    # 处理目录中的文件
    process_directory(source_directory, target_directory)
    print("模板制作完成!")


if __name__ == "__main__":
    main()
