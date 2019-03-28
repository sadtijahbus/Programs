import re
f= open('/home/vk/subha/mtech/Mycobacterium_tuberculosis_H37Rv_uid57777/NC_000962 (copy).ptt','rU')
t= sum(1 for line in f)-3
f= open('/home/vk/subha/mtech/Mycobacterium_tuberculosis_H37Rv_uid57777/NC_000962 (copy).ptt','rU')
line= f.readline()
line= f.readline()
line= f.readline()
z=[]
for i in range(t):
	line= f.readline()
	n=re.findall("..\d*\t", line)
	z.append(n[1])
z=[i.split('\t', 1)[0] for i in z]
g= open('/home/vk/subha/mtech/Mycobacterium_tuberculosis_H37Rv_uid57777/new/Number of Lines + Start and Stop Positions.txt','rU')
n = sum(1 for line in g)
l1=[]
l2=[]
l11=[]
l22=[]
g= open('/home/vk/subha/mtech/Mycobacterium_tuberculosis_H37Rv_uid57777/new/Number of Lines + Start and Stop Positions.txt','rU')
for i in range(n):
	line= g.readline()	
	m=re.findall(r'\d+', line)
	l1.append(m[0])
	l2.append(m[1])
n1=len(l1)
n2=len(l2)
j=[]
h=open('/home/vk/subha/mtech/Mycobacterium_tuberculosis_H37Rv_uid57777/NC_000962 (copy).fna','rU')
line= h.readline()
for line in h:
	for val in line:
		if val == '\n':
			j
		else:	
			j.append(val)
l1=map(int,l1)
l2=map(int,l2)
for i in l1:
	if i<36:
		l11.append("-")
	else:
		l11.append(j[(i-36):(i-1)])
ll=[]
for i in range(n1):
	if z[i]=='+':
		ll.append(l1[i])
k=[]
l=[]
m=[]
snpc=[]
snpd=[]
co=0
coo=0
import os
for file in os.listdir("/home/vk/subha/mtech/Mycobacterium_tuberculosis_H37Rv_uid57777/mtb1"):
	if file.endswith(".snp"):
		coo+=1		
		snp=0
		snpu=0
		print str(coo)+str("\t")+str(file)
		r=(str("/home/vk/subha/mtech/Mycobacterium_tuberculosis_H37Rv_uid57777/mtb1/")+str(file))
		m.append(str(file)+str("\n"))
		snpd.append(str(file)+str("\n"))
		snp= open(r,'r')
		for i in snp:
			k.append(i)
		l=[i.split('\t', 1)[0] for i in k]
		la=[i.split('\t', 1)[1] for i in k]
		l=map(int,l)
		for i in l:			
			for o in ll:
				if o==1:
					o
				else:	
					c=o
					e=c-35
					if i>=e & i<=(c-0):
						for p in range(e,(c-0)):
							if i==p:
								co+=1
								m.append(str(i)+str("\t"))
								snpd.append(str(i)+str("\t")+str(la[l.index(i)])+str("\n"))
								break
		print co
		snpc.append(str(file)+str("\t")+str(co)+str("\n"))
		m.append(str("\n"))
		m.append(str(co)+str("\n"))
		snpd.append(str("\n"))
		co=0
		del l[:]
		del k[:]
q=(str("/home/vk/subha/mtech/out/csnp-35+desc.txt"))
snpu=open(q,'w')
snpu.writelines(snpd)
snpu.close()
import collections
b=sum(1 for line in snpc)
print b
ci=0
a=[i.split('\t', 1)[0] for i in snpc]
r=[i.split('\t', 1)[1] for i in snpc]						
dict1={}
q=(str("/home/vk/subha/mtech/out/csnp-35sort.txt"))
snpu=open(q,'w')
for i in range(b):
	dict1[a[i]]=r[i]
	od = collections.OrderedDict(sorted(dict1.items()))
for q, v in od.iteritems():
	ci+=1
	snpu.write(str(ci)+str("\t")+str(q)+str("\t")+str(v)+str("\n"))
snpu.close()
q=(str("/home/vk/subha/mtech/out/csnp-35+.txt"))
snpu=open(q,'w')
snpu.writelines(m)
snpu.close()
q=(str("/home/vk/subha/mtech/out/csnp-35.txt"))
snpu=open(q,'w')
snpu.writelines(snpc)
snpu.close()
