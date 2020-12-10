# Histograms

# Example 1 - Investigating the distribution of Revenue

x = raw_data['Revenue'].values

sns.distplot(x, color = 'blue')
#-----------------------------------------------
# As you can see, it's a bit imbalance. Right skewd distribution as the mean is to the right

# Example 2 - Investigating the distribution of Revenue, adding the mean

x = raw_data['Revenue'].values

sns.distplot(x, color = 'blue')

# Calculating the mean
mean = raw_data['Revenue'].mean()
print(mean)

#ploting the mean
plt.axvline(mean, 0,1, color = 'red')
#----------------------------------------------
# Example 3 - Investigating the distribution of Visitors,
# adding the mean

x = raw_data['Visitors'].values

sns.distplot(x, color = 'red')

# Calculating the mean
mean = raw_data['Visitors'].mean()
print(mean)

#ploting the mean
plt.axvline(mean, 0,1, color = 'blue')
#------------------------------------------------
#ScatterPlots
raw_data.columns

# Example 1 - Relationship between Marketing Spend 
#and Revenue

ax = sns.scatterplot(x="Marketing Spend", y="Revenue", 
                     data=raw_data, color = 'green')


# Example 2 - Relationship between Marketing Spend 
#and Revenue - changing color, hue & Style

ax = sns.scatterplot(x="Marketing Spend", y="Revenue", 
                     data=raw_data, color = 'green', 
                     hue = 'Promo', style = 'Promo')

# Example 3 - Relationship between Marketing Spend and 
#Revenue - changing color & hue - adding size

ax = sns.scatterplot(x="Marketing Spend", y="Revenue", 
                     data=raw_data, color = 'green', 
                     hue = 'Promo', size = 'Revenue',
                    sizes=(20, 200))
# Example 4 - Relationship between Marketing Spend and 
#Revenue - changing color & hue - adding size - by day

ax = sns.scatterplot(x="Visitors", y="Revenue", 
                     data=raw_data, color = 'green', 
                     hue = 'Day_Name', size = 'Revenue',
                    sizes=(20, 200))

#-----------------------------------------------------------

#BoxPlots
# Example 1 - Investigating the distribution 
#of Revenue by Day
ax = sns.boxplot(x="Day_Name", y="Revenue", 
                 data=raw_data)

# Example 2 - Investigating the distribution of Revenue by Day - Horizontal - change color

ax = sns.boxplot(x="Revenue", y="Day_Name",
                 data=raw_data, 
                 color = '#CE578C')

# Cool Way to pick colours
# https://htmlcolorcodes.com/color-picker/


# Example 3 - Investigating the distribution of Revenue 
#by Day - changing color - adding hue

ax = sns.boxplot(x="Day_Name", y="Revenue", 
                 data=raw_data, color="#B971E7", 
                 hue = 'Promo')

# Cool Way to pick colours
# https://htmlcolorcodes.com/color-picker/

#-------------------------------------------

#lmplot-linear model
# Example 1 - Relationship between Marketing Spend and
# Revenue

ax = sns.lmplot(x="Marketing Spend", y="Revenue",
                data=raw_data, height=9)

# Notes:
# What is Linear Regression: 
#It is a predictive statistical method for modelling the 
#relationship between x (independent variable) &
# y (dependent V).

# Example 2 - Relationship between Marketing Spend and 
#Revenue - changing color, hue & Style

ax = sns.lmplot(x="Marketing Spend", y="Revenue", 
                data=raw_data,
                hue = 'Promo', ci= False, 
                height=9, 
                markers=["o", "x", "+"])

# Example 3 - Relationship between Marketing Spend and 
#Revenue - by column

ax = sns.lmplot(x="Marketing Spend", y="Revenue", 
                data=raw_data, col = 'Promo',
                ci= False, height=5, 
                line_kws={'color': 'red'}, 
                scatter_kws={'color':'#ADC11E'})


# Example 4 - Relationship between Marketing Spend and 
#Revenue - by column - by day - add Jitter too

