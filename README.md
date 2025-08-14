# Interactive Chatbot Interface for News Summarization

This repository contains the code for a chatbot-style graphical user interface (GUI) that performs automated news summarization. The system utilizes Google's Gemini 2.5 Flash model to generate concise summaries, topics, and reflective questions from news articles.

## Features

  - [cite\_start]**Automated Summarization**: Users can input long-form news articles and receive a concise summary of no more than five factual sentences[cite: 21].
  - [cite\_start]**Topic Extraction**: The interface can identify and list the top three topics covered in an article[cite: 21].
  - [cite\_start]**Question Generation**: It can also generate three thought-provoking questions a reader might have after reading the content[cite: 21].
  - [cite\_start]**User-Friendly Interface**: The GUI is developed using Streamlit, offering a responsive and interactive experience with features like real-time feedback and session state management[cite: 22, 24, 25].
  - [cite\_start]**Conversational Design**: The interface is designed in a chatbot style, maintaining a history of user interactions[cite: 23].

## Technology Stack

  - **Model**: Google Gemini 2.5 Flash
  - [cite\_start]**Framework**: Streamlit for the GUI [cite: 4, 22]
  - **Language**: Python
  - [cite\_start]**Dataset**: CNN/DailyMail summarization dataset (version 3.0.0) was used for benchmarking and evaluation[cite: 5, 15].
  - **Libraries**:
      - [cite\_start]`google-generativeai`: For accessing the Gemini model via API[cite: 20].
      - [cite\_start]`rouge_score`: For evaluating summary quality[cite: 6, 21].
      - [cite\_start]`Hugging Face datasets`: For loading and processing the CNN/DailyMail dataset[cite: 18].

## Methodology

[cite\_start]The project leverages prompt engineering to structure the output from the Gemini model[cite: 4, 21]. [cite\_start]The summaries were benchmarked against human-written highlights from the CNN/DailyMail dataset, and their quality was assessed using ROUGE-1, ROUGE-2, and ROUGE-L metrics[cite: 6, 17, 21]. [cite\_start]The average ROUGE scores for a sample batch of articles were 0.41 (ROUGE-1), 0.25 (ROUGE-2), and 0.39 (ROUGE-L)[cite: 28].

## Getting Started

Follow these steps to set up and run the project locally:

1.  **Clone the Repository**:

    ```sh
    git clone https://github.com/your-username/interactive-news-summarizer.git
    cd interactive-news-summarizer
    ```

2.  **Install Dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

3.  **Configure API Key**: Obtain a Google Gemini API key from the Google AI for Developers website.

4.  **Run the Application**:

    ```sh
    streamlit run app.py
    ```

    (Note: The main script may be named differently, e.g., `main.py` or `app.py`).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
