## Music Recommender System


Final Project for Practical Data Science course

University of Tartu, 
November 2023

### [Project Report](PAT23_report.pdf)

### TL;DR
A simple recommender system.

The training datasets are user-song playcounts and metadata for these songs. 

The user-song playcounts are limited to x playcounts or less (x=5 seems okay)
- KNNWithMeans
- KNN similarity matrix

song metadata numeric values scaled and genres encoded. Create cosine similarity matrix. create a weighted matrix from the other two matrices

Takes an artist and song as input and returns n most similar songs. 

### Requirements
- Jupyter Notebook
- at least 32GB RAM
- [notebook requirements](requirements.txt)

### Instructions
1. Download dataset from Kaggle:<br>
https://www.kaggle.com/datasets/undefinenull/million-song-dataset-spotify-lastfm/data
2. Unpack the dataset and place it in project root
3. Rename csv file spaces to underscores
4. Run the notebooks
5. Run flask directly or inside docker:
```
docker build . -t flask_app
docker run flask_app
```
6. Have fun! :+1:

### My optimal parameters

playcounts <=5

k = 9

