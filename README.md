# BKDS Heart Disease Multimodel

## Introduction
This is a multimodel for predicting heart disease. The multimodel is a combination of 3 models: Logistic Regression, Random Forest, and XGBoost. The multimodel is trained on the [BKDS Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease). The dataset contains 76 attributes, but all published experiments refer to using a subset of 14 of them. The "goal" field refers to the presence of heart disease in the patient. It is integer valued from 0 (no presence) to 4. Experiments with the Cleveland database have concentrated on simply attempting to distinguish presence (values 1,2,3,4) from absence (value 0).

## Installation
To install the multimodel, run the following command:
```bash
git clone bkds04
```
```bash
cd bkds04
pip install -r requirements.txt
```

## Usage
To run the multimodel, run the following command:
```bash
streamlit run apps/app.py
```
