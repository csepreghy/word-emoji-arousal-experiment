import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.import_datasets import get_word_rating_data, get_word_freq1_data, get_word_freq2_data, get_emoji_data
from process_data import process_word_ratings, assemble_word_data, split_by_arousal

word_rating_data = get_word_rating_data()
word_freq1_data = get_word_freq1_data()
word_freq2_data = get_word_freq2_data()
emoji_data = get_emoji_data()

word_rating_data_processed = process_word_ratings(word_rating_data)

# runtime = 10 mins!
word_clean = assemble_word_data(word_rating_data_processed, word_freq1_data, word_freq2_data, dropNaN=True)
#print(word_clean.head())

high_arousal, med_arousal, low_arousal = split_by_arousal(word_clean, stdnum=2, show_stats=True)

#print(high_arousal.head(), high_arousal.shape)
#print(med_arousal.head(), med_arousal.shape)
#print(low_arousal.head(), low_arousal.shape)