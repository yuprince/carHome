#小区车辆进出数据分析

* 目的：
通过分析小区车辆进出信息，得出分析结果。

1. 小区在xxx零时起至xxx二十四时止的小区车辆进出数据。
2. 进出的车辆总数为：
3. 地库车辆是否存在违停现象，个数为多少
4. 是否有车辆有异常行为：异常行为为与大多数业主作息相反，处于上班时间进入小区，下班时间离开小区，作为重点车辆进行分析
5. 利用进出方向，对车辆进行大致的abcd区划分
6. 分析车辆是否有大量长期不动用的问题
7. 分析车辆是否有非登记车辆过夜或存放时间超过6个小时以上的现象以及频次
8. 分析临时车辆存在时间对业主回家时间进行资源占用的冲突，如临时车辆5点前没有离开小区，而是在20点之后离开小区影响业主正常下班停车等现象的分析。

 #输入参数 "车牌号","进入时间","出门时间","出门地点","是否业主","是否地库车"

    # 车牌号carnumber
    # 进入时间in_time
    # 出门时间out_time
    # 进门时间in_time
    # 进门地点 in_door
    # 出门地点out_door
    # 是否业主if_master
    # 是否地库车if_under


#目前完成的模块

1. 判断进出门模块，是否地库车
2. 判断不是地库的车进入地库了
3. 判断地库车没有停进地库
4. 是否有车辆有异常行为：异常行为为与大多数业主作息相反，处于上班时间进入小区，下班时间离开小区，作为重点车辆进行分析
5. 是否为同一天进入小区
6. 是否为五点后进入小区
7. 是否为白天早6点至晚五点
8. 分析临时车辆存在时间对业主回家时间进行资源占用的冲突，如临时车辆5点前没有离开小区，而是在20点之后离开小区影响业主正常下班停车等现象的分析。

#需要完善修复的模块
1. 对所有车辆进行统计，掌握车辆在分析数据时间内的总数
2. 对分析数据车辆进出数据合并模块


#测试样例
        #主要获取 = "车牌号","进入时间","出门时间","进门地点","出门地点","是否业主","是否地库车"

        carnumber ="京XXXXXX"            
        in_time = "2019-03-26 08:42:26"
        out_time = "2019-04-28 21:42:26"
        in_door = "进门地点"
        out_door = "出门地点"
        if_master = 1 #1是业主，0不是业主
        if_under = 0 #1是地库车，0不是地库车
