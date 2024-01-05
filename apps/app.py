
import streamlit as st
import pandas as pd

import time
import pickle
import random
import os

from generate_ds import generate_random_dataframe


# models directory
models_dir = "models/"
model_files = [file for file in os.listdir(models_dir) if file.endswith(".pkl")]

# generate dataset
number = random.randint(5, 100)
df_final = generate_random_dataframe(number)

# streamlit
st.set_page_config(
    page_title = "Predict Hungarian heart disease",
    page_icon = ':heart'
)


# st.write dapat digunakan menampilkan test,dataframe,visualisasi
st.title('Predict Hungarian Heart Disease')
st.write('information about heart disease')
st.write("")

selected_model = st.selectbox("Select model", options=model_files)
model_path = os.path.join(models_dir, selected_model)
model = pickle.load(open(model_path, "rb"))


tab1, tab2 = st.tabs(["Single-predict", "Multi-predict"])
st.write("")
with tab1:
  st.header("User Input Features")


  age = st.number_input("Age", min_value=df_final['age'].min(), max_value=df_final['age'].max())
  st.write(f":orange[Min] value: :orange[**{df_final['age'].min()}**], :red[Max] value: :red[**{df_final['age'].max()}**]")
  sex = st.selectbox("Sex", options=["Male", "Female"])
  if sex == "Male":
      sex = 1
  elif sex == "Female":
      sex = 0
    # -- Value 0: Female
    # -- Value 1: Male
    
  cp = st.selectbox("Chest pain type", options=["Typical angina", "Atypical angina", "Non-anginal pain", "Asymptomatic"])
  if cp == "Typical angina":
      cp = 1
  elif cp == "Atypical angina":
    cp = 2
  elif cp == "Non-anginal pain":
    cp = 3
  elif cp == "Asymptomatic":
    cp = 4
    # -- Value 1: typical angina
    # -- Value 2: atypical angina
    # -- Value 3: non-anginal pain
    # -- Value 4: asymptomatic
    
  trestbps = st.number_input("resting blood pressure (in mm Hg on admission to the hospital)", min_value=df_final['trestbps'].min(), max_value=df_final['trestbps'].max())
  st.write(f":orange[Min] value: :orange[**{df_final['trestbps'].min()}**], :red[Max] value: :red[**{df_final['trestbps'].max()}**]")

  chol = st.number_input("Serum cholestrol (in mg/dl)", min_value=df_final['chol'].min(), max_value=df_final['chol'].max())
  st.write(f":orange[Min] value: :orange[**{df_final['chol'].min()}**], :red[Max] value: :red[**{df_final['chol'].max()}**]")

  fbs = st.selectbox("Fasting blood sugar > 120 mg/dl? ", options=["False", "True"])
  if fbs == "False":
    fbs = 0
  elif fbs == "True":
    fbs = 1
    # -- Value 0: false
    # -- Value 1: true
    
  restecg = st.selectbox("Resting electrocardiographic results", options=["Normal", "Having ST-T wave abnormality", "Showing left ventricular hypertrophy"])
  if restecg == "Normal":
    restecg = 0
  elif restecg == "Having ST-T wave abnormality":
    restecg = 1
  elif restecg == "Showing left ventricular hypertrophy":
    restecg = 2
  # -- Value 0: normal
  # -- Value 1: having ST-T wave abnormality (T wave inversions and/or ST  elevation or depression of > 0.05 mV)
  # -- Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria

  thalach = st.number_input("Maximum heart rate achieved", min_value=df_final['thalach'].min(), max_value=df_final['thalach'].max())
  st.write(f":orange[Min] value: :orange[**{df_final['thalach'].min()}**], :red[Max] value: :red[**{df_final['thalach'].max()}**]")

  exang = st.selectbox("Exercise induced angina?", options=["No", "Yes"])
  if exang == "No":
    exang = 0
  elif exang == "Yes":
    exang = 1
  # -- Value 0: No
  # -- Value 1: Yes

  oldpeak = st.number_input("ST depression induced by exercise relative to rest", min_value=df_final['oldpeak'].min(), max_value=df_final['oldpeak'].max())
  st.write(f":orange[Min] value: :orange[**{df_final['oldpeak'].min()}**], :red[Max] value: :red[**{df_final['oldpeak'].max()}**]")
    
  predict_btn = st.button("Predict", type=("primary"))
  result = ":violet[-]"

  st.write("")
  if predict_btn:
    inputs = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak]]
    prediction = model.predict(inputs)[0]

    bar = st.progress(0)
    status_text = st.empty()

    for i in range(1, 101):
      status_text.text(f"{i}% complete")
      bar.progress(i)
      time.sleep(0.01)
      if i == 100:
        time.sleep(1)
        status_text.empty()
        bar.empty()

    if prediction == 0:
      result = ":green[**Healthy**]"
    elif prediction == 1:
      result = ":orange[**Heart disease level 1**]"
    elif prediction == 2:
      result = ":orange[**Heart disease level 2**]"
    elif prediction == 3:
      result = ":red[**Heart disease level 3**]"
    elif prediction == 4:
      result = ":red[**Heart disease level 4**]"

  st.write("")
  st.write("")
  st.subheader("Prediction:")
  st.subheader(result)

  # st.write(f"**_Model's Accuracy_** :  :green[**{accuracy}**]%")
    

with tab2:
  st.header("Predict multiple data:")

  sample_csv = df_final.to_csv(index=False).encode('utf-8')

  st.write("")
  st.download_button("Download CSV Example", data=sample_csv, file_name='sample_heart_disease_parameters.csv', mime='text/csv')

  st.write("")
  st.write("")
  file_uploaded = st.file_uploader("Upload a CSV file", type='csv')

  if file_uploaded:
    uploaded_df = pd.read_csv(file_uploaded)
    prediction_arr = model.predict(uploaded_df)

    bar = st.progress(0)
    status_text = st.empty()

    for i in range(1, 70):
      status_text.text(f"{i}% complete")
      bar.progress(i)
      time.sleep(0.01)

    result_arr = []

    for prediction in prediction_arr:
      if prediction == 0:
        result = "Healthy"
      elif prediction == 1:
        result = "Heart disease level 1"
      elif prediction == 2:
        result = "Heart disease level 2"
      elif prediction == 3:
        result = "Heart disease level 3"
      elif prediction == 4:
        result = "Heart disease level 4"
      result_arr.append(result)

    uploaded_result = pd.DataFrame({'Prediction Result': result_arr})

    for i in range(70, 101):
      status_text.text(f"{i}% complete")
      bar.progress(i)
      time.sleep(0.01)
      if i == 100:
        time.sleep(1)
        status_text.empty()
        bar.empty()

    col1, col2 = st.columns([1, 2])

    with col1:
      st.dataframe(uploaded_result)
    with col2:
      st.dataframe(uploaded_df)
