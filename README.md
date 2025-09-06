# 📧 Daily SA News Digest Emailer

**Automate your morning routine with a personalized news briefing, delivered directly to your inbox.**

## 🧠 Inspiration

I realized I was becoming a "headless chicken" when it came to current affairs in my country. While countless news sites and YouTube channels exist, I never felt compelled to actively seek out the news. I noticed, however, that the first thing I do every morning is check my email.

This sparked an idea: **What if my daily news feed came directly to my inbox?** This would seamlessly integrate into my existing routine and ensure I never miss important local updates.

While I could subscribe to generic news site newsletters, they are often too broad. My core desire was to stay informed specifically about **South African governance and politics**. As a Computer Science and Applied Mathematics student, I decided to build a tailored solution myself.

The coolest part? The system is **fully customizable**. If I need to focus on specific individuals like President Cyril Ramaphosa or General Nhlanhla Mkhwanazi, I can simply adjust the script, and my daily digest will instantly reflect that focus.

## ⚙️ How It Works

This project is a Python-based automation tool that collects, filters, and delivers a tailored news digest directly to your inbox.

1.  **Fetch:** The script uses the NewsAPI to pull the latest headlines from specified South African news sources.
2.  **Filter:** It parses the results, focusing on keywords related to SA politics and governance.
3.  **Format:** The news is compiled into a clean, easy-to-read HTML email.
4.  **Deliver:** The script connects to a Gmail SMTP server and sends the digest.
5.  **Automate:** A Windows Task Scheduler job runs the script daily without any user interaction.

## 🛠️ Tech Stack

- **Python 3** (`requests`, `smtplib`, `email` libraries)
- **NewsAPI** (for news aggregation)
- **Gmail SMTP** (for email delivery)
- **Windows Task Scheduler** (for automation)

## 📦 Project Structure

```
daily-news-digest/
├── upTodate.py          # Main Python script
├── runDigest.bat        # Batch file to run the script
├── config.py            # Configuration file (API keys, emails - NOT tracked by git)
├── .gitignore          # Specifies files to ignore in version control
└── README.md           # This file
```

## 🚀 Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Ntsikayezwe-web/daily-news-digest.git
    cd daily-news-digest
    ```

2.  **Install required Python packages:**
    ```bash
    pip install requests
    ```

3.  **Configuration:**
    - Rename `config.example.py` to `config.py`.
    - Fill in your details:
        ```python
        # News API Configuration
        newsApiKey = "your_newsapi_key_here"

        # Email Configuration
        emailSender = "your.email@gmail.com"
        emailReceiver = "your.email@gmail.com"
        emailAppPass = "your_gmail_app_password" # 16-character token

        # Email Server Configuration
        smtpServer = "smtp.gmail.com"
        smtpPort = 587

        # News Sources & Filters
        newsSources = "news24,enca,dailymaverick"
        ```

4.  **Automation (Windows):**
    - Schedule the `runDigest.bat` file to run daily using **Task Scheduler**.

## 🔧 Customization

The true power of this project is its flexibility. Easily modify the `upTodate.py` script to:
- Change news sources (`newsSources` in `config.py`).
- Add or refine focus keywords (modify the `q` parameter in the API URL).
- Adjust the number of articles sent (change the slice `articles[:5]`).


**Enjoy your personalized news feed!** Now you can stay informed without even trying.

