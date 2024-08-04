import streamlit as st
import random
import time
import json
from helper_functions import get_llm_answer, build_prompt, add_logo, make_data, handle_query, display_conversation, response_generator


st.title("Travel.ai")

years=['2023', '2024', '2025']

logo_url = "https://upload.wikimedia.org/wikipedia/commons/c/c3/Ambigram_Travel_%28navy_blue_-_animated%29.gif"
st.sidebar.image(logo_url)
user_menu = st.sidebar.radio(
"Select your age group",
("20s","30s","40s", "50+")
)

if user_menu == "Page 1":
    pass
#your page content, filters etc
'''Your one stop AI assistant for all your travel needs!'''
selected_year = st.sidebar.selectbox("Select Year",years) #years is list of years

if user_menu == "Page 2":
    pass
#your page content, filters etc

st.divider()

# Example prompts
example_prompts = [
    "How do I plan a trip to India?",
    "What are some interesting places to visit in Dubai?",
    "What things should I pack before leaving for a long trip?",
    "What are the best places to travel to during the summer?",
    "Make me a 3 day plan to Goa.",
    "What are the top 3 places to visit in my 20s?",
]

example_prompts_help = [
    "Look for a specific card effect",
    "Search for card type: 'Vampires', card color: 'black', and ability: 'flying'",
    "Color cards and card type",
    "Specifc card effect to another mana color",
    "Search for card names",
    "Search for card types with specific abilities",
]

button_cols = st.columns(3)
button_cols_2 = st.columns(3)

button_pressed = ""

if button_cols[0].button(example_prompts[0], help=example_prompts_help[0]):
    button_pressed = example_prompts[0]
elif button_cols[1].button(example_prompts[1], help=example_prompts_help[1]):
    button_pressed = example_prompts[1]
elif button_cols[2].button(example_prompts[2], help=example_prompts_help[2]):
    button_pressed = example_prompts[2]

elif button_cols_2[0].button(example_prompts[3], help=example_prompts_help[3]):
    button_pressed = example_prompts[3]
elif button_cols_2[1].button(example_prompts[4], help=example_prompts_help[4]):
    button_pressed = example_prompts[4]
elif button_cols_2[2].button(example_prompts[5], help=example_prompts_help[5]):
    button_pressed = example_prompts[5]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Where would you like to travel this summer?") or button_pressed:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
