import pickle
import pathlib
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

# USER AUTHENTICATION
names = ["Peter Parker", "Mary Jane"]
usernames =["pparker", "MJ"]

#Load hashed passwords
file_path = pathlib.Path(__file__).parent / 'hashed_pw.pkl'
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "MDPS", "abcdef", cookie_expiry_days=30)


name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:

    #Logout button
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")

    diabetes_model = pickle.load(open('C:/Users/Vedantika/Desktop/DPSs/DPS/saved modles/diabetes_model.sav', 'rb'))
    hypertension_model = pickle.load(open('C:/Users/Vedantika/Desktop/DPSs/DPS/saved modles/hypertension_model.sav', 'rb'))
    thyroid_model = pickle.load(open('C:/Users/Vedantika/Desktop/DPSs/DPS/saved modles/thyroid_model.sav', 'rb'))

    with st.sidebar: 
    
        selected = option_menu('Multiple Disease Prediction System',
                          
                              ['Diabetes Prediction',
                               'Hypertension Prediction',
                               'Thyroid Prediction'],
                              icons=['activity','heart','person'],
                              default_index=0)
    

    if (selected == 'Diabetes Prediction'):

        st.title('Diabetes Prediction using ML')
    

        col1, col2, col3 = st.columns(3)
    
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')
        
        with col2:
            Glucose = st.text_input('Glucose Level')
    
        with col3:
            BloodPressure = st.text_input('Blood Pressure value')
    
        with col1:
            SkinThickness = st.text_input('Skin Thickness value')
    
        with col2:
            Insulin = st.text_input('Insulin Level')
    
        with col3:
            BMI = st.text_input('BMI value')
    
        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
        with col2:
            Age = st.text_input('Age of the Person')
    
    
        # code for Prediction
        diab_diagnosis = ''
    
        # creating a button for Prediction
    
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
            if (diab_prediction[0] == 1):
              diab_diagnosis = 'The person is diabetic'
            else:
              diab_diagnosis = 'The person is not diabetic'
        
        st.success(diab_diagnosis)




    # Hypertension Prediction Page
    if (selected == 'Hypertension Prediction'):
    
        # page title
        st.title('Hypertension Prediction using ML')
    
        col1, col2, col3 = st.columns(3)
    
        with col1:
            age = st.text_input('Age')
        
        with col2:
            sex = st.text_input('Sex')
        
        with col3:
            cp = st.text_input('Chest Pain types')
        
        with col1:
            trestbps = st.text_input('Resting Blood Pressure')
        
        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')
        
        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')
        
        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')
        
        with col3:
            exang = st.text_input('Exercise Induced Angina')
        
        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')
        
        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')
        
        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')
        
        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
        # code for Prediction
        hypertension = ''
    
        # creating a button for Prediction
    
        if st.button('Hypertension Test Result'):
            hypertension_prediction = hypertension_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
            if (hypertension_prediction[0] == 1):
              hypertension = 'The person is having hypertension'
            else:
              hypertension = 'The person does not have any hypertension'
        
        st.success(hypertension)
        
    
    

    # Thyroid Prediction Page
    if (selected == "Thyroid Prediction"):
    
        # page title
        st.title("Thyroid Disease Prediction using ML")
    
        col1, col2, col3, col4, col5 = st.columns(5)  
    
        with col1:
            age = st.text_input('age')
        
        with col2:
            sex = st.text_input('sex')
        
        with col3:
            on_thyroxine = st.text_input('on_thyroxine')
        
        with col4:
            query_on_thyroxine = st.text_input('query_on_thyroxine')
        
        with col5:
            on_antithyroid_medication = st.text_input('on_antithyroid_medication')
        
        with col1:
            sick = st.text_input('sick')
        
        with col2:
            pregnant = st.text_input('pregnant')
        
        with col3:
            thyroid_surgery = st.text_input('thyroid_surgery')
        
        with col4:
            I131_treatment = st.text_input('I131_treatment')
        
        with col5:
            query_hypothyroid = st.text_input('query_hypothyroid')
        
        with col1:
            query_hyperthyroid = st.text_input('query_hyperthyroid')
        
        with col2:
            lithium = st.text_input('lithium')
        
        with col3:
            goiter = st.text_input('goiter')
        
        with col4:
            tumor = st.text_input('tumor')
        
        with col5:
            hypopituitary = st.text_input('hypopituitary')
        
        with col1:
            psych = st.text_input('psych')
        
        with col2:
            TSH = st.text_input('TSH')
        
        with col3:
            T3 = st.text_input('T3')
        
        with col4:
            TT4 = st.text_input('TT4')
        with col5:
            T4U = st.text_input('T4U')
        with col1:
            FTI = st.text_input('FTI')
        
    
    
        # code for Prediction
        thyroid_diagnosis= ''
    
        # creating a button for Prediction    
        if st.button("Thyroid Test Result"):
            thyroid_prediction = thyroid_model.predict([[age,sex, on_thyroxine,query_on_thyroxine,on_antithyroid_medication, sick, pregnant,thyroid_surgery,I131_treatment,query_hypothyroid,query_hyperthyroid,lithium,goiter,tumor,hypopituitary,psych,TSH,T3,TT4,T4U,FTI]])
        
            if (thyroid_prediction[0] == 1):
              thyroid_diagnosis = "The person has thyroid disease"
            else:
              thyroid_diagnosis= "The person does not have thyroid disease"
        
        st.success(thyroid_diagnosis)


    








