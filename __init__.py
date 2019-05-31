
import numpy as np
import pandas as pd
from src.import_datasets import get_word_rating_data, get_word_freq1_data, get_word_freq2_data, get_emoji_data, get_csv_df
from process_data import process_word_ratings, assemble_word_data, split_by_asl_and_val, split_by_asl
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
words_with_freqs = get_csv_df("../datasets/words_with_freqs.csv")

# normalize and scale each group/whole set
words_with_freqs = center_and_scale(words_with_freqs)

# split dataset by top, middle, lowest arousal & top, lowest valence words
asl_high_val_high, asl_med_val_high, asl_low_val_high, asl_high_val_low, asl_med_val_low, asl_low_val_low = split_by_asl_and_val(words_with_freqs, stdnum=2.5, show_stats=False)
asl_high, asl_med, asl_low = split_by_asl(words_with_freqs, stdnum=2, show_stats=False)

# find close word combinations
word_combs_val_high = find_word_combs(asl_high_val_high, asl_med_val_high, asl_low_val_high)
word_combs_val_low = find_word_combs(asl_high_val_high, asl_med_val_high, asl_low_val_high)
word_combs_asl_only = find_word_combs(asl_high, asl_med, asl_low)

# calculate distances between combinations
dists_val_high = calc_dists(word_combs_val_high)
dists_val_low = calc_dists(word_combs_val_low)
dists_asl_only = calc_dists(word_combs_asl_only)

# save distances to csv
dists_val_high.to_csv("../datasets/dists_val_high_25_std.csv")
dists_val_low.to_csv("../datasets/dists_val_low_25_std.csv")
dists_asl_only.to_csv("../datasets/asl_only_25_std.csv")

# load distances file
combs_with_dists_high = get_csv_df("../datasets/asl_only_25_std.csv")

# show word groups with shortest distances
# df = dists_val_high("../datasets/combs_with_dists_25_std.csv")
for row in combs_with_dists_high.nsmallest(1000, "avg_dist").itertuples():
    print(row)