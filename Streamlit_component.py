###############################################################################################
# Filename: Streamlit_component
# Owner: Shreyas Sawant
# Purpose of code: Following code handles the front-end part of the Socratic Tutor chatvot.
# Copyright (c) 2024 by Shreyas Sawant All Rights Reserved
# Last modified: 31-05-2024
###############################################################################################

import groq_backend as grq
import streamlit as st

# Web Page configuration.
st.set_page_config(
    page_title = "Socratic tutor",
    page_icon = "💯",
    layout = "wide",
)

st.markdown(
    """
    # Socratic tutor AI chatbot
    \n                                                             -By Shreyas Sawant \n
    
    This is a socratic tutor Chatbot which utilises the Llama3, gemma and mixtral AI models to generate chat output.
    By clicking the "Initiate tutor" button, the model will teach you about 
    the significance of actuators and sensors for Raspberry Pi.
    \n For more information, I recommend you toread the Description page.

    """
)

def main():
    bot = grq.chatbot()

    with st.sidebar:
        select_model = st.selectbox(
                "Change model?",
                ("llama3-8b-8192", "gemma-7b-it", "mixtral-8x7b-32768")
            )
        st.write("Current model:", select_model)

    init_button = st.button("Initiate Tutor")
    prompt_2 = st.chat_input("Say Something")
    
    if prompt_2:
        result = bot.get_solution(prompt_2, select_model)
        for i in range(len(result["prompt"])):
            for j in result:
                if j == "result":
                    st.success(result[j][i])
                else:
                    st.write(result[j][i])
        st.success(result["result"][-1])

    if init_button:
        result = bot.change_subject(select_model)
        st.success(result["result"][0])

if __name__ == '__main__':
    main()
