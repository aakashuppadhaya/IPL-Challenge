
# coding: utf-8

# In[2]:



# coding: utf-8

# In[24]:


import pandas as pd

import re
from sklearn import  linear_model
#read excel file
#i have created dataset based on https://www.iplt20.com/teams/ each player stats based on year from 2008 to 2018
#created 2018 dataset as test and rest year dataset as train used multiple logistic regression model
df = pd.read_excel('Train.xlsx')
df.rename(columns={'Batting and Fielding': 'Year'}, inplace=True)

#Copying observations where year is not 2018 as training data

train = df[df['Year'] != 2018]

#Copying observations where year is 2018 as test data

test = df[df['Year'] == 2018]

#Deleting special chars from data --> HS and Ave

for i in range(len(train)):
    train['HS'].iloc[i] = int(re.sub("\D", "", str(train['HS'].iloc[i])))

for i in range(len(test)):
    test['HS'].iloc[i] = int(re.sub("\D", "", str(test['HS'].iloc[i])))
    
    
for i in range(len(train)):
    if train['Ave'].iloc[i] == '-':
        train['Ave'].iloc[i] = 0

for i in range(len(test)):
    if test['Ave'].iloc[i] == '-':
        test['Ave'].iloc[i] = 0

#Drop features that we wont use
    
X_train = train.drop(['Year', 'No','player_name','Runs'],axis=1)
Y_train = train['Runs']

X_test = test.drop(['Year', 'No','player_name','Runs' ],axis=1)

#Fit linear Regression model
# Create linear regression object
regr = linear_model.LinearRegression()
regr.fit(X_train,Y_train)





# In[25]:


# Make predictions using the testing set
Y_pred = regr.predict(X_test)

Y=list(Y_pred)
test['run_or_wickets']=Y

test_set=test.sort_values("run_or_wickets",ascending=False)





# In[28]:


test_set=test.sort_values("run_or_wickets",ascending=False)


# In[29]:




# In[33]:
final_csv = pd.DataFrame()


# final_csv = test.csv.head(3)




# In[3]:


test_set[['run_or_wickets']] = test_set[['run_or_wickets']].astype(int)


# In[4]:


final_csv['cap']=['orange','orange','orange']
final_csv['player_name'] = list(test_set['player_name'][0:3])
final_csv['run_or_wickets'] = list(test_set['run_or_wickets'][0:3])



# In[5]:


final_csv.head()


# In[6]:


#building model on bowlers
df = pd.read_excel('Train1.xlsx')
df.rename(columns={'Bowling': 'Year'}, inplace=True)
#Copying observations where year is not 2018 as training data

train_b = df[df['Year'] != 2018]

#Copying observations where year is 2018 as test data

test_b = df[df['Year'] == 2018]

#Deleting special chars from data --> Econ and Ave and SR

for i in range(len(train_b)):
    if train_b['Econ'].iloc[i] == '-':
        train_b['Econ'].iloc[i] = 0
        
for i in range(len(test_b)):
    if test_b['Econ'].iloc[i] == '-':
        test_b['Econ'].iloc[i] = 0
        
        
for i in range(len(train_b)):
    if train_b['SR'].iloc[i] == '-':
        train_b['SR'].iloc[i] = 0      

for i in range(len(test_b)):
    if test_b['SR'].iloc[i] == '-':
        test_b['SR'].iloc[i] = 0
        
for i in range(len(train_b)):
    if train_b['Ave'].iloc[i] == '-':
        train_b['Ave'].iloc[i] = 0
        
for i in range(len(test_b)):
    if test_b['Ave'].iloc[i] == '-':
        test_b['Ave'].iloc[i] = 0
        
#Drop features that we wont use
    
X_train_b = train_b.drop(['Year', 'WKTS','BBM','player_name','top_5'],axis=1)
Y_train_b = train_b['WKTS']

X_test_b = test_b.drop(['Year', 'WKTS','BBM','player_name','top_5'],axis=1)

#Fit linear Regression model 
# Create linear regression object
regr_b = linear_model.LinearRegression()
regr_b.fit(X_train_b,Y_train_b)




# In[7]:


# Make predictions using the testing set
Y_pred = regr_b.predict(X_test_b)

Y=list(Y_pred)
test_b['run_or_wickets']=Y

test_set_b=test_b.sort_values("run_or_wickets",ascending=False)


# In[25]:


test_set_b


# In[8]:


test_set_b[['run_or_wickets']] = test_set_b[['run_or_wickets']].astype(int)


# In[9]:


final_csv1=pd.DataFrame()


# In[10]:


final_csv1['cap']=['purple','purple','purple']
final_csv1['player_name'] = list(test_set_b['player_name'][0:3])
final_csv1['run_or_wickets'] = list(test_set_b['run_or_wickets'][0:3])


# In[ ]:


# creating empty dataframe


# In[11]:


result=pd.DataFrame()


# In[12]:


# code to concatenate two dataframe
frames=[final_csv1,final_csv]

result=pd.concat(frames)


# In[14]:


for i in range(len(result)):
    if result['player_name'].iloc[i] == 'A Tye':
        result['player_name'].iloc[i] = 'Andrew Tye'

for i in range(len(result)):
    if result['player_name'].iloc[i] == 'A Tye':
        result['player_name'].iloc[i] = 'Andrew Tye'
        
        
for i in range(len(result)):
    if result['player_name'].iloc[i] == 'Umesh yadav':
        result['player_name'].iloc[i] = 'Umesh Yadav'

for i in range(len(result)):
    if result['player_name'].iloc[i] == 'Umesh yadav':
        result['player_name'].iloc[i] = 'Umesh Yadav'

for i in range(len(result)):
    if result['player_name'].iloc[i] == 'R Khan':
        result['player_name'].iloc[i] = 'Rashid Khan'

for i in range(len(result)):
    if result['player_name'].iloc[i] == 'R Pant':
        result['player_name'].iloc[i] = 'Rishabh Pant'
        
        
for i in range(len(result)):
    if result['player_name'].iloc[i] == 'KL Rahul':
        result['player_name'].iloc[i] = 'Lokesh Rahul'

for i in range(len(result)):
    if result['player_name'].iloc[i] == 'K Williamson':
        result['player_name'].iloc[i] = 'Kane Williamson'


# In[ ]:


# saving the result in csv file


# In[16]:


result.to_csv('final_result.csv')


# In[15]:


result

