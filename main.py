import csv
import shutil
import pandas

all_car_num = 0
cal_unexpition_num = 0

# '''统计在场所有车辆'''未完成模块
def cal_all_car_num(carnumber):
    carlist = set()

    writePath = '车辆数据csv地址'
    readPath = '车辆数据csv地址'
    # carlist=open(readPath,'r',encoding='utf-8')
    f = open(readPath, 'r', encoding='utf-8')

    reader = csv.reader(f)
    carlist = next(reader)

    outfiile = open(writePath, 'a+', encoding='utf-8')
    #for carnumber in carlist:
    if carnumber not in carlist:
        all_car_num2 = all_car_num+1
        carlist.append(carnumber)
        outfiile.write(str(carlist))
    else:
        pass
    
    return all_car_num2
# '''x'''


#判断是否是出门还是入门 Done
def outorin(door):
    a = '入'
    b = '地库'
    if b in str(door):
        return 3#地库车
    elif a in str(door):    
        return 1#进入车
    else:
        return 0#出门车

#判断不是地库的车进入地库了 Done
def if_not_under_inside(carnumber,if_under,outorin):
    if if_under==0 & outorin==3:
        return 1,carnumber
    else:
        return 0,0

#判断地库车没有停进地库
def if_under_not_in(carnumber,if_under,outorin):
    if if_under==1 and outorin==1:
        return 1,carnumber
    else:
        return 0,0

#4. 是否有车辆有异常行为：异常行为为与大多数业主作息相反，处于上班时间进入小区，下班时间离开小区，作为重点车辆进行分析
def unexpition(carnumber,in_time,out_time):#done

    fenge=' '
    fenge2=':'
    date_time = in_time.partition(fenge)
    date_time_hour = date_time[2].partition(fenge2)
    date_time2 = out_time.partition(fenge)
    date_time_hour2 = date_time2[2].partition(fenge2) 
    
    if is_same_day(in_time,out_time)==1 and if_master==1 and int(date_time_hour[0])>=6 and int(date_time_hour2[0])<=11 :
            return 1,carnumber            
    else:
            return 0,0
        
#是否为同一天
def is_same_day(in_time,out_time):#done
    fenge=' '
    date_in_time = in_time.partition(fenge)
    date_out_time = out_time.partition(fenge)
    if date_in_time[0] == date_out_time[0]:
        return 1
    else:
        return 0

#是否为五点后
def is_after_17(in_time):#done
    fenge=' '
    fenge2=':'
    date_time = in_time.partition(fenge)
    date_time_hour = date_time[2].partition(fenge2) 
    if date_time_hour[0]>=17:#五点后
        return 1
    else:
        return 0 #五点前

#是否为白天早6点至晚五点 Done
def is_after6_before17(in_time):
    fenge=' '
    fenge2=':'
    date_time = in_time.partition(fenge)
    date_time_hour = date_time[2].partition(fenge2) 
    if int(date_time_hour[0])>=6:
        if int(date_time_hour[0])<=17:
            return 1
        else:
            return 0
    else:
        return 0 


#8. 分析临时车辆存在时间对业主回家时间进行资源占用的冲突，如临时车辆5点前没有离开小区，而是在20点之后离开小区影响业主正常下班停车等现象的分析。
def time_more_5_and_10(carnumber,in_time,out_time,if_master):
    fenge=' '
    fenge2=':'
    date_time = in_time.partition(fenge)
    date_time_hour = date_time[2].partition(fenge2)
    date_time2 = out_time.partition(fenge)
    date_time_hour2 = date_time2[2].partition(fenge2) 

    if if_master==0 and is_same_day(in_time,out_time)==1 and int(date_time_hour[0])<=17 and int(date_time_hour2[0])<=24:
        return 1,carnumber
    else:
        return 0,0




 # 车牌号carnumber
    # 进入时间in_time
    # 出门时间out_time
    # 进门时间in_door
    # 进门地点 in_door
    # 出门地点out_door
    # 是否业主if_master
    # 是否地库车if_under

#白天进晚上走
def if_not_master_for(carnumber,in_time,out_time,if_master):
    fenge=' '
    fenge2=':'
    date_time = in_time.partition(fenge)
    date_time_hour = date_time[2].partition(fenge2)
    date_time2 = out_time.partition(fenge)
    date_time_hour2 = date_time2[2].partition(fenge2) 
    #白天进晚上走
    if if_master ==0 and is_same_day(in_time,out_time)==1 and int(date_time_hour[0])>=6 and int(date_time_hour2[0])<=11:
        return 1,carnumber
    else:
        return 0,0

