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
time_in_day ={k:0 for k in xrange(0,24)}
for i in s_time:
 	if i.startswith('2012-11-03'):
 		hour =i.split(' ')[1].split(':')[0]
		time_in_day[int(hour)]= time_in_day[int(hour)]+1
print [(i,time_in_day[i]) for i in time_in_day.keys() ]
#统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）
source_in = {k:0 for k in  [s_data[i]['source'] for i in s_data.keys()]}
for i in source_in.keys():
	for j in s_data.values():
		if i in j.values():
			source_in[i]=source_in[i]+1
print source_in

#计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)
s_rt_v_url =[i['rt_v_url'] for i in s_data.values() if i['rt_v_url'].startswith('https://twitter.com/umiushi_no_uta')]
print len(s_rt_v_url)
#UID为573638104的用户 发了多少个微博
s_uid =[i for i in s_data.values() if i['uid'] == '573638104']
print len(s_uid)
#定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。
def user_max_num(*user_id): #此函数有缺陷，暂不修改了。
	s_id =[s_data[i]['uid'] for i in s_data.keys()]
	dict_id={i:0 for i in user_id}
	if len(user_id)>0:
		for id in s_id:
			id =int(id)
			if id in dict_id.keys():
				dict_id[id] =dict_id[id] +1
		list_box=[(k,i) for k,i in dict_id.items()]
		list_box.sort(key=lambda k:k[1])
		return list_box[-1][0]
	else:
		pass
#该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）
txt_tuple=[(s_data[i]['uid'],len(s_data[i]['content'])) for i in s_data.keys()]
txt_tuple.sort(key=lambda k:k[1],reverse=True)
print "微博内容最长用户：{0}，长度为{1}".format(txt_tuple[0][0],txt_tuple[0][1])
#该文本里，谁转发的URL最多
# s =set([s_data[i]['rt_v_url'] for i in s_data.keys()])
# print s
url_tuple=[(s_data[i]['uid'],s_data[i]['rt_v_url']) for i in s_data.keys()]

print url_tuple
url_tuple.sort(key=lambda k:k[1],reverse=True)
print "转发url最多用户：{0}，数量为{1}".format(url_tuple[0][0],url_tuple[0][1])
#该文本里，11点钟，谁发的微博次数最多。 （要求：输出用户的uid，字符串格式。）


#该文本里，哪个用户的源微博URL次数最多（要求：输出用户的uid，字符串格式。）


f.close()
if __name__ == '__main__':
	print "发微博最多用户{0}".format(user_max_num(111))