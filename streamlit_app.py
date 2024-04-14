# streamlit_app.py

import streamlit as st
import sqlite3

# Function to fetch poems from SQLite database
def fetch_poems():
    conn = sqlite3.connect('poems.db')
    c = conn.cursor()
    c.execute("SELECT title, author, text FROM poems")
    poems = c.fetchall()
    conn.close()
    return poems

# Main function to render the Streamlit app
def main():
    # Fetch poems from the database
    poems = fetch_poems()

    # Display each poem in the list
    st.title("List of Poems")
    for poem in poems:
        st.write(f"Title: {poem[0]}")
        st.write(f"Author: {poem[1]}")
        st.write(f"Text: {poem[2]}")
        st.write("---")

if __name__ == '__main__':
    main()
