import re
import numpy as np
import os
co=0
coo=0
for file in os.listdir("/home/vk/saya/test"):
	if file.endswith(".csv"):
		coo+=1		
		print str(coo)+str("\t")+str(file)
		r=(str("/home/vk/saya/test/")+str(file))
		f=open(r,'r')
		n=sum(1 for sum in f)
		f=open(r,'r')
		p="Chicken pox"
		vp=[]
		m="Malaria"
		vm=[]
		d="Dengue"
		vd=[]
		t="Tuberculosis"
		vt=[]
		c="Chikungunya"
		vc=[]
		al1=[]
		for i in range(n):
			line=f.readline()
			if(line!="\n"):
				li=((line.split("\n"))[0]).split("\t")
				if re.match("^[a-zA-Z]+.*", line):
					li
				else:
					al1.append(li)
		f.close()
		vp1=[]
		vm1=[]
		vd1=[]
		vt1=[]
		vc1=[]
		vp=np.array(al1[:12])
		vp=np.reshape(vp,(12, -15))
		vp2=vp.T
		vp3=vp2.tolist()
		for i in vp3:
			vp1.append(i)
		print len(vp1)
		vp4=[]
		for i in vp1:
			vp4=vp4+i		
		vm=np.array(al1[12:24])
		vm=np.reshape(vm,(12, -15))
		vm2=vm.T
		vm3=vm2.tolist()
		for i in vm3:
			vm1.append(i)
		print len(vm1)
		vm4=[]
		for i in vm1:
			vm4=vm4+i		
		vd=np.array(al1[24:36])
		vd=np.reshape(vd,(12, -15))
		vd2=vd.T
		vd3=vd2.tolist()
		for i in vd3:
			vd1.append(i)
		print len(vd1)
		vd4=[]
		for i in vd1:
			vd4=vd4+i		
		vt=np.array(al1[36:48])
		vt=np.reshape(vt,(12, -15))
		vt2=vt.T
		vt3=vt2.tolist()
		for i in vt3:
			vt1.append(i)
		print len(vt1)
		vt4=[]
		for i in vt1:
			vt4=vt4+i
		vc=np.array(al1[48:60])
		vc=np.reshape(vc,(12, -15))
		vc2=vc.T
		vc3=vc2.tolist()
		for i in vc3:
			vc1.append(i)
		print len(vc1)
		vc4=[]
		for i in vc1:
			vc4=vc4+i
		print vp4
		print vm4
		print vd4
		print vt4
		print vc4
		a=[]
		for i in range(15):
			for j in range(0,24,2):
				a.append(j)
		print len(a)
		st=r.split(".csv")[0]+"_"+p+".csv"
		f=open(st,'w')
		for i in range(180):
			f.write(str(a[i])+","+vp4[i]+"\n")
		f.close()
		st=r.split(".csv")[0]+"_"+m+".csv"
		f=open(st,'w')
		for i in range(180):
			f.write(str(a[i])+","+vm4[i]+"\n")
		f.close()
		st=r.split(".csv")[0]+"_"+d+".csv"
		f=open(st,'w')
		for i in range(180):
			f.write(str(a[i])+","+vd4[i]+"\n")
		f.close()
		st=r.split(".csv")[0]+"_"+t+".csv"
		f=open(st,'w')
		for i in range(180):
			f.write(str(a[i])+","+vt4[i]+"\n")
		f.close()
		st=r.split(".csv")[0]+"_"+c+".csv"
		f=open(st,'w')
		for i in range(180):
			f.write(str(a[i])+","+vc4[i]+"\n")
		f.close()
