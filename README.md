# Email Campaign Success Prediction

This project is designed to predict the success of an email marketing campaign based on customer engagement metrics. The model can help businesses make data-driven decisions to optimize their marketing strategies.

## Project Structure

- **app.py**: The main Streamlit application that allows users to input data and receive campaign success predictions.
- **stackking_classifier.pkl**: Pre-trained machine learning model used to make predictions.
- **requirements.txt**: List of dependencies for deploying the project on Streamlit Cloud.
- **EDA - (group 1).ipynb**: Notebook containing exploratory data analysis (EDA) and model training process.

## Features

- **Interactive Input Form**: Users can input customer data through Streamlit's sidebar.
- **Prediction Output**: Provides a prediction on whether the email campaign is likely to succeed or not.

## Dependencies

The project relies on several Python libraries listed in `requirements.txt`. Here’s a summary:
- `streamlit`: For deploying the interactive web app.
- `scikit-learn`: Used for model training and evaluation.
- `xgboost`: XGBoost classifier for prediction.
- `pandas`, `numpy`, `matplotlib`, `seaborn`: For data manipulation and visualization.
- `imblearn`: For handling class imbalances in the dataset.
- `statsmodels`: For calculating VIF to address multicollinearity.

## Setup and Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/devpkr1/Email-Marketing-Campaign-Project.git
   cd email-campaign-prediction
   ```

2. **Install dependencies**:
   Use the following command to install required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **Access the app**:
   Open a web browser and go to `http://localhost:8501` to interact with the app.

## Usage

1. Input customer engagement metrics in the sidebar:
   - **Emails Opened**: Number of emails the customer opened.
   - **Emails Clicked**: Number of clicks on emails.
   - **Purchase History**: Total purchases made by the customer.
   - **Time Spent on Website**: Time spent on the website in minutes.
   - **Days Since Last Open**: Days since the customer last opened an email.
   - **Customer Engagement Score**: A score between 0.0 and 1.0 indicating engagement level.

2. Click "Predict" to generate a prediction. The app will indicate whether the campaign is likely to succeed.

## Model Training

The model was trained using various machine learning algorithms, with `XGBClassifier` selected as the final model. Training and evaluation details are in the `EDA - (group 1).ipynb` notebook.

## License

This project is licensed under the MIT License.
