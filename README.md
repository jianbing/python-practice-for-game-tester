python-practice-for-game-tester
---

不少游戏测试同学在初学了Python后，不知道如何过渡引用到工作当中，所以建立了这个项目，整理了和游戏测试有关的Python编程入门练习题。


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
