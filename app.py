import streamlit as st
import random

# Function to determine the winner
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Streamlit UI
st.title("Rock Paper Scissors Game")

st.write("Choose one:")

col1, col2, col3 = st.columns(3)

user_choice = None
if col1.button("Rock 🪨"):
    user_choice = "rock"
elif col2.button("Paper 📄"):
    user_choice = "paper"
elif col3.button("Scissors ✂️"):
    user_choice = "scissors"

if user_choice:
    computer_choice = random.choice(["rock", "paper", "scissors"])
    st.write(f"You chose: {user_choice}")
    st.write(f"Computer chose: {computer_choice}")
    result = get_winner(user_choice, computer_choice)
    st.subheader(result)

# Deploy on Streamlit Cloud:
# 1. Save this script as `app.py`
# 2. Push to GitHub
# 3. Deploy on Streamlit Cloud: https://share.streamlit.io/
