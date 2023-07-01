import pickle
import streamlit as st
import numpy as np
import pandas as pd

def recommend_book(book_name):
    book_list = []
    author_list = []
    year_of_publication_list = []

    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1,-1), n_neighbors=6)
    poster_url = fecth_poster(suggestion)

    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            author = image_url_title_author[image_url_title_author['title'] == j].author.to_string(index=False)
            author_list.append(author)
            
            year_of_publication = image_url_title_author[image_url_title_author['title'] == j].year.to_string(index=False)
            year_of_publication_list.append(year_of_publication)

            book_list.append(j)

    return book_list, poster_url, author_list, year_of_publication_list

def fecth_poster(suggestion):
    books_name = []
    poster_url = []

    for i in range(len(suggestion)):
        books_tmp = book_pivot.index[suggestion[i]]
        for j in books_tmp:
            books_name.append(j)

    for name in books_name:
        url_str = image_url_title_author[image_url_title_author['title'] == name]['img_url'].to_string(index=False)

        poster_url.append(url_str)

    return poster_url

st.header('Book Recommender System')

model = pickle.load(open('artifacts/model.pkl', 'rb'))
books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
book_pivot = pd.read_pickle('artifacts/book_pivot.pkl')
image_url_title_author = pd.read_pickle('artifacts/image_url.pkl')

selected_books = st.selectbox("Select a book", books_name)

if st.button('Show Recommendation Books'):
    recommendation_books, poster_url, authors, years_of_publication = recommend_book(selected_books)
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.text("Title: ")
        st.text("Author: ")
        st.text("Year: ")

    with col2:
        st.text(recommendation_books[1])
        st.text(authors[1])
        st.text(years_of_publication[1])
        st.image(poster_url[1])

    with col3:
        st.text(recommendation_books[2])
        st.text(authors[2])
        st.text(years_of_publication[2])
        st.image(poster_url[2])

    with col4:
        st.text(recommendation_books[3])
        st.text(authors[3])
        st.text(years_of_publication[3])
        st.image(poster_url[3])

    with col5:
        st.text(recommendation_books[4])
        st.text(authors[4])
        st.text(years_of_publication[4])
        st.image(poster_url[4])

    with col6:
        st.text(recommendation_books[5])
        st.text(authors[5])
        st.text(years_of_publication[5])
        st.image(poster_url[5])