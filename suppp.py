import pickle
import streamlit as st
from os import path
import numpy as np

st.title("phishing website detection app")

filename="kmodel.pk"
with open(path.join(filename),'rb') as f:
    lr=pickle.load(f)
    
Domain=st.text_input("q")
Have_IP=st.number_input("w")
Have_At=st.number_input("e")
URL_Length=st.number_input("ee")
URL_Depth=st.number_input("r")
Redirection=st.number_input("it")
https_Domain=st.number_input("y")
TinyURL=st.number_input("yyy")
Prefix_Suffix=st.number_input("h")
DNS_Record=st.number_input("s")
Web_Traffic=st.number_input("f")
Domain_Age=st.number_input("ff")
Domain_End=st.number_input("v")
iFrame=st.number_input("vv")
Mouse_Over=st.number_input("vj")
Right_Click=st.number_input("bj")
Web_Forwards=st.number_input("fuck")
if st.button("predict"):
    pred=lr.predict(np.array([[Domain,Have_IP,Have_At,URL_Length,URL_Depth,Redirection,https_Domain,TinyURL,Prefix_Suffix,DNS_Record,Web_Traffic,Domain_Age,Domain_End,iFrame,Mouse_Over,Right_Click,Web_Forwards]]))
    st.write("the website is phishing",pred[0])
