# LinkedIn Birthday Wishes Agent 🎂 🤖

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python](https://img.shields.io/badge/python-3.6%2B-blue)

An automated browser agent built with Python, LangChain, and browser_use that helps you check GitHub followers and automatically respond to LinkedIn birthday wishes.

## 📝 Introduction

This project demonstrates how to build browser automation agents using Python, LangChain, and the browser_use library. It includes two example functions:

1. **GitHub Follower Check**: Automatically checks the number of followers for a specified GitHub account
2. **LinkedIn Birthday Wishes Responder**: Automatically responds to birthday wishes on LinkedIn with personalized thank you messages

Perfect for learning browser automation and AI agents while solving real-world tasks!

## ✨ Features

- **GitHub Follower Counter**: Automatically visits a GitHub profile and reports the follower count
- **LinkedIn Birthday Wishes Responder**:
  - Logs into your LinkedIn account
  - Navigates to unread messages
  - Identifies birthday wishes
  - Responds with randomized thank you messages
  - Skips non-birthday messages
  - Provides a summary of actions taken
- **Configurable**: Easy to customize through environment variables
- **AI-Powered**: Uses LangChain with either OpenAI or Google Gemini models

## 🔧 Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- A web browser (Chrome is recommended)
- LinkedIn account (for the birthday wishes feature)
- API keys for either OpenAI or Google Gemini

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/linkedin-birthday-wishes-agent.git
cd linkedin-birthday-wishes-agent
```

### Windows

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### macOS/Linux

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## ⚙️ Configuration

1. Copy the example environment file:

```bash
cp .env.example .env
```

2. Edit the `.env` file with your credentials:

```
# Choose one of the following API keys based on your preferred model
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key

# LinkedIn credentials
USERNAME=your_linkedin_email
PASSWORD=your_linkedin_password

# GitHub URL for follower check
GITHUB_URL=https://github.com/ahsanayaz
```

## 📋 Usage

To run the application, you need to select which task you want to execute by uncommenting the appropriate line in `agent.py` or modifying the `asyncio.run()` statement at the bottom of the file.

### For GitHub Follower Check:

```python
# At the bottom of agent.py
asyncio.run(run_github_task())
```

### For LinkedIn Birthday Wishes:

```python
# At the bottom of agent.py
asyncio.run(run_linkedin_task())
```

Then run the script:

```bash
python agent.py
```

## 🔍 How It Works

The agent uses browser automation through the `browser_use` library to interact with web pages. Here's a high-level overview:

1. **Initialization**: The script initializes the browser and LLM (Language Learning Model) from either OpenAI or Google Gemini
2. **Task Definition**: Tasks are defined as detailed instructions for the AI agent
3. **Execution**: The agent follows the instructions, navigating through websites and performing actions
4. **Feedback**: The agent provides feedback on its actions and results

For the LinkedIn birthday wishes task, the agent:
- Logs into LinkedIn
- Navigates to the messaging section
- Identifies unread messages
- Analyzes each message to determine if it's a birthday wish
- Responds appropriately to birthday wishes
- Skips non-birthday messages
- Provides a summary of actions taken

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 👨‍💻 About the Author

This project is maintained by [Ahsan Ayaz](https://github.com/ahsanayaz).

- **YouTube**: [Code with Ahsan](https://youtube.com/codewithahsan) - Subscribe for more coding tutorials and projects!
- **Blog**: [AHSYNC BYTES](https://blog.codewithahsan.dev) - Check out more technical content and tutorials

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
