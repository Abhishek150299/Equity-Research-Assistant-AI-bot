import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from constants import openai_key
from langchain.chat_models import ChatOpenAI
from openai import OpenAIError
import nltk
#nltk.download('punkt_tab')
#nltk.download('averaged_perceptron_tagger_eng')
 
if 'OPENAI_API_KEY' not in os.environ:
    st.error("The OPENAI_API_KEY environment variable is not set.")
    st.stop()

os.environ["OPENAI_API_KEY"] = openai_key

st.image('chatbot.png', width=200)
st.title("Equity Research Assistant")
st.sidebar.title("Research articles URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Analyze Articles!!")
file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()
llm = ChatOpenAI()
if process_url_clicked:
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()
    # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)
    if not docs:
        st.error("No data was retrieved from the provided URLs. Please check the links.")
        st.stop()
    # create embeddings and save it to FAISS index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)
    vectorstore_openai.save_local("faiss_index")


query = main_placeholder.text_input("Enter your Question: ")
if query:
    if os.path.exists(file_path):
        vectorstore = FAISS.load_local("faiss_index", OpenAIEmbeddings(), allow_dangerous_deserialization=True)
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
        result = chain({"question": query}, return_only_outputs=True)
       
        st.header("Answer")
        st.write(result["answer"])

        # Sources
        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n") 
            for source in sources_list:
                st.write(source)