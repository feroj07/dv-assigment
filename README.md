# File Data Visualizer

A Streamlit app that turns uploaded text into a word cloud or a word-frequency binning chart. It accepts `.csv`, `.xlsx`, and `.txt` files.

## Run it locally

You need Python 3.10 or newer.

```bash
git clone https://github.com/feroj07/dv-assigment.git
cd dv-assigment
python -m pip install -r requirements.txt
streamlit run App.py
```

Streamlit prints a **Local URL** in the terminal (usually <http://localhost:8501>). Open that address in your browser. Keep the terminal running while you use the app.

## Run it in Docker

With Docker installed, build and start the app:

```bash
docker build -t file-data-visualizer .
docker run --rm -p 8501:8501 file-data-visualizer
```

Then open <http://localhost:8501>. To make it available to other people, run the container on a server that allows inbound traffic to port 8501, or configure your hosting provider to forward its assigned port to the app.

## Deploy a public app with Streamlit Community Cloud

1. Sign in at <https://share.streamlit.io/> using GitHub.
2. Choose **Create app** and select `feroj07/dv-assigment`.
3. Set the branch to `main` and the app file to `App.py`.
4. Select **Deploy**. The service installs the dependencies from `requirements.txt` and provides a public app URL.

The repository contains deployment instructions and a Docker setup; it is not publicly hosted automatically. You need to deploy it through a hosting provider to get a live public URL.

## Use the app

1. Upload a `.csv`, `.xlsx`, or `.txt` file.
2. For tabular files, choose the column containing text. A text file is loaded into a `text_content` column.
3. Choose **Word Cloud** or **Word Binning**, then generate the visualization.

## Requirements

Dependencies are listed in [`requirements.txt`](requirements.txt). Excel files are read with `openpyxl`.
