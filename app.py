import streamlit as st
import claude as cl

# Initialize session state variables
if "email" not in st.session_state:
    st.session_state.email = ""
    st.session_state.prompt = ""

# Container 1: Image and Title
with st.container():
    st.image("banner.png")
    st.title("BCT1: Business Cyborgs Herrameinta 1")
    st.write("Una herramienta simple y sencilla para escribir correos electrónicos profesionales y claros")

# Container 2: User Input
with st.container():
    if st.session_state.email == "":
        with st.form(key='user_input_form'):
            user_name_input = st.text_input("¿Cómo se llama quién escribe el correo?", key="user_name_input")
            destinatary = st.text_input("¿A quién va dirigido el correo?", key="destinatary")
            user_speech_act = st.selectbox("El propósito principal del correo es hacer:", ['una afirmación','una promesa', 'un requerimiento'], key="user_multiselect_speech_act")
            message_user = st.text_input("¿Cuál es el mensaje central que quieres transmitir?", key="message_user")
            message_tone = st.selectbox("¿Cuál es el tono del mensaje", ['formal','informal', 'neutral', 'urgente'], key="message_tone")
            submit_button_container_2 = st.form_submit_button(label='Enviar')

            if submit_button_container_2 and user_name_input and destinatary and user_speech_act and message_user and message_tone:
                st.session_state.user_name = user_name_input
                st.session_state.prompt = f"Role: You are a communications expert using the speech acts of Fernando Flores. Task: you are going to write an email in Spanish to {destinatary} with the following speech act: {user_speech_act}, with the following {message_tone} the email should transmit the following message {message_user}.\n\n The person that sends the email is: {st.session_state.user_name} Never mention that you use speech acts or that you use a tool to write the email."
                with st.spinner('Escribiendo correo...'):
                    st.session_state.email = cl.send_message(st.session_state.prompt)


## Container 3: Response
with st.container():
    if st.session_state.email != "":
        st.write(f"Aquí está el cuerpo del correo propuesto:")
        st.write(f"{st.session_state.email}")

# Container 4: User Text and Buttons
with st.container():
    if st.session_state.email != "":
        with st.form(key='user_text_form'):
            user_text = st.text_input("¿Qué cambios quiéres hacerle cambios al mensaje?", key="user_text")
            submit_button = st.form_submit_button(label='Enviar')
            reset_button = st.form_submit_button(label='Reiniciar')

            if submit_button and user_text:
                st.session_state.prompt += f" Please change the email with the following instructions: {user_text.strip()} \n\n remember that the email is sent by \n {st.session_state.user_name}. Write only the email content. Never mention that you use speech acts or that you use a tool to write the email."
                with st.spinner('Modificando el correo...'):
                    st.session_state.email = cl.send_message(st.session_state.prompt)
                st.experimental_rerun()

            if reset_button:
                st.session_state.prompt = ""
                st.session_state.email = ""
                st.session_state.user_name = ""
                st.experimental_rerun()