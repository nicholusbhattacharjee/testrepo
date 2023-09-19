#!/usr/bin/python3
from sys import argv
readfile = open(argv[1], "r")
writefile= open(argv[2], "w")
lines=readfile.readlines()
num=[]
cal=0
for line in lines:
	if line[:4]=='ATOM':
		num.append(line[17:26])
	elif line[:3]=='END':
		cal+=1
num.sort()
num_set=set(num)
for s_n in num_set:
	a=s_n[-3:]+' '+str(num.count(s_n)/cal)+'\n'
	writefile.write(a)
	
readfile.close()
writefile.close()

