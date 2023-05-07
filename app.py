import streamlit as st
import claude as cl

# Initialize session state variables
if "email" not in st.session_state:
    st.session_state.email = ""
    st.session_state.prompt = ""
    st.session_state.user_name_input = ""
    st.session_state.destinatary = ""
    st.session_state.user_multiselect_speech_act = ""
    st.session_state.message_user = ""
    st.session_state.message_tone = ""

# Container 1: Image and Title
with st.container():
    st.image("banner.png")
    st.title("BCT1: Business Cyborgs Tool 1")
    st.write("A simple and powerful tool to write professional and clear emails")

# Container 2: User Input
with st.container():
    if st.session_state.email == "":
        st.session_state.user_name_input = st.text_input("What is your name:", value=st.session_state.user_name_input, key="user_name_input")
        st.session_state.destinatary = st.text_input("Who will receive this email:", value=st.session_state.destinatary, key="destinatary")
        st.session_state.user_multiselect_speech_act = st.selectbox("The main purpose of the message is to make:", ['an assertion','a promise', 'a request'], key="user_multiselect_speech_act")
        st.session_state.message_user = st.text_input("What is the core message you want to send:", value=st.session_state.message_user, key="message_user")
        st.session_state.message_tone = st.selectbox("What is the tone of the message:", ['formal','informal', 'neutral', 'urgent'], key="message_tone")
        submit_button_container_2 = st.button(label='Send')

        if submit_button_container_2 and st.session_state.user_name_input.strip() and st.session_state.destinatary.strip() and st.session_state.user_multiselect_speech_act and st.session_state.message_user.strip() and st.session_state.message_tone:
            st.session_state.user_name = st.session_state.user_name_input.strip()
            st.session_state.prompt = f"You are a communications expert using the speech acts of Fernando FLores and you are going to write an email to {st.session_state.destinatary.strip()} with the following speech act: {st.session_state.user_multiselect_speech_act}, with the following {st.session_state.message_tone} tone. The email should transmit the following message {st.session_state.message_user.strip()}.\n\nBest regards,\n\n {st.session_state.user_name} Never mention that you use speech acts or that you use a tool to write the email."
            with st.spinner('Generating email...'):
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

            if submit_button and user_text.strip():
                st.session_state.prompt += f" Please change the email as follows: {user_text.strip()} \n\n remember that the email is sent by \n {st.session_state.user_name}. Write only the email content. Never mention that you use speech acts or that you use a tool to write the email."
                with st.spinner('Modifying email...'):
                    st.session_state.email = cl.send_message(st.session_state.prompt)
                # Clear the text input after hitting send
                user_text = ""

            if reset_button:
                st.session_state.prompt = ""
                st.session_state.email = ""
                st.session_state.user_name = ""
                st.session_state.user_name_input = ""
                st.session_state.destinatary = ""
                st.session_state.user_multiselect_speech_act = ""
                st.session_state.message_user = ""
                st.session_state.message_tone = ""




