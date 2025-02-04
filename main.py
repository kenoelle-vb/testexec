import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
input_df = pd.DataFrame({
    'A': range(1, 101),
    'B': [i * 0.1 for i in range(1, 101)],
    'C': [i * 10 for i in range(1, 101)],
    'D': [i * 100 for i in range(1, 101)],
    'E': [i * 1000 for i in range(1, 101)]
})

# Function to create the bar plot
def plot_bar(df, jpg_name):
    columns = df.columns
    values = df.sum()
    plt.figure(figsize=(10, 6))
    plt.bar(columns, values)
    plt.xlabel('')
    plt.ylabel('Sum')
    plt.title('')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(jpg_name)
    plt.show()

# Streamlit app
st.title("Customizable Bar Plot")

# Text input for plot name
name = st.text_input("Enter plot name", "Amazingness Plot")

# Button to generate plot
if st.button("Generate Plot"):
    jpg_name = f'{name}.jpg'
    plot_bar(input_df, jpg_name)
    
    # Download button
    with open(jpg_name, "rb") as file:
        btn = st.download_button(
            label="Download plot",
            data=file,
            file_name=jpg_name,
            mime="image/jpeg"
        )
