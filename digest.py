#!/usr/bin/python

from __future__ import division
import sys

#filename="egalit_paxos-out.txt"
if(len(sys.argv)!=2):
    print "Usage : python digest.py [filename]"
    sys.exit()

filename=str(sys.argv[1])

with open(filename) as inf:
    data = []
    num_runs = int(inf.readline())
    for line in inf:
        line = [float(x) for x in line.split()]
        if(len(line)==2):
            data.append(line)
    
data.sort(key=lambda x:x[1])
average=[]
count=0
sum=0
for entry in data:
   count=count+1
   sum=sum+entry[0]
   throughput=entry[1]
   if(count==num_runs):
        average.append([sum/count,throughput])
        count=0
        sum=0

with open(filename, 'w') as f_out:
    for x in average:
        f_out.write("%s %s\n" % (x[0], int(x[1])))


for x in average:
    print x


