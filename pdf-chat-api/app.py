import pickle
import os
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS 
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from langchain.text_splitter import CharacterTextSplitter
import faiss
from langchain.embeddings.huggingface import HuggingFaceEmbeddings


load_dotenv()

# os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = "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"

def main():
    st.header("PDF Chat API")

    pdf = st.file_uploader("Upload a PDF file", type=["pdf"])
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        raw_text = ''
        for i,page in enumerate(pdf_reader.pages):
            text = page.extract_text()  # page.extractText() in PyPDF2
            if text:
                raw_text += text
        
        text_splitter = CharacterTextSplitter(
        separator = '\n',
        chunk_size = 1000, # 1000 characters
        chunk_overlap = 200, # 200 characters
        length_function = len # len(text) to get number of characters
        )
        text_chunks = text_splitter.split_text(raw_text)

        store_name = pdf.name[:-4]
        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl", "rb") as f:
                pkl = pickle.load(f)
                docsearch = FAISS.deserialize_from_bytes(pkl,OpenAIEmbeddings())
            st.write("Loaded docsearch from pickle")
        else:
            docsearch = FAISS.from_texts(text_chunks, OpenAIEmbeddings())
            pkl = docsearch.serialize_to_bytes()  # serializes the faiss index to bytes
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(pkl, f)
            st.write("Created docsearch and saved to pickle")

        query = st.text_input("Ask a question")

        if query:
            docs = docsearch.similarity_search(query)
            chain = load_qa_chain(OpenAI(), chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query)
                print(cb)
            st.write(response)
    return "Hello World!"

if __name__ == '__main__':
    main()