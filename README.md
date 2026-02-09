
# 🚀 Growth Engine AI

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20AI-Gemini%202.0%20Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An AI-powered "Content Velocity Engine" designed to accelerate organic growth on LinkedIn and X (Twitter) without using spam bots.**

---

## 📖 Overview

**Growth Engine AI** is a Human-in-the-Loop (HITL) application that leverages the **Google Gemini LLM** to eliminate writer's block and optimize content for social media algorithms. 

Unlike automation tools that risk account bans, this app focuses on **content creation and strategy**. It uses "Intent-based" posting, allowing you to generate high-quality drafts and post them directly to social platforms with a single click, keeping your account 100% safe.

### 🌟 Key Features

* **✍️ Viral Post Generator:**
    * Takes raw ideas/notes and transforms them into two formats simultaneously:
        * **LinkedIn:** Professional, story-driven, formatted for readability.
        * **Twitter/X:** Thread-style format (Hook + Value + Conclusion) under 280 chars.
    * *Tech:* Uses Few-Shot Prompting to mimic top-performing creator styles.

* **🎣 Hook Smith (A/B Tester):**
    * Analyzes your opening line and rewrites it using 5 viral psychological frameworks (e.g., Negative Bias, Curiosity Gap, Social Proof).
    * *Goal:* Increase "Stop Scroll" rate.

* **🔍 Profile Auditor:**
    * Acts as a Senior Personal Brand Consultant.
    * Grades your bio (0-10), identifies buzzwords, and suggests SEO-optimized improvements for higher conversion.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (Rapid UI Development)
* **LLM Engine:** [Google Gemini API](https://ai.google.dev/) (Model: `gemini-2.0-flash`)
* **Authentication:** Streamlit Secrets Management (Secure API Key handling)
* **Posting Mechanism:** Web Intent URLs (No paid platform APIs required)

---

## 📂 Repository Structure

```text
growth_engine_app/
├── app.py                  # Main application logic and UI
├── requirements.txt        # Python dependencies
├── .gitignore              # Security rules (prevents uploading keys)
├── README.md               # Project documentation
└── .streamlit/             # (Local only) Configuration folder
   └── secrets.toml        # (Local only) Stores your API Key

🚀 Installation & Local Setup
​Follow these steps to run the app on your own machine.
​1. Clone the Repository
git clone [https://github.com/Shwetam77777/growth-engine-ai.git](https://github.com/Shwetam77777/growth-engine-ai.git)
cd growth-engine-ai
2. Create Virtual Environment (Optional but Recommended)
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure API Key
​You need a free API key from Google.
​Get your key here: Google AI Studio
​Create a folder named .streamlit in the root directory.
​Create a file named secrets.toml inside that folder.
​Add the following line:
​<!-- end list -->
# .streamlit/secrets.toml
GOOGLE_API_KEY = "AIzaSy...[PASTE YOUR KEY HERE]"
5. Run the App
streamlit run app.py
The app will open in your browser at http://localhost:8501.
​☁️ Deployment (Streamlit Cloud)
​Deploying this app for public use is free and takes less than 2 minutes.
1.Push to GitHub: Ensure your code (excluding .streamlit/secrets.toml) is on GitHub.
2.Streamlit Cloud: Log in to share.streamlit.io.
3.New App: Click "New App" and select your repository.
4.Add Secrets (Crucial):
Before clicking "Deploy", click on Advanced Settings.
Go to the Secrets field.

Paste your API key in the TOML format:

GOOGLE_API_KEY = "AIzaSy...[PASTE YOUR KEY HERE]"

5.Deploy: Click the Deploy button.


❓ Troubleshooting
​Issue: ModuleNotFoundError: No module named 'google'
​Fix: Run pip install -r requirements.txt again. Ensure you are in the correct virtual environment.
​Issue: API Key not found
​Fix: Check that your .streamlit/secrets.toml file exists and is spelled correctly. If on Cloud, check the "Secrets" settings in the dashboard.
​Issue: Quota Exceeded
​Fix: The Gemini Free tier has limits (approx. 60 requests/minute). If you hit this, wait a minute and try again.
​🤝 Contributing
​Contributions are welcome!
​Fork the Project
​Create your Feature Branch (git checkout -b feature/AmazingFeature)
​Commit your Changes (git commit -m 'Add some AmazingFeature')
​Push to the Branch (git push origin feature/AmazingFeature)
​Open a Pull Request
​📄 License
​Distributed under the MIT License. See LICENSE for more information.
​Built with ❤️ by Shweta Mishra 
