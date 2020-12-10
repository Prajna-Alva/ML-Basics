
import matplotlib.pyplot as plt

#Basic Graph
m = [0,2,4,6,8]

# Resize your Graph (dpi specifies pixels per inch. When saving probably should use 300 if possible)
plt.figure(figsize=(12,5), dpi=100)
plt.plot(m)

# Line 1

# Keyword Argument Notation
plt.plot(m, color='green', linewidth=2, 
         marker='.', linestyle='--', markersize=20, 
         markeredgecolor='red')

'''
Color codes
Character	Color
‘b’	Blue
‘g’	Green
‘r’	Red
‘c’	Cyan
‘m’	Magenta
‘y’	Yellow
‘k’	Black
‘w’	White  
    
    
Marker codes
Character	Description
‘.’	Point marker
‘o’	Circle marker
‘x’	X marker
‘D’	Diamond marker
‘H’	Hexagon marker
‘s’	Square marker
‘+’	Plus marker
'^' Triangle marker

Line styles
Character	Description
‘-‘	Solid line
‘—‘	Dashed line
‘-.’	Dash-dot line
‘:’	Dotted line


'''

# Shorthand notation
# fmt = '[color][marker][line]'
plt.plot(m, 'rH--')
#------------------------------------------------------

y = [1, 4, 9, 16, 25,36,49, 64]
x = [1, 16, 30, 42,55, 68, 77,88]
fig = plt.figure()
plt.plot(x,y,'rH-', linewidth=2,markeredgecolor='g') # solid line with yellow colour and square marker

plt.legend(labels ='tv', loc = 'lower right') # legend placed at lower right
plt.title("Advertisement effect on sales")
plt.xlabel('medium')
plt.ylabel('sales')

plt.savefig("fig3.png",dpi=300)#should be before plt.show; else blank pic
plt.show()
#---------------------------------------------

'''
loc
right,lower right,upper right
left,lower left,upper left
center,lower center,upper center'''

y1 = [1,4, 9, 16, 25, 36, 49, 64]
y2 = [2,6, 8, 10, 12, 24, 32, 73]
x1 = [1,16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
l1 = ax.plot(x1,y1,'rH-') # solid line with yellow colour and square marker
l2 = ax.plot(x2,y2,'go--') # dash line with green colour and circle marker
ax.legend(labels = ('tv','smartphone'), 
          loc = 'lower right') # legend placed at lower right


ax.set_title("Advertisement effect on sales")
ax.set_xlabel('medium')
ax.set_ylabel('sales')
plt.show()

# plot a line, implicitly creating a subplot(111)
plt.plot([1,2,3])

# now create a subplot which represents the top plot of a grid with 2 rows and 1 column.
#Since this subplot will overlap the first, the plot (and its axes) previously created, will be removed

plt.subplot(211)#(row,column,cell)
plt.plot(range(12))
plt.subplot(212, facecolor='y') # creates 2nd subplot with yellow background
plt.plot(range(12))

#--------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot([1,2,3])
ax2 = fig.add_subplot(212, facecolor='y')
ax2.plot([1,2,3])
#---------------------------------------------
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot([1,2,3])
ax2 = fig.add_subplot(224, facecolor='y')#inset figure
ax2.plot([1,2,3])

#----------------------------

import numpy as np
# select interval we want to plot points at
x = np.arange(0,4.5,0.5) #0,0.5,1,1.5,2,2.5,3,3.5,4
print(x)

# Plot part of the graph as line
plt.plot(x[:6], x[:6]**2, 'r^-')#0,0.5.1.1.5,2.2.5

# Plot remainder of graph as a dot
plt.plot(x[5:], x[5:]**2, 'g^--')#2.5,3.0,3.5,4.0

# Add a title (specify font parameters with fontdict)
plt.title('Our First Graph!', 
          fontdict={'name': 'Comic Sans MS', 
                    'size': 30,
                    'color':'red',
                    'weight':'bold',
                    })
# X and Y labels
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# X, Y axis Tickmarks (scale of your graph)
plt.xticks([0,1,2,3,4,5])
plt.yticks([0,2,4,6,8,10,12,14,16])
#-----------------------------------------------------

import pandas as pd
plt.figure(figsize=[8,5])

plt.title('Gas Prices over Time (in USD)', 
          fontdict={'weight':'bold', 'size': 18})

gas = pd.read_csv("gas_prices.csv")

plt.plot(gas.Year, gas.USA, 'b.-', 
         label='United States')
plt.plot(gas.Year, gas.Canada, 'r.-',label='Canada')
plt.plot(gas.Year, gas['South Korea'], 'g.-')
plt.plot(gas.Year, gas.Australia, 'y.-')
plt.legend()
plt.show()


# Another Way to plot many values
countries = ['Australia', 'USA', 
                        'Canada', 'South Korea']
for country in gas:
    if country in countries:
        plt.plot(gas.Year, gas[country], 
                 marker='.',label=country)

plt.xticks(gas.Year[::3].tolist()+[2011])

plt.xlabel('Year')
plt.ylabel('US Dollars')

plt.legend()

plt.savefig('Gasprice.png', dpi=300)
plt.show()

#plotting all countries

for country in gas:
    if country!= 'Year':
        plt.plot(gas.Year, gas[country],
                 marker='.',label=country)

plt.xticks(gas.Year[::3].tolist()+[2011])

plt.xlabel('Year')
plt.ylabel('US Dollars')

plt.legend()

plt.savefig('Gasprice1.png', dpi=300)
plt.show()
#---------------------------------------------------------


import matplotlib.pyplot as plt
import numpy as np


fig, axes = plt.subplots(1, 2, figsize=(10,4))
x = np.arange(1,5)
axes[0].plot( x, np.exp(x))
axes[0].plot(x,x**2)
axes[0].set_title("Normal scale")
axes[1].plot (x, np.exp(x))
axes[1].plot(x, x**2)
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic scale (y)")
axes[0].set_xlabel("x axis")
axes[0].set_ylabel("y axis")
axes[0].xaxis.labelpad = 10
axes[1].set_xlabel("x axis")
axes[1].set_ylabel("y axis")
plt.show()


#------------------