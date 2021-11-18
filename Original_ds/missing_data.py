# based on https://www.justintodata.com/data-cleaning-python-ultimate-guide/
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

matplotlib.rcParams['figure.figsize'] = (30,30)

pd.options.mode.chained_assignment = None

df = pd.read_csv('Original_ds/dataset.csv')

print(df.shape)

cols = df.columns 
colours = ['#000099', '#ffff00'] # yellow = missing data.
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colours))
plt.show()