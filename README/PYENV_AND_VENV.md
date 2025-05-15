# 🐍 Pyenv

## 📦 Pyenv — Python Version Manager

**Pyenv** lets you easily install and switch between multiple Python versions on your computer.

### 🔧 Install Pyenv

Pyenv is a separate tool that you need to install manually.

👉 Follow the guide here based on your OS:
[https://github.com/pyenv/pyenv#installation](https://github.com/pyenv/pyenv#installation)

---

### 💡 Why Use Pyenv?

* Your system might come with Python pre-installed.
* You might want to use a different Python version for a specific project.
* Pyenv helps you manage different versions easily.

---

### 📥 Install Python Versions

After installing pyenv, you can install Python versions like this:

```bash
pyenv install 3.13
pyenv install 3.9
```

✅ Now your system has Python 3.13 and 3.9 (along with the system version).

---

## 🧪 Start a New Python Project

### 📁 1. Create a Project Folder

```bash
mkdir ProjectName
cd ProjectName
```

---

### 🐍 2. Set the Python Version for This Project

```bash
pyenv local 3.13
```

✅ This creates a `.python-version` file in the folder with the content:

```
3.13
```

💡 This means Python 3.13 will always be used inside this project.

---

## 🧪 Create a Virtual Environment (venv)

### 🔨 3. Create a venv (based on `.python-version`)

```bash
python -m venv .venv
```

✅ This creates a `.venv/` folder using Python 3.13 (or whichever version is in `.python-version`).

---

### 🚀 4. Activate the venv

```bash
# For Unix/macOS:
source .venv/bin/activate

# For Windows:
.venv\Scripts\activate
```

💡 Your terminal will now look like this:

```
(.venv) /your/path/ProjectName
```

✅ This means you're inside the virtual environment.

---

## 📦 Manage Project Dependencies

### 🧾 5. Create `requirements.txt`

This file lists all libraries your project needs:

Example `requirements.txt`:

```
fastapi[standard]==0.115.12
pydantic==2.11.4
```

---

### 📥 6. Install Dependencies

```bash
pip install -r requirements.txt
```

✅ All packages are installed inside `.venv`.

---

## 📂 Final Project Structure

```
ProjectName/
│
├── .python-version     # Specifies Python 3.13 for this project
├── requirements.txt    # Lists project dependencies
└── .venv/              # Virtual environment folder
```

---

## ✅ Summary

| Step | Action                     | Command                               |
| ---- | -------------------------- | ------------------------------------- |
| 1    | Install Python version     | `pyenv install 3.13`                  |
| 2    | Create project folder      | `mkdir ProjectName && cd ProjectName` |
| 3    | Set local Python version   | `pyenv local 3.13`                    |
| 4    | Create virtual environment | `python -m venv .venv`                |
| 5    | Activate venv              | `source .venv/bin/activate`           |
| 6    | Add dependencies           | Edit `requirements.txt`               |
| 7    | Install dependencies       | `pip install -r requirements.txt`     |

---
