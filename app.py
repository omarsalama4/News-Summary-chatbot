import streamlit as st
import google.generativeai as genai

# ==== Setup ====
st.set_page_config(page_title="Article Summarizer Chatbot", layout="centered", page_icon="📰")
st.title("📰 Article Summarizer Chatbot")

# ==== Session State ====
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "last_article" not in st.session_state:
    st.session_state.last_article = ""

# ==== API Key Entry ====
api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")

    st.success("API key accepted. You can start chatting! ✨")

    # ==== Input Box ====
    article_input = st.text_area("📝 Enter a news article:", height=200)

    if st.button("🧾 Summarize"):
        if article_input.strip():
            # if article_input != st.session_state.last_article:
                # New article submitted → reset chat history
            st.session_state.chat_history = []
            st.session_state.last_article = article_input

            prompt = f"Summarize the following news article in no more than 5 concise, factual sentences:\n\n{article_input}"
            try:
                response = model.generate_content(prompt)
                summary = response.text.strip()
                st.session_state.chat_history.append(("You", article_input))
                st.session_state.chat_history.append(("Summary", summary))
            except Exception as e:
                st.error(f"Error generating summary: {e}")
        else:
            st.warning("Please paste an article first.")


    # ==== Show Chat History ====
    for role, message in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"**🧑 You:**\n\n{message}")
        elif role == "Summary":
            st.markdown(f"**🧾 Summary:**\n\n{message}")
        elif role == "Topics":
            st.markdown(f"**🧠 Topics:**\n\n{message}")
        elif role == "Questions":
            st.markdown(f"**❓ Questions:**\n\n{message}")

    # ==== Optional Buttons ====
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧠 Show Topics"):
            article = st.session_state.last_article
            if article:
                topic_prompt = f"List the top 3 topics covered in this article in bullet points:\n\n{article}"
                try:
                    response = model.generate_content(topic_prompt)
                    topics = response.text.strip()
                    st.session_state.chat_history.append(("Topics", topics))
                    st.rerun()
                except Exception as e:
                    st.error(f"Error generating topics: {e}")
            else:
                st.warning("Please summarize an article first.")

    with col2:
        if st.button("❓ Show Questions"):
            article = st.session_state.last_article
            if article:
                q_prompt = f"Based on the article below, write 3 thought-provoking questions a reader might ask:\n\n{article}"
                try:
                    response = model.generate_content(q_prompt)
                    questions = response.text.strip()
                    st.session_state.chat_history.append(("Questions", questions))
                    st.rerun()
                except Exception as e:
                    st.error(f"Error generating questions: {e}")
            else:
                st.warning("Please summarize an article first.")

else:
    st.info("Please enter your Gemini API key to begin.")

