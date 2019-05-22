def get_word_rating_data():
  import pandas as pd
  word_arousal = pd.read_csv("word_ratings.csv", index_col=1)
  return word_arousal

def get_word_freq1_data():
  import pandas as pd
  freq1_data = pd.read_csv("freq_1.al", sep=" ", index_col = 2, names=["rank", "freq", "word", "POS"])
  freq1_data.reset_index(inplace=True)
  return freq1_data

def get_word_freq2_data():
  import pandas as pd
  freq_2 = pd.read_csv("freq_2.txt", sep="\t", index_col = 1)
  return freq_2

def get_emoji_data():
  import pandas as pd
  emoji_arousal = pd.read_excel("emoji_ratings.xlsx", index_col=0, header=1)
  return emoji_arousal

#print(get_emoji_data())