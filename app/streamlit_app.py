import pandas as pd
import streamlit as st
from utils.sentiment import analyze_sentiment

st.set_page_config(page_title="Student Feedback Sentiment Analysis", page_icon="🎓", layout="wide")
st.title("🎓 Student Feedback Sentiment Analysis")
st.write("Analyze student feedback as Positive, Neutral, or Negative.")

mode=st.sidebar.radio("Choose input",["Single feedback","CSV file"])

if mode=="Single feedback":
    text=st.text_area("Enter student feedback",height=160,
        placeholder="Example: The teacher explains concepts clearly, but assignments are difficult.")
    if st.button("Analyze Feedback",type="primary"):
        if not text.strip(): st.warning("Please enter feedback.")
        else:
            r=analyze_sentiment(text)
            a,b,c=st.columns(3)
            a.metric("Sentiment",r["label"]); b.metric("Score",f'{r["score"]:.2f}'); c.metric("Confidence",f'{r["confidence"]:.0f}%')
            st.subheader("Explanation"); st.write(r["explanation"])
            st.subheader("Sentiment Keywords"); st.write(", ".join(r["keywords"]) if r["keywords"] else "None detected.")
else:
    up=st.file_uploader("Upload CSV",type=["csv"])
    st.caption("CSV must contain a column named feedback.")
    if up:
        df=pd.read_csv(up)
        if "feedback" not in df.columns: st.error("CSV must contain a 'feedback' column.")
        elif st.button("Analyze All Feedback",type="primary"):
            results=pd.DataFrame([analyze_sentiment(x) for x in df["feedback"].fillna("").astype(str)])
            out=pd.concat([df.reset_index(drop=True),results],axis=1)
            st.dataframe(out,use_container_width=True)
            st.subheader("Sentiment Distribution"); st.bar_chart(out["label"].value_counts())
            x,y,z=st.columns(3)
            x.metric("Positive",int((out.label=="Positive").sum()))
            y.metric("Neutral",int((out.label=="Neutral").sum()))
            z.metric("Negative",int((out.label=="Negative").sum()))
            st.download_button("Download Results CSV",out.to_csv(index=False).encode(), "sentiment_results.csv","text/csv")
st.divider()
st.subheader("About")
st.write("Educational prototype for analyzing student feedback. It uses lightweight rule-based NLP and is not intended for high-stakes decisions.")
