# 🚗 Car Price Prediction using MLflow and Streamlit

A complete end-to-end Machine Learning project built using Python, Scikit-learn, MLflow, and Streamlit to predict car prices based on vehicle specifications.

## 📌 Features

* Data preprocessing and cleaning
* Machine Learning model training using Random Forest Regressor
* MLflow experiment tracking
* Streamlit web application UI
* Model evaluation using MAE and R² Score
* Model saving using Joblib
* VS Code project structure

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* MLflow
* Streamlit
* Joblib

## 📊 Model Metrics

* MAE (Mean Absolute Error)
* R² Score

## 📂 Project Structure

```text
car_mlflow_project/
│
├── Data/
│   └── Cars.csv.csv
│
├── Src/
│   ├── preprocess.py
│   └── train.py
│
├── app.py
├── requirements.txt
└── model.pkl
```

## ▶️ How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python Src/train.py
```

### Launch MLflow UI

```bash
mlflow ui
```

Open:

```text
http://127.0.0.1:5000
```

### Run Streamlit App

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

## 🎯 Output

The application predicts the MSRP (Manufacturer Suggested Retail Price) of a car using features such as:

* Engine Size
* Horsepower
* Cylinders
* Mileage
* Weight
* Wheelbase
* Car Type
* Origin
* DriveTrain

## 📈 Future Improvements

* Deploy on AWS / Azure / GCP
* Add deep learning models
* Docker support
* CI/CD integration
* Model monitoring

## 👨‍💻 Author

Gopinath B

APP : 
<img width="1312" height="807" alt="image" src="https://github.com/user-attachments/assets/93b620c3-8092-4195-a3c2-60d94540d3b4" />

Prediction : 

<img width="1280" height="247" alt="image" src="https://github.com/user-attachments/assets/c6b321a3-10a7-4259-9379-f03576b227bf" />

r2 & MAE Score : 

<img width="1280" height="477" alt="image" src="https://github.com/user-attachments/assets/567862ca-4a5f-4327-a6a6-6a853517929f" />


