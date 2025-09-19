Here’s your **README.md** with icons and badges added — content is exactly the same, only more attractive ✨

---

# 📌 Issue Summarizer to CSV

> 📝 A simple app to summarize technical issue messages and store the results in a CSV file.
> ⚡ Powered by **Groq API** for fast LLM-based summarization, with a clean **Streamlit** interface.

---

## 📑 Table of Contents

* [✨ Features](#-features)
* [🛠 Requirements](#-requirements)
* [📥 Installation](#-installation)
* [🔑 Configuration](#-configuration)
* [🚀 Usage](#-usage)
* [📂 Directory Structure](#-directory-structure)
* [📌 Examples](#-examples)
* [🤝 Contributing](#-contributing)
* [📄 License](#-license)

---

## ✨ Features

* 🎯 Enter any technical issue message through a friendly **Streamlit** UI.
* 🤖 Summarize the message instantly using the **Groq API** (LLM).
* 💾 Save transcripts, summaries, and sentiments into a CSV file (`data/result.csv`).
* 👀 View or download the CSV directly from the app.
* 🧩 Modular code (separate logic for summarization, sentiment, and frontend).

---

## 🛠 Requirements

* 🐍 Python 3.8+
* 🌐 [Streamlit](https://streamlit.io/) for the web interface
* 🔑 [Groq API](https://console.groq.com/) account and key
* 📦 All dependencies listed in `requirements.txt`

---

## 📥 Installation

1️⃣ Clone the repository:

```bash
git clone https://github.com/Ajan2k/issue-summarizer-to-csv.git
cd issue-summarizer-to-csv
```

2️⃣ Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

### Groq API Key

This project uses the **Groq API** for summarization.

1. 🔐 Get an API key from [Groq Console](https://console.groq.com/).
2. Set it as an environment variable before running the app:

   ```bash
   export GROQ_API_KEY="your_api_key_here"
   ```

   *(Windows PowerShell)*:

   ```powershell
   setx GROQ_API_KEY "your_api_key_here"
   ```

> ⚠️ **Never** hardcode or commit your API key.

---

## 🚀 Usage

Launch the **Streamlit** frontend:

```bash
streamlit run app/app.py
```

* 🌐 Open the URL displayed in the terminal (usually `http://localhost:8501`).
* 🖊 Enter a technical issue message in the text box.
* 🔍 Click **Summarize & Save**.
* 📊 View results or download the CSV from `data/result.csv`.

---

## 📂 Directory Structure

```
.
├── app/
│   └── app.py            # Streamlit frontend
├── data/
│   └── result.csv        # Output CSV with summaries
├── src/
│   ├── llm.py            # Groq API integration
│   ├── sentiment.py      # Sentiment analysis helper
│   └── utils.py          # (optional) utility functions
├── requirements.txt
└── README.md
```

---

## 📌 Examples

1️⃣ Start the app:

```bash
streamlit run app/app.py
```

2️⃣ Input:

> “Facing authentication errors when logging into the dashboard.”

3️⃣ Output in `result.csv`:

| 🗒 Transcript                 | ✍️ Summary                     | 🙂 Sentiment |
| ----------------------------- | ------------------------------ | ------------ |
| Facing authentication errors… | Login fails due to auth issues | Negative     |

---

## 🤝 Contributing

💡 We welcome contributions!

* 🍴 Fork the repo
* 🌱 Create a feature branch
* 💻 Commit your changes with clear messages
* 🚀 Submit a PR

---

## 📄 License

📜 Specify your license (e.g., MIT).

---

Would you like me to save this as a `README.md` file so you can drop it straight into your repo?
