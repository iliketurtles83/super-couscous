1. Download dataset from Kaggle
https://www.kaggle.com/datasets/undefinenull/million-song-dataset-spotify-lastfm/data

2. Unzip the dataset and put it in the same folder as the code

3. Rename csv file spaces to underscores

4. Run the notebooks

5. For docker, run the following commands in project root:

```
docker build . -t flask_app
docker run flask_app
```
6. Have fun!