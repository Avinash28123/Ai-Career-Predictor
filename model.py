import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib

MODEL_PATH = "model.joblib"

def load_data(path="data/career_dataset.csv"):
    df = pd.read_csv(path)
    df['text_features'] = df['skills'].astype(str) + ' ' + df['interests'].astype(str) + ' cgpa_' + df['cgpa'].astype(str)
    return df

def train_and_save(path="data/career_dataset.csv"):
    df = load_data(path)
    X = df['text_features']
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    pipe = Pipeline([
        ('vec', CountVectorizer()),
        ('clf', RandomForestClassifier(n_estimators=200, random_state=42))
    ])
    pipe.fit(X_train, y_train)
    joblib.dump(pipe, MODEL_PATH)
    print("Model trained and saved to", MODEL_PATH)
    return pipe

def load_model():
    try:
        model = joblib.load(MODEL_PATH)
        return model
    except Exception:
        return None

def predict(model, skills_list, cgpa, interests):
    text = ';'.join(skills_list) + ' ' + ';'.join(interests) + ' cgpa_' + str(cgpa)
    # ensure model supports predict_proba
    try:
        pred = model.predict_proba([text])
        classes = model.classes_
        results = sorted(list(zip(classes, pred[0])), key=lambda x: x[1], reverse=True)
    except Exception:
        # fallback to predict
        pred_class = model.predict([text])[0]
        results = [(pred_class, 1.0)]
    return results
