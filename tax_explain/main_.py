import pandas as pd
from mailmerge import MailMerge
from docx import Document

# 将df中一行数据，填入模板中说明部分的MergeField中
def merge_explanation(row):
    keys = ['Name', 'ID', 'Product', 'Amount', 'Count']
    kwargs = {key:row[key] for key in keys}             
    document.merge(**kwargs)

# 将明细数据填入模板表格中
def merge_detail(data):
    data = data.to_dict(orient='records')
    document.merge_rows('LoanID', data)

# 合并第y列，从x行开始的n行单元格
def merge_cell_lines(tb, n, x, y):
    start = tb.cell(x, y)
    end = tb.cell(x+n-1, y)

    # 记录第一行内容，合并后写入该内容
    text = start.text
    start.merge(end)
    start.text = text

# 合并单元格
def merge_cell(file_name, data):
    # 用python-docx重新打开文件，读取表格
    doc = Document(file_name)
    tb = doc.tables[0]

    # 根据data行数，合并n行姓名为一行
    n = len(data)
    merge_cell_lines(tb, n, x=1, y=0) # type: ignore

    # 合并借据号单元格，从第1行始，n行合并一次
    x = 1
    for n in data['LoanID'].value_counts():
        merge_cell_lines(tb, n, x=x, y=1)
        x += n
    
    # 保存
    doc.save(file_name)


if __name__ == '__main__':
    # 读入data.xlsx, detail.xlsx
    df = pd.read_excel('data.xlsx', dtype=str)
    detail = pd.read_excel('details.xlsx', dtype=str)


    # 遍历df中每行数据
    for index, row in df.iterrows():
        # 打开word模板template.docx
        document = MailMerge('template.docx')

        # 根据ID\Product，查得对应明细数据，drop多余列
        data = detail[(detail.ID==row.ID)&(detail.Product==row.Product)].drop(['ID', 'Product'], axis=1)

        # 填写模板中说明信息
        merge_explanation(row)

        # 填写模板中明细表格
        merge_detail(data)

        # 保存文件并关闭
        file_name = f"output\\手工开票情况说明_{row.Name}_{row.Product}.docx"
        document.write(file_name)
        document.close()

        # 重新打开word文件，进行单元格合并
        merge_cell(file_name, data)