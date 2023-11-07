import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
sns.set_style('ticks')

# Formatting to billion, million or thousand
def numeric_formatter(x, pos):
    if x >= 1e9:
        return f'{x/1e9:.1f} B'
    elif x >= 1e6:
        return f'{x/1e6:.1f} M'
    elif x >= 1e4:
        return f'{x/1e3:.1f} K'
    else:
         return str(int(x))

# Line chart visualization
def line_subplotting(ax, df, xcolumn, ycolumn, moving_average_column, label, color, linewidth, fontsize):
    sns.lineplot(data=df, x=xcolumn, y=ycolumn, color=color, label=label, ax=ax, lw=linewidth)
    sns.lineplot(data=df, x=xcolumn, y=moving_average_column, color='#FFB000', label=f'Moving Average ({label})', ax=ax, lw=linewidth, linestyle='dashed')
    ax.tick_params(axis='y')
    ax.set_ylabel(label, color='black', fontsize=fontsize)
    ax.set_xlabel('Date', color='black', fontsize=fontsize)
    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_formatter(FuncFormatter(numeric_formatter))
    ax.legend(loc='upper left')

# Histogram visualization
def hist_subplotting(ax, df, column, label, color, fontsize, bins):
    sns.histplot(data=df[column], color=color, ax=ax, bins=bins)
    ax.set_ylabel('Count', fontsize=fontsize)
    ax.set_xlabel(label, color='black', fontsize=fontsize)
    ax.set_ylim(bottom=0)
    ax.xaxis.set_major_formatter(FuncFormatter(numeric_formatter))

# Area chart visualization
def area_subplotting(ax, df, groupcolumn, xcolumn, ycolumn, plot_value, color, max_value, opacity):
    for x, y in enumerate(plot_value.index):
        plot_data = df[df[groupcolumn] == y]
        moving_average = plot_data[ycolumn].rolling(window=7).mean()
        ax.fill_between(plot_data[xcolumn], 0, moving_average, label=y, color=color[y], alpha=opacity, zorder=max_value - moving_average.max())
        ax.set_ylim(bottom=0)
        ax.yaxis.set_major_formatter(FuncFormatter(numeric_formatter))
        ax.legend(loc='upper left')


# Bar chart visualization
def bar_subplotting(ax, df, column, color, xlabel, ylabel, title, fontsize):
    sns.barplot(data=df, x=df.index, y=column, ax=ax, color=color)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.set_title(title, fontsize=14)

# Violin plot visualization
def violin_subplotting(ax, df, xcolumn, ycolumn, xlabel, ylabel, palette, fontsize):
    sns.violinplot(ax=ax, data=df, x=xcolumn, y=ycolumn, palette=palette)
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)
    ax.yaxis.set_major_formatter(FuncFormatter(numeric_formatter))

# Regression plot visualization
def reg_subplotting(ax, df, xcolumn, ycolumn, xlabel, ylabel, color, fontsize):
    sns.regplot(ax=ax, data=df, x=xcolumn, y=ycolumn, color=color, scatter_kws={'s': 50, 'alpha': 0.6})
    ax.set_xlabel(xlabel, fontsize=fontsize)
    ax.set_ylabel(ylabel, fontsize=fontsize)

# Despine subplot
def despine_subplot(ax):
    sns.despine(bottom=False, left=True, top=True, right=True, trim=False, ax=ax)
    ax.set_yticks([])
