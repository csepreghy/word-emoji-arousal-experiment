import pandas as pd
import numpy as np

# reduce dataframe to arousal and valence
def process_word_ratings(word_data):
    w_asl = word_data.loc[:, "A.Mean.Sum"]
    w_val = word_data.loc[:, "V.Mean.Sum"]

    w_join = pd.concat([w_asl, w_val], axis=1)
    w_join.reset_index(inplace=True)
    return w_join

def assemble_word_data(word_ratings, freq_1, freq_2, add_letter_count=True, dropNaN=True):
    # add empty columns to fill later
    word_ratings["freq1"] = np.nan
    #word_ratings["pos1"] = np.nan
    word_ratings["freq2"] = np.nan
    #word_ratings["pos2"] = np.nan
    
    # renaming column labels
    word_ratings = word_ratings.rename(columns={"Word":"word", "A.Mean.Sum":"a_mean", "V.Mean.Sum":"v_mean"})

    # iterate over over word and its index
    for i, word in word_ratings.loc[:,"word"].iteritems():
        # iterate over every row as a tuple
        for rowtuple in freq_1.itertuples():
            #w = rowtuple[1] #freq = rowtuple[3] #pos = rowtuple[4]
            if word == rowtuple[1] and rowtuple[4] == "n":
                word_ratings.loc[i, "freq1"] = rowtuple[3]
                #word_ratings.loc[i, "pos1"] = rowtuple[4]
        
        for rowtuple in freq_2.itertuples():
            #w = rowtuple[0]
            #pos = rowtuple[2]
            #freq = rowtuple[4]
            # multiple POS'es to same word necessitates a solution
            if word == rowtuple[0] and rowtuple[2] == "NoC":
                word_ratings.loc[i, "freq2"] = rowtuple[4]
                #word_ratings.loc[i, "pos2"] = rowtuple[2]

    # freq2 needs to be numeric int64, not object dtype
    word_ratings.loc[:, "freq2"] = pd.to_numeric(word_ratings.loc[:, "freq2"], errors="coerce")

    # remove rows with NaN values, makes future easier
    if dropNaN:
        word_ratings = word_ratings.dropna()
    
    # add number of letters for every word
    if add_letter_count:
        word_ratings["letter_count"] = word_ratings.word.apply(len)

    return word_ratings

def split_by_asl_and_val(dataset, stdnum, show_stats=True):
    if show_stats:
        print("Descriptive statistics of dataset: \n", dataset.describe())
    
    # get means and standard deviations
    a_mean = dataset.describe().a_mean[1]
    a_std = dataset.describe().a_mean[2]
    v_mean = dataset.describe().v_mean[1]
    v_std = dataset.describe().v_mean[2]
    print(v_mean, v_std)
    
    # return dataframe where a_mean values are two standard deviations over mean
    asl_high_val_high = dataset[(dataset.a_mean >= (a_mean + a_std * stdnum)) & (dataset.v_mean >= (v_mean + v_std*stdnum))]
    asl_med_val_high = dataset[((dataset.a_mean <= (a_mean + a_std)) & (dataset.a_mean >= (a_mean - a_std))) & (dataset.v_mean >= (v_mean + v_std*stdnum))]
    asl_low_val_high = dataset[(dataset.a_mean <= (a_mean - a_std * stdnum)) & (dataset.v_mean >= (v_mean + v_std*stdnum))]
    
    asl_high_val_low = dataset[(dataset.a_mean >= (a_mean + a_std * stdnum)) & (dataset.v_mean <= (v_mean - v_std*stdnum))]
    asl_med_val_low = dataset[(dataset.a_mean <= (a_mean + a_std)) & (dataset.a_mean >= (a_mean - a_std)) & (dataset.v_mean <= (v_mean - v_std*stdnum))]
    asl_low_val_low = dataset[(dataset.a_mean <= (a_mean - a_std * stdnum)) & (dataset.v_mean <= (v_mean - v_std*stdnum))]
    
    return asl_high_val_high, asl_med_val_high, asl_low_val_high, asl_high_val_low, asl_med_val_low, asl_low_val_low

def split_by_asl(dataset, stdnum, show_stats=True):
    if show_stats:
        print("Descriptive statistics of dataset: \n", dataset.describe())
    
    # get means and standard deviations
    mean = dataset.describe().a_mean[1]
    std = dataset.describe().a_mean[2]
    
    # return dataframe where a_mean values are two standard deviations over mean
    high = dataset[(dataset.a_mean >= (mean + std * stdnum))]
    med = dataset[(dataset.a_mean <= (mean + std)) & (dataset.a_mean >= (mean - std))]
    low = dataset[(dataset.a_mean <= (mean - std * stdnum))]

    return high, med, low
