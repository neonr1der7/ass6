# import packages

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')
# show the title

st.title('Titanic App by Lihong Luo')
# read csv and show the dataframe

df = pd.read_csv('train.csv')
st.write(df)
# create a figure with three subplots, size should be (15, 5)
fig, ax = plt.subplots(1,3,figsize=(15, 5))

# show the box plot for ticket price with different classes
df.groupby('Pclass')['Fare'].get_group(1).plot.box(ax=ax[0])
df.groupby('Pclass')['Fare'].get_group(2).plot.box(ax=ax[1])
df.groupby('Pclass')['Fare'].get_group(3).plot.box(ax=ax[2])

# you need to set the x labels and y labels
ax[0].set_xlabel('PClass = 1')
ax[1].set_xlabel('PClass = 2')
ax[2].set_xlabel('PClass = 3')
st.pyplot(fig)

# a sample diagram is shown below

