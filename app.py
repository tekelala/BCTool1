import streamlit as st
import claude as cl

# Initialize session state variables
if "email" not in st.session_state:
    st.session_state.email = ""
    st.session_state.prompt = ""

# Container 1: Image and Title
with st.container():
    st.image("banner.png")
    st.title("BCT1: Business Cyborgs Tool 1")
    st.write("A simple and powerful tool to write professional and clear emails")

# Container 2: User Input
with st.container():
    if st.session_state.email == "":
        with st.form(key='user_input_form'):
            user_name = st.text_input("What is your name:", key="user_name")
            destinatary = st.text_input("Who will receive this email:", key="destinatary")
            user_speech_act = st.selectbox("The main purpose of the message is to make:", ['an assertion','a promise', 'a request'], key="user_multiselect_speech_act")
            message_user = st.text_input("What is the core message you want to send:", key="message_user")
            message_tone = st.selectbox("What is the tone of the message:", ['formal','informal', 'neutral', 'urgent'], key="message_tone")
            submit_button_container_2 = st.form_submit_button(label='Send')

            if submit_button_container_2 and user_name and destinatary and user_speech_act and message_user and message_tone:
                st.session_state.prompt = f"role: you are a communications expert using the speech acts of Fernando Flores \n  you are going to write an email to {destinatary} with the following speech act: {user_speech_act}, with the following {message_tone} to deliver the following message {message_user}.\n\nBest regards,\n\n {user_name}"
                st.session_state.email = cl.send_message(st.session_state.prompt)

# Container 3: Response
with st.container():
    if st.session_state.email != "":
        st.write(f"Here is the email that was generated:")
        st.write(f"{st.session_state.email}")

# Container 4: User Text and Buttons
with st.container():
    if st.session_state.email != "":
        with st.form(key='user_text_form'):
            user_text = st.text_input("Do you want me to make any change to the message?", key="user_text")
            submit_button = st.form_submit_button(label='Send')
            reset_button = st.form_submit_button(label='Restart')

            if submit_button and user_text:
                st.session_state.prompt += f"Please change the email as follows: {user_text}"
                st.session_state.email = cl.send_message(st.session_state.prompt)
                st.experimental_rerun()

            if reset_button:
                st.session_state.prompt = ""
                st.session_state.email = ""
                st.experimental_rerun()
