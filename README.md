# CineSage-GenAI-Project

<img width="840" height="789" alt="image" src="https://github.com/user-attachments/assets/2c6757c6-0ab5-4425-a31d-b14223fecba9" />

# 🎬 Movie Information Extractor (AI-Powered)

A **Streamlit** web application that uses **LangChain** and **Mistral AI** to automatically extract structured, professional-grade movie information from any plain text description. 

This project demonstrates **Structured Output Generation** using **Pydantic** and **PydanticOutputParser**.

---

## ✨ Features

- **📝 Intelligent Extraction:** Converts unstructured movie paragraphs into a clean JSON format.
- **🎭 Structured Data:** Automatically extracts:
  - Title
  - Release Year
  - Genre
  - Director
  - Cast
  - Rating
  - Summary
- **🛡️ Zero Hallucination:** Uses a Pydantic schema to force the AI to stick to the required fields and avoid inventing data.
- **⚡ Fast & Responsive:** Built with Streamlit and cached model loading for instant performance.
- **🖥️ Beautiful UI:** Simple, centered, and interactive interface.

---

## 🛠️ Tech Stack

| Category | Technology |
| :--- | :--- |
| Frontend | Streamlit |
| AI Framework | LangChain |
| Language Model | Mistral AI (`mistral-small-2506`) |
| Output Parsing | Pydantic + PydanticOutputParser |
| Environment | Python 3.9+ |

---

## 📁 Project Structure

```text
Movie_Info_Extractor/
├── app.py                 # Main Streamlit application
├── requirements.txt       # List of Python dependencies
├── .env                   # API keys (DO NOT push to GitHub)
└── README.md              # Project documentation
" />
