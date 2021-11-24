import streamlit as st
from model_methods import predict
import  numpy as np
st.title("Customer Churn Prediction")
st.subheader("Age")
age = st.slider('', min_value= 18 , max_value=90)  # 👈 this is a widget


st.subheader("Credit Score")
creditscore = st.slider("", min_value=350 , max_value=850)



st.subheader("Tenure")
tenure = st.slider("", min_value=0, max_value=10)



st.subheader("Balance")
balance = st.slider("", min_value=0, max_value=250000 , step = 1000)


st.subheader("Salary")
salary = st.slider("", min_value=0, max_value=200000 , step = 1000 , key="salary")

st.subheader("Number of Products")
products = st.slider("", min_value=1, max_value=5)

creditcard = st.radio("Do you have a Credit Card" , ('Yes','No' ))

activemember = st.radio("Are you Active Member" , ('Yes','No' ) , key = "member")
country = st.radio("Country" , ('France','Spain' , 'Germany' ) , key = "country")
gender = st.radio("Gender" , ('Male','Female' ) , key = "gender")



st.write("Age: ", age)
st.write("Credit Score: ", creditscore)
st.write("Tenure: ", tenure)
st.write("Balance: ", balance)
st.write("Salary: ", salary)
st.write("Number of Products: ", products)



Mage = age
Mcreditscore = creditscore
Mtenure = tenure
Mbalance = balance
Mproducts = products
Msalary = salary
Mcreditcard = None
MGender = None
Mactivemember = None
Mcountry = None

if creditcard == "Yes":
    st.write("Credit Card: Yes")
    Mcreditcard = 1

else:
    st.write("Credit Card: No")
    Mcreditcard = 0

if activemember == "Yes":
    st.write("Active Member: Yes")
    Mactivemember = 1
else:
    st.write("Active Member: No")
    Mactivemember = 0

if country == "France":
    st.write("Country: France")
    Mcountry = 0
elif country == "Germany":
    st.write("Country: Germany")
    Mcountry = 1
else:
    st.write("Country: Spain")
    Mcountry = 2

if gender == "Male":
    st.write("Gender: Male")
    MGender = 1
else:
    st.write("Gender: Female")
    MGender = 0




input = [Mcreditscore , Mcountry , MGender , Mage ,
         Mtenure , Mbalance , Mproducts , Mcreditcard ,
         Mactivemember , Msalary]
input = np.array(input).reshape(1 , -1)


if st.button("Predict"):
    final = predict(input)
    st.header(final)