import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash-latest')

st.set_page_config(
    page_title="ChatterPDF",
    page_icon="icon.png"
)

st.title("Chatting with PDF and LLM")
user_question = st.text_input("Ask a Question from the PDF File")
st.sidebar.title("MENU:")
st.sidebar.text("Upload your PDF Files and Click on the submit & Process Button")
pdf = st.sidebar.file_uploader("Upload your PDF here:")
if st.button("Submit & Process"):

    # Get the text from the pdf(Working like pdf loader)
    text=""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        text+=page.extract_text()

    # Text Splitter -> Recursive character text splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )
    chunks = splitter.split_text(text)

    # Vector Store for store and semantic search of embeddings
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(chunks, embedding=embedding)
    vector_store.save_local('faiss_index') # Locally save the embedding into the faiss store

    # user input
    user_ques_vector_store = FAISS.load_local("faiss_index", embedding, allow_dangerous_deserialization=True)
    docs = user_ques_vector_store.similarity_search(user_question)

    prompt = PromptTemplate(
        template="""
        Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
        provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
        Context:\n {context}?\n
        Question: \n{question}\n

        Answer:
        """,
        input_variables=['context', 'question']
    )

    parser = StrOutputParser()

    chain = prompt | model | parser

    response = chain.invoke({'context': docs, 'question': user_question})

    print(response)

    st.write("Reply :\n", response)
    st.success("Done")