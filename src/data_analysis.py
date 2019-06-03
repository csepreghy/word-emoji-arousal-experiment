import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

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
  word_stats_df.to_csv('2_word_stats.csv')

  print('word_stats_df.head()', word_stats_df)


def individual_accuracy(df):
  answers = list(df['key_resp_7.keys'])
  response_times = list(df['key_resp_7.rt'])
  ground_truth = list(df['ground_truth'])

  n_correct = 0

  for answer, truth in zip(answers, ground_truth):
    if answer == truth:
      n_correct += 1


def sort_by_category(df):
  df = df.sort_values(by=['Category'])

  return df


def read_stats_from_csv(path):
  df = pd.read_csv(path)
  return df

def stats_for_word_category(df):
  print(df)


####################################################################

# df_list = read_data()
# get_stats_for_every_word(df_list)
df = read_stats_from_csv('word_stats_2.csv')
# df = sort_by_category(df)
# df.to_csv('2_word_stats_2_category_columns.csv')

def category_averaging(df):
  df = df.loc[df['Emoji Category'] == 'high']

  print('df', df)
  mean_accuracy_high = np.mean(np.array(list(df['Mean Accuracy'])))
  mean_rt_high = np.mean(np.array(list(df['Mean RT'])))
  std_rt = np.mean(np.array(list(df['Standard Deviation RT'])))
  print('mean_accuracy_high', mean_accuracy_high)
  print('mean_rt_high', mean_rt_high)
  print('std_rt', std_rt)

  df = read_stats_from_csv('word_stats_2.csv')
  df = df.loc[df['Emoji Category'] == 'med']

  print('df', df)
  mean_accuracy_med = np.mean(np.array(list(df['Mean Accuracy'])))
  mean_rt_med = np.mean(np.array(list(df['Mean RT'])))
  std_rt_med = np.mean(np.array(list(df['Standard Deviation RT'])))
  print('mean_accuracy_med', mean_accuracy_med)
  print('mean_rt_med', mean_rt_med)
  print('std_rt_med', std_rt_med)

  df = read_stats_from_csv('word_stats_2.csv')
  df = df.loc[df['Emoji Category'] == 'low']

  print('df', df)
  mean_accuracy_low = np.mean(np.array(list(df['Mean Accuracy'])))
  mean_rt_low = np.mean(np.array(list(df['Mean RT'])))
  std_rt_low = np.mean(np.array(list(df['Standard Deviation RT'])))
  print('mean_accuracy_low', mean_accuracy_low)
  print('mean_rt_low', mean_rt_low)
  print('std_rt_low', std_rt_low)

  df = read_stats_from_csv('word_stats_2.csv')
  df = df.loc[df['Emoji Category'] == 'none']

  print('df', df)
  mean_accuracy_none = np.mean(np.array(list(df['Mean Accuracy'])))
  mean_rt_none = np.mean(np.array(list(df['Mean RT'])))
  std_rt_none = np.mean(np.array(list(df['Standard Deviation RT'])))
  print('mean_accuracy_none', mean_accuracy_none)
  print('mean_rt_none', mean_rt_none)
  print('std_rt_none', std_rt_none)

  # --------------------------- CONGRUENT ACCURACY --------------------------- #
  df = read_stats_from_csv('word_stats_2.csv')
  # df = df.loc[df['Word Category'] == 'high' and df['Emoji Category'] == 'low']
  df_high_high = df.loc[(df['Word Category'] == 'high') & (df['Emoji Category'] == 'high')]
  df_med_med = df.loc[(df['Word Category'] == 'med') & (df['Emoji Category'] == 'med')]
  df_low_low = df.loc[(df['Word Category'] == 'low') & (df['Emoji Category'] == 'low')]

  high_high_accuracies = list(df_high_high['Mean Accuracy'])
  med_med_accuracies = list(df_med_med['Mean Accuracy'])
  low_low_accuracies = list(df_low_low['Mean Accuracy'])

  congruent_accuracies = high_high_accuracies + med_med_accuracies + low_low_accuracies
  mean_congruent_accuracies = np.mean(np.array(congruent_accuracies))
  print('mean_congruent_accuracies', mean_congruent_accuracies)

  high_high_rt = list(df_high_high['Mean RT'])
  med_med_rt = list(df_med_med['Mean RT'])
  low_low_rt = list(df_low_low['Mean RT'])

  congruent_rt = high_high_rt + med_med_rt + low_low_rt
  mean_congruent_rt = np.mean(np.array(congruent_rt))
  mean_congruent_std = np.std(np.array(congruent_rt))
  print('mean_congruent_rt', mean_congruent_rt)
  print('mean_congruent_std', mean_congruent_std)

  # --------------------------- INCONGRUENT --------------------------- #

  df = read_stats_from_csv('word_stats_2.csv')
  # df = df.loc[df['Word Category'] == 'high' and df['Emoji Category'] == 'low']
  df_high_low = df.loc[(df['Word Category'] == 'high') & (df['Emoji Category'] == 'low')]
  df_high_med = df.loc[(df['Word Category'] == 'high') & (df['Emoji Category'] == 'med')]
  df_med_high = df.loc[(df['Word Category'] == 'med') & (df['Emoji Category'] == 'high')]
  df_med_low = df.loc[(df['Word Category'] == 'med') & (df['Emoji Category'] == 'high')]
  df_low_high = df.loc[(df['Word Category'] == 'low') & (df['Emoji Category'] == 'high')]
  df_low_med = df.loc[(df['Word Category'] == 'low') & (df['Emoji Category'] == 'med')]

  high_low_accuracies = list(df_high_low['Mean Accuracy'])
  high_med_accuracies = list(df_high_med['Mean Accuracy'])
  med_high_accuracies = list(df_med_high['Mean Accuracy'])
  med_low_accuracies = list(df_med_low['Mean Accuracy'])
  low_high_accuracies = list(df_low_high['Mean Accuracy'])
  low_med_accuracies = list(df_low_med['Mean Accuracy'])

  incongruent_accuracies = high_low_accuracies + \
                         high_med_accuracies + \
                         med_high_accuracies + \
                         med_low_accuracies + \
                         low_high_accuracies + \
                         low_med_accuracies

  mean_incongruent_accuracies = np.mean(np.array(incongruent_accuracies))
  print('mean_incongruent_accuracies', mean_incongruent_accuracies)

  high_low_rt = list(df_high_low['Mean RT'])
  high_med_rt = list(df_high_med['Mean RT'])
  med_high_rt = list(df_med_high['Mean RT'])
  med_low_rt = list(df_med_low['Mean RT'])
  low_high_rt = list(df_low_high['Mean RT'])
  low_med_rt = list(df_low_med['Mean RT'])

  incongruent_rt = high_low_rt + high_med_rt + med_high_rt + med_low_rt + low_high_rt + low_med_rt
  mean_incongruent_rt = np.mean(np.array(incongruent_rt))
  mean_incongruent_std = np.std(np.array(incongruent_rt))
  print('mean_incongruent_rt', mean_incongruent_rt)
  print('mean_incongruent_std', mean_incongruent_std)
  

