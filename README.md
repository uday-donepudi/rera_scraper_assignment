
# 🏗️ RERA Odisha Project Scraper

This Python script scrapes the first 6 projects listed under the “Projects Registered” section on the [Odisha RERA Project List](https://rera.odisha.gov.in/projects/project-list) website using Selenium.

## 📋 Data Extracted Per Project

For each of the first 6 projects, the script extracts:

- ✅ **RERA Regd. No.**
- 🏘️ **Project Name**
- 👤 **Promoter Name** 
- 🏠 **Promoter Address** 
- 💰 **GST No.**

## ⚙️ Requirements

Install the required Python package:

```bash
pip install -r requirements.txt
```

## 🐍 Environment

- **Python:** 3.11.9  
- **Selenium:** 4.32.0  
- **Google Chrome:** (latest recommended, tested on Chrome 125+)  
- **ChromeDriver:** Must match your installed Chrome version  

### 🔧 Set up ChromeDriver

1. Download the appropriate ChromeDriver version:  
   [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

2. Update the path in your script:

```python
path = r"C:\path\to\chromedriver.exe"
```

## 🚀 How to Run

Use the following command:

```bash
python app.py
```

## 📦 Output

The script prints a JSON array of the 6 project details to the console. Example Output Structure
```json
[
  {
    "RERA Regd. No.": "",
    "Project Name": "",
    "Promoter Name": "",
    "Address": "",
    "GST No.": ""
  },
  ...
]
```

## 📄 License

This project is for educational and evaluation purposes only.
