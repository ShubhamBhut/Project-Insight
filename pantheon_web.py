import numpy as np
import pandas as pd
import streamlit as st
import plotly_express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Project Insight")

st.header("Select the timeline")
#timeline = st.selectbox('',['All', 'Preclassical Era', 'Classical Era', 'Medievel Era', 'Early modern Era', 'Era of Revolutions', 'Information Era'])
timeline = st.multiselect('',['All', 'Preclassical Era', 'Classical Era', 'Medievel Era', 'Early-Modern Era', 'Era of REvolutions', 'Information Era'], ['All'])
#st.write('The selected timeline is ', timeline)
st.sidebar.header("Project Insight")

df = pd.read_csv('database.csv')
df['birth_year'] = (
    pd.to_numeric(df['birth_year'],
                  errors='coerce')
      .fillna(0)
    )
continents = ['Europe', 'North America', 'Asia', 'Africa', 'Unknown', 'South America', 'Ocenia']

df_prehistoric = df.loc[df['birth_year'] < -600]
continents_prehistoric = ['Unknown', 'Asia', 'Europe', 'Africa']

df_classical_temp = df.loc[df['birth_year'] < 476]
df_classical = df_classical_temp.loc[df['birth_year']>-600]
continents_classical = ['Europe', 'Unknown', 'Asia', 'Africa',]

df_medievel_temp = df.loc[df['birth_year'] < 1450]
df_medievel = df.loc[df['birth_year'] > 476]



if "Preclassical Era" in timeline:
    df = df_prehistoric
    continents = continents_prehistoric
elif "Classical Era" in timeline:
    df = df_classical
    continents = continents_classical

values = df.continent.value_counts()
fig1 = px.pie(df, values = values, names = continents)
fig2 = px.bar(df, x=continents, y=values)
fig3 = px.strip(df, x='continent', y='birth_year', color='sex')
#fig4 = px.bar(df, x='industry', y=df.industry.value_counts())

fig5 = plt.figure(figsize=(14,9))
ax = sns.countplot(x='industry',data=df, order=df.industry.value_counts().iloc[:15].index)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
ax.set(facecolor="black")
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
fig5.patch.set_facecolor('black')
plt.tight_layout()

fig6 = px.scatter(df, x='birth_year', y='historical_popularity_index', color='sex')



st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
#st.plotly_chart(fig4)
st.pyplot(fig5)
st.plotly_chart(fig6)





