# -*- coding: utf-8 -*-
# from db_users import *
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('white')
# %matplotlib inline

# main
if __name__ == "__main__":
    column_name = ['user_id', 'item_id', 'rating']
    data_frame = pd.read_csv(
        "u.data", sep='\t', names=column_name, usecols=column_name)

    column_name = ['item_id', 'title']
    movie_title = pd.read_csv(
        "u.item", sep='|', names=column_name, usecols=column_name)

    #ne = movie_title[['item_id', 'title']]

    data_frame = pd.merge(data_frame, movie_title, on='item_id')

    #print(data_frame.head())
    
    #print(data_frame.groupby('title')['rating'].mean().sort_values(ascending=False))
    
    #print(data_frame.groupby('title')['rating'].count().sort_values(ascending=False).head(10) )

    ratings = pd.DataFrame( data_frame.groupby('title')['rating'].mean() )

    ratings['count'] = data_frame.groupby('title')['rating'].count()

    plt.figure( figsize=(10,6) )

    #ratings['rating'].hist( bins=70 )

    sns.jointplot( x='rating', y='count', data=ratings, alpha=0.4)

    print( ratings.shape )
    plt.show()