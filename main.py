import streamlit as st;
import random;
import string;
import re;


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
    strength_password = st.success(f"Your password is: {password}");

    score : int = 0;

    if length >= 8:
        score += 1;        
    else:
        st.warning("❌ Password must be 8 characters long or more.");
    
    if re.search(r"\d", password):
        score += 1;
    else:
        st.warning("❌ Too Week password, must contain at least one number.");
  
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1;
    else:
        st.warning("❌ Too Week password, must contain both uppercase and lowercase letters.");

    if re.search(r"[!@#$%^&*()_+=><;:.,?/|]", password):
        score += 1;
    else:
        st.warning("❌ Too Week password, must contain at least one special character.");


    if score == 4:
        st.success("💪 Strong password.");

    elif score == 3:
        print("⚠️ Moderate Password - Consider adding more security features.")
    else:
        print("❌ Weak Password - Improve it using the suggestions above.")

