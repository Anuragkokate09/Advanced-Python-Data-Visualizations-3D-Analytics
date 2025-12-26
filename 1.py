import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Product_Sales_Cat.csv')


# 📊 Pair Plot
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

sns.pairplot(df[numeric_cols], diag_kind='kde')  # diag_kind='kde' for smooth distributions
plt.suptitle("Pair Plot - Multivariate Relationships", y=1.02)
plt.show()

# 💡 Insight:
# Shows relationships between all numerical columns (Price, Quantity, Discount, Revenue).
# Diagonal shows the distribution of each variable.


# 🟠 Bubble Chart (Scatter with Size and Hue)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='Price',
    y='Revenue',
    size='Quantity',          # bubble size
    hue='Category',           # color by category
    palette='Set2',
    sizes=(20, 200)           # min and max bubble size
)

plt.title("Bubble Chart: Price vs Revenue (Size=Quantity, Color=Category)")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2)  # move legend outside
plt.show()

# 💡 Insight:
# Bigger bubbles = higher quantity sold.


# 3D Scatter Plot
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# Load the dataset
df = pd.read_csv('IT_Employees_Info_2000.csv')

# Example: Plot salary, age, and experience in a 3D space
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Define the data
x = df['Experience(Years)']
y = df['Age']
z = df['AnnualSalary']

# Create the 3D scatter plot
ax.scatter(x, y, z, c=z, cmap='seismic')

# Label the axes
ax.set_xlabel('Experience(Years)')
ax.set_ylabel('Age')
ax.set_zlabel('AnnualSalary')

plt.title("3D Scatter Plot: Experience vs Age vs Salary")
plt.show()

# Sequential colormaps (good for data that goes from low to high):
# 'viridis' (default, great for most uses)

#######################################################################

import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# Load data
df = pd.read_csv('IT_Employees_Info_2000.csv')

# Prepare figure
fig = plt.figure(figsize=(8, 10))
ax = fig.add_subplot(111, projection='3d')

# Set unique color for each department
colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'brown'] # Add more if needed
departments = df['Department'].unique()

# Plot each department separately
for i, dept in enumerate(departments):
    data = df[df['Department'] == dept]
    ax.scatter(
        data['Experience(Years)'],
        data['Age'],
        data['AnnualSalary'],
        color=colors[i % len(colors)],
        label=dept,
        s=50
    )

# Labels and title
ax.set_xlabel('Experience (Years)')
ax.set_ylabel('Age')
ax.set_zlabel('AnnualSalary')
plt.title('3D Scatter Plot by Department')
ax.legend(title='Department')
plt.tight_layout()
plt.show()

#5. Stacked Bar Chart (e.g., Gender-wise Count per Department)
# Group data
stacked_data = df.groupby(['Department', 'Gender']).size()

# Plot
stacked_data.plot(kind='bar', stacked=False, figsize=(10, 6), colormap='viridis')
plt.title('Stacked Bar Chart: Gender Distribution per Department')
plt.ylabel('Number of Employees')
plt.tight_layout()
plt.show()
