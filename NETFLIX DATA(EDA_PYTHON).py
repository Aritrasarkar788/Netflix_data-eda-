#!/usr/bin/env python
# coding: utf-8

# # EDA of Netflix Data on Python

# In[1]:


#importing libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# reading our dataset
df = pd.read_csv('C:\\Users\\ARITRA\Downloads\\netflix_titles.csv')
df.head(20)


# In[3]:


df.shape # tells us the rows and columns of the dataset


# In[4]:


df.describe() # tells us some basic statistics about or columns


# In[5]:


df.info() # shows the count and datatypes of our columns


# ## Missing Values

# In[6]:


df.isna().sum()


# In[7]:


#convert integer to float
df['runtime'] = df['runtime'].astype(float)


# In[8]:


df.head(20)


# ## Handling Missing Values

# In[9]:


# Filling the nan values.
df.fillna({'title':'unavailable', 'description':'unavailable', 'age_certification':'All_Age', 'seasons':'unavailable', 'imdb_id':'unavailable', 'imdb_score':'unavailable', 'imdb_votes':'unavailable', 'tmdb_popularity':'unavailable', 'tmdb_score':'unavailable'}, inplace = True)
df.isna().sum()


# In[10]:


df[df.release_year == 1980].head(20)


#  ### VISUALIZATIONS

# In[11]:


df.type.value_counts() #value_counts shows the count of different categories in a given column


# In[12]:


sns.countplot(x = 'type', data = df) #countplot helps us to plot counts of each category
plt.title('Count vs Type of Shows')


# Its's clearly visible that there are more movies compared to shows in Netflix

# #### Country Analysis

# In[13]:


df['production_countries'].value_counts().head(20)


# In[14]:


plt.figure(figsize = (12, 6))
sns.countplot(y ='production_countries', order = df['production_countries'].value_counts().index[:20], data = df)
plt.title('Countrywise Content on Netflix')


# In[15]:


plt.figure(figsize = (9,6))
sns.countplot(x = 'tmdb_score', order = df['tmdb_score'].value_counts().index[:20], data = df)
plt.title('Scores of netflix shows vs counts')


# In[16]:


df.release_year.value_counts()[:20]


# In[17]:


# Highest number of contents released in each year
plt.figure(figsize = (12,6)) 
sns.countplot(x= 'release_year', order = df['release_year'].value_counts().index[0:20], data = df)
plt.title('Content released in years on netflix')


# In[18]:


# Visualization of the Age certification of the contents
plt.figure(figsize = (12,7))
sns.countplot(x = 'age_certification', order = df['age_certification'].value_counts().index[0:20], data = df)
plt.title('Age certification of the contents')


# ### Popular genres of Netflix shows

# In[19]:


plt.figure(figsize = (12,9))
sns.countplot(y = 'genres', order = df['genres'].value_counts().index[0:20], data = df)
plt.title('Top 20 Genres of Netflix shows')


# ## Summary

# We have performed some operstions to find out some very useful information. The important findings from the analysis are listed below
#  1. Netflix has more movies than shows
#  2. Most number of Netflix contents were released by US followed by India and Japan.
#  3. Most of contents are for people of all age group, followed by Mature Audiences.
#  4. 2019 has the maximum number of contents released by Netflix.
#  5. Comedy is the most popular genre in Netflix.
