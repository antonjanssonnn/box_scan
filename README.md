# 🛡️ Secure File Downloader & Virus Scanner

Download files inside an **isolated container**, scan them for viruses, and decide whether to save the file on your host computer. This tool ensures a safer way to handle potentially risky downloads. 🧼💻

---

## 🚀 **How to Run**
1. Make sure you have **Python** and **Podman** (or Docker) installed.
2. Run the script with the download URL:

```bash
python main.py <download_url>
```

🔍 **Example:**
```bash
python main.py https://secure.eicar.org/eicar.com.txt
```

---

## 📝 **Features**
✅ Downloads the file directly into an isolated container.  
✅ Scans the file with **ClamAV** to detect viruses or malware.  
✅ Provides a scan report indicating if the file is clean or infected.  
✅ Prompts you to decide whether to keep or discard the file.  
✅ Ensures the container is destroyed after scanning for maximum security. 🔒

---

## ⚙️ **Requirements**
- Python 3.7+
- Podman or Docker
- `requests` Python package

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🛡️ **Why Use This?**
When dealing with files from unknown sources, running them directly on your host can be risky. This tool helps you:
- Prevent accidental execution of malicious files 🐛
- Keep your host environment safe 🔐
- Quickly decide if a file is safe to use or should be deleted 🗑️

