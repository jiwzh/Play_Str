#coding=utf-8
import time
import re

keys=['bid', 'uid', 'username', 'v_class', 'content', 'img', 'time', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_mid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url']
f=open(r'D:\Item\umb\tencent\file\twitter1.txt','rb+')
s_data={}
for i in f.readlines():
	s_data[i.split('","')[0]]=dict(zip(keys,i.split('","')))
#-----该文本里，有多少个用户-------------
username=[s_data[i]['username'] for i in s_data.keys()]
print "用户数目： %s"%(len(set(username)))
#该文本里，每一个用户的名字
# print list(set(username))
#该文本里，有多少个2012年11月发布的tweets
s_time=[s_data[i]['time'] for i in s_data.keys()]
d=[i for i in s_time if i.startswith('2012-11')]
print "2012年11月发布的tweets: %s"%(len(d))
#该文本里，有哪几天的数据？
days=[i.split(' ')[0] for i in s_time]
day=list(set(days))
print "哪几天的数据: %s"%(day)
#该文本里，在哪个小时发布的数据最多？
times=[i.split(' ')[1].split(':')[0] for i in s_time]
time_d=[]
time_d=[(i,times.count('%s'%i)) for i in xrange(0,24)]
time_d.sort(key=lambda k:k[1])
print '哪个小时发布的数据最多: %s'%(time_d[-1][0])
#该文本里，输出在每一天发表tweets最多的用户。（例如 {'2012-03-04':'agelin','2012-03-5':'twa'}）
# print time_name=[[s_data.values()[i]['time'].split(' ')[0],s_data.values()[i]['username']] for i in xrange(0,len(s_data))]
name_num={k:{} for k in day}
for i in s_data.keys():
	name_num[s_data[i]['time'].split(' ')[0]][s_data[i]['username']] =0
for i in s_data.keys():
	if name_num.has_key(s_data[i]['time'].split(' ')[0]):
		name_num[s_data[i]['time'].split(' ')[0]][s_data[i]['username']] +=1
for i in name_num.keys():
	d=[]
	for j in name_num[i].keys():
		a=(j,name_num[i][j])
		d.append(a)
	name_num[i] =d
for  i in name_num:
	name_num[i].sort(key=lambda k:k[1],reverse=True)
	name_num[i]=name_num[i][0][0]
print "每一天发表tweets最多的用户: %s"%(name_num)
#请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets）
