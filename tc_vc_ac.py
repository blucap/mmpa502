#%%
import pandas as pd
import matplotlib.pyplot as plt
#%%
# Create dataframe
data = {
    'Units': [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000],
    'Variable_Cost': [30000, 60000, 90000, 120000, 150000, 180000, 210000, 240000, 270000, 300000, 330000, 360000, 390000],
    'Total_Cost': [530000, 560000, 590000, 620000, 650000, 680000, 710000, 740000, 770000, 800000, 830000, 860000, 890000],
    'Allocated': [80000, 160000, 240000, 320000, 400000, 480000, 560000, 640000, 720000, 800000, 880000, 960000, 1040000],
    'Average_Cost': [530, 280, 197, 155, 130, 113, 101, 93, 86, 80, 75, 72, 68],
    'Marginal_Cost': [30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
}

df = pd.DataFrame(data)

# Graph 1: Total Variable Cost, Total Cost, Allocated
fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(df['Units'], df['Variable_Cost'], marker='o', label='Total Variable Cost')
ax1.plot(df['Units'], df['Total_Cost'], marker='s', label='Total Cost')
ax1.plot(df['Units'], df['Allocated'], marker='^', label='Allocated')
ax1.set_xlabel('Units')
ax1.set_ylabel('Cost ($)')
ax1.set_title('Total Costs vs Units')
ax1.legend()
ax1.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Graph 2: Average and Marginal Cost
fig, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(df['Units'], df['Average_Cost'], marker='o', label='Average Cost')
ax2.plot(df['Units'], df['Marginal_Cost'], marker='s', label='Marginal Cost')
ax2.set_xlabel('Units')
ax2.set_ylabel('Cost ($)')
ax2.set_title('Average and Marginal Cost vs Units')
ax2.legend()
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# %%
