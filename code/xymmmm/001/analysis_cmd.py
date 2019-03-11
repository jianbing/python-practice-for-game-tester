#! /usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created by Administrator on 2019-03-11
"""


def analysis_cmd(s):

    cmdlist = []
    cmd_name = s[:s.rfind("{{")]
    num = s.split("}}")[-1]
    if s.find("not") > -1:
        item_id = s[s.rfind("{{")+2:s.rfind(" not")].split(' to ')
        item_id = list(map(int, item_id))
        not_id = s[s.rfind("not ")+4:s.rfind("}}")].split(',')
        not_id = list(map(int, not_id))

        for i in range(int(item_id[0]), int(item_id[-1])+1):
            if i in not_id:
                continue
            cmd = cmd_name + str(i) + num
            cmdlist.append(cmd)

    elif s.find("to") > -1:
        item_id = s[s.rfind("{{")+2:s.rfind("}}")].split(' to ')
        item_id = list(map(int, item_id))
        for i in range(int(item_id[0]), int(item_id[-1])+1):
            cmd = cmd_name + str(i) + num
            cmdlist.append(cmd)

    else:
        item_id = s[s.rfind("{{")+2:s.rfind("}}")].split(",")
        item_id = list(map(int, item_id))
        for i in item_id:
            cmd = cmd_name + str(i) + num
            cmdlist.append(cmd)

    return cmdlist


if __name__ == '__main__':
    print(analysis_cmd('add_item {{1001 to 1010 not 1002,1006,1004}},10'))
