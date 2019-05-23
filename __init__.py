
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.import_datasets import get_word_rating_data, get_word_freq1_data, get_word_freq2_data, get_emoji_data
from process_data import process_word_ratings, assemble_word_data, split_by_arousal
from analyze_data import center_and_scale
from sklearn.decomposition import PCA

word_rating_data = get_word_rating_data()
word_freq1_data = get_word_freq1_data()
#print(word_freq1_data.head())
word_freq2_data = get_word_freq2_data()
#print(type(word_freq2_data))
#freq_2 = word_freq2_data.reset_index(inplace=True)
#print(word_freq2_data.head())
#emoji_data = get_emoji_data()

word_rating_data_processed = process_word_ratings(word_rating_data)
print('word_rating_data_processed', word_rating_data_processed)

# runtime = 10 mins!
word_clean = assemble_word_data(word_rating_data_processed, word_freq1_data, word_freq2_data, add_letter_count=False, dropNaN=False)
print(word_clean.head())

# split dataset by top, middle and lowest arousal words
# high_arousal, med_arousal, low_arousal = split_by_arousal(word_clean, stdnum=2, show_stats=True)

# print(high_arousal.head(), high_arousal.shape)
# print(med_arousal.head(), med_arousal.shape)
# print(low_arousal.head(), low_arousal.shape)

# normalize and scale each group
# high_scaled, med_scaled, low_scaled = center_and_scale(high_arousal), center_and_scale(med_arousal), center_and_scale(low_arousal)