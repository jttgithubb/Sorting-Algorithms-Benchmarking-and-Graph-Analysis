import csv
import matplotlib.pyplot as plt
from pathlib import Path
from benchmark import PermutationType, get_data_path
import pandas as pd
import numpy as np
from math import log2, e
from sklearn.metrics import r2_score

OKABE_COLORS = ['#000000', '#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7']
plt.rcParams['axes.prop_cycle'] = plt.cycler(color= OKABE_COLORS)

FIGURE_DIRECTORY = Path('figures')
FIGURE_DIRECTORY.mkdir(exist_ok= True)

def plot(title: str, figure_name: str, save: bool):
    plt.title(title)
    if save:
        plt.savefig(FIGURE_DIRECTORY / figure_name, dpi= 300)
    plt.show()

def load_data(algorithm_name: str, permutation: PermutationType) -> dict[int, list[int]]:
    df = pd.read_csv(get_data_path(permutation, algorithm_name), sep= ' ', header= None)
    columns = ['size', 'time']
    df.columns = columns
    data_dict = {}
    for row in df.itertuples():
        if row.size not in data_dict:
            data_dict[row.size] = []
        data_dict[row.size].append(row.time)
    return data_dict

def load_avg_data(algorithm_name: str, permutation: PermutationType) -> dict[int, float]:
    data_dict = load_data(algorithm_name, permutation)
    avg_data_dict = {}
    for key in data_dict.keys():
        summed = 1 if sum(data_dict[key]) == 0 else sum(data_dict[key])
        avg_data_dict[key] = summed/ float(len(data_dict[key]))
    return avg_data_dict

def add_to_plot(algorithm_name: str, permutation: PermutationType, skip: int = 0):
    avg_data_dict = load_avg_data(algorithm_name, permutation)
    x = np.array(list(avg_data_dict.keys()))
    y = np.array(list(avg_data_dict.values()))
    x = x[skip:]
    y = y[skip:]
    xlog = np.log(x)
    ylog = np.log(y)
    m, b = np.polyfit(xlog, ylog, 1)
    fit = np.poly1d((m, b))
    expected_logy = fit(xlog)
    r2 = r2_score(ylog, expected_logy)
    p = plt.loglog(x, y, '.', base= 2, label= f'{algorithm_name} ({permutation.value}): $\\log T(n) \\approx {m: .5} \\log n + {b: .5}$, $R^2 = {r2: .5}$')
    p_fit =plt.loglog(x, e**expected_logy, '--', base= 2, color = p[-1].get_color())
    

if __name__ == "__main__":
    plt.figure(num= 1, figsize= (10, 6), facecolor= 'w', edgecolor= 'k')

    add_to_plot('insertion_sort', PermutationType.REVERSE_SORTED, 0)
    add_to_plot('merge_sort', PermutationType.REVERSE_SORTED, 2)

    plt.legend(bbox_to_anchor=(0, 1), loc= 'upper left', fontsize= 9)
    plt.xlabel('Input size: (n, # of elements)', fontsize= 12)
    plt.ylabel('Elasped time (ns)', fontsize= 12)
    plt.title('Comparison of Insertion and Merge sorts on Reverse-Sorted input', fontsize= 16)
    plt.show()
    