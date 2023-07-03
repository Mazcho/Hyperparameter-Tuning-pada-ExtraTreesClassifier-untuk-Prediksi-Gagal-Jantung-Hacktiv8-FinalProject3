import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pickle
from sklearn.ensemble import RandomForestClassifier

model = pickle.load(open('model.pkl', 'rb'))

# Title
st.title('Prediksi Reisko Terkena Penyakit Gagal Jantung')
st.write('Gagal jantung adalah kondisi medis yang terjadi ketika jantung tidak dapat memompa darah dengan efektif seperti yang seharusnya. Ini terjadi ketika otot jantung yang bertanggung jawab untuk memompa darah mengalami kerusakan atau melemah, sehingga tidak mampu memenuhi kebutuhan darah tubuh secara optimal.')
st.write('Silahkan isi form berikut: ')

col1, col2 = st.columns(2)

# Input

with col1:
    umur = st.number_input("Masukan umur", value=0)

with col2:
    # anemia = st.number_input("Masukan anemia", value=0)
    anemia_options = {
    1 : "Anemia",
    0 : "Tidak Anemia"
    }
    anemia = st.selectbox("Pilih Anemia", options=list(anemia_options.keys()), format_func=lambda x: anemia_options[x])
    selected_value = anemia_options[anemia]

with col1:    
    # diabetes = st.number_input("Masukan diabetes", value=0)
    diabetes_options = {
    1 : "Diabetes",
    0 : "Tidak Diabetes"
    }
    diabetes = st.selectbox("Pilih Diabetes", options=list(diabetes_options.keys()), format_func=lambda x: diabetes_options[x])
    selected_value = diabetes_options[diabetes]

with col2:
    fraksi_ejeksi = st.number_input("Masukan fraksi ejeksi", value=0)

with col1:
    # tekanan_darah_tinggi = st.number_input("Masukan tekanan darah tinggi", value=0)
    tekanan_darah_tinggi_options = {
    1 : "Tekanan Darah Tinggi",
    0 : "Tidak Tekanan Darah Tinggi"
    }
    tekanan_darah_tinggi = st.selectbox("Pilih Tekanan Darah Tinggi", options=list(tekanan_darah_tinggi_options.keys()), format_func=lambda x: tekanan_darah_tinggi_options[x])
    selected_value = tekanan_darah_tinggi_options[tekanan_darah_tinggi]

with col2:
    serum_creatinine = st.number_input("Masukkan serum creatinine", value=0.0, step=0.1)

with col1:
    sodium_kreatin = st.number_input("Masukan sodium kreatin", value=0)

with col2:
    # jenis_kelamin = st.number_input("Masukan jenis kelamin", value=0)
   gender_options = {
    1 : "Laki-laki",
    0 : "Perempuan"
    }
   jenis_kelamin = st.selectbox("Pilih Jenis Kelamin", options=list(gender_options.keys()), format_func=lambda x: gender_options[x])
   selected_value = gender_options[jenis_kelamin]

with col1:
    # perokok = st.number_input("Masukan perokok", value=0)
    perokok_options = {
    1 : "Perokok",
    0 : "Bukan Perokok"
    }
    perokok = st.selectbox("Pilih Perokok", options=list(perokok_options.keys()), format_func=lambda x: perokok_options[x])
    selected_value = perokok_options[perokok]

with col2:
    waktu = st.number_input("Masukan waktu", value=0)


#prediksi
pred_gagalJantung = ''

# #tombol untuk prediksi
if st.button('Prediksi'):
    pred_gagalJantung = model.predict([[umur, anemia, diabetes, fraksi_ejeksi, tekanan_darah_tinggi, serum_creatinine, sodium_kreatin, jenis_kelamin, perokok, waktu]])
    # st.write('Hasil Prediksi: ', pred_bus)
    
    if pred_gagalJantung == 1:
        st.success('Memiliki Resiko Gagal Jantung')
    else:
        st.error('Tidak Memiliki Resiko Gagal Jantung')