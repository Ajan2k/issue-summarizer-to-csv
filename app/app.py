import streamlit as st
import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.llm import LLM
from src.sentiment import find_sentiment

llm =LLM()
file_path = "data/result.csv"
st.title("Issue Summarizer")
message = st.text_input("enter the technical issue message here")

df = pd.DataFrame([{
    "Transcript": message,
    "Summary": llm.llm_summarize(message),
    "Sentiment": find_sentiment(message)
}])

results, save_csv,show_csv = st.columns(3)
if results.button("results", width="stretch"):
    if llm.llm_summarize(message) == "I only summarize your given problems.":
        st.warning("Please give a valid problem statement as input")
    else :
        st.table(df)

if show_csv.button("show csv datas",width="stretch"):
    st.write(pd.DataFrame(pd.read_csv(file_path,encoding="utf-8")))

if save_csv.button("save_csv", icon="😃", width="stretch"):
    if not message.strip() or llm.llm_summarize(message) == "I only summarize your given problems.":
        st.warning("Please give a valid problem statement as input")
    elif not os.path.isfile(file_path):
        df.to_csv(file_path, index=False)
    else:
        df.to_csv(file_path, mode='a', header=False, index=False)
        st.success("data added")