import streamlit as st
import random
import string
import re

def password_generator(length, use_digit, use_special):
    characters = string.ascii_letters
    if use_digit:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def suggest_strong_password():
    suggested_password = password_generator(12, True, True)
    return suggested_password

st.title("AI Password Generator 🔐")

st.write("This is a simple password generator that generates a random password based on the length and the characters you want to include in the password.")

length = st.slider("Length of the password", 6, 20, 12)
use_digit = st.checkbox("Include numbers in the password")
use_special = st.checkbox("Include special characters in the password")

if st.button("Generate Password"):
    password = password_generator(length, use_digit, use_special)
    st.success(f"Your password is: {password}")

    score = 0
    warnings = []

    if length >= 8:
        score += 1
    else:
        warnings.append("❌ Password must be 8 characters long or more.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        warnings.append("❌ Too weak - must contain at least one number.")
  
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        warnings.append("❌ Too weak - must contain both uppercase and lowercase letters.")

    if re.search(r"[!@#$%^&*()_+=><;:.,?/|]", password):
        score += 1
    else:
        warnings.append("❌ Too weak - must contain at least one special character.")

    if score == 4:
        st.success("💪 Strong password.")
    elif score == 3:
        st.warning("⚠️ Moderate password - Consider adding more security features.")
    else:
        st.error("❌ Weak password - Improve it using the suggestions above.")
  



st.title("AI Password Strength Checker 🔍")

st.write("This is a simple password strength checker that checks the strength of your password based on the following criteria:")
st.write("1. Password length must be 8 characters or more.")
st.write("2. Password must contain at least one number.")
st.write("3. Password must contain both uppercase and lowercase letters.")
st.write("4. Password must contain at least one special character.")

strength_password = st.text_input("Enter your password", type="password")



if st.button("Check Password"):
    score = 0
    warnings = []

    if len(strength_password) >= 8:
        score += 1
    else:
        warnings.append("❌ Password must be 8 characters long or more.")
    
    if re.search(r"\d", strength_password):
        score += 1
    else:
        warnings.append("❌ Too weak - must contain at least one number.")
  
    if re.search(r"[A-Z]", strength_password) and re.search(r"[a-z]", strength_password):
        score += 1
    else:
        warnings.append("❌ Too weak - must contain both uppercase and lowercase letters.")

    if re.search(r"[!@#$%^&*()_+=><;:.,?/|]", strength_password):
        score += 1
    else:
        warnings.append("❌ Too weak - must contain at least one special character.")

    if score == 4:
        st.success("💪 Strong password.")
    elif score == 3:
        st.warning("⚠️ Moderate password - Consider adding more security features.")
    else:
        st.error("❌ Weak password - Improve it using the suggestions below.")
        suggested_password = suggest_strong_password()
        st.info(f"🔹 Suggested Strong Password: {suggested_password}")

    for warning in warnings:
        st.warning(warning)

