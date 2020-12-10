#Bar graph
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,79,12]
ax.bar(langs,students)
plt.show()

#OR

langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,79,12]
plt.bar(langs,students)
plt.show()
#-------------------------------------------------------
data = [[30, 25, 50, 20],
        [40, 23, 51, 17],
        [35, 22, 45, 19]]
X = np.arange(4)
print(X)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
#ax.bar(x, height, width, bottom, align)
ax.bar(X + 0.00, data[0], color = 'b', width = 0.25)
ax.bar(X + 0.25, data[1], color = 'g', width = 0.25)
ax.bar(X + 0.50, data[2], color = 'r', width = 0.25)

#-----------------------------------------------------------
#histogram

fig,ax = plt.subplots(1,1)
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
ax.hist(a, bins = [0,25,50,75,100])#bins -divides into categories
ax.set_title("histogram of result")
ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('marks')
ax.set_ylabel('no. of students')
plt.show()
#--------------------------------------------
#pie chart
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
ax.pie(students, labels = langs,autopct='%1.2f%%')
plt.show()

#----------------------------------
'''
The default startangle is 0, which would start the "Frogs"
 slice on the positive x-axis. 
 startangle = 90 such that everything is rotated 
 counter-clockwise by 90 degrees, 
 and the frog slice starts on the positive y-axis.
'''


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
label = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
exp= (0, 0.2, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=exp, labels=label,
        autopct='%1.1f%%',shadow=True,
        startangle=90,radius=2)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
#___________________________________
#Scatter plot

girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [30, 29, 49, 48, 78, 100, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(grades_range, girls_grades, color='r')
ax.scatter(grades_range, boys_grades, color='b')
ax.set_xlabel('Grades Range')
ax.set_ylabel('Grades Scored')
ax.set_title('scatter plot')
plt.show()
#-------------------------------------------------


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Loading the data

raw_data = pd.read_csv("Marketing Raw Data.csv")
# runs all the data
raw_data 

print(raw_data.shape)

#runs the first 5 rows
raw_data.head()


# Example 1 - Simple 1 line graph
# Assuming we want to investigate the Revenue by Date

ax = sns.lineplot(x='Week_ID', y='Revenue', 
                       data = raw_data)


ax = sns.lineplot(x='Week_ID', y='Revenue', 
                  data = raw_data,ci=None)

# Notes: error bands show the confidence interval

# Example 2 - Adding Categories

# By Promo
ax = sns.lineplot(x='Week_ID', y='Revenue',
                  hue = 'Promo', 
                  data = raw_data)

# Example 3 - By Promo with style
ax = sns.lineplot(x='Week_ID', y='Revenue', 
                  hue = 'Promo', 
                  style = 'Promo', data = raw_data)


# Example 4 - By Promo with style & Increase the size & Remove error bars

# increase the size
sns.set(rc={'figure.figsize':(12,10)})

ax = sns.lineplot(x='Week_ID', y='Revenue', 
                  hue = 'Promo', 
                  style = 'Promo', 
                  data = raw_data, ci=None)


# Example 5 - By Promo with style & Increase the size & Remove error bars & adding markers & by month

ax = sns.lineplot(x='Month_ID', y='Revenue', 
                  hue = 'Promo', style = 'Promo', 
                  data = raw_data, ci=None,  
                  markers=True)

# Example 6 - By Day_Name with style & Increase the size & Remove error bars & adding markers & by month
ax = sns.lineplot(x='Month_ID', y='Revenue', 
                  hue = 'Day_Name', style = 'Promo', 
                  data = raw_data, ci=None,  
                  markers=True)

# Example 7 - By Year with style & Increase the size & Remove error bars & adding markers & by month
ax = sns.lineplot(x='Year', y='Revenue', 
                  hue = 'Day_Name', style = 'Promo', 
                  data = raw_data, ci=None,  
                  markers=True)
#------------------------------------------------------------------------------------------
# Bar Plots

# Example 1 - Total Revenue by Month

ax = sns.barplot(x="Month_ID", y="Revenue",
                 data=raw_data)

# Example 2 - Total Revenue by Month - Remove the Confidence Interval
ax = sns.barplot(x="Month_ID", y="Revenue", 
                 data=raw_data, ci=False)

# Example 3 - Total Revenue by Month - Remove the Confidence Interval - By Promo
ax = sns.barplot(x="Month_ID", y="Revenue", 
                 data=raw_data, ci=False, 
                 hue = 'Promo')

# Example 4 - Total Revenue by Month - Remove the Confidence Interval - By Promo - Changing direction
sns.set_style("white")
ax = sns.barplot(x="Revenue", y="Year", 
                 ci=False, hue = 'Promo', 
                 orient = 'h', data=raw_data)



# Example 5 - Total Revenue by Month - Remove the Confidence Interval - By Promo - Changing direction - Changing Colour
ax = sns.barplot(x="Revenue", y="Year", ci=False, 
                 hue = 'Promo', orient = 'h', 
                 data=raw_data, color="#5CB879")

# Cool Way to pick colours
# https://htmlcolorcodes.com/color-picker/
#---------------------------------------