import numpy as np
#nd array
m=np.array([1.9,2.9,3.3])#ndarray
print(m)

print(type(m))

print("m.shape:",m.shape)

print("m.ndim",m.ndim)

print("m.dtype",m.dtype)

print(m.itemsize)
#Bytes allocated to each item internally
print(m.size)#Number of items in the ndarray



#or a=np.array([(1,2,3),[3,4,5]])

a=np.array([[1,2,3],[5,6,7],[4,8,9]])
print(a)

print("a.shape:",a.shape)
print("a.ndim:",a.ndim)
print("a.dtype:",a.dtype)
print(a.size)
print(a.itemsize)


f=np.array([1,2,3,4],dtype=complex)
print(f)

e=np.array([1,2,3,4],dtype=float)
print(e)
print(e.dtype)
#-----------------------------------------
#np.ones() and np.zeros()
g=np.zeros((4,3))
print(g)

print(g.dtype)
print(type(g))

h=np.ones((3,3))
print(h)
#---------------------------------------
#arange()
i=np.arange(0,10)
print(i)
print(type(i))

j=np.arange(3,20)
print(j)

k=np.arange(20,50,7)#6 values
print(k)

l=np.arange(0,6,0.6)
print(l)

p=np.arange(1,13).reshape(3,4)
print(p)

#generating ndarray with random numbers
a1=np.random.random(3)
print(a1)

a2=np.random.random((4,3))
print(a2)

#Arithmetic Operations
b1=np.array([1,2,3,4])
print(b1)

b2=b1+2
print(b1)
print(b2)

b3=b1-2
print(b1)
print(b3)

b4=b1*3
print(b4)
                                                                                                         
b5=b1/2
print(b5)

b6=b1//2
print(b6)

b7=b1**2
print(b7)

#-------------------------------
c1=np.arange(1,5).reshape(2,2)
print(c1)

c2=np.array([1,1,1,1]).reshape(2,2)
print(c2)

print(c1*c2)#element wise multiplication

#Matrix multiplication
print(c1)
print(c2)
c3=np.dot(c1,c2)
print(c3)

#Arithmetic assignment operator
r=np.arange(1,6)#[1,2,3,4,5]
print(r)
#c=r+1
#print(c)
print(r+1)
print(r)#original array not affected

r+=1  #r=r+1  #r=[2,3,4,5,6]
print(r)
#------------------------------------------------------
#Universal functions
c4=np.array([1,2,3,4])
print(c4)
print(np.sqrt(c4))
print(np.log(c4))
print(np.sin(c4))

#agregate functions
d1=np.array([3.3,4.6,7.8,2.1,1.0])
print(d1.sum())
print(d1.min())
print(d1.max())
print(d1.mean())
print(d1.std())
#----------------------------------------
#indexing
d2=np.arange(10,16)
print(d2)
print(d2[3])
print(d2[-5])
print(d2)
print(d2[[2,4,5]])
print(d2[1:4])#Slicing
print(d2[::2])#1
print(d2[::3])#2
print(d2[::])#0
print(d2[0:5:])#0

d3=np.arange(10,19).reshape(3,3)
print(d3)
print(d3[0,1])
print(d3[1,2])

#slice
print(d3[0,:])
print(d3[1,:])
print(d3[2,:])

print(d3[:,0])
print(d3[:,1])
print(d3[:,2])

print(d3)
print(d3[0:2,:])

print(d3[0:2,0:2])

print(d3[1:3,1:3])

print(d3[[0,2],0:2])

print(d3[0:2,2])


for i in d3:
    print(i)

for i in d3.flat:
    print(i)

#Conditions and boolean
e1=np.random.random((3,3))
print(e1)

print(e1>0.5)

print(e1[e1>0.5])

print(e1[e1<0.5])

#-------------------------------------------------------------------
#one dimensional->multi dimension
a=np.random.random(12)
print(a)
b=a.reshape(3,4)#a not affected
print(a)
print(b)

c=np.random.random(12)
print(c)
c.shape=(3,4)#c is affected
print(c)
#-------------------------------
#multi dimension->one dimension
c=np.random.random((4,3))
d=c.ravel()#c not affected
print(d)
print(c)

c.shape=(12,)#c is affected
print(c)
#----------------------------------------
e=np.arange(1,13).reshape(3,4)
print(e)
f=e.transpose()
print(f)
print(e)
#----------------------------------------
#multidimensional ndarray--merging
A=np.zeros((3,3))
B=np.ones((3,3))
print(A)
print(B)
C=np.vstack((A,B))
print(C)
D=np.hstack((A,B))
print(D)
#-------------------------------------
#one dimensional array
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.array([7,8,9])
print(a)
print(b)
print(c)
d=np.column_stack((a,b,c))
print(d)
e=np.row_stack((a,b,c))
print(e)
#------------------------------------