# AI Career Path Predictor

This is a starter project for an AI-based career path predictor. It includes a demo ML pipeline and a Streamlit UI.

## Quick start (local)
1. Create virtualenv and install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\\Scripts\\activate
   pip install -r requirements.txt
   ```
2. Train demo model:
   ```bash
   python -c "from model import train_and_save; train_and_save()"
   ```
3. Run Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Deploy on Streamlit Cloud
1. Push this repo to GitHub
2. Go to https://share.streamlit.io and connect your GitHub account
3. Click "New app", select the repo, branch (main) and file `app.py`
4. Deploy and get the public URL

## Firebase (optional) - Secrets
1. Create Firebase project and enable Firestore
2. Create service account JSON and keep it safe
3. On Streamlit Cloud, go to "Secrets" and add key `FIREBASE_SERVICE_ACCOUNT` with the JSON content
4. In code, load secrets and initialize firestore using firebase_admin and credentials.Certificate
