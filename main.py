import pandas as pd
import numpy as np
from datetime import datetime

# Load the csv file
df = pd.read_csv("~/Downloads/Sp 23 Registration.csv")

# Apply the helper function to the 'Age' column
df['Age'] = df['Age'].apply(convert_age)

# Replace non-finite 'Age' values with 'None'
df['Age'] = df['Age'].apply(lambda x: None if not np.isfinite(x) else x)

# Convert the 'Age' column to integer
df['Age'] = df['Age'].astype(float).astype('Int64')

# Group by 'Site' and 'Age', and get the size of each group
grouped = df.groupby(['Site','Age']).size()

# Define age groups and get counts per site
age_group1_per_site = grouped.groupby(level=0).apply(lambda x: sum(x[i] for i in x.index if i[1] <= 8))
age_group2_per_site = grouped.groupby(level=0).apply(lambda x: sum(x[i] for i in x.index if 9 <= i[1] <= 10))
age_group3_per_site = grouped.groupby(level=0).apply(lambda x: sum(x[i] for i in x.index if i[1] >= 11))

# Combine results into a dataframe
counts_per_site = pd.DataFrame({
    '8 and under': age_group1_per_site,
    '9 to 10': age_group2_per_site,
    '11 and older': age_group3_per_site
})

# Print the result
print(counts_per_site)
