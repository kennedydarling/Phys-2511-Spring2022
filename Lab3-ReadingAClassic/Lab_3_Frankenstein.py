#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np 

import matplotlib as mpl

import matplotlib.pyplot as plt 


# In[67]:


frankenstein = open('Frankenstein.txt','r')

chapters = frankenstein.read().split('Chapter')

frankenstein.close()

chapterNumber = 1

names = ['Victor', 'creature', 'Agatha', 'Caroline', 'Lacey', 'Elizabeth','Ernest', 'Felix', 'Henry', 'Justine','William']

chapters = chapters[1:]

for chapter in chapters:
    scores = [0] * len(names) 
    print("Chapter Number:" + str(chapterNumber))
    chapterNumber = chapterNumber + 1 
    for line in chapter.split('\n'): 
        for phrase in line.split():
            y = 0
            for character in names:
                if character in phrase: 
                    scores[y] = scores[y] + 1
                y = y + 1
            
    print(scores)

scores = [0] * len(names) 

for chapter in chapters:
    for line in chapter.split('\n'): 
        for phrase in line.split():
            y = 0
            for character in names:
                if character in phrase: 
                    scores[y] = scores[y] + 1
                y = y + 1

print('Total Number of Appearances')

print(scores)


# In[65]:


Characters = ['Victor', 'creature', 'Agatha', 'Caroline', 'De Lacey', 'Elizabeth','Ernest', 'Felix', 'Henry', 'Justine','William']

Number_Appearances = [28, 69, 22, 3, 9, 92, 13, 50, 26, 55, 25]

fig = plt.figure(figsize = (15, 5))
plt.bar(Characters, Number_Appearances, color = 'green')
plt.title('Total Number of Appearances of Each Character in Frankenstein', fontsize = 14)
plt.xlabel('Character', fontsize = 14)
plt.ylabel('Total Number of Appearances', fontsize = 14)
plt.show()

