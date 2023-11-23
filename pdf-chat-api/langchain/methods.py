from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS 
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

def read_pdf_text(file_path):
    """ Read a PDF file and return the text"""
    pdf = PdfReader(file_path)
    raw_text = ''
    for i,page in enumerate(pdf.pages):
        text = page.extract_text()  # page.extractText() in PyPDF2
        if text:
            raw_text += text
    return raw_text

def text_splitter(text):
    """Split text into chunks of 1000 characters with 200 characters overlap"""
    text_splitter = CharacterTextSplitter(
        separator = '\n',
        chunk_size = 1000, # 1000 characters
        chunk_overlap = 200, # 200 characters
        length_function = len # len(text) to get number of characters
    )
    return text_splitter.split_text(text)

def embeddings(text):
    """Return embeddings for text"""
    embeddings = OpenAIEmbeddings()
    return embeddings.embed(text)


def create_docsearch(file_path):
    """Create a docsearch object from a PDF file"""
    print(file_path)
    raw_text = read_pdf_text(file_path)
    text_chunks = text_splitter(raw_text)
    embeddings = OpenAIEmbeddings()
    docsearch = FAISS.from_texts(text_chunks,embeddings)
    return docsearch

def query_docsearch(docsearch,query):
    """Query a docsearch object"""
    chain = load_qa_chain(OpenAI(), 
                      chain_type="stuff")
    docs = docsearch.similarity_search(query)
    response = chain.run(input_documents=docs, question=query)
    return response