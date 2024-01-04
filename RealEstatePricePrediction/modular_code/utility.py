import json
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import base64

def login(func):
    with open('./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    # hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
    # st.write(hashed_passwords)

    authenticator.login('Sign-In', 'main')

    if st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

    if st.session_state["authentication_status"]:
        with st.sidebar:
            authenticator.logout('Sign Out', 'main', key='unique_key')
            st.write(f'Welcome {st.session_state["name"]} 🤗')

    def execute(*args, **kwargs):
        func(*args, **kwargs)
    return execute