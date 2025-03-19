# Portfolio Review Project

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org)
[![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)](https://www.javascript.com/)
[![Voiceflow](https://img.shields.io/badge/Voiceflow-000000?style=for-the-badge&logo=voiceflow&logoColor=white)](https://voiceflow.com/)

This is a web application designed to analyze and provide feedback on portfolio websites. It leverages AI Agents built using Voiceflow integration to analyze UX elements and generate comprehensive reports.

## Overview

The core functionality of this project revolves around AI-powered analysis of user experience (UX) elements within portfolio websites. By inputting a website URL, the application employs AI Agents to scrutinize various aspects of the site, delivering detailed reports on strengths and areas for improvement. This is done via integration with Voiceflow AI agents.

## Tech Stack

* **Backend:** Python (Django)
* **AI Agents Integration:** Voiceflow
* **Frontend:** HTML, Tailwind CSS, JavaScript

## Features

* **AI-Driven UX Analysis:** Utilizes Voiceflow AI Agents for in-depth website analysis.
* **Comprehensive Reports:** Generates detailed reports highlighting UX strengths and weaknesses.
* **Website Input:** Accepts website URLs for analysis.
* **User-Friendly Interface:** Provides a clean and intuitive user experience with Tailwind CSS and JavaScript.

## Getting Started

### Prerequisites

* Python 3.x
* pip (Python package installer)
* Virtual environment (recommended)
* Voiceflow Account and API Key

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/SonalSahwal/portfolio_review_project.git
    cd portfolio-review-project
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Configure Voiceflow Integration:**

    * Add your Voiceflow API Key and project ID to the appropriate settings in your Django project.
    * Ensure your Voiceflow AI Agents are configured to handle website analysis.
  
    * VoiceFlow Code to query OpenAI Vision:

```
{
    "model": "gpt-4o-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Take a good look at the image, it is a full screenshot of a portfolio website. Analyse the image I have provided, understand and review the UX design and give me a full detailed review of the portfolio website. Everything from the good and bad, and also things to improve on. Go into details and provide a constructive feedback."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "{last_utterance}"
                    }
                }
            ]
        }
    ],
    "max_tokens": 1000
}
```


4.  **Run the development server:**

    ```bash
    python3 manage.py runserver
    ```

5.  **Access the application:**

    * Open your browser and navigate to `http://127.0.0.1:8000/`.

## AI Agents (Voiceflow)

The AI Agents, powered by Voiceflow, are the core of the website analysis functionality. They are configured to:

* Receive website URLs as input.
* Scrape and analyze the website's HTML structure.
* Evaluate UX elements such as navigation, design, content, and accessibility.
* Generate detailed reports with actionable feedback.

