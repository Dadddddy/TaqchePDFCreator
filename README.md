
---

## 🔐 Disclaimer

This project is intended **only for personal use** by individuals who have **legitimately purchased** their books from [taaghche.com](https://taaghche.com).

It allows you to read your owned content in an offline environment or on devices like Kindle, for personal convenience.

**Do not** use this tool to:
- Share, distribute, or publish copyrighted content
- Bypass paywalls for unauthorized access
- Violate Taaghche’s terms of service or copyright policies

📛 **Using this script to generate and distribute PDFs of books you don’t own is illegal.**

The author takes no responsibility for any misuse of this code. By using this project, you agree to use it lawfully and ethically.

---


# 📚 Taghche PDF Creator

This project automates the process of:

1. Logging into a web reader (e.g., [taaghche.com](https://taaghche.com/))
2. Taking screenshots of each page
3. Enhancing and converting those screenshots into a high-quality, printable PDF

It’s perfect for saving your purchased digital books into an offline format for personal use.

---

## ✨ Features

- Automates screenshot capture using Selenium
- Converts `.png` images to `.jpg` with enhanced contrast & brightness
- Assembles images into a single PDF
- Clean project structure with output stored separately
- One-command setup via `setup.sh`

---

## 🚀 Quick Start

### 1. Clone the project

```bash
git clone https://github.com/your-username/TaghchePDFCreator.git
cd TaghchePDFCreator
```

### 2. Set up the environment

```bash
bash setup.sh
```

💡 After setup, activate the virtual environment:

```bash
source venv/bin/activate
```

---

## 📷 How the Code Works

### Step 1: `screenshot_all_page()`
- Uses Firefox + Selenium to open the given URL
- Waits 45 seconds for you to log in manually
- Then it:
  - Detects the total number of pages
  - Takes screenshots of each visible page
  - Saves each one as `1.png`, `2.png`, ... in `output/screenshots/<your-folder>`

### Step 2: `pngs_to_pdf()`
- Resizes and enhances contrast/brightness of the screenshots
- Converts `.png` images to `.jpg` in memory
- Merges them into a single `.pdf` file saved in `output/pdfs/<your-file>.pdf`

---

## 🧪 Usage

After activating the environment:

```bash
python3 main.py
```

Then choose an option:
- 1: Start the screenshot process
- 2: Convert screenshots to PDF
- 3: Exit

For example, after choosing option 1:
- Open the login page
- Log in manually within 45 seconds
- The script takes screenshots automatically

Later, choose option 2 to generate a PDF from the screenshots.

---

## 🛠 Requirements

- Python 3.6+
- Firefox browser
- Geckodriver (must be in your system PATH)

🔗 Download: https://github.com/mozilla/geckodriver/releases

💡 On macOS, install Geckodriver with Homebrew:

```bash
brew install geckodriver
```

---

## 📁 Project Structure

```
TaghchePDFCreator/
├── main.py             # Main script to run the tool
├── setup.sh            # Environment setup script
├── requirements.txt    # Dependencies (auto-generated)
├── output/             # (gitignored) Contains screenshots & PDFs
│   ├── screenshots/
│   └── pdfs/
├── .gitignore
└── README.md
```

---

## 🧼 .gitignore Highlights

This repo ignores:
- `venv/` — local virtual environment
- `output/` — all generated images and PDFs
- Temporary & OS files like `.DS_Store`, `__pycache__/`, etc.

---

## 🙏 Disclaimer

This tool is intended only for personal use on content you own. Respect the platform’s terms of service and copyright laws in your region.

---

## 📬 Feedback & Contributions

Pull requests and suggestions are welcome! Feel free to fork the repo or reach out.
