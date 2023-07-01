# Book System Recommendation Using Collaborative Filtering-Based Machine Learning

## Project Description
The Book System Recommendation project is an innovative application of machine learning techniques, specifically Collaborative Filtering, to provide personalized book recommendations to users. Collaborative Filtering is a powerful approach that leverages the wisdom of the crowd to predict user preferences and make accurate suggestions. In this project, the system analyzes a vast dataset of user-book interactions, such as ratings, reviews, and reading history, to understand individual preferences and similarities between users.

Additionally, for a seamless and user-friendly experience, the Book System Recommendation incorporates the Streamlit library to create an intuitive web interface. Streamlit provides a straightforward framework for building interactive web applications with Python, making it an ideal choice for showcasing the machine learning model and delivering personalized book recommendations to users.

In the project, the machine learning model is created using the NearestNeighbors algorithm. The NearestNeighbors algorithm works by measuring the distance between instances in a dataset.

<img width="959" alt="Screenshot 2023-07-01 at 17 13 51" src="https://github.com/semeniuk4/BooksRecommendationSystem-UsingMachineLearning/assets/36206527/7895309b-0f40-4282-87a5-d514a9410771">

## How to run?
1. Clone this repository
2. Create a conda environment after opening the repository
```bash
conda create -n books python=3.10.9
```

```bash
conda activate books
```
3. Install the requirements
```bash
pip install -r requirements.txt
```
4. Run the app
```bash
streamlit run app.py
```
