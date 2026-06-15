import numpy as np
print("numpy works")
a=np.array([1,2,3])
print(a)

b=np.array([[9.0,8.0,7.0],[4.0,5.0,6.0]])
print(b)
#gety dimension
a.ndim
b.ndim
#get shape
a.shape
b.shape
#get size
a.itemsize
b.itemsize
#get type
a.dtype
b.dtype


#total size = a.size * a.itemsize

c=np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(c)
c.shape
print(c[1,5])
#get specificv row
print(c[0,:])

#get specific column
print(c[:,2])

# getting a little more fancy [startindex:endindex:stepsize]
print(c[0,1:-2:2])

c[1,5]=20
print(c)

d=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])
print(d)
print(d[1,2,2])

np.zeros((2,3))
np.ones((4,2))
np.full((3,3),99)
np.random.rand(4,2)
np.random.randint(1,100,(3,3))  
np.identity(5)  
r1=np.repeat(a,3,axis=0)
print(r1)


o=np.ones((5,5))
print(o)
p=np.zeros((3,3))
print(p)
p[1,1]=9
o[1:4,1:4]=p
print(o)

a+b
a**2
np.sin(a)
np.cos(a)
np.tan(a)

#linear algebra
a=np.full((2,3),1)
b=np.full((3,2),2)
np.matmul(a,b)
print(np.matmul(a,b))
c=np.identity(3)
np.linalg.det(c)

#statistics
stats=np.array([[1,2,3],[4,5,6]])
print(stats)
print(np.min(stats))
print(np.max(stats))
print(np.mean(stats))
print(np.std(stats))
print(np.sum(stats,axis=0))

#reorganize arrays

a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
b=np.reshape(a,(8,1))
print(b)
c=np.reshape(a,(4,2))
print(c)    

v1=np.array([1,2,3])
v2=np.array([4,5,6])
print(np.vstack([v1,v2,v1,v2]))
print(np.hstack([v1,v2,v1,v2]))
