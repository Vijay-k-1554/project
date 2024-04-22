import streamlit as st
import pandas as pd

# Load the updated dataset
try:
    data = pd.read_csv("combined_exercises.csv")
except FileNotFoundError:
    st.error("Error: File 'updated_combined_exercises.csv' not found.")
    st.stop()

# Create age selection widget
age_options = data['Age Group'].unique()
age = st.selectbox("Select Age Group:", age_options)

# Filter based on age
filtered_data = data[data['Age Group'] == age]

# Create location selection widget
location_options = ("Without Equipment", "With Equipment")
location = st.radio("Select Type:", location_options)

# Filter based on location
if location == "Without Equipment":
    filtered_data = filtered_data[filtered_data['Home'] == 'Yes']
else:
    filtered_data = filtered_data[filtered_data['Home'] == 'No']

# Create experience selection widget
experience_options = ("Beginner", "Intermediate", "Advanced")
experience = st.selectbox("Select Experience Level:", experience_options)

# Filter based on experience
filtered_data = filtered_data[filtered_data['Experience'] == experience]

# Create exercise type selection widget
exercise_type_options = filtered_data['Type'].unique()
exercise_type = st.selectbox("Select Exercise Type:", exercise_type_options)

# Filter the dataset based on user input
if exercise_type == "Muscle Growth":
    muscle_type_options = filtered_data[filtered_data['Type'] == 'Muscle Growth']['Muscle'].unique()
    muscle_type = st.selectbox("Select Muscle Group:", muscle_type_options)

    filtered_data = filtered_data[(filtered_data['Type'] == exercise_type) & (filtered_data['Muscle'] == muscle_type)]
else:
    filtered_data = filtered_data[filtered_data['Type'] == exercise_type]

# Create health selection widget
health_options = ("Yes", "No")
health = st.selectbox("Any Health Issues?", health_options)

# Filter based on health
filtered_data = filtered_data[filtered_data['Health'] == health]

# Display the filtered results
if filtered_data.empty:
    st.warning("No exercises found based on the selected criteria.")
else:
    st.write("Recommended Exercises:")
    st.write(filtered_data[['Exercise', 'No. of Reps/Duration', 'No. of Sets', 'Home']])
