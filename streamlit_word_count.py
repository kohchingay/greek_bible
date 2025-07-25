import streamlit as st
import pandas as pd
import os
import glob
import plotly.express as px

# Set Streamlit page config
st.set_page_config(page_title="Word Count Across CSVs", layout="centered")

st.title("Word Count Search Across CSV Files")
st.write("Enter a word and see its count in each CSV file in this repository, visualized as a donut chart.")

# User input
word = st.text_input("Enter a word to search for (case-insensitive):", "").strip()

# Find all CSV files in the repo (recursive)
csv_files = glob.glob("**/*.csv", recursive=True)

file_word_counts = {}

if word and csv_files:
    for file in csv_files:
        try:
            # Try reading with utf-8, fallback to latin-1 if error
            try:
                df = pd.read_csv(file, dtype=str, encoding="utf-8")
            except Exception:
                df = pd.read_csv(file, dtype=str, encoding="latin-1")

            # Concatenate all text fields into single string
            text = " ".join(df.astype(str).fillna("").agg(" ".join, axis=1)).lower()
            count = text.count(word.lower())
            file_word_counts[os.path.basename(file)] = count
        except Exception as e:
            st.warning(f"Could not process {file}: {e}")

    if file_word_counts:
        df_counts = pd.DataFrame({
            "CSV File": list(file_word_counts.keys()),
            "Count": list(file_word_counts.values())
        })

        st.write("### Word counts by file")
        st.dataframe(df_counts, use_container_width=True)

        # Only show donut chart if there are non-zero counts
        if df_counts["Count"].sum() > 0:
            fig = px.pie(
                df_counts, 
                values="Count", 
                names="CSV File", 
                hole=0.5,
                title=f"Distribution of '{word}' across CSV files"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info(f"No occurrences of '{word}' found in any CSV file.")
    else:
        st.info("No CSV files processed.")
elif word:
    st.warning("No CSV files found in this directory.")

st.caption("To deploy this app to GitHub Pages, use [Streamlit Community Cloud](https://streamlit.io/cloud) or a compatible service. For static GitHub Pages, Streamlit apps are not natively supported, but you can use a cloud deployment and link to it from your GitHub Pages site.")