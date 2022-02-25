#!/usr/bin/env python
# coding: utf-8

# In[70]:


import matplotlib.pyplot as plt
import numpy as np

data = open("Lab_6_STAT2mutations.csv", "r")

# Types
amino_acids = ['R', 'H', 'K', 'D', 'E', 'S', 'T', 'N', 'Q', 'C', 'G', 'P', 'A', 'V', 'I', 'L', 'M', 'F', 'Y', 'W']

charged = ['R', 'H', 'K', 'D', 'E']

uncharged_polar = ['S', 'T', 'N', 'Q']

uncharged_nonpolar = ['A','V', 'I', 'L', 'M', 'F', 'Y', 'W']

special = ['C', 'G', 'P']

# Protein Domains 
STAT2_domains = [1, 141, 316, 475, 556, 706, 786, 838, 851]

# Protein Domain Names 
domains = ['NTD', 'CC', 'DBD', 'Linker', 'SH2', 'Undef 1','TAD', 'Undef 2']

# Results Groups
change_charge = []

change_polarity = []

change_special = []

# Aggregate Groups

nonpolarTransGroup = special + uncharged_nonpolar

polarTransGroup = charged + uncharged_polar  


# Remove Header 
data.readline()

# Read Data
for line in data: 
    aas = line.split(',')[0]
    original_aa = aas[:1]
    aa_number = aas[1:-1]
    new_aa = aas[-1:]
    if original_aa in charged and new_aa not in charged:
        change_charge.append(aas)
    if original_aa not in charged and new_aa in charged:
        change_charge.append(aas)
    if original_aa in nonpolarTransGroup and new_aa in polarTransGroup: 
        change_polarity.append(aas)
    if original_aa in polarTransGroup and new_aa in nonpolarTransGroup:
        change_polarity.append(aas)
    #only count if substitution is special amino acid to not special 
    if original_aa in special and new_aa not in special: 
        change_special.append(aas)
data.close()

# Process Data
change_charge_counts = [0]*8

change_polarity_counts = [0]*8

change_special_counts = [0]*8

for i in range(0,len(STAT2_domains)-1):
    lowerBound = STAT2_domains[i]
    upperBound = STAT2_domains[i+1]
    for aas in change_charge: 
        aa_number = int(aas[1:-1])
        if aa_number <= upperBound and aa_number > lowerBound: 
            change_charge_counts[i] += 1
    for aas in change_polarity: 
        aa_number = int(aas[1:-1])
        if aa_number <= upperBound and aa_number > lowerBound: 
            change_polarity_counts[i] += 1
    for aas in change_special: 
        aa_number = int(aas[1:-1])
        if aa_number <= upperBound and aa_number > lowerBound: 
            change_special_counts[i] += 1

# Plot Data 
bottom_special = [0]*8
for i in range(0,len(bottom_special)-1):
    bottom_special[i] += change_polarity_counts[i]
    bottom_special[i] += change_charge_counts[i]

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(domains, change_charge_counts)
ax.bar(domains, change_polarity_counts, bottom=change_charge_counts)
ax.bar(domains, change_special_counts, bottom=bottom_special)
ax.set_xlabel("STAT2 Domain")
ax.set_ylabel("Number of Changes")
ax.set_title("Types of Amino Acid Substitution by STAT2 Domain")
ax.set_yticks(np.arange(0, 50, 10))
ax.legend(labels=['Change in Charge', 'Change in Polarity', 'Change in Special'])
plt.show()

