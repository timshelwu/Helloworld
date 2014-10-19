# -*- coding: utf-8 -*-

try:
	import cStringIO as StringIO
	print "success in cStringIO as StringIO"
except ImportError: # 导入失败会捕获到ImportError
	import StringIO
	print "success in StringIO"
'''
try:
	import json # python >= 2.6
	print "success in json"
except ImportError:
	import simplejson as json # python <= 2.5
	print "success in simplejson as json"
'''
#name = raw_input("please input:");




def log(func):
	def wrapper(*args, **kw):
		print "begin call: %s" % func.__name__
		func(*args, **kw)
		print "end call: %s" % func.__name__
	return wrapper;

@log
def output():
	print "haha"

if __name__=='__main__':
	print output
	output()
	print output.__name__
	
	
	

'''
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print [x * x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]



def proc(list):
	def multiply(x, y):
		return x*y
	return reduce(multiply, list)
print proc([1,3,5,7])



def myMap(fn, args):
	L = []
	for x in args:
		L.append(fn(x))
	return L
def sum(x):
	return x*2
print myMap(sum, [1,3,5,7])
print len(myMap(sum, [1,3,5,7]))



def myMap(fn, *args):
	L = []
	for x in args:
		L.append(fn(x))
	return L
def sum(x):
	return x*2
print myMap(sum, 1,3,5,7)
print len(myMap(sum, 1,3,5,7))



print 'Hello:' #, name
x=5
if x>5:
	print x
	x='asdfasf'
	print x
	print u'哈哈'
elif x>3:
	a = ['test','haha']
	a.append('byeeeeee')
	print a[0] + a[1] + a[2]

y=0
for x in range(100):
	y+=x
print y

z = '123'
print z
print int(z)
'''