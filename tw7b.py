# -*- coding: utf-8 -*-
"""


@author: win7
"""

import pandas as pd
import numpy as np
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination
import csv

lines = list(csv.reader(open('data7_names.csv','r')))
attributes = lines[0]

heart_disease = pd.csv_read('data7_heart.csv',names = attributes)
heart_disease = heart_disease.replace('?',np.nan)

print("few datasets")
print("",heart_disease.head())

print("attributes and datatypes")
print("",heart_disease.dtypes())

model = BayesianModel([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'), ('exang',
'trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','restecg'),
('heartdisease','thalach'), ('heartdisease','chol')])

model.fit(heart_disease, estimator=MaximumLikelihoodEstimator)

HeartDisease_infer = VariableElimination(model)

print("probability for getting heart disease when age is 40")
q = HeartDisease_infer.query(variables=['heart_disease'], evidence={'age': 40})
print(q['heart_disease'])

print("probability for getting heart disease when cholestrol is 100")
q = HeartDisease_infer.query(variables=['heart_disease'], evidence={'age': 100})
print(q['heart_disease'])






