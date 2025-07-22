from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st 
load_dotenv()
model = ChatOpenAI(model='gpt-4')

st.header("My Chat Model")
papertype = st.selectbox("Select the documentary",["Scotland: A Wild Year","The Story of Scotland","Scotland: Rome’s Final Frontier","Scotland’s Greatest Escape","secrets of Great British Castles","Scotlands Greatest Castles","Castles: Britain’s Fortified History"])
styleType = st.selectbox("Select the explanation type",["Example-Based","Analytical","Technical","StoryTelling"])
lengthInput = st.selectbox("Select the length:",["Short","Detailed","Indepth","Brief",])

template = PromptTemplate(
    template = """Please summarize the follwing documentary {papertype}"with the following specifications:
    1.Explanation Style : {styleType}
    2.Explanation length : {lengthInput}
      """  , 
    input_variables=["papertype","styleType","lengthInput"]
)

prompt = template.invoke({
    'papertype':papertype,
    'styleType':styleType,
    'lengthInput': lengthInput
    })

if st.button("ENTER"):
     result = model.invoke(prompt)
     st.markdown(result.content)