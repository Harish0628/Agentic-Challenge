
# Agentic Challenge

## Project Overview

This project demonstrates building agentic AI workflows using **LLMs** and **tool integration**. It includes:

1. **Level 1**: Exploration & setup

   * Simple LLM call using Google Gemini API
   * PDF reading & analysis with a GUI interface

2. **Level 2**: Building agent behaviors

   * MCP server (`weather_mcp.py`) exposing a weather tool
   * Client agent (`client_agent.py`) querying the MCP tool and LLM

---

## Folder Structure

```
/agentic-challenge
 ├── level1/
 │   ├── llm_call.py          # simple Gemini API call
 │   └── pdf_reader.py        # PDF reader with GUI
 ├── level2/
 │   ├── weather_mcp.py       # MCP server with get_weather tool
 │   └── client_agent.py      # client calling MCP + LLM
 ├── requirements.txt         # Python dependencies
 └── README.md                # this file
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <your_github_repo_link>
cd agentic-challenge
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**Note:**

* `tkinter`, `pathlib`, and `ctypes` are standard Python libraries.
* Make sure Python 3.9+ is installed.

### 3. Environment Variables

* **Gemini API Key**

```bash
export GEMINI_API_KEY="your_gemini_key"      # Linux / Mac
setx GEMINI_API_KEY "your_gemini_key"        # Windows
```

* **OpenWeather API Key**
  Currently stored in `weather_mcp.py`. Optionally, you can move it to an environment variable.

---

## Level 1: LLM & PDF Interaction

### LLM Call

```bash
python level1/llm_call.py
```

* Sends a prompt to Gemini and prints the response.

### PDF Reader

```bash
python level1/pdf_reader.py
```

* Input: PDF file path and user prompt
* Output: LLM’s response based on PDF content
* GUI allows pasting file path and entering prompts.

**Sample Input:**

```
Prompt: "Summarize this PDF."
```

**Sample Output:**

```
"The document describes the architecture of a weather forecasting system..."
```

---

## Level 2: Weather Agent

### Start MCP Server

```bash
python level2/weather_mcp.py
```

* Starts a FastMCP server with a `get_weather(city)` tool.

### Run Client Agent

```bash
python level2/client_agent.py
```

* Input: natural language query, e.g., `"Is it raining in Hyderabad today?"`
* Output: parsed weather response from API, e.g.:

```
"According to the weather API, it's cloudy with light rain, 27°C with 65% humidity in Hyderabad."
```

---

## LLM API Used

* **Google Gemini 2.5 Flash**

---

## Submission

* Push repository to GitHub
* Submit the public GitHub link via the form:
  `https://formsxxxxxxxxxxxrJtR9`

---

This README is **complete and clear**, covers setup, usage, sample inputs/outputs, API info, and submission instructions.

---

If you want, I can **also make a polished `requirements.txt` + final folder structure ready to push** alongside this README. That way you can submit immediately.

Do you want me to do that?
