python-practice-for-game-tester
---

不少游戏测试同学在初学了Python后，不知道如何应用到工作当中，所以建立了这个项目，整理了一些和游戏测试有关的Python入门练习题作为过渡练习。


题目清单

- [GM指令模版解析](#GM指令模版解析)
- [命令行工具](#命令行工具)


## GM指令模版解析

`add_item item_id, num` 是一个增加道具的GM指令，如果我们想增加1001~1005这几个道具各10个，需要这么执行5次。

```
add_item 1001,10
add_item 1002,10
add_item 1003,10
add_item 1004,10
add_item 1005,10
```
为了提升效率，设计GM指令模版，需要满足以下几种形式


```
add_item {{1001 to 1005}},10
解析为：
add_item 1001,10
add_item 1002,10
add_item 1003,10
add_item 1004,10
add_item 1005,10

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

![bstest风格](https://github.com/jianbing/python-practice-for-game-tester/raw/master/img/cmdtool.png)