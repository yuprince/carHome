import csv
import shutil
import pandas
import copy

with open("车辆数据csv地址", 'r') as f,open ("车辆数据csv地址", 'r') as g:
    # 创建阅读器对象
    reader=csv.reader(f)
    reader2=csv.reader(g)
    #scopy.copy(reader)
    # for head_row in reader:
    #     print(head_row)
    csvFile = open("车辆数据csv地址", "w")
    writer = csv.writer(csvFile)
    fileHeader = ["车牌号","进入时间","出门时间","进入地点","出门地点","是否业主","是否地库"]

    #head_row2=next(reader2)

    # 读取文件的第一行数据
    # head_row = reader.next()
    for head_row in reader:
        carnumber = head_row[0]
        for head_row2 in reader2:
            #head_row=next(reader)
            carnumber2 = head_row2[0]
            if carnumber == head_row2[0]:
                print(head_row2)
                print(head_row)
                #print(list(set(head_row).union(set(head_row2))))
                result = [head_row[0],head_row2[1],head_row[1],head_row2[2],head_row[2],head_row[3],head_row[4]]
                writer.writerows([fileHeader,result])
                #writer.writerows(result)
                print(result)
                break

    

    # car = [row[0] for row in reader]
    # print(car)
#     cal = 0
#     for row in reader:
#         cal = cal+1
# print list(set(a).union(set(b)))
