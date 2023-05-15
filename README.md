# Film content/ collaborative recommendation system

This project is a web application that provides movie recommendations based on both film content and collaborative filtering using the IMDb formula. It aims to help users discover relevant films to watch.

## Table of Contents
* [Dataset](#Dataset)
* [Technologies](#Technologies-Used)
* [API_key](#How-to-get-the-API-key)
* [Website Interface](#Website-Interface)
* [Conclusion](#Conclusion)

## Dataset
The project used [this](https://www.kaggle.com/code/strikoder/recommendation-systems-content-collaborative) dataset to train the models:


## Technologies Used
* Cosine similarity
* NLTK
* Streamlit for web development
* Heroku for deoployment 

## How to get the API key?
Create an account in https://www.themoviedb.org/, click on the API link from the left hand sidebar in your account settings and fill all the details to apply for API key. If you are asked for the website URL, just give "NA" if you don't have one. You will see the API key in your API sidebar once your request is approved.

## Website Interface
The website features a simple and intuitive interface that allows users to select a film and receive recommendations based on their preferences. The results are displayed in a clear and organized way!

![result](https://github.com/Strikoder/FilmRecommender/blob/main/readme.jpg?raw=true)


# Conclusion
To run the project, clone or download this repository to your local machine. Install all the libraries mentioned in the `requirements.txt` file using the command `pip install -r requirements.txt`. Replace `YOUR_API_KEY` in both the places and save the changes. Open your terminal or command prompt from the project directory and run the main.py file by executing the command `streamlit run main.py`. That's it! Enjoy exploring movie recommendations tailored to your taste.