def plot_all_words():
  df = read_stats_from_csv('word_stats_2.csv')
  print('df.head', df.head())
  df = df.sort_values(by=['Mean Accuracy'], ascending=False)
  print('df.head', df.head())
  mean_accuracy_list = list(df['Mean Accuracy'])
  mean_rt_list = list(df['Mean RT'])
  rt_list_std = list(df['Standard Deviation RT'])
  word_list = list(df['Word'])

  ind = np.arange(48)  # the x locations for the groups
  width = 0.35       # the width of the bars

  fig, ax = plt.subplots(figsize=(14, 9))
  rects1 = ax.bar(ind, mean_accuracy_list, width, color='#F2B134')
  rects2 = ax.bar(ind + width, mean_rt_list, width,color='#4FB99F')  # , yerr=rt_list_std)

  ax.set_ylabel('Accuracy and RT in seconds')
  ax.set_title('Accuracy and RT for all words')
  ax.set_xticks(ind + width / 2)
  ax.set_xticklabels(word_list)
  plt.xticks(rotation=90)
  ax.legend((rects1[0], rects2[0]), ('Accuracy', 'Response Time (RT)'))

  for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(10)

  fig.tight_layout()

  plt.show()

def plot_congruent_categories():
  high_arousal_word_acc = 0.9675
  high_arousal_word_rt = 0.9024
  high_arousal_word_rt_std = 0.33672

  med_arousal_word_acc = 0.9675
  med_arousal_word_rt = 0.84175
  med_arousal_word_rt_std = 0.33672

  low_arousal_word_acc = 0.9575
  low_arousal_word_rt = 0.88329
  low_arousal_word_rt_std = 0.35598

  high_arousal_emoji_acc = 0.89
  high_arousal_emoji_rt = 1.05348
  high_arousal_emoji_rt_std = 0.51829

  med_arousal_emoji_acc = 0.9036
  med_arousal_emoji_rt = 1.005
  med_arousal_emoji_rt_std = 0.45499

  low_arousal_emoji_acc = 0.935
  low_arousal_emoji_rt = 1.06041
  low_arousal_emoji_rt_std = 0.62732

  no_emoji_acc = 0.912
  no_emoji_rt = 0.99086
  no_emoji_rt_std = 0.43795

  congruent_acc = 0.966
  congruent_rt = 0.83649
  congruent_rt_std = 0.08514

  incongruent_acc = 0.98
  incongruent_rt = 0.88146
  incongruent_rt_std = 0.1294

  acc = (high_arousal_word_acc, med_arousal_word_acc, low_arousal_word_acc,
         high_arousal_emoji_acc, med_arousal_emoji_acc, low_arousal_emoji_acc,
         no_emoji_acc, congruent_acc, incongruent_acc)

  rt = (high_arousal_word_rt, med_arousal_word_rt, low_arousal_word_rt,
        high_arousal_emoji_rt, med_arousal_emoji_rt, low_arousal_emoji_rt,
        no_emoji_rt, congruent_rt, incongruent_rt)
  
  rt_std = (high_arousal_word_rt_std, med_arousal_word_rt_std, low_arousal_word_rt_std,
            high_arousal_emoji_rt_std, med_arousal_emoji_rt_std, low_arousal_emoji_rt_std,
            no_emoji_rt_std, congruent_rt_std, incongruent_rt_std)

  word_list = ('High Arousal Words', 'Medium Arousal Words',
               'Low Arousal Words', 'High Arousal Emojis', 'Medium Arousal Emojis', 'Low Arousal Emojis', 'No Emojis', 'Congruent', 'Incongruent')

  ind = np.arange(9)  # the x locations for the groups
  width = 0.2         # the width of the bars

  fig, ax = plt.subplots(figsize=(14, 9))
  rects1 = ax.bar(ind, acc, width, color='#F2B134')
  rects2 = ax.bar(ind + width, rt, width, color='#4FB99F', yerr=rt_std)

  ax.set_ylabel('Accuracy and RT in seconds')
  ax.set_title('Accuracy and RT for all words')
  ax.set_xticks(ind + width / 2)
  ax.set_xticklabels(word_list)
  plt.xticks(rotation=45)
  ax.legend((rects1[0], rects2[0]), ('Accuracy', 'Response Time (RT)'))

  for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(10)

  fig.tight_layout()

  plt.show()

