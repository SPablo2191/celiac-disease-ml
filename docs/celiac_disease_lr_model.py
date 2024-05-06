import pandas as pd
import numpy as np
import warnings

# Ignorar todos los warnings
warnings.filterwarnings("ignore")

data = pd.read_csv('docs\dataset_celiac.csv', delimiter=';', header=0)


from sklearn.preprocessing import LabelEncoder
# encoding
label_encoder = LabelEncoder()
categorical_columns = data.columns

for column in categorical_columns:
    data[column] = label_encoder.fit_transform(data[column])

# feature selection
from mlxtend.feature_selection import SequentialFeatureSelector
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data.replace([np.inf, -np.inf], np.nan, inplace=True)

data = data.dropna()

target = 'Disease_Diagnose'
X = data.drop(columns=[target])

y = data[target]

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(penalty=None, max_iter=1000)
# Crear el objeto SequentialFeatureSelector
sfs_forward = SequentialFeatureSelector(estimator=model,
                                        k_features=5,
                                        forward=True,
                                        floating=False,
                                        scoring='accuracy',
                                        cv=5)


sfs_forward.fit(X_train, y_train)
selected_features = list(X.columns[list(sfs_forward.k_feature_idx_)])
print("Características seleccionadas:", selected_features)


# creación del modelo
from sklearn.metrics import accuracy_score
# Dividir el dataset en conjuntos de entrenamiento y prueba
X = data[selected_features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8,
random_state = 42,
shuffle = True)

model = LogisticRegression(penalty=None)
model.fit(X = X_train, y = y_train)

# Información del modelo
print("Intercept:", model.intercept_)
print("Coeficiente:", list(zip(X.columns, model.coef_.flatten(), )))
print("Accuracy de entrenamiento:", model.score(X, y))
predictions = model.predict_proba(X = X_test)
predictions = pd.DataFrame(predictions, columns = model.classes_)
predictions.head(3)
predictions = model.predict(X = X_test)
clasification = np.where(predictions<0.5, 0, 1)
accuracy = accuracy_score(
y_true = y_test,
y_pred = clasification,
normalize = True
)
print(f"este modelo tiene una precisión del {accuracy*100} %")

from joblib import dump

dump(model, 'docs\celiac_disease_lr_model.joblib')