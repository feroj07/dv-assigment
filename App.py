import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import re

# Set page configuration
st.set_page_config(layout="wide", page_title="File Data Visualizer")

## --- Functions for Data Handling and Visualization --- ##

@st.cache_data
def load_data(uploaded_file):
    """
    Loads data from different file types into a Pandas DataFrame.
    """
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.txt'):
            # Read text file and create a single-column DataFrame
            text_data = uploaded_file.getvalue().decode("utf-8")
            df = pd.DataFrame([text_data], columns=['text_content'])
        else:
            st.error("Unsupported file format. Please upload a .csv, .xlsx, or .txt file.")
            return None
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def create_word_cloud(text_data):
    """
    Generates a word cloud from text data.
    """
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text_data)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

def bin_words(text_data, num_bins=10):
    """
    Creates a histogram-like visualization by binning word frequencies.
    """
    words = re.findall(r'\b\w+\b', text_data.lower())
    word_counts = pd.Series(words).value_counts().reset_index()
    word_counts.columns = ['word', 'count']

    # Create bins
    bins = pd.cut(word_counts['count'], bins=num_bins, labels=False)
    word_counts['bin'] = bins

    bin_counts = word_counts.groupby('bin').size().reset_index(name='number_of_words')
    
    st.write("### Word Binning Visualization")
    st.bar_chart(bin_counts, x='bin', y='number_of_words')

## --- Main Streamlit App Layout --- ##

st.title("Data Visualization App")
st.write("Upload a file (.csv, .xlsx, or .txt) to get started with visualizations like Word Cloud and Word Binning.")

# File uploader widget
uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx', 'txt'])

if uploaded_file is not None:
    data = load_data(uploaded_file)
    if data is not None:
        st.success("File uploaded and loaded successfully!")

        # Display raw data
        st.subheader("Raw Data Preview")
        st.dataframe(data.head())

        # Select visualization type
        viz_type = st.selectbox(
            "Select a visualization:",
            ("None", "Word Cloud", "Word Binning")
        )

        if viz_type == "Word Cloud":
            # Check if data contains text for word cloud
            text_column = st.selectbox(
                "Select the text column for Word Cloud:",
                options=data.columns,
                help="Choose a column that contains text data."
            )
            if st.button("Generate Word Cloud"):
                text_content = " ".join(data[text_column].astype(str).tolist())
                if text_content:
                    create_word_cloud(text_content)
                else:
                    st.warning("Selected column is empty or does not contain text.")

        elif viz_type == "Word Binning":
            text_column = st.selectbox(
                "Select the text column for Word Binning:",
                options=data.columns,
                help="Choose a column that contains text data."
            )
            num_bins = st.slider("Number of bins for word frequency", 5, 20, 10)
            if st.button("Generate Word Binning"):
                text_content = " ".join(data[text_column].astype(str).tolist())
                if text_content:
                    bin_words(text_content, num_bins)
                else:
                    st.warning("Selected column is empty or does not contain text.")