# plot_congruent_categories()
# plot_all_words()
# category_averaging(df)


df = read_stats_from_csv('word_stats_2.csv')
df_words = df.loc[(df['Truth'] == 'w')]
word_accuracies = list(df_words['Mean Accuracy'])
word_accuracies_mean = np.mean(np.array(word_accuracies))
print('word_accuracies_mean', word_accuracies_mean)

word_rt = list(df_words['Mean RT'])
word_rt_mean = np.mean(np.array(word_rt))
print('word_rt_mean', word_rt_mean)
word_rt_std = np.std(np.array(word_rt))
print('word_rt_std', word_rt_std)

df_nonwords = df.loc[(df['Truth'] == 'n')]
nonword_accuracies = list(df_nonwords['Mean Accuracy'])
nonword_accuracies_mean = np.mean(np.array(nonword_accuracies))
nonword_rt = list(df_nonwords['Mean RT'])
nonword_rt_mean = np.mean(np.array(nonword_rt))
print('nonword_rt_mean', nonword_rt_mean)
nonword_rt_std = np.std(np.array(nonword_rt))
print('nonword_rt_std', nonword_rt_std)

print('nonword_accuracies_mean', nonword_accuracies_mean)

# NON-WORDS EMOJIS

df_nonwords_emojis = df.loc[(df['Truth'] == 'n') & (df['Emoji Category'] != 'none')]

