a = '''访问日志
状态码
4xx
400
499
5xx
502
504
503
不均衡
rt
请求时间长
timeout
健康检查
up
down
不通
丢包
重传
超时
解析
mtr
dig
ping
tcpping
抓包
rst
reset
tcp
udp
长连接
短连接
ipv6
跨境
网络
抖动
ip
telnet
时间
timeout
不通
中断
丢包
重传
超时
解析
mtr
dig
ping
tcpping
抓包
rst
reset
tcp
udp
路由
全连接
半连接
iptables
安全组
mtu
mss
ip
域名
dns
网络
ecs
slb
'''
# print(','.join(a.split('\n')))

b = "访问日志,状态码,4xx,400,499,5xx,502,504,503,不均衡,rt,请求时间长,timeout,健康检查,up,down,不通,丢包,重传,超时,解析,mtr,dig,ping,tcpping,抓包,rst,reset,tcp,udp,长连接,短连接,ipv6,跨境,网络,抖动,ip,telnet,时间,timeout,不通,中断,丢包,重传,超时,解析,mtr,dig,ping,tcpping,抓包,rst,reset,tcp,udp,路由,全连接,半连接,iptables,安全组,mtu,mss,ip,域名,dns,网络,ecs,slb,日志,rt,时间,timeout,不通,丢包,重传,超时,解析,mtr,dig,ping,tcpping,抓包,rst,reset,tcp,udp,长连接,短连接,ipv6,跨境,网络,抖动,ip,telnet,中断,协商,vpn"
# print(','.join(list(set(b.split(',')))))




import csv
import json
import codecs
import re


# class Json_Csv():
#
#     # 初始化方法，创建csv文件。
#     def __init__(self, name):
#         self.save_csv = open(name, 'w', encoding='utf-8', newline='')
#         self.write_csv = csv.writer(self.save_csv, delimiter=',')  # 以，为分隔符
#
#     def trans(self, filename):
#         file = open(filename, 'a', encoding='utf-8')
#         with open('/Users/fjc/Desktop/data.json', 'r') as f:
#             for i in json.loads(f.read())['data']['Data']['ActionLists']:
#                 a = {}
#                 a["RamAction"] = i["RamAction"]
#                 a["OperationType"] = i["OperationType"]
#                 file.write((json.dumps(a)+'\n'))
#         file.close()
#
#         with codecs.open(filename, 'r', encoding='utf-8') as f:
#             read = f.readlines()
#             flag = True
#             for index, info in enumerate(read):
#                 data = json.loads(info)
#                 # if index <3000: #读取json文件的前3000行写入csv文件 。要是想写入全部，则去掉判断。
#                 if flag:  # 截断第一行当做head
#                     keys = list(data.keys())  # 将得到的keys用列表的形式封装好，才能写入csv
#                     self.write_csv.writerow(keys)
#                     flag = False  # 释放
#                 value = list(data.values())   # 写入values，也要是列表形式
#                 self.write_csv.writerow(value)
#             self.save_csv.close()  # 写完就关闭

# c = """
# Options: (20 bytes), Maximum segment size, SACK permitted, Timestamps, No-Operation (NOP), Window scale
#             Maximum segment size: 1460 bytes
#                 Kind: MSS size (2)
#                 Length: 4
#                 MSS Value: 1460
#             TCP SACK Permitted Option: True
#                 Kind: SACK Permission (4)
#                 Length: 2
#             Timestamps: TSval 3143800264, TSecr 0
#                 Kind: Timestamp (8)
#                 Length: 10
#                 Timestamp value: 3143800264
#                 Timestamp echo reply: 0
#             No-Operation (NOP)
#                 Type: 1
#                     0... .... = Copy on fragmentation: No
#                     .00. .... = Class: Control (0)
#                     ...0 0001 = Number: No-Operation (NOP) (1)
#             Window scale: 7 (multiply by 128)
#                 Kind: Window Scale (3)
#                 Length: 3
#                 Shift count: 7
#                 [Multiplier: 128]
# """
# mss = re.search(r'Maximum segment size: (\d+) bytes', c)
# window_scale = re.search(r'Window scale: (\d+) \(multiply by (\d+)\)', c)
# sack = re.search(r'TCP SACK Permitted Option: Truea', c)


from datetime import datetime
import pytz

# 给定的日期和时间字符串
date_string = "Oct 30, 2023 15:11:10.635679000 CST"

# 使用strptime将日期和时间字符串转换为datetime对象
# 注意：CST可以代表多个不同的时区，这里假设它表示中国标准时间（UTC+8）
# 如果它代表中美洲标准时间，则应相应选择正确的时区。
date_object = datetime.strptime(date_string, '%b %d, %Y %H:%M:%S.%f000 %Z')

# 为date_object设置正确的时区
# 这一步非常重要因为Unix时间戳是根据UTC来计算的
timezone = pytz.timezone('Asia/Shanghai')  # 假设CST为中国标准时间，UTC+8
date_object = timezone.localize(date_object)

# 转换成Unix时间戳（去掉小数点后的毫秒数）
unix_timestamp = int(date_object.timestamp())

print(unix_timestamp)