###############################################################################################
# Filename: Breif_Description
# Owner: Shreyas Sawant
# Purpose of code: Following code provides a description for the Socratic Tutor chatvot.
# Copyright (c) 2024 by Shreyas Sawant All Rights Reserved
# Last modified: 31-05-2024
###############################################################################################

import streamlit as st

# Web Page configuration.
st.set_page_config(
    page_title = "Socratic tutor",
    page_icon = "💯",
    layout = "wide",
)

st.markdown(
    """
    # Socratic Tutor AI Chatbot
    ## What is it?
    The streamlit app that you are using is a chatbot and as the name suggests it uses the Socratic method of teaching.
    It supports the Llama3, gemma and mixtral AI models as of now. 
    You as a user can choose which AI model you want and converse with it. 
    It has two modes of usage:
    1. Regualsr chatbot to whom you can ask any question.
    2. A Socratic tutor who helps you as user to learn a concept of your choice.

    ## How to use it?
    As said above, there are two ways to use it:
    1. Regular Chatbot: As you use the ChatGPT to resolve your doubts, this works in the same fashion, 
                        There is no limit to the size if your prompt. So ask away and get rid of your doubts.
    2. Socratic Tutor:  In a mood for actually learning something? Then this is the real purpose of this app.
                        simply click the initiate tutor button and you will start learning about a pre-defined concept
                        that is the significance of actuators and sensors for Raspberry Pi.
                        However, how can i possibly limit it to that?
                        you can learn the topic of ur chioce by simply telling the Chatbot about your needs
                        and at the end of it you can add something like "Pleas use the Socratic tutor method for this"
                        and thw model will do so.
    
    ## Key Features: 
    * The chatting experience is as smooth as any other.
    * You as a user will be able to view your chat history of the current session as much as you want.
    * You have the ability to change the model on the fly (no need to create another session for another model)

    At the end of it, I am thankful for you to use my app and I hope this was a great learning experience.
    Thank You!! 
    """
)
