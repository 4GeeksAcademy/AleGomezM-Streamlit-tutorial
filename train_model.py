import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Cargar dataset
df = pd.read_csv('winequality-red.csv', sep=';')

# Clasificar la calidad
def categorizar_calidad(valor):
    if valor <= 4:
        return 'Baja'
    elif valor <= 6:
        return 'Media'
    else:
        return 'Alta'

df['quality_cat'] = df['quality'].apply(categorizar_calidad)

# Features y etiquetas
X = df.drop(['quality', 'quality_cat'], axis=1)
y = df['quality_cat']

# Escalado
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# División y entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Guardar modelo y scaler
joblib.dump(model, 'modelo.pkl')
joblib.dump(scaler, 'scaler.pkl')