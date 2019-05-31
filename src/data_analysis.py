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
  response_times_mean = {}
  response_times_std = {}

  for index, word in enumerate(list(df_list[0]['word'])):
    print(word)
    # correct_incorrect_answers = []

    correct_incorrect_answers[word] = []
    response_times_mean[word] = []
    response_times_std[word] = []

    for df in df_list:
      response_times_mean[word].append(df['key_resp_7.rt'][index])
      response_times_std[word].append(df['key_resp_7.rt'][index])

      if df['key_resp_7.keys'][index] == df['ground_truth'][index]:
        correct_incorrect_answers[word].append(1)
      
      else:
        correct_incorrect_answers[word].append(0)

    correct_incorrect_answers[word] = np.mean(np.array(correct_incorrect_answers[word]))
    response_times_mean[word] = np.mean(np.array(response_times_mean[word]))
    response_times_std[word] = np.std(np.array(response_times_std[word]))

  truth_list = list(df_list[0]['ground_truth'])
  category_list = list(df_list[0]['category'])

  data = {
    'Word': list(correct_incorrect_answers.keys()),
    'Mean Accuracy': list(correct_incorrect_answers.values()),
    'Mean RT': list(response_times_mean.values()),
    'Standard Deviation RT': list(response_times_std.values()),
    'Truth': truth_list,
    'Category': category_list
  }

  print(list(response_times_mean.values()))
  print(list(response_times_std.values()))
  word_stats_df = pd.DataFrame(data)
  word_stats_df.to_csv('word_stats.csv')

  print('word_stats_df.head()', word_stats_df)


def individual_accuracy(df):
  answers = list(df['key_resp_7.keys'])
  response_times = list(df['key_resp_7.rt'])
  ground_truth = list(df['ground_truth'])

  n_correct = 0

  for answer, truth in zip(answers, ground_truth):
    if answer == truth:
      n_correct += 1

# df_list = read_data()
# get_stats_for_every_word(df_list)