ax = sns.lmplot(x="Visitors", y="Revenue", 
                data=raw_data, col = 'Day_Name', 
                ci= False, height=4, 
                line_kws={'color': '#031722'}, 
                scatter_kws={'color':'#1E84C1'},  
                col_wrap=3,
                 x_jitter=.3
              )

#---------------------------------------------------
# SubPlots

# Set up the matplotlib figure
fig, axes = plt.subplots(2, 2, figsize=(12, 7))

a = raw_data['Revenue'].values
b = raw_data['Visitors'].values
c = raw_data['Marketing Spend'].values
d = raw_data['Month'].values
# plot 1
sns.distplot(a, color = 'blue', ax=axes[0,0])
# plot 2
sns.distplot(b, color = 'yellow', ax=axes[0,1])
# plot 3
sns.distplot(c, color = 'green', ax=axes[1,0])
# plot 4
sns.distplot(d, color = 'red', ax=axes[1,1])
#--------------------------------------------------------
# Pairplots

# Example 1 - running on all dataframe - green color
g = sns.pairplot(raw_data,
                 plot_kws={'color':'green'})

# Example 2 - running on specific columns - green color
g = sns.pairplot(raw_data[['Revenue','Visitors',
                           'Marketing Spend']], 
                 plot_kws={'color':'#0EDCA9'})

# Example 3 - running on specific columns - adding hue
g = sns.pairplot(raw_data[['Revenue','Visitors',
                           'Marketing Spend', 
                           'Promo']],hue = 'Promo')

# Example 4 - running on specific columns - adding hue - adding kind = reg
g = sns.pairplot(raw_data[['Revenue','Visitors',
                           'Marketing Spend', 
                           'Promo']],hue = 'Promo', 
                 kind="reg", height = 6)


g = sns.pairplot(raw_data[['Revenue','Visitors',
                           'Marketing Spend', 
                           'Promo']],hue = 'Promo', 
                 kind="reg", height = 6,
                 diag_kind="hist")
#----------------------------------------------------
#JointPlots
#Draw a plot of two variables with bivariate and univariate graphs.
# Example 1 - Revenue vs marketing Spend Relationship with 
g = sns.jointplot("Revenue", "Marketing Spend", 
                  data=raw_data,
                  kind="reg", 
                  color = 'green', height = 4)
#--------------------------------------------------------
#Heat Map
# First we need to create a "Dataset" to display on a Heatmap - we will use a correlation dataset
# .corr() is used to find the pairwise correlation of all columns in the dataframe. Any null values are automatically excluded
# The closer to 1 or -1 the better. As one variable increases, the other variable tends to also increase / decrease
# More Info here: https://statisticsbyjim.com/basics/correlations/
# Example 1 - Heatmap for PC
pc = raw_data[['Revenue','Visitors',
  'Marketing Spend', 'Promo']].corr(method ='pearson')

cols = ['Revenue CC',
        'Visitors CC','Marketing Spend CC']

ax = sns.heatmap(pc, annot=False,
                 yticklabels=cols,
                 xticklabels=cols,
                 annot_kws={'size': 25})

# Example 2 - Heatmap for PC - changing cmap
ax = sns.heatmap(pc, annot=True,
                 yticklabels=cols,
                 xticklabels=cols,                
                 annot_kws={'size': 25},
                 cmap="YlGnBu")

# Examples:
# cmap="YlGnBu"
# cmap="Blues"
# cmap="BuPu"
# cmap="Greens"
#------------------------------------------------------------

sns.swarmplot("Revenue","Marketing Spend",
              data=raw_data)

#---------------------------------------------
sns.violinplot(x="Day_Name",y="Revenue",
               hue="Promo",
              data=raw_data)


sns.violinplot(x="Day_Name",y="Revenue",
               hue="Promo",palette='muted',
              data=raw_data)


sns.violinplot(x="Day_Name",y="Revenue",
               hue="Promo",palette='muted',
               order=["Friday","Saturday"],
              data=raw_data)

#----------------------------------------------------------