#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 15:34:59 2021

@author: allie
"""
# NLP - Preprocessing 

import pandas as pd
#from textblob import TextBlob
import numpy as np
from langdetect import detect

listings_cph = pd.read_csv("listings_CPH.csv")
reviews_cph = pd.read_csv("reviews_CPH.csv")
listings_shl = pd.read_csv("listings_SLH.csv")
reviews_shl = pd.read_csv("reviews_SLH.csv")
listings_osl = pd.read_csv("listings_OSL.csv")
reviews_osl = pd.read_csv("reviews_OSL.csv")

# filter out non-english reviews

### detect english reviews
def detect_language(text):
    try: 
        return detect(text)
    except: 
        return np.nan
    
reviews_cph['lang'] = reviews_cph['comments'].apply(lambda x: detect_language(x))
reviews_cph = reviews_cph[reviews_cph['lang']=='en']
reviews_cph.reset_index(inplace = True)

reviews_shl['lang'] = reviews_shl['comments'].apply(lambda x: detect_language(x))
reviews_shl = reviews_shl[reviews_shl['lang']=='en']
reviews_shl.reset_index(inplace = True)

reviews_osl['lang'] = reviews_osl['comments'].apply(lambda x: detect_language(x))
reviews_osl = reviews_osl[reviews_osl['lang']=='en']
reviews_osl.reset_index(inplace = True)

# rename the columns
listings_cph = listings_cph.rename(columns= {'id': 'listing_id'})
listings_shl = listings_shl.rename(columns= {'id': 'listing_id'})
listings_osl = listings_osl.rename(columns= {'id': 'listing_id'})

# join the data based on listings id
data_cph = listings_cph.merge(reviews_cph, on = 'listing_id', how = 'left')
data_shl = listings_shl.merge(reviews_shl, on = 'listing_id', how = 'left')
data_osl = listings_osl.merge(reviews_osl, on = 'listing_id', how = 'left')

data = pd.concat([data_cph, data_shl, data_osl])

withdata.to_csv("final_data.csv")