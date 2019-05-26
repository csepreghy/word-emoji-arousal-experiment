
import numpy as np
import pandas as pd
from src.import_datasets import get_word_rating_data, get_word_freq1_data, get_word_freq2_data, get_emoji_data, get_csv_df
from process_data import process_word_ratings, assemble_word_data, split_by_arousal
from analyze_data import center_and_scale, find_word_combs, calc_dists

# import data
# word_rating_data = get_word_rating_data()
# word_freq1_data = get_word_freq1_data()
# word_freq2_data = get_word_freq2_data()
# emoji_data = get_emoji_data()

# preprocess data
# word_rating_data_processed = process_word_ratings(word_rating_data)
# words_with_freqs = assemble_word_data(word_rating_data_processed, word_freq1_data, word_freq2_data, add_letter_count=True, dropNaN=True)

# save intermediate data
# words_with_freqs.to_csv("../datasets/words_with_freqs.csv")

# import intermediate data
# words_with_freqs = get_csv_df("../datasets/words_with freqs.csv")

# normalize and scale each group/whole set
# words_with_freqs = center_and_scale(words_with_freqs)

# split dataset by top, middle and lowest arousal words
# high_arousal, med_arousal, low_arousal = split_by_arousal(words_with_freqs, stdnum=2.25, show_stats=False)

# find close word combinations - 2,5 million!
# word_combs = find_word_combs(high_arousal, med_arousal, low_arousal)

# calculate distances between combinations
# combs_with_dists = calc_dists(word_combs)

# save distances to csv
# combs_with_dists.to_csv("../datasets/combs_with_dists_225_std.csv")

# load distances file
# combs_with_dists = get_csv_df("../datasets/combs_with_dists_225_std.csv")

# show word groups with shortest distances
df = get_csv_df("../datasets/combs_with_dists_25_std.csv"
print(df.nsmallest(100, "avg_dist"))