import pickle
import pandas as pd 
import numpy as np 
import streamlit as st 
from PIL import Image

pickle_in = open("BankNote_ML.pkl", "rb")
CLS = pickle.load(pickle_in)

def welcome():
    return 'Welcome All' 

def prediction(variance, skew, curtosis, entropy):
    prediction = CLS.predict(np.array([[variance, skew, curtosis, entropy]]))
    print(prediction[0])
    return prediction[0]

def main():
    st.title("Bank Note Class Prediction")
    html_temp = """
                <div style ="background-color:green;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Bank Note Class Prediction ML App </h1> 
    </div> 
"""

    st.markdown(html_temp, unsafe_allow_html = True)

    variance = st.text_input("Variance", "Type Here") 
    skew = st.text_input("Skew", "Type Here") 
    curtosis = st.text_input("Curtosis", "Type Here") 
    entropy = st.text_input("Entropy", "Type Here") 
    result ="" 

    if st.button("Predict"): 
        # Convert input strings to floats
        try:
            variance = float(variance)
            skew = float(skew)
            curtosis = float(curtosis)
            entropy = float(entropy)
            
            result = prediction(variance, skew, curtosis, entropy)
            if result == 0:
                res = "Fake Note"
            else:
                res = "True Note"
            st.success('The Note Class is {}'.format(res))
        except ValueError:
            st.error("Please enter valid numerical values.")

if __name__ == '__main__':
    main()
