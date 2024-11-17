import streamlit as st
import pickle
import pandas as pd

# Define hybrid_recommendations function here (simplified version)
def hybrid_recommendations(input_song_name, num_recommendations=5):
    if input_song_name not in music_df['Track Name'].values:
        return pd.DataFrame()  # Return empty DataFrame if song not found
    # Example: Just return top 5 songs (for simplicity)
    return music_df.head(num_recommendations)

# Load the saved model and dataset
with open("data.pkl", "rb") as data_file:
    music_df = pickle.load(data_file)

# Mock `hybrid_model` as hybrid_recommendations directly for simplicity
hybrid_model = hybrid_recommendations

# Streamlit app
st.title("Hybrid Song Recommendation System")
st.write("Enter a song name to get recommendations.")

# Input field for the song name
input_song_name = st.text_input("Enter the name of the song:")

# Recommendation button
if st.button("Get Recommendations"):
    if input_song_name in music_df['Track Name'].values:
        # Call the hybrid recommendation function
        recommendations = hybrid_model(input_song_name, num_recommendations=5)

        if not recommendations.empty:
            st.write(f"Here are 5 song recommendations based on '{input_song_name}':")
            
            # Display recommendations with details
            for idx, row in recommendations.iterrows():
                st.subheader(f"Track Name: {row['Track Name']}")
                st.write(f"Artists: {row['Artists']}")
                st.write(f"Album Name: {row['Album Name']}")
                st.write(f"Release Date: {row['Release Date']}")
                st.write(f"Popularity Score: {row['Popularity']}")
                st.write("---")
        else:
            st.write("No recommendations found. Try another song.")
    else:
        st.write(f"'{input_song_name}' is not found in the dataset. Please try another song.")
