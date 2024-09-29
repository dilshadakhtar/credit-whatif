import streamlit as st
import pandas as pd
import numpy as np

def simulate_credit_score(base_score, actions):
    score = base_score
    for action, impact in actions.items():
        score += impact
    return max(300, min(850, score))

st.title("Credit Score Simulator")

base_score = st.slider("Current Credit Score", 300, 850, 700)

st.subheader("Select actions to simulate:")

actions = {
    "Pay all bills on time for 6 months": st.checkbox("Pay all bills on time for 6 months", value=False),
    "Miss a payment": st.checkbox("Miss a payment", value=False),
    "Apply for a new credit card": st.checkbox("Apply for a new credit card", value=False),
    "Pay off a credit card balance": st.checkbox("Pay off a credit card balance", value=False),
    "Close your oldest credit account": st.checkbox("Close your oldest credit account", value=False),
    "Increase credit utilization to over 50%": st.checkbox("Increase credit utilization to over 50%", value=False),
    "Decrease credit utilization to under 10%": st.checkbox("Decrease credit utilization to under 10%", value=False)
}

impact = {
    "Pay all bills on time for 6 months": 25,
    "Miss a payment": -75,
    "Apply for a new credit card": -10,
    "Pay off a credit card balance": 15,
    "Close your oldest credit account": -30,
    "Increase credit utilization to over 50%": -50,
    "Decrease credit utilization to under 10%": 30
}

selected_actions = {action: impact[action] for action, selected in actions.items() if selected}

if st.button("Simulate Credit Score"):
    new_score = simulate_credit_score(base_score, selected_actions)
    st.subheader(f"Simulated Credit Score: {new_score}")
    
    change = new_score - base_score
    if change > 0:
        st.success(f"Your credit score increased by {change} points!")
    elif change < 0:
        st.error(f"Your credit score decreased by {abs(change)} points.")
    else:
        st.info("Your credit score remained unchanged.")

    st.write("Breakdown of changes:")
    for action, score_impact in selected_actions.items():
        if score_impact > 0:
            st.write(f"- {action}: +{score_impact}")
        else:
            st.write(f"- {action}: {score_impact}")

st.info("Note: This is a simplified simulation. Real credit scores are calculated using complex algorithms with many variables.")
