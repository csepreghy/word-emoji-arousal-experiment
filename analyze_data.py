import pandas as pd
import numpy as np
from numpy.linalg import norm
from itertools import product

def center_and_scale(dataset):

    # select numeric and non-numeric
    num_dataset = dataset.select_dtypes(include = ["float64", "int64"])
    num_dataset.reset_index(drop=True, inplace=True)
    obj_dataset = dataset.select_dtypes(include = ["object"])
    obj_dataset.reset_index(drop=True, inplace=True)

    # divide elements of every column of data set by that columns biggest value
    for col in num_dataset:
        num_dataset[col] = num_dataset[col] / num_dataset[col].max()

    dataset = pd.concat([obj_dataset, num_dataset], axis=1)

    return dataset

def find_word_combs(set1, set2, set3):
    # list of cartesian products of the three sets
    return [el for el in product(set1.itertuples(), set2.itertuples(), set3.itertuples())]

#euclid_dist = numpy.linalg.norm(a-b)

def calc_dists(combs):
    # every row is a dictionary
    row_dicts = []
    
    # iterate and index over all word combinations
    for el in combs:
        high, med, low = np.array(el[0][5:]), np.array(el[1][5:]), np.array(el[2][5:])
        dict1 = {"word_high": el[0][1], "word_med": el[1][1], "word_low": el[2][1], "avg_dist": (norm(high-med) + norm(high-low) + norm(med-low))/3}
        row_dicts.append(dict1)

    data = pd.DataFrame(row_dicts, columns=["word_high", "word_med", "word_low", "avg_dist"])

    return data