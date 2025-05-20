📄 ChatterPDF - Chat with Your PDFs Using Google Gemini + LangChain
Welcome to ChatterPDF, a powerful Streamlit-based application that allows you to chat with any PDF file using Google's Gemini (Generative AI) and LangChain. Upload a PDF, ask questions, and get accurate, context-based answers instantly.

🚀 Features
🤖 Uses Gemini 1.5 Flash for fast, high-quality responses.

🧠 Semantic search with FAISS vector store.

🔍 Smart text chunking via RecursiveCharacterTextSplitter.

📂 Supports PDF uploads directly in the web UI.

🗣️ Natural language question answering from PDF content.

🧠 Embedding powered by Google Generative AI Embeddings.

🛠️ Tech Stack
Streamlit: UI for interactive web app.

LangChain: Chain management and LLM integration.

Gemini 1.5 Flash: LLM via ChatGoogleGenerativeAI.

FAISS: Vector store for semantic similarity.

PyPDF2: PDF text extraction.

Google Generative AI: For both embedding and chat model.

📷 Screenshot
![image](https://github.com/user-attachments/assets/27cc3e9a-56d3-4773-9f91-0fa3588c8a0e)

⚙️ How It Works
Upload a PDF via the sidebar.

Submit & Process: The app extracts and chunks the text.

Chunks are embedded using Google's embedding-001 model.

Stored in a local FAISS vector store for retrieval.

Enter your question in the input box.

The app performs similarity search and passes relevant context to Gemini.

Final answer is streamed back to you!
