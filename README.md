# Text Analytics Tools for Identifying Political Disinformation  
This project aimed to design and implement a robust classification system to detect political disinformation in Spanish-language news articles. The work followed a complete data engineering and machine learning pipeline, from acquisition and preprocessing of raw data to the deployment of an operational application with retraining capabilities.

The preprocessing stage included contraction expansion, case normalization, tokenization, stopword removal, non-ASCII filtering, noise elimination (punctuation and numbers), and lexical reduction through stemming and lemmatization. These steps ensured that the processed corpus was homogeneous, consistent, and semantically rich. Textual data was vectorized using the TF-IDF (Term Frequency–Inverse Document Frequency) technique, which allowed the extraction of discriminative features for classification.

Several algorithms were tested, including **Naïve Bayes** and **K-Nearest Neighbors**, but the final model was built using a **Gradient Boosting Classifier** optimized with GridSearchCV. This model was selected due to its superior performance in minimizing both bias and variance across cross-validation folds. The resulting pipeline integrates preprocessing, feature extraction, and classification into a single reproducible workflow, persisted for inference and retraining.

The solution was deployed as a **RESTful API using FastAPI**, exposing three main endpoints:  
1. **/predict/** – Individual news prediction.  
2. **/predictMany/** – Batch classification from CSV files.  
3. **/retrain/** – Model retraining with new labeled datasets, ensuring adaptability to emerging disinformation patterns.  

Finally, a web application was developed to provide users with an intuitive interface for testing predictions, uploading datasets, and visualizing results. The system is designed for use by journalists, fact-checkers, political analysts, and institutional stakeholders. By automating disinformation detection, it reduces manual workload, accelerates content verification processes, and supports evidence-based decision-making in contexts where the spread of false information can have a significant social impact.

## Documents
- [Project Report – English](https://github.com/user-attachments/files/22415793/Project.Overview.pdf)
- [Reporte del Proyecto – Español](https://github.com/user-attachments/files/22415794/Resumen.del.proyecto.pdf)

## Presentations
- [Presentation – English](https://github.com/user-attachments/files/22415820/Presentation.pdf)
- [Presentacion – Español](https://github.com/user-attachments/files/22415815/Presentacion.pdf)

---

## Authors
- Natalia Villegas Calderón – 202113370  
- Carol Sofía Florido Castro – 202111430  
- Juan Martín Vásquez Cristancho – 202113314  

Course: Business Intelligence – ISIS 3301  
City: Bogotá, Colombia  
Year: 2025  

---

## Project Overview
[Insert the English project overview here]  

[Insert the Spanish project overview here]  

---

## Repository Structure
```bash
Fase1/
│── BI - Proyecto 1 Etapa 1.pdf
│── LinkVideo.txt
│── ModelosCode.ipynb
│── modelo_GB_mejoresHiperparametros.pkl
│── modelo_KNN_mejoresHiperparametros.pkl
│── modelo_naiveBayes_SinSmote.pkl
│── particion_prueba_estudiantes.csv
│── tfidf_vectorizer.pkl

Fase2/
│── app.py
│── ClasificarArchivo.csv
│── Reentrenar.csv
│── static/
│── templates/
```

## Technologies Used
- Python 3.11  
- scikit-learn, pandas, joblib, nltk, FastAPI  
- Uvicorn (ASGI server)  
- Deployment: Local / AWS / Google Cloud  

---

## Documentation
- [Project Report – English](./Fase1/BI%20-%20Proyecto%201%20Etapa%201.pdf)  
- [Reporte del Proyecto – Español](./Fase1/BI%20-%20Proyecto%201%20Etapa%201.pdf)  

---

## How to Run
1. Install dependencies
```bash
pip install -r requirements.txt
```

2. Run the API
```bash
uvicorn app:app --reload
```
3. Access at
```bash
http://127.0.0.1:8000
```
