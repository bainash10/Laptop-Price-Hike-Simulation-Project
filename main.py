import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the random seed for reproducibility
np.random.seed(42)

# Generate random data
months = pd.date_range(start='2023-01-01', periods=12, freq='M')
prices = np.random.uniform(low=800, high=1500, size=len(months))

# Create a DataFrame
data = pd.DataFrame({'Month': months, 'Price': prices})

# Create a figure and a set of subplots
fig, axs = plt.subplots(3, 2, figsize=(15, 18))

# Line Graph
axs[0, 0].plot(data['Month'], data['Price'], marker='o', linestyle='-', color='b')
axs[0, 0].set_title('Laptop Price Hike Over Time - Line Graph')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Price (USD)')
axs[0, 0].grid(True)

# Bar Graph
axs[0, 1].bar(data['Month'].dt.strftime('%Y-%m'), data['Price'], color='c')
axs[0, 1].set_title('Laptop Price Hike Over Time - Bar Graph')
axs[0, 1].set_xlabel('Month')
axs[0, 1].set_ylabel('Price (USD)')
axs[0, 1].tick_params(axis='x', rotation=45)

# Scatter Plot
axs[1, 0].scatter(data['Month'], data['Price'], color='m')
axs[1, 0].set_title('Laptop Price Hike Over Time - Scatter Plot')
axs[1, 0].set_xlabel('Month')
axs[1, 0].set_ylabel('Price (USD)')
axs[1, 0].grid(True)

# Histogram
axs[1, 1].hist(data['Price'], bins=10, color='g', edgecolor='k')
axs[1, 1].set_title('Distribution of Laptop Prices - Histogram')
axs[1, 1].set_xlabel('Price (USD)')
axs[1, 1].set_ylabel('Frequency')

# Box Plot
sns.boxplot(data['Price'], color='y', ax=axs[2, 0])
axs[2, 0].set_title('Distribution of Laptop Prices - Box Plot')
axs[2, 0].set_xlabel('Price (USD)')

# Remove the empty subplot (bottom right corner)
fig.delaxes(axs[2, 1])

# Adjust layout
plt.tight_layout()
plt.show()
