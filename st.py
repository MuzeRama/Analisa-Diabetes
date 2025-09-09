import streamlit as st
import pickle
import streamlit as st
import pandas as pd
import numpy as np

# Fungsi untuk login
def login(username, password):
    # Gantilah ini dengan logika otentikasi sesuai kebutuhan Anda
    return username == "user" and password == "password"

# Cek apakah pengguna sudah login
def is_user_authenticated():
    return st.session_state.is_authenticated

# Tampilan halaman login
def show_login_page():
    st.title("Login Page")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    if st.button("Login"):
        if login(username, password):
            st.success("Login successful!")
            st.session_state.is_authenticated = True
        else:
            st.error("Login failed. Please check your credentials.")

# Tampilan halaman utama setelah login
def show_main_page():       
    app_mode = st.sidebar.selectbox(
        'Select Page', ['Home', 'Prediction', 'Logout'])  # two pages

    if app_mode == "Home":
        st.title('Diabetes')
        st.markdown('Dataset :')
        dataset = pd.read_csv('diabetes.csv')
        st.table(dataset.head(11))

    elif app_mode == "Prediction":
        st.title('Prediksi Diabetes')
        col1, col2, col3 = st.columns(3)
        with col1:
            Pregnancies = st.number_input(
                'Input Nilai Pregnancies', min_value=1, max_value=17, value=1)
            Glucose = st.number_input(
                'Input Nilai Glucose', min_value=0, max_value=199, value=1)
            BloodPressure = st.number_input(
                'Input Nilai BloodPressure', min_value=0, max_value=122, value=1)
        with col2:
            SkinThickness = st.number_input(
                'Input Nilai SkinThickness', min_value=0, max_value=99, value=1)
            Insulin = st.number_input(
                'Input Nilai Insulin', min_value=0, max_value=846, value=1)
            BMI = st.number_input('Input Nilai  BMI',
                                min_value=0, max_value=55, value=1)
        with col3:
            DiabetesPedigreeFunction = st.number_input(
                'Input Nilai  DiabetesPedigreeFunction', min_value=0.000, max_value=2.329, value=0.001)
            Age = st.number_input('Input Nilai  Age',
                                min_value=0, max_value=81, value=1)

        feature_list = [Pregnancies, Glucose, BloodPressure,
                        SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        single_sampel = np.array(feature_list).reshape(1, -1)
        if st.button('Test Prediksi Diabetes'):
            file_model = pickle.load(open('diabetes_model.sav', 'rb'))
            prediction = file_model.predict(single_sampel)
            if prediction[0] == 1:
                st.error('Maaf Anda Mempunyai Penyakit Diabetes')
            elif prediction[0] == 0:
                st.success('Selamat Anda Tidak Mempunyai Penyakit Diabetes')
    elif app_mode == "Logout":
        st.session_state.is_authenticated = False

# Cek apakah pengguna sudah login sebelum menampilkan halaman
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False

if st.session_state.is_authenticated:
    show_main_page()
else:
    show_login_page()