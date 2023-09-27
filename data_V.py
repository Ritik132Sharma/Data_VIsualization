import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('C:\\Users\\Admin\\Downloads\\Mall_Customers.csv')
print(df.head())


'''Line plot'''

plt.figure(figsize=(8,6))
plt.plot(df['Age'],df['Annual Income (k$)'],label = 'Line Plot')
plt.title("Mall customer")
plt.ylabel("Age")
plt.xlabel("Annual Income (k$)")
plt.show()


'''area plot'''

plt.fill_between(df.index,df['Age'],df['Annual Income (k$)'])
plt.figure(figsize=(8,6))
plt.title("Mall customer")
plt.ylabel("Age")
plt.xlabel("Annual Income (k$)")
plt.show()

'''histogram'''

df.index = df.index.map(int)
df.iloc[:,4].plot(kind='hist',stacked=False,figsize=(8, 6))
plt.title("Mall customer")
plt.ylabel("Age")
plt.xlabel("Annual Income (k$)")
plt.show()

'''bar plot'''

counts = df['Genre'].value_counts()
counts.plot(kind='bar',stacked=False,figsize=(8, 6))
plt.title("Mall customer")
plt.ylabel("Age")
plt.xlabel("Annual Income (k$)")
plt.show()

'''pie chart'''

counts = df['Genre'].value_counts()
plt.pie(counts, labels=counts.index, autopct='%2.1f%%')
plt.axis('equal')
plt.title('Gender Distribution')
plt.show()


'''box plot'''

df.plot(kind='box')
plt.title("Mall customer")
plt.ylabel("Age")
plt.xlabel("Annual Income (k$)")
plt.show()

'''scatter plot'''

df.plot(x='Age',y='Annual Income (k$)',kind='scatter')
plt.title("Mall customer")
plt.ylabel("Age")
plt.xlabel("Annual Income (k$)")
plt.show()


'''Regression plot'''

sns.regplot(x='Age',y='Annual Income (k$)',data=df)
plt.title("Mall customer")
plt.ylabel("Age")
plt.xlabel("Annual Income (k$)")
plt.show()


























