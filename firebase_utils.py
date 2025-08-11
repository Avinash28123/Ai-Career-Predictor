import firebase_admin
from firebase_admin import credentials, firestore

def init_firebase(service_account_json_path):
    cred = credentials.Certificate(service_account_json_path)
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db

def save_report(db, collection_name, data):
    doc_ref = db.collection(collection_name).document()
    doc_ref.set(data)
    return doc_ref.id
