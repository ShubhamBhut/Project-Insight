import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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

if "Preclassical Era" in timeline:
    df_prehistoric = df.loc[df['birth_year'] < -600]
    continents_prehistoric = ['Unknown', 'Asia', 'Europe', 'Africa',]
    values = df_prehistoric.continent.value_counts()
    fig = px.pie(df_prehistoric, values=values, names=continents_prehistoric)
    st.plotly_chart(fig, use_container_width=True)
else:
    df = df
    st.write("You can select or unselect desired continents by clicking on their names")
    values = df.continent.value_counts()
    continents = ['Europe', 'North America', 'Asia', 'Africa', 'Unknown', 'South America', 'Ocenia']
    fig = px.pie(df, values=values, names=continents)
    st.plotly_chart(fig, use_container_width=True)
