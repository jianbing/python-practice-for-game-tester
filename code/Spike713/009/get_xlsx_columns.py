import xlrd
import os

#得到某个表中所有列的数据
def get_xlsx_columns(path):
        work_book = xlrd.open_workbook(path)
        sheet_0 =  work_book.sheet_by_index(0)
        columns=[]
        #xlrd会把int 自动转成浮点，所以做了点特殊处理 ，不让它带小数点同时转成str方便后面的搜索
        for  i in range(sheet_0.ncols):
            column=[]
            for j in range(sheet_0.nrows):
                cell = sheet_0.cell(j,i)
                cell_value = cell.value
                if cell.ctype ==  2 and cell.value%1  ==0 :
                    cell_value=  str(int(cell_value))
                column.append(cell_value)
            columns.append(column)
        return columns


#得到配置表文件夹下所有的xlsx路径
def get_xlsx_path_list(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
             if os.path.splitext(file)[1] == '.xlsx':
                L.append(os.path.join(root, file))
    return L

#从阿拉伯数字的列数转换成 表格中的字母列数
#比如 0 行显示成A 行 ，26行显示成AA行
def num_2_column(num):
   m  =num//26
   r  =num%26
   if(m>=1): #超过了Z列
       left = chr(m+64)
       right = chr(r+65)
       return left+right
   else:     #没有超过Z列（A~Z)
       return chr(num+65)


if __name__ == '__main__':

    key = input("请输入要搜索的关键字:")
    file_dir = "E:\Common\Config"  #配置表所在位置
    #file_dir = "D:\configtest"
    xlsx_list = get_xlsx_path_list(file_dir)

    for xlsx  in xlsx_list:
        for index,column  in  enumerate(get_xlsx_columns(xlsx)):
            #print(column)
            if key in column:
                print("{0}  第{1}行 第{2}列".format(xlsx,column.index(key)+1,num_2_column(index)))