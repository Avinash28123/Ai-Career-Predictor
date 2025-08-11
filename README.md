# AI Career Path Predictor

This is a starter project for an AI-based career path predictor. It includes a demo ML pipeline and a Streamlit UI.

## Quick start (local)
1. Create virtualenv and install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
python -c "from model import train_and_save; train_and_save()"
streamlit run app.py
