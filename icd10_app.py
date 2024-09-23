
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('df.csv', usecols = ["code", "diagnosis", "use", "year"])


st.title("ICD-10 HES Usage Visualiser")

# User input
icd10_code = st.text_input("Enter the ICD-10 Code:", value="A000")

# Filtered df
filtered_df = df[df['code'] == icd10_code]

if not filtered_df.empty:
    # Slider
    min_year = int(filtered_df['year'].min())
    max_year = int(filtered_df['year'].max())
    year_range = st.slider("Select Year Range:", min_value=min_year, max_value=max_year, value=(min_year, max_year))

    # Filter df by years
    filtered_df = filtered_df[(filtered_df['year'] >= year_range[0]) & (filtered_df['year'] <= year_range[1])]

    # Display
    st.write(filtered_df[['year', 'use']])

    # Plot
    fig, ax = plt.subplots()
    ax.plot(filtered_df['year'], filtered_df['use'], marker='o')
    ax.set_xlabel('Year')
    ax.set_ylabel('Usage in HES')
    ax.set_title(f'HES Usage over time for {icd10_code}')
    st.pyplot(fig)
else:
    st.write("No such code.")