nonword_emojis_accuracies = list(df_nonwords_emojis['Mean Accuracy'])
nonword_emojis_accuracies_mean = np.mean(np.array(nonword_emojis_accuracies))
print('nonword_emojis_accuracies_mean', nonword_emojis_accuracies_mean)

nonword_emojis_rt = list(df_nonwords_emojis['Mean RT'])
nonword_emojis_rt_mean = np.mean(np.array(nonword_emojis_rt))
print('nonword_emojis_rt_mean', nonword_emojis_rt_mean)
nonword_emojis_rt_std = np.std(np.array(nonword_emojis_rt))
print('nonword_emojis_rt_std', nonword_emojis_rt_std)


# NON-WORDS NO EMOJIS

df_nonwords_no_emojis = df.loc[(df['Truth'] == 'n') & (df['Emoji Category'] == 'none')]

nonword_no_emojis_accuracies = list(df_nonwords_no_emojis['Mean Accuracy'])
nonword_no_emojis_accuracies_mean = np.mean(np.array(nonword_no_emojis_accuracies))
print('nonword_no_emojis_accuracies_mean', nonword_no_emojis_accuracies_mean)

nonword_no_emojis_rt = list(df_nonwords_no_emojis['Mean RT'])
nonword_no_emojis_rt_mean = np.mean(np.array(nonword_no_emojis_rt))
print('nonword_no_emojis_rt_mean', nonword_no_emojis_rt_mean)
nonword_no_emojis_rt_std = np.std(np.array(nonword_no_emojis_rt))
print('nonword_no_emojis_rt_std', nonword_no_emojis_rt_std)

# ALL REAL WORDS EMOJIS

df_words_no_emojis = df.loc[(df['Truth'] == 'w') & (df['Emoji Category'] != 'none')]

word_no_emojis_accuracies = list(df_words_no_emojis['Mean Accuracy'])
word_no_emojis_accuracies_mean = np.mean(np.array(word_no_emojis_accuracies))
print('word_no_emojis_accuracies_mean', word_no_emojis_accuracies_mean)

word_no_emojis_rt = list(df_words_no_emojis['Mean RT'])
word_no_emojis_rt_mean = np.mean(np.array(word_no_emojis_rt))
print('word_no_emojis_rt_mean', word_no_emojis_rt_mean)
word_no_emojis_rt_std = np.std(np.array(word_no_emojis_rt))
print('word_no_emojis_rt_std', word_no_emojis_rt_std)

# ALL REAL WORDS NO EMOJIS

df_words_emojis = df.loc[(df['Truth'] == 'w') & (df['Emoji Category'] == 'none')]

word_emojis_accuracies = list(df_words_emojis['Mean Accuracy'])
word_emojis_accuracies_mean = np.mean(np.array(word_emojis_accuracies))
print('word_emojis_accuracies_mean', word_emojis_accuracies_mean)

word_emojis_rt = list(df_words_emojis['Mean RT'])
word_emojis_rt_mean = np.mean(np.array(word_emojis_rt))
print('word_emojis_rt_mean', word_emojis_rt_mean)
word_emojis_rt_std = np.std(np.array(word_emojis_rt))
print('word_emojis_rt_std', word_emojis_rt_std)


from scipy.stats import ttest_ind
