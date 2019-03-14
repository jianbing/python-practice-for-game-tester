#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re


def normal_parse(gm_order: str):
    """ 普通指令解析
    :param gm_order:
    :return:
    """
    order_parse = re.compile('(.*){{(.*)}},(.*)')
    gm_oder_name, gm_oder_id_list, gm_order_num = order_parse.findall(gm_order)[0]
    for gm_oder_id in gm_oder_id_list.split(','):
        print(gm_oder_name + ' ' + gm_oder_id + ',' + gm_order_num)


def has_to_parse(gm_order: str):
    """ 包含to的gm指令的解析
    :param gm_order:
    :return:
    """
    order_parse = re.compile('(.*){{(.*)}},(.*)')
    gm_oder_name, gm_oder_id_list, gm_order_num = order_parse.findall(gm_order)[0]
    first_num, last_num = gm_oder_id_list.strip().split('to')
    for gm_oder_id in range(int(first_num), int(last_num) + 1):
        print(gm_oder_name + ' ' + str(gm_oder_id) + ',' + gm_order_num)


def has_not_to_parse(gm_order: str):
    """ 包含not to的gm指令的解析
    :param gm_order:
    :return:
    """
    order_parse = re.compile('(.*){{(.*) not (.*)}},(.*)')
    gm_oder_name, gm_oder_id_list, filter_id, gm_order_num = order_parse.findall(gm_order)[0]
    first_num, last_num = gm_oder_id_list.strip().split('to')
    order_id_list = set(range(int(first_num), int(last_num) + 1))-set([int(i) for i in filter_id.split(',')])
    for gm_oder_id in order_id_list:
        print(gm_oder_name + ' ' + str(gm_oder_id) + ',' + gm_order_num)


if __name__ == '__main__':
    normal_str = r'add_item {{1001,1003,1006}},10'
    has_to_str = r'add_item {{1001 to 1003}},10'
    has_not_to_str = r'add_item {{1001 to 1005 not 1002,1003}},10'
    normal_parse(normal_str)
    has_to_parse(has_to_str)
    has_not_to_parse(has_not_to_str)
