python-practice-for-game-tester
---

不少游戏测试同学在初学了Python，掌握了基础的语法后，不知道如何应用到工作当中，所以建立了这个项目，整理了一些和游戏测试有关的Python入门练习题作为过渡练习。

> 题库完善后，会开放提交答案到本仓库~



题目清单

- [GM指令模版解析](#GM指令模版解析)
- [命令行工具](#命令行工具)
- [安卓APK安装器](#安卓APK安装器)
- [安卓CPU，内存监控工具](#安卓CPU，内存监控工具)
- [安卓截图工具](#安卓截图工具)
- [PC游戏客户端Monkey测试工具](#PC游戏客户端Monkey测试工具)
- [生成奖励配置](#生成奖励配置)
- [Excel配置表检查工具](#Excel配置表检查工具)
- [配置表关键字搜索](#配置表关键字搜索)
- [内网APK包下载网页](#内网APK包下载网页)

> 建议使用Py3.6以上版本，IDE推荐Pycharm

## GM指令模版解析

`add_item item_id, num` 是一个增加道具的GM指令，如果我们想增加1001~1003这几个道具各10个，需要这么执行3次，如果要加大量的道具，那执行的次数就更多了

```
add_item 1001,10
add_item 1002,10
add_item 1003,10
```
为了提升效率，设计GM指令模版，需要满足以下几种形式

```
add_item {{1001 to 1003}},10
解析为：
add_item 1001,10
add_item 1002,10
add_item 1003,10

add_item {{1001,1003,1006}},10
解析为：
add_item 1001,10
add_item 1003,10
add_item 1006,10

add_item {{1001 to 1005 not 1002,1003}},10
解析为：
add_item 1001,10
add_item 1004,10
add_item 1005,10
```

## 命令行工具

制作一个命令行工具，将常见的工作辅助脚本整合起来，需要包括的功能有

- SVN更新指定目录
- SVN还原指定目录
- 启动游戏客户端
- 打开指定文件夹

参考界面效果，使用prettytable库

![](https://github.com/jianbing/python-practice-for-game-tester/raw/master/img/cmdtool.png)

## 安卓APK安装器

遍历文件夹，获取全部的APK文件，依次调用`adb install`命令安装到测试机中

```
遍历可以使用 os.walk 函数
```


## 安卓CPU，内存监控工具

通过adb命令，获取APP的CPU和内存占用，使用[pyecharts](https://github.com/pyecharts/pyecharts)库，生成测试结果图表

```
获取内存占用：
adb shell dumpsys meminfo package_name

获取CPU占用：
adb shell cat /proc/pid/stat
```

## 安卓截图工具

通过adb，对当前安卓界面进行截图，需要支持 `adb screencap` 和 minicap 两个方式，截图后导出截图文件到指定文件夹

> [minicap](https://github.com/openstf/minicap)是STF的一个工具，截图速度是screencap方式的几十倍，官方定义是：Stream real-time screen capture data out of Android devices。

## PC游戏客户端Monkey测试工具

制作一个PC游戏游戏客户端可用的Monkey测试工具，功能上模拟adb monkey，支持单击，双击，长按，拖动等操作，可配置各操作的百分比

```
可以试试 PyAutoGUI 这个库
```

## 生成奖励配置

编写一个脚本，读取下图的[奖励配置Excel文件](https://github.com/jianbing/python-practice-for-game-tester/tree/master/res/生成奖励配置)

![](https://github.com/jianbing/python-practice-for-game-tester/raw/master/img/excel.png)

解析为下边的Lua格式，`reward_type`固定为`REWARD_TYPE_ITEM`，并保存到`reward.lua`文件中 

```
{
    [1] = {
      [1] = {reward_type = REWARD_TYPE_ITEM, item_type = 2001, item_count = 80,},
      [2] = {reward_type = REWARD_TYPE_ITEM, item_type = 2004, item_count = 80,},
      [3] = {reward_type = REWARD_TYPE_ITEM, item_type = 3001, item_count = 25,},
      [4] = {reward_type = REWARD_TYPE_ITEM, item_type = 6101, item_count = 11,},
    },
    [2] = {
      [1] = {reward_type = REWARD_TYPE_ITEM, item_type = 2001, item_count = 70,},
      [2] = {reward_type = REWARD_TYPE_ITEM, item_type = 2004, item_count = 70,},
      [3] = {reward_type = REWARD_TYPE_ITEM, item_type = 3002, item_count = 20,},
    },
    [3] = {
      [1] = {reward_type = REWARD_TYPE_ITEM, item_type = 2001, item_count = 60,},
      [2] = {reward_type = REWARD_TYPE_ITEM, item_type = 2004, item_count = 60,},
      [3] = {reward_type = REWARD_TYPE_ITEM, item_type = 3003, item_count = 15,},
      [4] = {reward_type = REWARD_TYPE_ITEM, item_type = 6103, item_count = 13,},
    },
}
```

## Excel配置表检查工具

读取策划配置的Excel数值表，检查是否有配置错误，支持以下检查方式

- id列是否存在重复的id，如两个2001的id
- id列是否连续，不存在如 1，2，3，4，4，6这样的错误
- Lua数据列是否存在中文标底符号，如"，"
- Lua数据列是否存在不成对的 {} ，如 `{{reward_type = REWARD_TYPE_ITEM, item_type = 2001, item_count = 80}`

## 配置表关键字搜索

根据输入的关键字，在配置表目录下进行遍历，讲包含该关键字的配置表路径，关键字所在行数，及附近几行的内容打印出来，支持`xml,lua,json`等文本格式即可

```
应用场景

策划：我把配置表里边的XXX道具全删了，你看看有没有漏的
测试：噢，我跑下脚本
```

## 内网APK包下载网页

制作一个网页，网页会展示已经上传到网页目录下的APK文件，包括文件名字，文件大小，修改日期，下载二维码，使用手机扫描该二维码，会触发下载。

```
网页可以基于Flask框架运行，二维码生成可以使用qrcode库
```