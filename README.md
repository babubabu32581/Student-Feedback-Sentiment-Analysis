# Student Feedback Sentiment Analysis
Educational Python + Streamlit project for **Sentiment Analysis of Student Feedback for Course Improvement**.

## Features
- Single feedback sentiment classification
- Positive / Neutral / Negative result
- Score, confidence and keywords
- CSV batch analysis
- Sentiment distribution chart
- Downloadable results

## Run
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m streamlit run app/streamlit_app.py
```
Use `data/sample_feedback.csv` for a quick demo.

## Method
Lightweight rule-based NLP with positive/negative vocabulary and simple negation handling. It is designed for an academic demonstration.
