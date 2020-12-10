import numpy as np
#symmetrical split
G=np.arange(1,17).reshape(4,4)
print(G)
H,I=np.hsplit(G,2)
print(H)
print(I)

J,K=np.vsplit(G,2)
print(J)
print(K)
print(type(J))

#Non symmetrical split
G=np.arange(1,17).reshape(4,4)
print(G)
A1,A2,A3=np.split(G,[1,2],axis=1)#column
print("A1=",A1)
print("A2=",A2)
print("A3=",A3)

A1,A2,A3=np.split(G,[1,3],axis=0)#row
print("A1=",A1)
print("A2=",A2)
print("A3=",A3)
#----------------------------------------------
#copy
x=np.arange(5,11)
print(x)
y=x
print(y)

print(id(x))
print(id(y))

x[3]=70
print(x)
print(y)

x=np.arange(5,11)
print(x)
y=x.copy()
print(y)

print(id(x))
print(id(y))

x[3]=70
print(x)
print(y)

#--------------------------------------------------
x=[1,2,3,5,4]
y=x.copy()#can be used for list also
x[3]=70
print(x)
print(y)
#----------------------------------------------------------

#casting float -> int
arr = np.array([3.7, -1.2, -2.6, 0.5, 
                12.9, 10.1])
print(arr)

print(arr.astype(np.int32))

#string to int
s = np.array(['1.25', '-9.6', '42'])
print(s.astype(np.float64))

a=np.array([1,2,3,4])
a.astype()#Error,must specify dtype
a.dtype
#If casting were to fail for some reason
# (like a string that cannot be converted to float64), 
#a TypeError will be raised

#---------------------------------------------
#Operations between Arrays and Scalars
arr = np.array([[1., 2., 3.], 
                [4., 5., 6.]])

print( 1 / arr )
print(arr*2)

# Boolean indexing 
from numpy.random import randn

data = randn(7, 4)
print(data)


'''
difference between random and rand:
    to create an array of samples with 
    shape (3, 5), you can write

sample = np.random.rand(3, 5)
or

sample = np.random.random_sample((3, 5))


 only difference is in how the arguments are handled.
 With numpy.random.rand, the length of each dimension of the output array is a separate argument. 
 With numpy.random.random_sample, the shape argument is a single tuple.

'''
c = np.full((2,2), 7)  # Create a constant array
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(3,dtype=int)         # Create a 2x2 identity matrix
print(d)              # Prints "[[ 1.  0.]
                      #          [ 0.  1.]]"

x = np.array([[1,2],[3,4]])
print(x)
print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1)) 

#------------------------------------



#PANDAS
#Pandas Series
#-------------

#creating series 
import pandas as pd
a= pd.Series([12,-4,7,9])
print(a)
print(type(a))
print(a.values)
print(a.index)

#creating series with user defined row-index
b = pd.Series([12,-4,7,9], 
              index=['a','b','c','d'])
print(b)
#retrieving values and index
print(b.values)
print(b.index)

#indexing and slicing
print(b)
print(b[2])
print(b['c'])
print(b[0:2])
print(b['a':'c'])
print(b[['a','c']])

#Changing Series Values
b[1]=16
print(b)
b['d']=15
print(b)

#creating series from ndarray
import numpy as np
arr = np.array([1,2,3,4])
print(arr)
c= pd.Series(arr)
print(c)
print(arr)
print(type(c))
print(type(arr))

#creating series from another series
a= pd.Series([12,-4,7,9])
d= pd.Series(a)
print(d)

#filtering values
print(a)
print(a>8)
print(a[a>8])

#arithmetic operations 
print(a)
e=a/2
print(e)
print(a)

#universal functions
a=pd.Series([1,2,3,4])
f=np.log(a)
print(f)
print(a)

#Evaluating values
g=pd.Series([1,0,2,1,2,3], 
            index=['white','white','blue',
                   'green','green','yellow'])

print(g)
print(g.unique())
print(g.value_counts())
print(g.isin([0,3]))
print(g[g.isin([0,3])])

#___________________________________________________

#Pandas DataFrame
#-----------------
 #creating a dataframe using dictionary
data = {'state': ['Ohio', 'Ohio', 'Ohio',
                  'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]
        }
frame = pd.DataFrame(data)
print(data)
print(frame)

 #creating a dataframe using an existing DataFrame
frame1=pd.DataFrame(frame)
print(frame1)

#Not A Number - missing values


#if you pass a column that isn’t contained in data, 
#it will appear with NAN values in the result:
frame2 = pd.DataFrame(data,
                      columns=['year', 'state', 
                               'pop', 'debt'],
                      index=['one', 'two', 
                             'three', 'four', 
                             'five'])
print(frame2)

#Retrieving DataFrame values using dict-like notation 
print(frame2['state'])

#Retrieving DataFrame values using attribute notation
print(frame2.state)

#loc index field
print(frame2)
print(frame2.loc['three'])

#Checking for missing values
h= pd.Series([5,-3,np.NaN,14])
print(h)
print(h.isnull())
print(h[h.isnull()])

print(h.notnull())
print(h[h.notnull()])

#the dropna() function:eliminates the NaN values during data analysis
data = pd.Series([1, np.NAN, 3.5, np.NAN, 7])
print(data)
data2=data.dropna()
print(data)
print(data2)

#-------------------------------------------

