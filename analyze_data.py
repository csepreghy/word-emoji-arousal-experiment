def center_and_scale(dataset):
    from sklearn.preprocessing import normalize, StandardScaler
    dataset = normalize(dataset)
    dataset = StandardScaler(dataset)
    return dataset

