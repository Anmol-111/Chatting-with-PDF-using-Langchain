<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>ChatterPDF - Chat with Your PDFs</title>
  <style>
    body {
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 2rem;
      background-color: #f5f7fa;
      color: #333;
    }

    h1, h2 {
      color: #2c3e50;
    }

    h1 {
      border-bottom: 3px solid #2980b9;
      padding-bottom: 0.5rem;
    }

    ul {
      list-style-type: none;
      padding: 0;
    }

    li {
      background-color: #fff;
      border-left: 5px solid #3498db;
      padding: 1rem;
      margin: 0.5rem 0;
      box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }

    .screenshot img {
      max-width: 100%;
      margin: 1rem 0;
      border: 2px solid #ccc;
      border-radius: 8px;
    }

    .section {
      margin-bottom: 2rem;
    }

    code {
      background-color: #e8e8e8;
      padding: 2px 5px;
      border-radius: 3px;
    }

    .highlight {
      background-color: #ecf0f1;
      padding: 1rem;
      border-left: 5px solid #2980b9;
      font-family: monospace;
      white-space: pre-wrap;
    }
  </style>
</head>
<body>

  <h1>📄 ChatterPDF - Chat with Your PDFs Using Google Gemini + LangChain</h1>

  <div class="section">
    <p>
      Welcome to <strong>ChatterPDF</strong>, a powerful Streamlit-based application that allows you to chat with any PDF file using 
      <strong>Google's Gemini (Generative AI)</strong> and <strong>LangChain</strong>. Upload a PDF, ask questions, and get accurate, context-based answers instantly.
    </p>
  </div>

  <div class="section">
    <h2>🚀 Features</h2>
    <ul>
      <li>🤖 Uses <strong>Gemini 1.5 Flash</strong> for fast, high-quality responses.</li>
      <li>🧠 Semantic search with <strong>FAISS vector store</strong>.</li>
      <li>🔍 Smart text chunking via <strong>RecursiveCharacterTextSplitter</strong>.</li>
      <li>📂 Supports <strong>PDF uploads</strong> directly in the web UI.</li>
      <li>🗣️ Natural language <strong>question answering</strong> from PDF content.</li>
      <li>🧠 Embedding powered by <strong>Google Generative AI Embeddings</strong>.</li>
    </ul>
  </div>

  <div class="section">
    <h2>🛠️ Tech Stack</h2>
    <ul>
      <li><strong>Streamlit</strong>: UI for interactive web app.</li>
      <li><strong>LangChain</strong>: Chain management and LLM integration.</li>
      <li><strong>Gemini 1.5 Flash</strong>: LLM via ChatGoogleGenerativeAI.</li>
      <li><strong>FAISS</strong>: Vector store for semantic similarity.</li>
      <li><strong>PyPDF2</strong>: PDF text extraction.</li>
      <li><strong>Google Generative AI</strong>: For both embedding and chat model.</li>
    </ul>
  </div>

  <div class="section screenshot">
    <h2>📷 Screenshot</h2>
    <img src="https://github.com/user-attachments/assets/27cc3e9a-56d3-4773-9f91-0fa3588c8a0e" alt="ChatterPDF Screenshot 1">
    <img src="https://github.com/user-attachments/assets/8bcf6836-662f-4b82-bb1a-84e8e00491d0" alt="ChatterPDF Screenshot 2">
  </div>

  <div class="section">
    <h2>⚙️ How It Works</h2>
    <ol>
      <li>📁 Upload a PDF via the sidebar.</li>
      <li>🧩 <strong>Submit & Process</strong>: The app extracts and chunks the text.</li>
      <li>🔗 Chunks are embedded using <code>embedding-001</code> model.</li>
      <li>💾 Stored in a local <strong>FAISS vector store</strong> for retrieval.</li>
      <li>💬 Enter your question in the input box.</li>
      <li>🧠 Performs <strong>similarity search</strong> and passes relevant context to Gemini.</li>
      <li>📨 Final <strong>answer is streamed</strong> back to you!</li>
    </ol>
  </div>

</body>
</html>
