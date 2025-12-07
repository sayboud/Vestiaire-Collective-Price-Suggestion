# Vestiaire-Collective-Price-Suggestion

What is the price of a listing on Vestiaire Collective?

Designer fashion can hold good value and be sold on the second-hand market but the appropriate price could be challenging. The purpose of the project is to fit the best regression model to suggest a selling price in order to list on Vestiaire Collective, an online marketplace for buying and selling pre-owned luxury fashion items.

On the way, we will also uncover which features of a product are most important in the pricing.

## Installation process
This project uses python `3.11` as core interpreter, and poetry `1.8.3` as dependency manager.
1) Create a new conda environment with
```
conda env create -f environment.yml
```

2) Activate the environment with
```
conda activate ecl-course-2025
```

3) Move to the project directory, and install the project dependencies with
```
poetry install
```

4) Launch a jupyter server with
```
jupyter notebook
```

5) Remove the environment with
```
conda remove -n ecl-course-2025 --all
```

## Collect data
For this Machine Learning project the dataset we consider is the [Vestiaire Collective Dataset](https://www.kaggle.com/c/bluebook-for-bulldozers/overview](https://www.kaggle.com/datasets/justinpakzad/vestiaire-fashion-dataset
). 

## How to use it
run the streamlit app
```shell
streamlit run demo.py
```
