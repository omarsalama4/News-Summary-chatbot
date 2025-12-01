# 📰 Article Summarizer Chatbot

An interactive chatbot interface for automated **news summarization**, powered by **Google Gemini 2.5 Flash**.  
The system generates concise summaries, extracts key topics, and proposes reflective questions from long-form articles — all within a **Streamlit** app.

---

## ✨ Features

- **Automated Summarization** → Summarize articles in ≤ 5 factual sentences  
- **Topic Extraction** → Identify the top 3 topics covered  
- **Question Generation** → Generate 3 thought-provoking reader questions  
- **Chatbot Interface** → Conversational design with session history  
- **Responsive GUI** → Built with Streamlit for real-time interaction  

---

## 🛠️ Technology Stack

- **Model**: Google Gemini 2.5 Flash  
- **Framework**: Streamlit  
- **Language**: Python  
- **Libraries**:  
  - `google-generativeai` → Gemini API access  
  - `rouge-score` → Summary evaluation  
  - `datasets` (Hugging Face) → Benchmarking with CNN/DailyMail  

---

## 📊 Methodology

- Uses **prompt engineering** to structure Gemini outputs  
- Benchmarked against CNN/DailyMail highlights  
- Evaluated with **ROUGE-1, ROUGE-2, ROUGE-L** metrics  
- Average scores:  
  - ROUGE-1 → 0.41  
  - ROUGE-2 → 0.25  
  - ROUGE-L → 0.39  

---

## 🚀 Deployment & Usage

1. Open the app in your browser.  
2. Enter your **Google Gemini API key** when prompted.  
3. Paste a news article into the input box.  
4. Use the chatbot interface to:  
   - 🧾 Summarize  
   - 🧠 Extract Topics  
   - ❓ Generate Questions  

---

## 📜 License

Licensed under the **MIT License**. See the `LICENSE` file for details.
