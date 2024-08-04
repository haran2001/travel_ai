import requests
import json
import os
import streamlit as st
import os
from transformers import pipeline
from langchain.document_loaders import PyPDFLoader, DirectoryLoader, PDFMinerLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
import requests, json, sys

import pandas as pd
import simplejson as json

from dotenv import load_dotenv

load_dotenv('.env')

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_EMBEDDING_MODEL = "text-embedding-ada-002"
PROMPT_LIMIT = 3750
CHATGPT_MODEL = "gpt-4-1106-preview"


def get_embedding(chunk):
    url = "https://api.openai.com/v1/embeddings"
    headers = {
        "content-type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    data = {"model": OPENAI_EMBEDDING_MODEL, "input": chunk}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    embedding = response_json["data"][0]["embedding"]
    return embedding

# Display conversation history using Streamlit messages
def display_conversation(history):
    for i in range(len(history["generated"])-1,-1,-1):
        st.write(history["past"][i])
        st.write(history["generated"][i])

def create_pdf(path: str)->str:
    loader = PyPDFLoader(path)
    data = loader.load()
    pdfLoaderData = ""
    for page in data:
        pdfLoaderData = pdfLoaderData + page.page_content

    pdfLoaderData = pdfLoaderData.encode('utf-8').decode('unicode_escape')
    return pdfLoaderData

def make_data():
    for file in os.listdir('docs'):
        if '.pdf' in file:
            filepath = 'docs/' + file
    data = create_pdf(filepath)
    return data

def handle_query(question, data):
    prompt = build_prompt(question, data)
    print("\n==== PROMPT ====\n")
    print(prompt)
    answer = get_llm_answer(prompt)
    return json.dumps({"question": question, "answer": answer})

def add_logo():
    st.image("assets/images/images.jpg",width=250)

# Streamed response emulator
def response_generator(prompt):
    data = make_data()
    response = handle_query(prompt, data)
    response = json.loads(response)
    answer = response['answer']
    response = answer

    return response

def load_css():
    css_file = open('assets/style.css', 'r')
    st.markdown(f'<style>{css_file.read()}</style>', unsafe_allow_html=True)
    css_file.close()

def get_llm_answer(prompt):
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    messages.append({"role": "user", "content": prompt})

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "content-type": "application/json; charset=utf-8",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    data = {
        "model": CHATGPT_MODEL,
        "messages": messages,
        "temperature": 1,
        "max_tokens": 1000,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    print(response_json)
    print('KEY', OPENAI_API_KEY)
    completion = response_json["choices"][0]["message"]["content"]
    return completion


def read_csv_data():
    df = pd.read_excel("data/Countries.xlsx")
    json_data = df.to_json(orient="records")
    json_object = json.loads(json_data)
    print(json_object)
    return json_object

def build_prompt(query, data):
    prompt_start = (
        "Answer the question based on the context below. Use the context given to the best extent.  Don't start your response with the word 'Answer:'"
        "Rules: Rules: \
            List the best places to visit in country ‘X’ \
            Things to pack when visiting country ‘X’ \
            Any special health or visal requirements when visiting country ‘X’ \
            Best ways to convert currencies when visiting country ‘X’ \
            Best way to book travel, hotels and tickets in country ‘X’ \
            Other general tips when visiting country ‘X’ \
            User: I want to travel to India. Make a travel plan. \
            Identify the country that User wants to travel to and give him recommendations based on Rules \
            List best places to visit: \
            What is the best time to visit country ‘X’ \
            Most popular tourist spots in country ‘X’ \
            Hidden gems in country ‘X’"
        "Context:\n"
    )
    
    countries = read_csv_data()

    prompt_end = (
        f"\n\nQuestion: {query}\nAnswer:"
    )

    prompt = prompt_start + data + str(countries) + prompt_end
    
    return prompt  
