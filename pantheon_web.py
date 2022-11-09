import numpy as np
import pandas as pd
import streamlit as st
import plotly_express as px

st.title("Project Insight")

st.header("Select the timeline")
#timeline = st.selectbox('',['All', 'Preclassical Era', 'Classical Era', 'Medievel Era', 'Early modern Era', 'Era of Revolutions', 'Information Era'])
timeline = st.multiselect('',['All', 'Preclassical Era', 'Classical Era', 'Medievel Era', 'Early-Modern Era', 'Era of REvolutions', 'Information Era'])
#st.write('The selected timeline is ', timeline)
st.sidebar.header("Project Insight")

df = pd.read_csv('database.csv')
df['birth_year'] = (
    pd.to_numeric(df['birth_year'],
                  errors='coerce')
      .fillna(0)
    )


df_prehistoric = df.loc[df['birth_year'] < -600]
continents_prehistoric = ['Unknown', 'Asia', 'Europe', 'Africa']

df_classical_temp = df.loc[df['birth_year'] < 476]
df_classical = df_classical_temp.loc[df['birth_year']>-600]
continents_classical = ['Europe', 'Unknown', 'Asia', 'Africa',]

if "Preclassical Era" in timeline:
    df = df_prehistoric
    continents = continents_prehistoric
elif "Classical Era" in timeline:
    df = df_classical
    continents = continents_classical

values = df.continent.value_counts()
fig = px.pie(df, values = values, names = continents)
st.plotly_chart(fig)
