import numpy as np
from datasets import get_emoji_data
import pandas as pd
import matplotlib.pyplot as pl

emoji_data = get_emoji_data()
emoji_data_processed = process_emoji_daeta()

word_clusters = run_kmeans(emoji_data_processed)