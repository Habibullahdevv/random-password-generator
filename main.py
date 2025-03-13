import streamlit as st;
import random;
import string;



def password_generator(length, use_digit, use_special):
    characters = string.ascii_letters;

    if use_digit:
        characters += string.digits;
    if use_special:
        characters += string.punctuation;

    return ''.join(random.choice(characters) for _ in range(length));
     

st.title("🔐 Password Generator");

st.write("This is a simple password generator that generates a random password based on the length and the characters you want to include in the password.");

length = st.slider("Length of the password", 6, 20, 12);

use_string = st.checkbox("Include numbers in the password");
use_special = st.checkbox("Include special characters in the password");

if st.button("Generate Password"):
    password = password_generator(length, use_string, use_special);
    st.write(f"Your password is: {password}");