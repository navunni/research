import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = "/Users/navunni/Desktop/research/data/dhs-daily-report-updates.csv"
data = pd.read_csv(filepath)

print("Column Names", data.columns)

data['Date of Census'] = pd.to_datetime(data['Date of Census'])
data = data.sort_values('Date of Census')

x = data['Date of Census'].map(pd.Timestamp.toordinal)
y = data['Total Individuals in Shelter']

coefficients = np.polyfit(x, y, 1)
poly = np.poly1d(coefficients)

x_fit = np.linspace(x.min(), x.max(), 100)
y_fit = poly(x_fit)

summary_stats = data.describe()
print (summary_stats)

plt.figure(figsize=(18, 10))
plt.plot(data['Date of Census'], data['Total Individuals in Shelter'], label='Total Individuals in Shelter')
plt.plot(data['Date of Census'], data['Total Single Adults in Shelter'], label='Total Single Adults in Shelter')
plt.plot(data['Date of Census'], data['Total Individuals in Families with Children in Shelter '], label='Total Individuals in Families with Children in Shelter')

plt.xlabel('Census Dates')
plt.ylabel('Number of Individuals')
plt.title('Trends In Shelter Usage Over Time')
plt.legend()
plt.show() 