# 🩺 Medical RAG Chatbot

An AI-powered Medical Question Answering chatbot built using **LangChain**, **Groq Llama 3.1**, **FAISS**, **Hugging Face Embeddings**, and **Streamlit**.

The chatbot retrieves relevant information from medical documents using Retrieval-Augmented Generation (RAG) and generates accurate, context-aware responses using a Large Language Model (LLM).

---

## 🚀 Features

* 📚 Retrieval-Augmented Generation (RAG)
* 🤖 Powered by Groq Llama 3.1
* 🔍 Semantic Search using FAISS Vector Database
* 🧠 Hugging Face Sentence Transformer Embeddings
* 💬 Interactive Chat Interface built with Streamlit
* 📖 Answers generated only from the uploaded medical knowledge base
* ⚡ Fast inference using Groq API

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Groq API
* Hugging Face Embeddings
* FAISS
* Sentence Transformers
* Python Dotenv

---

## 📂 Project Structure

```text
Medical-RAG-Chatbot/
│
├── app.py
├── connect_memory_llm.py
├── create_memory_llm.py
├── requirements.txt
├── The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf
├── index.faiss
├── index.pkl
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/medical-rag-chatbot.git
```

```bash
cd medical-rag-chatbot
```

---

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create a `.env` file

```env
GROQ_API_KEY=_groq_api_key
```

---

### 5. Run the application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Medical documents are converted into vector embeddings.
2. Embeddings are stored in a FAISS vector database.
3. When a user asks a question:

   * Similar medical content is retrieved from FAISS.
   * Retrieved context is sent to the Groq Llama 3.1 model.
   * The model generates a context-aware answer.
4. The chatbot displays the response in a Streamlit interface.

---

## 📚 Knowledge Base

The chatbot uses:

* **The Gale Encyclopedia of Medicine (Second Edition)**

as its primary source for retrieval.



## 🔮 Future Improvements

* Upload custom medical PDFs
* Conversation memory
* Multi-document retrieval
* Source citations for answers
* Chat history export
* Voice input
* Medical image support
* Deployment on Streamlit Community Cloud

---

## ⚠️ Disclaimer

This chatbot is intended for educational and research purposes only.

It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical concerns.

---

## 👨‍💻 Author

**Dilip Singh**

GitHub: https://github.com/DilipSingh03

LinkedIn: https://www.linkedin.com/in/dilip-singh-77581b409

---

## ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.
