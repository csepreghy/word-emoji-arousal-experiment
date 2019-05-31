import pandas as pd

def get_word_rating_data():
  word_arousal = pd.read_csv("../datasets/word_ratings.csv", index_col=1)
  return word_arousal

def get_word_freq1_data():
  freq1_data = pd.read_csv("../datasets/freq_1.al", sep=" ", index_col=2, names=[
                           "rank", "freq", "word", "POS"])
  freq1_data.reset_index(inplace=True)
  return freq1_data

def get_word_freq2_data():
  freq_2 = pd.read_csv("../datasets/freq_2.txt", sep="\t", index_col=1)
  return freq_2

def get_emoji_data():
  emoji_arousal = pd.read_excel(
      "../datasets/emoji_ratings.xlsx", index_col=0, header=1)
  return emoji_arousal

#print(get_emoji_data())

def get_csv_df(filepath):
  dataframe = pd.read_csv(filepath, index_col = 0)
  return dataframe
