# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 18:00:00 2022

@author: Sonny Smith
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('Website (Chrome).xlsx')
df2 = pd.read_excel('Website (Firefox).xlsx')
df3 = pd.read_excel('Website (Edge).xlsx')


#Basic Structure
df.head()
df.describe()
df.dtypes
df.columns
df.shape
pd.set_option('expand_frame_repr', False)

#x = np.array(df.columns[2:7])
#y = np.array(df.iloc[:, 2:7])

#plt.bar(x, y)
#plt.show()

#Renames Name column for clarity
df.rename(columns={'Name' : 'Website Names'}, inplace = True)

#Displays the amount of trackers/ads blocked on each website for each blocker
df.plot.bar(x = 'Website Names', y = 'PrivacyBadger', color = 'orange')
df.plot.bar(x = 'Website Names', y = 'uBlockOrigin', color = 'green')
df.plot.bar(x = 'Website Names', y = 'AdBlock', color = 'red')
df.plot.bar(x = 'Website Names', y = 'AdBlock Plus', color = 'gold')
df.plot.bar(x = 'Website Names', y = 'Ghostery', color = 'purple')


#Average Calculations
avgs_blocker = df.mean() #average block count by blocker
avgs_website = df.mean(axis = 1) #average block count by website


#Convert from wide format to long formation
melted_df = df.melt(id_vars = 'Website Names', value_vars=['PrivacyBadger', 'uBlockOrigin', 'AdBlock', 'AdBlock Plus', 'Ghostery'],
                    value_name='Count', var_name='Blocking Software')

melted_df.plot('Blocking Software', 'Count')
melted_df.columns[1]
melted_df.head()



#Add average calculations to dataframe
df_copy = df
df_copy["Average_Blocker_Website"] = avgs_website
#df_copy["Average_Blocker_Program"] = avgs_blocker
#df_copy.drop(columns=['Average_Blocker_Website', 'Average_Blocker_Program'], inplace = True)
df_copy.head()

#Troubleshooting Code
df['uBlockOrigin'].mean()
df.drop(columns = ['Average_Blocker_Website', 'Average_Blocker_Program'], inplace = True)
df.mean(axis=0)

df_copy.plot.bar(x = 'Website Names', y = 'Average_Blocker_Website')

#Average blocks per blocker program(Only include tracker columns)
x = df_copy.append(avgs_blocker, ignore_index = True)#adds average values to dataframe
x.drop(columns=['Website Names', 'URL', 'Average_Blocker_Website'], inplace=True)
x.iloc[30].plot.bar(color = ['yellow', 'green', 'red', 'gold', 'purple'])###Pandas picks colors on its own without square brackets


#Average blockers per blocker program in matplot
colors = {'PrivacyBadger' : 'yellow', 'uBlockOrigin' : 'green', "AdBlock" : 'red', 'AdBlock Plus' : 'gold', 'Ghostery' : 'purple'}
plt.title('Average # of Domains Blocked By Blocker')
plt.xlabel('Blocking Software')
plt.xticks(rotation = 90)
plt.bar(df.columns[2:7], avgs_blocker, color = [colors[r] for r in colors])
plt.show()

#==================================Total =========================

combined = pd.concat([df,df2, df3], axis = 0)
#combined.plot.bar(x = 'Name', y = 'PrivacyBadger')

#df.drop(columns = ['Average_Blocker_Website'], inplace = True)

#combined['PrivacyBadger'].mean()


grouped = combined.groupby(combined.index).mean()
# grouped['Website Name'] = df['Name']   #Run to add name column to grouped 
grouped.plot.bar(x = 'Website Name', y = 'PrivacyBadger', color = 'orange', title = 'Average Number of Blocked Domains Reported by Blocker')
grouped.plot.bar(x = 'Website Name', y = 'uBlockOrigin', color = 'green', title = 'Average Number of Blocked Domains Reported by Blocker')
grouped.plot.bar(x = 'Website Name', y = 'AdBlock', color = 'red', title = 'Average Number of Blocked Domains Reported by Blocker')
grouped.plot.bar(x = 'Website Name', y = 'AdBlock Plus', color = 'gold', title = 'Average Number of Blocked Domains Reported by Blocker')
grouped.plot.bar(x = 'Website Name', y = 'Ghostery', color = 'purple', title = 'Average Number of Blocked Domains Reported by Blocker')


#======= Average By Program ==============
sum_grouped = combined.groupby(combined.index).sum() 
adjusted_mean = (sum_grouped.mean() / 3)
adjusted_mean.plot(kind = 'bar', title = 'Average Domains Blocked By Program',
                            xlabel = 'Blocker Program',
                            yticks = [0,2,4,6,8,10,12,14,16,18],
                            color = ['yellow', 'green', 'red', 'gold', 'purple'])




#========Average By Website ===============
avgs_group = (sum_grouped.sum(axis = 1) / 15)
grouped['AVG'] = avgs_group

grouped.plot(kind = 'bar', 
             x = 'Website Name', 
             y = 'AVG',
             yticks = [0,4,8,12,16,20,24,28],
             title = 'Average Number of Domains Blocked')
