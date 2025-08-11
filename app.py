import streamlit as st
from model import load_model, train_and_save, predict
from roadmap_generator import generate_roadmap
from pdf_exporter import create_pdf

st.set_page_config(page_title="AI Career Path Predictor", layout='centered')
st.title("AI Career Path Predictor")

with st.expander("Instruction"):
    st.write("Enter your skills (comma separated), CGPA, and interests. Click Predict.")

if st.button('Train Demo Model'):
    pipe = train_and_save()
    st.success('Demo model trained and saved (model.joblib)')

skills_input = st.text_input('Skills (comma separated)', 'python, pandas, machine learning')
cgpa_input = st.number_input('CGPA', min_value=0.0, max_value=10.0, value=6.5, step=0.1)
interests_input = st.text_input('Interests (comma separated)', 'data science, ml')

if st.button('Predict Career Paths'):
    model = load_model()
    if model is None:
        st.warning('No model found. Click Train Demo Model first.')
    else:
        skills = [s.strip() for s in skills_input.split(',') if s.strip()]
        interests = [s.strip() for s in interests_input.split(',') if s.strip()]
        results = predict(model, skills, cgpa_input, interests)
        roadmap = generate_roadmap(results, skills, cgpa_input)
        st.write('### Top Predictions')
        for career, score in results[:3]:
            try:
                pct = round(float(score)*100,2)
            except Exception:
                pct = score
            st.write(f"**{career}** - {pct}%")
        st.write('### Suggested Roadmaps')
        for career, info in roadmap.items():
            st.write(f"**{career}** - Confidence: {info['confidence']}%")
            for step in info['recommended_path']:
                st.write('- ' + step)
        if st.button('Download PDF Report'):
            report = {'Name': 'Demo User', 'CGPA': cgpa_input, 'Predictions': {c: float(s) for c, s in results[:3]}}
            out = create_pdf(report, out_path='career_report.pdf')
            with open(out, 'rb') as f:
                st.download_button('Download Report', f, file_name='career_report.pdf')
