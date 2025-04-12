import streamlit as st
import pandas as pd

# Sample DataFrame to simulate the library collection
books_data = pd.DataFrame(columns=["Book Title", "Author", "Genre", "Year"])

# Function to display the library
def display_books():
    if not books_data.empty:
        st.write("### Your Library Collection")
        st.dataframe(books_data)
    else:
        st.write("No books in the library yet.")

# Function to add a book
def add_book(title, author, genre, year):
    global books_data
    new_book = pd.DataFrame([[title, author, genre, year]], columns=["Book Title", "Author", "Genre", "Year"])
    books_data = pd.concat([books_data, new_book], ignore_index=True)

# Function to delete a book
def delete_book(title):
    global books_data
    books_data = books_data[books_data["Book Title"] != title]

# App layout
st.title("Personal Library Manager")

# Sidebar for navigation
st.sidebar.title("Options")
option = st.sidebar.selectbox("Choose an action", ("View Books", "Add a Book", "Delete a Book"))

if option == "View Books":
    display_books()

elif option == "Add a Book":
    st.write("### Add a new book")
    book_title = st.text_input("Book Title")
    author = st.text_input("Author")
    genre = st.text_input("Genre")
    year = st.number_input("Year", min_value=1900, max_value=2025)

    if st.button("Add Book"):
        if book_title and author and genre and year:
            add_book(book_title, author, genre, year)
            st.success(f"Book '{book_title}' added successfully!")
        else:
            st.error("Please fill in all fields.")

elif option == "Delete a Book":
    st.write("### Delete a Book")
    book_to_delete = st.text_input("Enter the title of the book to delete")

    if st.button("Delete Book"):
        if book_to_delete:
            delete_book(book_to_delete)
            st.success(f"Book '{book_to_delete}' deleted successfully!")
        else:
            st.error("Please enter a valid book title.")

