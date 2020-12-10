#dropna by default drops any row containing a missing value:
import pandas as pd
import numpy as np
data = pd.DataFrame([[1., 6.5, 3.], 
                     [1., np.NAN, np.NAN],
                     [np.NAN,np.NAN, np.NAN], 
                     [np.NAN, 6.5, 3.]])
data
c1 = data.dropna()#row
c1

#Passing how='all' will only drop rows that
#are all NA:
c2=data.dropna(how='all')
c2#index 2 dropped

#Dropping columns in the same way is only a matter of passing axis=1:
data2 =pd.DataFrame([[1., np.NAN, 3.], 
                     [1., np.NAN, np.NAN],
                     [np.NAN,np.NAN, np.NAN], 
                     [np.NAN, np.NAN, 3.]])
print(data2)

d1=data2.dropna(axis=1)#column
d1

d2=data2.dropna(axis=1, how='all')
d2


#Filling missing data
print(data)
e1=data.fillna(0)
print(e1)
print(data)

#Calling fillna with a dict you can use a 
#different fill value for each column:

print(data)
e2=data.fillna({1: 0.5, 2: -1})
print(e2)
print(data)

#Hierarchical Indexing
data = pd.Series(np.random.randn(10),
                 index=[['a', 'a', 'a', 'b', 'b', 
                         'b', 'c', 'c','d', 'd'],
                [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
data
data.index
data['b']
data[:, 3]

#-----------------------------------------------------------------------
data
data.unstack()
data.unstack().stack()
#------------------------------------------------------------------------
frame = pd.DataFrame(np.arange(12).reshape((4, 3)), 
                     index=[['a', 'a', 'b', 'b'], 
                            [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])

frame
frame.index.names = ['key1', 'key2']
frame
frame.columns.names = ['state', 'color']
frame
frame['Ohio']
frame.swaplevel('key1', 'key2')
#-----------------------------------------------------
import numpy as np
import pandas as pd

sample_dict = { 'S1': [10, 20, np.NaN, np.NaN],
                'S2': [5, np.NaN, np.NaN, 29],
                'S3': [15, np.NaN, np.NaN, 11],
                'S4': [21, 22, 23, 25],
                'Subjects': ['Maths', 'Finance', 
                             'History','Geography']}
# Create a DataFrame from dictionary
df = pd.DataFrame(sample_dict)

print(df)
df['S2'].fillna(value=df['S2'].mean(),inplace=True)
print('Updated Dataframe:')
print(df)

#----------------------------------------------
import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils',
                     'Devils', 'Kings',   'kings', 
                     'Kings', 'Kings', 'Riders', 
                     'Royals', 'Royals', 'Riders'],

   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   
   'Year': [2014,2015,2014,2015,2014,2015,2016,
            2017,2016,2014,2015,2017],
            
   'Points':[876,789,863,673,741,812,756,788,
             694,701,804,690]}
    
df = pd.DataFrame(ipl_data)

print(df)
#------------------------------------------------------------------
'''
Split Data into Groups
Pandas object can be split into any of their objects. 
There are multiple ways to split an object like :
obj.groupby('key')
obj.groupby(['key1','key2'])

'''
g=df.groupby('Team')
for name,group in g:
   print(name)
   print(group)
#----------------------------------------------------------------------------
h=df.groupby(['Year','Rank'])
for a,b in h:
   print(a)
   print(b)
#---------------------------------------------------------------------------------
#Group by with multiple columns 
print(df.groupby(['Team','Year']).groups)

#Iterating through Groups
i= df.groupby('Year')

for name,group in i:
   print(name)
   print(group)#By default, the groupby object has the same label name as the group name
 
#------------------------------------
'''
Select a Group
Using the get_group() method, we can select a single group
'''
g = df.groupby('Year')
#print g:
for name,group in g:
   print(name)
   print(group)
   
#print(g)- returns an object
print(g.get_group(2014))

#Aggregations
import numpy as np
g = df.groupby('Year')
print(g['Points'].agg(np.mean))

#Attribute Access in Python Pandas
g = df.groupby('Team')
print(g.agg(np.size))

'''
Applying Multiple Aggregation Functions at Once
With grouped Series, you can also pass a list 
or dict of functions to do aggregation with, 
and generate DataFrame as output 
'''
g = df.groupby('Team')
print(g['Points'].agg([np.sum, np.mean, 
                             np.std]))
#--------------------------------------------
d = {'one' : pd.Series([1, 2, 3], 
                       index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], 
                     index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)

# Adding a new column to an existing DataFrame object with column label by passing new series
#print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],
                          index=['a','b','c'])
print(df)
#----------------------------------------------
#print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']
print(df)
#-------------------------------------------------------------------------
# delete a column
# using del function
d = {'one' : pd.Series([1, 2, 3], 
                       index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4],
                     index=['a', 'b', 'c', 'd']), 
   'three' : pd.Series([10,20,30], 
                       index=['a','b','c'])}
df = pd.DataFrame(d)
print ("Our dataframe is:")
print(df)

# using del function
#print ("Deleting the first column using DEL function:")
del df['one']
print( df)
# using pop function
#print ("Deleting another column using POP function:")
a=df.pop('two')
print(df)
print(a)
print(type(a))
#---------------------------------------------------------------------
#Slice Rows
d = {'one' : pd.Series([1, 2, 3], 
                       index=['a', 'b', 'c']), 
   'two' : pd.Series([1, 2, 3, 4], 
                     index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
print(df[2:4])
#----------------------------------------------------------------
#Add new rows to a DataFrame using the append function.
df = pd.DataFrame([[1, 2], [3, 4]], 
                  columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]],
                   columns = ['a','b'])
print(df)
print(df2)
df = df.append(df2)
print(df)
#----------------------------------------------------------------
'''Deletion of Rows:
Use index label to delete or drop rows from a DataFrame.
 If label is duplicated, then multiple rows will be dropped.
'''
print(df)

df = df.drop(0)# Drop rows with label 0
print(df)

df = df.drop('a',axis=1)#drop column
print(df)
#--------------------------------------------------------------
#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky',
                    'Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'GPA':pd.Series([4.23,3.24,3.98,2.56,3.20,
                    4.6,3.8])}
#Create a DataFrame
df = pd.DataFrame(d)
df
print(df.axes)#prints row and column axes
print(df.info())#gives information about the dataframe
print(df.dtypes)

print(df.empty)#returns True/False if dataframe is empty
print(df.ndim)
print(df.shape)
print(df.size)#total number of elements in the dataframe

#values -Returns the actual data in the DataFrame as an NDarray.
print(df.values) 
print(df.head())#default is 5
print(df.tail())

print(df.head(2))
print(df.tail(2))
#----------------------------------------------------------------
