# 🧠 Resume Analyzer Template

이 프로젝트는 **Google Gemini API**를 활용해 이력서(PDF)를 자동으로 분석하고,
결과를 JSON 형식으로 정리해주는 템플릿입니다.
Python 스크립트와 Gemini CLI를 조합해 작동하며, 로컬 환경에서 쉽게 실행할 수 있습니다.

---

## 🚀 주요 기능

* 📄 **PDF 이력서 자동 텍스트 변환**
  → `scripts/pdf_to_text.py` 사용
* 🤖 **Gemini 모델을 이용한 이력서 분석**
  → `prompts/evaluate.txt` 프롬프트 기반
* 🧾 **분석 결과 자동 저장 (JSON)**
  → `outputs/` 폴더에 결과 파일 생성
* 🧰 **자동화된 배치 실행 (PowerShell 명령으로 여러 파일 분석)**

---

## 📁 폴더 구조

```
resume-analyzer-template/
│
├── resumes/                # 분석할 PDF 이력서들을 넣는 폴더
├── outputs/                # Gemini 결과(JSON)가 저장되는 폴더
│
├── prompts/
│   └── evaluate.txt        # Gemini 모델에게 전달할 프롬프트 템플릿
│
├── scripts/
│   └── pdf_to_text.py      # PDF → 텍스트 변환 스크립트
│
├── requirements.txt        # 필요한 Python 패키지 목록
└── README.md               # 이 파일
```

---

## ⚙️ 환경 설정

### 1. Python 설치

[Python 3.9+](https://www.python.org/downloads/) 버전을 설치하세요.

### 2. 필요한 패키지 설치

터미널에서 다음 명령어를 실행합니다:

```bash
pip install -r requirements.txt
```

**requirements.txt 예시**

```
PyMuPDF
```

> ⚠️ `fitz` 모듈이 없다는 에러가 날 경우 →
> `pip install PyMuPDF` 를 직접 실행하세요.

---

## 🔑 Gemini API Key 설정

1. [Google AI Studio](https://aistudio.google.com/app/apikey)에서 API Key를 발급받습니다.
2. Windows PowerShell에서 다음 명령으로 등록합니다:

   ```powershell
   setx GEMINI_API_KEY "your_api_key_here"
   ```
3. 등록 확인:

   ```powershell
   echo $env:GEMINI_API_KEY
   ```

---

## 💻 실행 방법

1. `resumes` 폴더에 분석할 PDF 파일을 넣습니다.
2. PowerShell에서 프로젝트 폴더로 이동:

   ```powershell
   cd "C:\Users\<사용자>\Downloads\resume-analyzer-template"
   ```
3. 다음 명령어를 실행:

   ```powershell
   Get-ChildItem resumes\*.pdf | ForEach-Object {
       python scripts\pdf_to_text.py $_.FullName |
       gemini -p prompts\evaluate.txt |
       Out-File ("outputs\" + $_.BaseName + ".json") -Encoding UTF8
   }
   ```
4. 완료 후 `outputs` 폴더에 각 이력서별 `.json` 결과 파일이 생성됩니다.

---

## 📘 참고

* 공식 Gemini CLI 문서: [https://ai.google.dev/docs/gemini_api_overview](https://ai.google.dev/docs/gemini_api_overview)
* PyMuPDF 문서: [https://pymupdf.readthedocs.io](https://pymupdf.readthedocs.io)

---

## 🧑‍💻 작성자

> Maintainer: [Marcus Gong]
> Updated: October 5th, 2025
> Description: Resume analyzer project powered by Google Gemini CLI.
