import streamlit as st
import pandas as pd
import requests
import uvicorn
from fastapi import FastAPI
import joblib
from PropertyVariables import ProperyPricePred


fileName = 'property_price_prediction_voting.sav'
loaded_model = joblib.load(fileName)


def call_fastapi_predict_endpoint(data: ProperyPricePred):
        # data = data.dict()
        st.write(data)
        data = pd.DataFrame([data])
        st.write(data.head())

        prediction = loaded_model.predict(data)
        st.write(str(prediction))
        return str(prediction)


def inputform():
    st.header("Enter Your Input")
    with st.form(key='submit_form', clear_on_submit=False, border=True):
            PropertyType = st.number_input('Enter property type*')
            ClubHouse = st.number_input('Enter ClubHouse*')
            School_University_in_Township = st.number_input("Enter School_University_in_Township*")
            Hospital_in_TownShip = st.number_input("Enter Hospital_in_TownShip*")
            Mall_in_TownShip = st.number_input("Enter Mall_in_TownShip*")
            Park_Jogging_track = st.number_input("Enter Park_Jogging_track*")
            Swimming_Pool = st.number_input("Enter Swimming_Pool*")
            Gym = st.number_input("Enter Gym*")
            Property_Area_in_Sq_Ft = st.number_input("Enter Property_Area_in_Sq_Ft*")
            Price_by_sub_area = st.number_input("Enter Price_by_sub_area*")
            Amenities_score = st.number_input("Enter Amenities_score*")
            Price_by_Amenities_score = st.number_input("Enter Price_by_Amenities_score*")
            Noun_Counts = st.number_input("Enter Noun_Counts*")
            Verb_Counts = st.number_input("Enter Verb_Counts*")
            Adjective_Counts = st.number_input("Enter Adjective_Counts*")
            boasts_elegant = st.number_input("Enter boasts_elegant*")
            elegant_towers = st.number_input("Enter elegant_towers*")
            every_day = st.number_input("Enter every_day*")
            great_community = st.number_input("Enter great_community*")
            mantra_gold = st.number_input("Enter mantra_gold*")
            offering_bedroom = st.number_input("Enter offering_bedroom*")
            quality_specification = st.number_input("Enter quality_specification*")
            stories_offering = st.number_input("Enter stories_offering*")
            world_class = st.number_input("Enter world_class*")



            user_input = {
                "PropertyType": PropertyType,
                "ClubHouse": ClubHouse,
                "School_University_in_Township": School_University_in_Township,
                "Hospital_in_TownShip": Hospital_in_TownShip,
                "Mall_in_TownShip": Mall_in_TownShip,
                "Park_Jogging_track": Park_Jogging_track,
                "Swimming_Pool": Swimming_Pool,
                "Gym": Gym,
                "Property_Area_in_Sq_Ft": Property_Area_in_Sq_Ft,
                "Price_by_sub_area": Price_by_sub_area,
                "Amenities_score": Amenities_score,
                "Price_by_Amenities_score": Price_by_Amenities_score,
                "Noun_Counts": Noun_Counts,
                "Verb_Counts": Verb_Counts,
                "Adjective_Counts": Adjective_Counts,
                "boasts_elegant": boasts_elegant,
                "elegant_towers": elegant_towers,
                "every_day": every_day,
                "great_community": great_community,
                "mantra_gold": mantra_gold,
                "offering_bedroom": offering_bedroom,
                "quality_specification": quality_specification,
                "stories_offering": stories_offering,
                "world_class": world_class,
                # Add more fields accordingly
            }


            if st.form_submit_button(label='Submit'):
                    if not(PropertyType and ClubHouse and School_University_in_Township):
                        st.error('Please fill all the * fields')
                    else:
                        prediction = call_fastapi_predict_endpoint(user_input)
                        st.success(f"The predicted price is: {prediction}") 
                        st.write('successfully submitted')