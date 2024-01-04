import uvicorn
from fastapi import FastAPI
from PropertyVariables import ProperyPricePred
import pandas as pd
import joblib
import streamlit as st
import requests
from utility import login
from operation import inputform

# 1.  Creating the App object
PropertyPricePredApp = FastAPI()

# 2.  Load the model from disk
fileName = 'property_price_prediction_voting.sav'
loaded_model = joblib.load(fileName)





@login
def main():
    cols1, cols2, cols3 = st.columns((1, 4, 1))
    # cols1.image('smart-group-logo-r.png')
    cols2.markdown("<h1 style='text-align: left;margin-top:-2rem; margin-left:1rem; color: #E12D06;'>Real State Price prediction</h1>", unsafe_allow_html=True)
    st.write('\n')

    if st.session_state["authentication_status"]:
        inputform()



# 3. Index route, opens automatically on http://127.0.0.1:8000
@PropertyPricePredApp.get('/')
def index():
    st.write("Hello ")
    return {'message': 'Hello, World!'}





# 4. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted price with the confidence (http://127.0.0.1:8000/predict)
@PropertyPricePredApp.post('/predict')
def predict_price(data: ProperyPricePred):
    data = data.dict()
    st.write(data)
    data = pd.DataFrame([data])
    st.write(data.head())

    prediction = loaded_model.predict(data)
    st.write(str(prediction))
    return str(prediction)


# # 5. Run the API with uvicorn
# #    Will run on http://127.0.0.1:8005
if __name__ == '__main__':
    # uvicorn.run("app:PropertyPricePredApp",host='127.0.0.1', port=8005, reload=True, workers=3)
    res = requests.post(url = "http://127.0.0.1:8501", data= main())
    
