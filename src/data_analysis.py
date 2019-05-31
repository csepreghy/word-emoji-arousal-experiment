import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join

def read_data():
  all_participants = []
  files = [f for f in listdir('experiment_data') if isfile(join('experiment_data', f))]
  
  if any('.DS_Store' in s for s in files): files.remove('.DS_Store') # removes .DS_Store if it's there (a file Mac creates)

  for index, filename in enumerate(files):
    df = pd.read_csv('experiment_data/' + filename)

    # print('df.head()', df.columns)

    del df['frameRate']
    del df['psychopyVersion']
    del df['key_resp_5.keys']
    del df['key_resp_5.rt']
    del df['key_resp_4.rt']
    del df['key_resp_4.keys']
    del df['key_resp_6.keys']
    del df['distance_x']
    del df['distance_y']
    del df['session']
    del df['trials.thisRepN']
    del df['expName']
    del df['trials.thisTrialN']
    del df['trials.thisN']

    if any('fbclid' in column for column in list(df.columns)): del df['fbclid']
    
    all_participants.append(df)

  return all_participants


def get_stats_for_every_word(df_list):
  correct_incorrect_answers = {}

  for index, word in enumerate(list(df_list[0]['word'])):
    print(word)
    # correct_incorrect_answers = []

    correct_incorrect_answers[word] = []

    for df in df_list:
      # print('df[word][index]', df['word'][index])
      if df['key_resp_7.keys'][index] == df['ground_truth'][index]:
        correct_incorrect_answers[word].append(1)
      
      else:
        correct_incorrect_answers[word].append(0)

    correct_incorrect_answers[word] = np.mean(np.array(correct_incorrect_answers[word]))

  
  print(len(list(correct_incorrect_answers.keys())))
  print(len(list(correct_incorrect_answers.values())))
  data = {
    'Word': list(correct_incorrect_answers.keys()),
    'Mean Accuracy': list(correct_incorrect_answers.values())
  }
  word_stats_df = pd.DataFrame(data)
  word_stats_df.to_csv('word_accuracies.csv')

  print('word_stats_df.head()', word_stats_df)
  # for df in df_list:
  #   answers = list(df['key_resp_7.keys'])
  #   ground_truth = list(df['ground_truth'])
  #   response_times = list(df['key_resp_7.rt'])
  #   words = list(df['word'])

  #   for word in words:



df_list = read_data()

get_stats_for_every_word(df_list)



#  answers = list(df['key_resp_7.keys'])
#  response_times = list(df['key_resp_7.rt'])
#  ground_truth = list(df['ground_truth'])

# n_correct = 0

# for answer, truth in zip(answers, ground_truth):
#   if answer == truth:
#     n_correct += 1
