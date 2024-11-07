# app.py
import streamlit as st
import pickle
import pandas as pd

# Load the pre-trained model
model_path = 'stackking_classifier.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Define a function to take user inputs
def get_user_input():
    st.sidebar.header("Input Parameters")
    emails_opened = st.sidebar.number_input("Emails Opened", 0, 1000, 10)
    emails_clicked = st.sidebar.number_input("Emails Clicked", 0, 1000, 5)
    purchase_history = st.sidebar.number_input("Purchase History (Total Purchases)", 0, 1000, 10)
    time_spent = st.sidebar.slider("Time Spent on Website (minutes)", 0.0, 500.0, 20.0)
    days_since_last_open = st.sidebar.number_input("Days Since Last Open", 0, 365, 30)
    engagement_score = st.sidebar.slider("Customer Engagement Score", 0.0, 1.0, 0.5)

    # Gather inputs in a dictionary format to convert to DataFrame
    data = {
        'Emails_Opened': emails_opened,
        'Emails_Clicked': emails_clicked,
        'Purchase_History': purchase_history,
        'Time_Spent_On_Website': time_spent,
        'Days_Since_Last_Open': days_since_last_open,
        'Customer_Engagement_Score': engagement_score
    }
    # Convert inputs to a DataFrame
    input_df = pd.DataFrame([data])
    return input_df

# Function to make predictions
def make_prediction(input_data):
    prediction = model.predict(input_data)
    return prediction[0]

# Main function to display Streamlit elements
def main():
    st.title("Email Campaign Success Prediction")
    st.write("This app predicts the success of an email campaign based on customer data.")

    # Get user input
    input_data = get_user_input()
    st.write("### Input Data")
    st.write(input_data)

    # Make prediction and display results
    if st.button("Predict"):
        result = make_prediction(input_data)
        st.write("### Prediction")
        if result == 1:
            st.write("The campaign is likely to be successful! 🎉")
        else:
            st.write("The campaign may not succeed. 😞")

if __name__ == "__main__":
    main()
