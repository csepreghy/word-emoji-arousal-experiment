# reduce dataframe to arousal and valence
def process_word_ratings(word_data):
    import pandas as pd
    w_asl = word_data.loc[:, "A.Mean.Sum"]
    w_val = word_data.loc[:, "V.Mean.Sum"]

    w_join = pd.concat([w_asl, w_val], axis=1)
    w_join.reset_index(inplace=True)
    return w_join

def assemble_word_data(word_ratings, freq_1, freq_2, dropNaN=True):
    import pandas as pd
    import numpy as np
    
    # add empty columns to fill later
    word_ratings["freq1"] = np.nan
    word_ratings["pos1"] = np.nan
    word_ratings["freq2"] = np.nan
    word_ratings["pos2"] = np.nan
    
    # iterate over over word and its index
    for i, word in word_ratings.loc[:,"Word"].iteritems():
        # iterate over every row as a tuple
        for rowtuple in freq_1.itertuples():
            w = rowtuple[1]
            freq = rowtuple[3]
            pos = rowtuple[4]
            if word == w:
                word_ratings.loc[i, "freq1"] = freq
                word_ratings.loc[i, "pos1"] = pos
        
        for rowtuple in freq_2.itertuples():
            w = rowtuple[0]
            pos = rowtuple[2]
            freq = rowtuple[4]
            # multiple POS'es to same word necessitates a solution
            if word == w and pos == "NoC":
                word_ratings.loc[i, "freq2"] = freq
                word_ratings.loc[i, "pos2"] = pos
    
    # renaming column labels
    word_ratings = word_ratings.rename(columns={"Word":"word", "A.Mean.Sum":"a_mean", "V.Mean.Sum":"v_mean"})

    # remove rows with NaN values, makes future easier
    if dropNaN:
        word_ratings = word_ratings.dropna()

    return word_ratings

def split_by_arousal(dataset, stdnum=2, show_stats=True):
    import pandas as pd
    if show_stats:
        print("Descriptive statistics of dataset: \n", dataset.describe())
    
    mean = dataset.describe().a_mean[1]
    std = dataset.describe().a_mean[2]
    
    # return dataframe where a_mean values are two standard deviations over mean
    group_high = dataset[dataset.a_mean >= (mean + std * stdnum)]
    group_med = dataset[(dataset.a_mean <= (mean + std)) & (dataset.a_mean >= (mean - std))]
    group_low = dataset[dataset.a_mean <= (mean - std * stdnum)]

    """
    middle_a = w_dropped[(w_dropped.a_mean <= (a_mean + a_std)) & (w_dropped.a_mean >= (a_mean - a_std))
                    & (w_dropped.v_mean <= (v_mean + v_std)) & (w_dropped.v_mean >= (v_mean - v_std))]
    """

    return group_high, group_med, group_low