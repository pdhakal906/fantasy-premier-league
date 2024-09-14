import streamlit as st
import pandas as pd
import json

with open('download.json', 'r', encoding='utf-8') as file:
    players = json.load(file)

with open("player_history.json", "r", encoding="utf-8") as file:
    history = json.load(file)

players_df = pd.DataFrame(players['elements'])
this_season = pd.DataFrame(history["history"])
past_history_df = pd.DataFrame(history["history_past"])
# df.
st.write("<h1> Players </h1>", unsafe_allow_html=True)
st.write(players_df)
st.write("<h1> This Season </h1>", unsafe_allow_html=True)
st.write(this_season)
st.write("<h1> Past History </h1>", unsafe_allow_html=True)
st.write(past_history_df)


# import streamlit as st
# import pandas as pd
# import json

# # Path to your JSON file
# json_file_path = "download.json"

# # Function to load JSON file
# def load_json(file):
#     with open(file) as f:
#         data = json.load(f)
#     return data

# # Main function to run the Streamlit app
# def main():
#     st.title("JSON to DataFrame Viewer")

#     # Load JSON file
#     data = load_json(json_file_path)

#     # Convert JSON to DataFrame
#     df = pd.json_normalize(data)
#     df = df.drop_duplicates()
#     # Display DataFrame
#     st.write("### DataFrame:")
#     st.dataframe(df)


# if __name__ == "__main__":
#     main()
