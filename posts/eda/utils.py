import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def plt_hist_score(scores, title=None, dark=True):
    if dark:
        plt.style.use('dark_background')
    ymax = max(scores.value_counts().values) + 2
    scores = [int(x) for x in scores]
    bin_width = 1
    left_edge = 0.5
    right_edge = 5
    edges = np.arange(left_edge,
                    right_edge + bin_width,   # include rightmost edge
                    bin_width)

    plt.figure(figsize=(6,4))
    if title is None:
        title = 'Score Distribution Across Swings'
    plt.title(title)
    plt.xlabel('Scores')
    plt.ylabel('Frequency')
    plt.ylim(0, ymax)
    plt.hist(sorted(scores), bins=edges, align='mid', rwidth=0.5);