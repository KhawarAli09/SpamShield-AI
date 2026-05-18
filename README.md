# SpamShield-AI

<img width="484" height="299" alt="image" src="https://github.com/user-attachments/assets/a68bc300-cfb9-4504-9983-b49977cd7a02" />

## Intelligent Spam Email Detection System Using Machine Learning

---

## Overview

SpamShield AI is a Machine Learning and Natural Language Processing (NLP) based spam email detection system developed in Python. The project classifies emails into two categories:

* Spam
* Ham (Legitimate Email)

The system uses text preprocessing, feature extraction, visualization, and machine learning algorithms to accurately detect unwanted emails.

This project is beginner-friendly and demonstrates the complete machine learning workflow from dataset loading to model evaluation.

---

## Features

* Spam vs Ham email classification
* NLP-based text preprocessing
* Data visualization and analysis
* CountVectorizer for feature extraction
* Naive Bayes classification
* Accuracy, Precision, Recall, and F1-score evaluation
* Confusion Matrix visualization
* Simple and clean notebook implementation
* CSV dataset integration

---

## Technologies Used

| Technology       | Purpose                 |
| ---------------- | ----------------------- |
| Python           | Programming Language    |
| Pandas           | Data Handling           |
| NumPy            | Numerical Operations    |
| Matplotlib       | Data Visualization      |
| Seaborn          | Visualization           |
| Scikit-learn     | Machine Learning        |
| Jupyter Notebook | Development Environment |

---

## Machine Learning Workflow

1. Import Required Libraries
2. Load Dataset (CSV)
3. Data Exploration
4. Data Visualization
5. Text Preprocessing
6. Feature Extraction using CountVectorizer
7. Train-Test Split
8. Train Naive Bayes Model
9. Evaluate Model Performance
10. Predict Spam or Ham Emails

---

## Project Structure

```text
SpamShield-AI/
│
├── spam_detection_project.ipynb
├── spam.csv
├── screenshots/
├── README.md
└── requirements.txt
```

---

## Installation

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## Run the Project

```bash
jupyter notebook spam_detection_project.ipynb
```

---

## Dataset

The project uses a CSV dataset containing labeled email messages.

Dataset Columns:

* Category → Spam or Ham
* Message → Email/SMS text

---

## Prediction
<img width="565" height="309" alt="image" src="https://github.com/user-attachments/assets/d2b0acc6-e5eb-4f18-a230-14460213fbd5" />

<img width="565" height="309" alt="image" src="https://github.com/user-attachments/assets/6b042fdf-532e-4244-8fc4-626c66eae93a" />


## Evaluation Metrics

The model evaluates performance using:

* Accuracy Score
* Precision Score
* Recall Score
* F1 Score
* Confusion Matrix
* Classification Report

---

## Learning Outcomes

This project helps in understanding:

* Machine Learning basics
* Text classification
* NLP preprocessing
* Spam filtering systems
* Data visualization
* Model evaluation techniques

---

## Future Improvements

* Deep Learning Integration
* Web Application Deployment
* Real-time Email Detection
* GUI Interface
* Phishing Detection
* Multi-language Support
* Advanced NLP Models

---

## Author

Khawar Ali
BS Computer Science Student

---
