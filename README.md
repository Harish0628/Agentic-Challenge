
# Agentic Challenge

## Project Overview

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
 │   ├── llm_call.py          
 │   └── pdf_reader.py
 |   └──  pdf_analyzer.py
 |   └── test_pdf.pdf      
 ├── level2/
 │   ├── weather_mcp.py       
 │   └── client_agent.py       
 ├── requirements.txt
 └── README.md                
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
setx GEMINI_API_KEY "your_gemini_key"        
```

* **OpenWeather API Key**
```bash
setx OPENWEATHER_API_KEY "your_gemini_key"        
```

---

## Level 1: LLM & PDF Interaction

### LLM Call

**Sample :** ![LLM Call Screenshot](Images\llm_call_sample.png)

### PDF Analyzer

**Sample :**
 ![PDF Analyzer Screenshot](Images\PDF_analyzer_sample.png)


---

## Level 2: Weather Agent

### Start MCP Server

```bash
python level2/weather_mcp.py
```

* Starts a FastMCP server with a `get_weather(city)` tool.

**Sample :**
 ![MCP server Screenshot](Images\MCP_server_sample.png)

### Run Client Agent
**Sample :**
 ![CLient output Screenshot](Images\client_output1.png)

  ![CLient output Screenshot](Images\client_output2.png)

---

## LLM API Used

* **Google Gemini 2.5 Flash**

---

