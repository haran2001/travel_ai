import streamlit as st
import random
import time
import json
from helper_functions import (
    get_llm_answer,
    build_prompt,
    add_logo,
    make_data,
    handle_query,
    display_conversation,
    response_generator,
)


st.title("Travel.ai")

years = ["2023", "2024", "2025"]

logo_url = "assets/images/logo.gif"
st.sidebar.image(logo_url)
user_menu = st.sidebar.radio("Select your age group", ("20s", "30s", "40s", "50+"))

if user_menu == "Page 1":
    pass
"""Your one stop AI assistant for all your travel needs!"""
selected_year = st.sidebar.selectbox("Select Year", years)  # years is list of years

if user_menu == "Page 2":
    pass

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

Rules = "Rules: Rules: \
        List the best places to visit in country ‘X’ \
        Things to pack when visiting country ‘X’ \
        Any special health or visa requirements when visiting country ‘X’ \
        Best ways to convert currencies when visiting country ‘X’ \
        Best way to book travel, hotels and tickets in country ‘X’ \
        Other general tips when visiting country ‘X’ \
        User: I want to travel to India. Make a travel plan. \
        Identify the country that User wants to travel to and give him recommendations based on Rules \
        List best places to visit: \
        What is the best time to visit country ‘X’ \
        Most popular tourist spots in country ‘X’ \
        Hidden gems in country ‘X’"

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

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if (
    prompt := st.chat_input("Where would you like to travel this summer?")
    or button_pressed
):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = response_generator(Rules + prompt)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
