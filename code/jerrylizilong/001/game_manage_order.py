import re

def re_tempalte(key,p1):
    """
    使用正则表达式，获取对应文本
    :param key:
    :param p1:
    :return:
    """
    pattern1 = re.compile(p1)#我们在编译这段正则表达式
    matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
    return matcher1.group(0)#打印出来

def read_para_from_gmorder(gm_order):
    """
    解析原始 gm 指令
    :param gm_order:
    :return: ['add_item ', '1001,1003,1006', ',10']
    """
    key = gm_order
    return [re_tempalte(key,r"\w.+? "), re_tempalte(key,r"{{.+}}").replace("{{","").replace("}}",""), re_tempalte(key,r",.+?\w")]

def get_item_list(item_template):
    """
    解析参数模板。 根据三种格式进行拆分
    :param item_template:
    :return: 实际的道具列表，例如： 1001,1003,1006
    """

    item_list = []
    if 'to' in item_template:
        start, end =int(item_template.split(" to ")[0]),int(item_template.split(" to ")[1].split(" not ")[0])
        not_list = []
        if 'not' in item_template:
            not_list = item_template.split(" to ")[1].split(" not ")[1].split(",")
        # print(start,end)
        if start>end:
            print('error! %d > %d' %(start,end))
        else:
            for i in range(end-start+1):
                if str(start+i) not in not_list:
                    item_list.append(str(start+i))
    else:
        item_list=item_template.split(',')
    return item_list

def generate_order_list(gm_order):
    """
    返回实际的道具指令列表
    :param gm_order:
    :return: ['add_item 1001,10', 'add_item 1003,10', 'add_item 1006,10']
    """
    paras = read_para_from_gmorder(gm_order)
    # print(paras)
    item_list = get_item_list(paras[1])
    gm_order_list = []
    if len(item_list):
        for item in item_list:
            # print(item)
            gm_order_list.append(paras[0]+item+paras[2])
    return gm_order_list

if __name__ == "__main__":
    gm_order = r"add_item {{1001 to 1003}},10"
    print("input %s, \nreturn %s" %(gm_order,generate_order_list(gm_order)))
    print("input %s, \return %s" %(gm_order,generate_order_list(gm_order)))
    print(gm_order, generate_order_list(gm_order))
    print("input %s, \return %s" %(gm_order,generate_order_list(gm_order)))
    print(gm_order, generate_order_list(gm_order))