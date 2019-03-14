#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re


def gm_order_parse(gm_order: str):
    """ GM指令解析
    :param gm_order:
    :return:
    """
    order_parse = re.compile('(.*){{(.*)}},(.*)')
    gm_oder_name, gm_oder_id_str, gm_order_num = order_parse.findall(gm_order)[0]
    if "to" in gm_oder_id_str:
        if "not" in gm_oder_id_str:
            first_num, last_num, filter_id = re.split('to|not', gm_oder_id_str)
            gm_order_list = set(range(int(first_num), int(last_num) + 1)) - set([int(i) for i in filter_id.split(',')])
        else:
            first_num, last_num = gm_oder_id_str.strip().split('to')
            gm_order_list = list(range(int(first_num), int(last_num) + 1))
    else:
        gm_order_list = gm_oder_id_str.split(',')
    for gm_oder_id in gm_order_list:
        print(gm_oder_name + ' ' + str(gm_oder_id) + ',' + gm_order_num)


if __name__ == '__main__':
    normal_str = r'add_item {{1001,1003,1006}},10'
    has_to_str = r'add_item {{1001 to 1003}},10'
    has_not_to_str = r'add_item {{1001 to 1005 not 1002,1003}},10'
    gm_order_parse(has_to_str)
