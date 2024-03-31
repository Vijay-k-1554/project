import streamlit as st
import pandas as pd

# Load the combined dataset
data = pd.read_csv("combined_exercises.csv")

# Create age, location, and exercise type selection widgets
age = st.selectbox("Select Age Group:", data['Age Group'].unique())
location = st.radio("Select Location:", ("HOME", "GYM"))
exercise_type = st.selectbox("Select Exercise Type:", data['Type'].unique())

# Filter the dataset based on user input
if location == "HOME":
    filtered_data = data[(data['Age Group'] == age) & (data['Type'] == exercise_type) & (data['Home'] == 'Yes')]
else:
    filtered_data = data[(data['Age Group'] == age) & (data['Type'] == exercise_type) & (data['Home'] == 'No')]

# Display the filtered results
st.write("Recommended Exercises:")
st.write(filtered_data[['Exercise', 'No. of Reps', 'No. of Sets', 'Home']])
