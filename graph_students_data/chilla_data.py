#import liabrary
import pandas as pd


# import data from file

datafile = pd.read_csv("data_viz.csv")
#print(datafile)

# step 1 import Liabraries
import seaborn as sns
import matplotlib.pyplot as plt
# step 2 set a theme
sns.set_theme(style="ticks", color_codes=True)

# Step 3 import data sets
#kashti = sns.load_dataset("titanic")
# print(kashti)

# #step 4 plot basic graph    you can also import your own data
# p = sns.countplot(x="sex", data=kashti   )
# plt.show()

#step 5 plot basic graph  with 2 variables  you can also import your own data with Title
p = sns.countplot(x="Gender", data=datafile , hue="Age")
p.set_title("Tahseen count Plot")
plt.show()