# 📂 Resume Analyzer Template

This repository is a **template project** for automating resume analysis using **Gemini CLI**.  
It includes a folder structure, scripts, and prompts to streamline the workflow.

---

## 🚀 Folder Structure

```

resume-analyzer-template/
├── resumes/    # PDF resumes to analyze
├── prompts/    # Prompt files for Gemini
├── scripts/    # Python helper scripts
├── outputs/    # JSON results
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/USERNAME/resume-analyzer-template
cd resume-analyzer-template
````

2. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

---

## 📝 Usage

1. Put your resume PDF files in the `resumes/` folder.
2. Ensure you have your optimized prompt in `prompts/evaluate_v2.txt`.
3. Run the batch command (Windows example):

```cmd
for %%f in (resumes\*.pdf) do (python scripts\pdf_to_text.py "%%f" | gemini -p prompts\evaluate_v2.txt > "outputs\%%~nf.json")
```

4. Check the `outputs/` folder for the JSON analysis results.

---

## 📌 Notes

* Update `requirements.txt` if you add more Python packages.
* This repo is designed as a **template**: click **“Use this template”** on GitHub to start a new project with the same structure.

---

## 🔑 License

Add your license info here (MIT, Apache 2.0, etc.).

```

---

👉 Now you can edit the README directly on GitHub (click the pencil ✏️ icon on the file) or locally in VS Code/Notepad and push changes.  

Would you like me to also give you a **requirements.txt** snippet (so new users just run `pip install -r requirements.txt`)?
```
