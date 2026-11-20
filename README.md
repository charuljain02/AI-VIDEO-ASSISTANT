
# 🎬 AI Video Assistant

An AI-powered application that converts YouTube videos and audio/video recordings into meaningful summaries, transcripts, and actionable insights.

🔗 **Live Demo:** https://ai-video-assistant-r6fugt9sgxkfpxzt9xye5m.streamlit.app/

## ✨ Features

- 🎥 **YouTube & Local File Support** – Process YouTube videos and uploaded media files.
- 🎙️ **Speech-to-Text** – Generate transcripts using OpenAI Whisper.
- 🌐 **Multilingual Transcription** – Support for Hindi/Hinglish transcription using Sarvam AI.
- 📝 **AI Summarization** – Generate concise summaries of lengthy videos and meetings.
- 📌 **Automatic Title Generation** – Generate meaningful titles from video content.
- ✅ **Action Item Extraction** – Identify important tasks and follow-ups.
- 🔑 **Decision Extraction** – Extract key decisions from meetings.
- ❓ **Question Extraction** – Identify important questions and unresolved points.
- 💬 **AI Chatbot** – Ask questions about processed content.
- 🧠 **RAG Pipeline** – Retrieve relevant information using Hugging Face embeddings and ChromaDB.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Frontend | Streamlit |
| Language | Python |
| Audio Processing | yt-dlp, pydub, FFmpeg |
| Speech Recognition | OpenAI Whisper |
| Multilingual AI | Sarvam AI |
| LLM | Groq |
| LLM Framework | LangChain |
| Embeddings | Hugging Face |
| Vector Database | ChromaDB |
| Deep Learning | PyTorch |
| PDF Generation | ReportLab, FPDF |

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-VIDEO-ASSISTANT
```

### 2. Create a Virtual Environment

```bash
uv venv
```

Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

Make sure FFmpeg is installed on your system.

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
SARVAM_API_KEY=your_sarvam_api_key
```

Add other API keys if required by your configuration.

### 5. Run the Application

```bash
streamlit run app.py
```

## 🔄 How It Works

1. Enter a YouTube URL or upload a media file.
2. Extract and preprocess the audio.
3. Split long audio into manageable chunks.
4. Generate a transcript using the selected transcription service.
5. Generate an AI-powered summary and title.
6. Extract action items, decisions, and questions.
7. Store transcript information as embeddings in ChromaDB.
8. Ask questions through the RAG-based chatbot.

## 💡 Use Cases

- Summarizing long YouTube videos and lectures.
- Creating notes from educational content.
- Generating meeting summaries.
- Extracting tasks and important decisions.
- Asking questions about video content.
- Understanding lengthy recordings quickly.

## 🔐 Security

- Store API keys in environment variables or Streamlit Secrets.
- Never commit your `.env` file.
- Do not expose API keys publicly.

## 🎯 Project Objective

To simplify the process of understanding long videos and meeting recordings using Speech Recognition, Large Language Models, and Retrieval-Augmented Generation (RAG).

---

**Built with ❤️ using Python, Streamlit, Groq, Whisper, Sarvam AI, LangChain, and ChromaDB.**
