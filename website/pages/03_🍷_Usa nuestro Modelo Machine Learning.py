
# importar librerias
import numpy as np
import pandas as pd
import random
import os
import streamlit as st
import joblib


from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


st.header("Prueba nuestro modelo Machine Learning 🤓")
st.write("Puedes leer las reseñas y resultados")
# get data
#df = pd.read_parquet('Cluster_result.parquet')
ruta_cluster = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Cluster_CountVectorizer_KMeans.parquet')
df = pd.read_parquet(ruta_cluster)

# Seleccionar variables predictoras X - variable a predecir y
X = df['review processed']
y = df['cluster']

# obtener datos de entrenamiento - datos de prueba (split)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1, stratify=y)

# pipeline
# from sklearn.pipeline import Pipeline
# clf_model = Pipeline([('tfidf_v', TfidfVectorizer(ngram_range=(1, 1))), ('clf_m', LinearSVC(C=2, loss='squared_hinge'))])

# entrenar modelo
# clf_model.fit(X_train, y_train)

# evaluar modelo
# pred_test = clf_model.predict(X_test)

# from sklearn.metrics import accuracy_score

# print('Exactitud:', accuracy_score(y_test, pred_test))

#Cargar Modelo Preentrenado
ruta_modelo = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'clf_model_v1.2.2.pkl')
clf_model = joblib.load(ruta_modelo)

# inicializar resultado a vacio
result = 2 

# seleccionar modo 
modo = st.selectbox(
    'Como quieres probar el modelo?',
    ('Seleccionar review de forma aleatoria', 'Ingresar review de forma manual'))

if modo == 'Seleccionar review de forma aleatoria':
    # testA
    st.write("""



    """)

    st.write('Presiona TEST y selecciona una review aleatoria entre los datos del set de prueba')

    button_test = st.button('Test')

    if button_test:

        index = X_test.index[random.randint(0, len(X_test))]
        review = df['review'][index]
        review_processed = X_test[index]

        st.write(' ')
        st.write('#### review:')
        st.write(review)
        
        result = clf_model.predict([review_processed])[0]

else:

    # testB
    st.write("""



    """)

    input_review = st.text_input('Ingresa una nueva review 👇')

    if input_review:
        st.write('#### review:')
        st.write(input_review)

        result = clf_model.predict([input_review])[0]

st.write("""



""")

if result == 0:
    st.write('### Resultado de la Clasificacion:')
    st.write('## Conocedor 🍾🎉')
elif result == 1:
    st.write('### Resultado de la Clasificacion:')
    st.write('## Consumidor Casual 🥴')
else:
    st.write(' ')
