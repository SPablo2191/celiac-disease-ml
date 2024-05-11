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

from mlxtend.feature_selection import SequentialFeatureSelector
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

target = 'Disease_Diagnose'
X = data.drop(columns=[target])
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=42, shuffle=True)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
svm_model = SVC(kernel='linear', C=1.0)
svm_model.fit(X_train_scaled, y_train)
sfs = SequentialFeatureSelector(estimator=svm_model,
                                        k_features=5,
                                        forward=True,
                                        floating=False,
                                        scoring='accuracy',
                                        cv=5)


X_train_selected = sfs.fit_transform(X_train_scaled, y_train)

selected_features = list(X.columns[list(sfs.k_feature_idx_)])


svm_model_selected = SVC(kernel='linear', C=1.0)
svm_model_selected.fit(X_train_selected, y_train)


X_test_selected = sfs.transform(X_test_scaled)


y_pred_selected = svm_model_selected.predict(X_test_selected)

accuracy_selected = accuracy_score(y_test, y_pred_selected)
conf_matrix_selected = confusion_matrix(y_test, y_pred_selected)
classification_rep_selected = classification_report(y_test, y_pred_selected)



print("Características seleccionadas:", selected_features)
print("Accuracy del modelo SVM con características seleccionadas:", accuracy_selected)
print("Matriz de Confusión con características seleccionadas:")
print(conf_matrix_selected)
print("Reporte de Clasificación con características seleccionadas:")
print(classification_rep_selected)



example_index = X_test.index[0]
example = X_test.loc[example_index].values.reshape(1, -1)
example_scaled = scaler.transform(example)
example_selected = sfs.transform(example_scaled)


prediction = svm_model_selected.predict(example_selected)
print("Predicción para el ejemplo de prueba:", prediction)

# from joblib import dump

# dump(svm_model_selected, 'docs\celiac_disease_svm_model.joblib')