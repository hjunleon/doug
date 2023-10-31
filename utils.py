import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

import scipy.stats as ss

def visualise_value_counts(df):
    for col in df.columns:
        ax = sns.countplot(x=col, data=df)
        xticks = ax.xaxis.get_major_ticks()
        for i,tick in enumerate(xticks):
            if i%5 != 0:
                tick.label1.set_visible(False)
        plt.show()
        # print(df_b[col].value_counts())
def print_heatmap(corr_df, figsize=(12,12)):
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(corr_df, 
                ax=ax,
            xticklabels=corr_df.columns.values,
            yticklabels=corr_df.columns.values,
               annot = True)
    plt.show()
def analyze_correlation(df, is_pearson=False):
    corr_methods = ['pearson','spearman','kendall']
    if is_pearson:
        corr_methods = ['pearson']
    for method in corr_methods:
        corr_df = df.corr(method='pearson', min_periods=1, numeric_only=False)
        print(method)
        print_heatmap(corr_df)
def get_top_5_overall(df):
    #assumes columns are rank-based
    final_rank = df.apply(lambda x: sum(x), axis=1)
    print("Top 5")
    print(final_rank.nlargest(n=5))
    