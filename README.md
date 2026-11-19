
# 📊 File Data Visualizer

A Streamlit app that turns uploaded text into a word cloud or a word-frequency binning chart. It accepts `.csv`, `.xlsx`, and `.txt` files.

## 🌐 Live Application

🚀 **Try the application here:**

[**Open File Data Visualizer**](https://adj8hx7p5p3fnuhgrtntm5.streamlit.app/)

## ✨ Key Features

- Upload CSV, XLSX, and TXT files
- Select text columns for analysis
- Generate word clouds
- Visualize word frequencies using charts
- Simple and interactive Streamlit interface
- Docker support for deployment

## 📸 Project Screenshots

### 1. Project Overview

![File Data Visualizer Project Banner](images/project-banner.png)

### 2. Application Dashboard

![File Data Visualizer Dashboard](images/dashboard.png)

### 3. Word Cloud Visualization

![Word Cloud](images/wordcloud.png)

### 4. Word Frequency Chart

![Word Frequency Chart](images/frequency.png)

> Screenshots must be uploaded to the `images` folder.
> The project banner and dashboard designs are illustrative;
> use actual app screenshots for the visualization examples.

## 💻 Technologies Used

- Python
- Streamlit
- Pandas
- WordCloud
- Docker
- OpenPyXL

## ⚙️ Run it locally

You need Python 3.10 or newer.

```bash
git clone https://github.com/feroj07/dv-assigment.git
cd dv-assigment
python -m pip install -r requirements.txt
streamlit run App.py
```

Streamlit prints a **Local URL** in the terminal, usually http://localhost:8501.

Open that address in your browser. Keep the terminal running while you use the app.

## 🐳 Run it in Docker

With Docker installed, build and start the app:

```bash
docker build -t file-data-visualizer .
docker run --rm -p 8501:8501 file-data-visualizer
```

Then open http://localhost:8501.

To make it available to other people, run the container on a server that allows inbound traffic to port 8501, or configure your hosting provider to forward its assigned port to the app.

## ☁️ Deploy with Streamlit Community Cloud

1. Sign in at https://share.streamlit.io/ using GitHub.
2. Choose **Create app**.
3. Select `feroj07/dv-assigment`.
4. Set the branch to `main`.
5. Set the app file to `App.py`.
6. Select **Deploy**.

### Deployed Application

https://adj8hx7p5p3fnuhgrtntm5.streamlit.app/

## 📖 Use the App

1. Upload a `.csv`, `.xlsx`, or `.txt` file.
2. For tabular files, choose the column containing text.
3. A text file is loaded into a `text_content` column.
4. Choose **Word Cloud** or **Word Binning**.
5. Generate the visualization.

## 📦 Requirements

Dependencies are listed in
[`requirements.txt`](requirements.txt).

Excel files are read using `openpyxl`.

## 👨‍💻 Developed By

**Shaik Feroj**

B.Tech — Artificial Intelligence & Data Science

GitHub: https://github.com/feroj07

---

⭐ If you find this project useful, consider starring the repository!