#非法过夜的
def not_master_during_night(carnumber,in_time,out_time,if_master):
    if if_master ==0 and is_same_day(in_time,out_time)==0:
        return 1,carnumber
    else:
        return 0,0

#访客时间是否过长
def if_vister_too_long(carnumber,in_time,out_time,if_master):
    fenge=' '
    fenge2=':'
    date_time = in_time.partition(fenge)
    date_time_hour = date_time[2].partition(fenge2)
    date_time2 = out_time.partition(fenge)
    date_time_hour2 = date_time2[2].partition(fenge2) 

    if if_master ==0 and is_same_day==1 and int(date_time_hour2[0])-int(date_time_hour[0])>=8:
        return 1,carnumber
    else:
        return 0,0


#停留时间,返回天数
def stay_days(carnumber,in_time,out_time):
    fenge=' '
    fenge2='-'
    date_time = in_time.partition(fenge)
    date_time2 = out_time.partition(fenge)

    moon_date = date_time[0].partition(fenge2)
    moon_date2 = date_time2[0].partition(fenge2)

    moon_date3 = moon_date[2].partition(fenge2)
    moon_date4 = moon_date2[2].partition(fenge2)

    if moon_date3[0]==moon_date4[0]:
        stay_day= int(moon_date4[2])-int(moon_date3[2])
        return 0,stay_day
    else:
        stay_day = int(moon_date4[2])+30-int(moon_date3[2])
        return 1,stay_day

#是否是僵尸车
def if_zoobie(carnumber,in_time,out_time):
    stay_day_temp = stay_days(carnumber,in_time,out_time)
    if int(stay_day_temp[1])>=7:
        return 1,carnumber
    else:
        return 0,0

with open("车辆数据csv地址", 'r') as f:
    # 创建阅读器对象
    reader=csv.reader(f)
    # 读取文件的第一行数据
    # head_row = reader.next()
    head_row=next(reader)
    # print(head_row)
    # car = [row[0] for row in reader]
    # print(car)
    cal = 0
    for row in reader:
        cal = cal+1

        #获取信息模块
        #主要获取"车牌号","进入时间","出门时间","出门地点","是否业主","是否地库车"
        carnumber=row[0]#车牌号
        time=row[1]
        door=row[2]#地点
        if outorin(door)==0:
            out_time = time#进出门时间
            in_time = 0
        else: 
            in_time = time
            out_time = 0
        if_master=row[3]#是否是业主
        if_under=row[4]#是否是地库权限
        

        #需要再加入一个对于进出门时间的整合
        #进门时间和出门时间能否凑成一对，有没有这一个月没有出来的车
        #'''开始进行函数工具分析'''
        #1 #出入状态，0出门车，1入门车，3地库车
        result_outorin = outorin(door)

        #2 #不是地库车是否进入地库
        result_not_under_inside = if_not_under_inside(carnumber,if_under,outorin(door))

        #3 #判断地库车没有停进地库
        result_under_not_in = if_under_not_in(carnumber,if_under,outorin(door))

        #4 #车辆异常行为，大概率为在小区上班的人
        result_unexpition = unexpition(carnumber,in_time,out_time)

        #5 #是否五点后还有临时车在
        result_time_more_5_and_10 = time_more_5_and_10(carnumber,in_time,out_time,if_master)

        #6 #不是业主白天进晚上走
        result_if_not_master_for = if_not_master_for(carnumber,in_time,out_time,if_master)

        #7 #不是业主非法过夜的
        result_not_master_during_night = not_master_during_night(carnumber,in_time,out_time,if_master)


    

        #print(if_not_under_inside(if_under,outorin(door)))
        #总车辆数
        # all_car_num=cal_all_car_num(carnumber)
        # print("最终车辆总数是")
        # print(all_car_num)
        # print(row)


        # print(in_time)
    #print(cal)
    print('all set')




# readPath='cnews.test1.txt'
# lines_seen=set()
# outfiile=open(writePath,'a+',encoding='utf-8')
# f=open(readPath,'r',encoding='utf-8')
# for line in f:
#     if line not in lines_seen:
#         outfiile.write(line)
#         lines_seen.add(line)
