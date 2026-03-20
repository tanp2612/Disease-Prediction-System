import pickle
import pathlib

import streamlit_authenticator as stauth 

names = ["Peter Parker", "Mary Jane"]
usernames =["pparker", "MJ"]
passwords = ["abc123", "def456"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = pathlib.Path(__file__).parent / 'hashed_pw.pkl'
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)