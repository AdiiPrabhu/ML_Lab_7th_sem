import numpy as np
import pandas as pd
import csv
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination
lines=list(csv.reader(open('t7_names.csv','r')))
attributes=lines[0]
heartDisease=pd.read_csv('t7_heart.csv',names=attributes)
heartDisease=heartDisease.replace('?',np.nan)

model=BayesianModel([('age','trestbps'),('age','fbs'),('sex','trestbps'),('sex','trestbps'),('exang','trestbps'),('trestbps','heartDisease'),('fbs','heartDisease'),('heartDisease','restecg'),('heartDisease','thalach'),('heartDisease','chol')])
print('learning cdps using maximumlikelihoodestimator')
model.fit(heartDisease,estimators=MaximumLikelihoodEstimator)

print('inferencing bayesian network')
heartDisease_infer=VariableElimination(model)
print('1.Probability of heartdisease given age=40')