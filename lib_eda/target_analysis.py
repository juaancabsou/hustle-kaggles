# Script for gathering all the target analysis functions


import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')


def basic_eda_target(target):
    """
    Plot a chart with a barplot at the left and a pie chart at the right.
    The goal is to study the target distribution.
    Return None
    """
    # 2 charts in 1 row
    fig, ax = plt.subplots(1, 2, figsize=(9, 4))

    # Chart 1: Barplot
    sns.countplot(x=target, ax=ax[0])
    ax[0].set_title('Target Distribution - Absolute Values')
    ax[0].set_xlabel('Target')
    ax[0].set_ylabel('Count')

    # Add values
    for p in ax[0].patches:
        ax[0].annotate('{:.0f}'.format(p.get_height()), (p.get_x() + 0.4, p.get_height() + 50), fontsize=10,
                       ha='center', va='bottom')

    # Remove top and right borders
    ax[0].spines['top'].set_visible(False)
    ax[0].spines['right'].set_visible(False)

    # Add some padding
    ax[0].margins(0.25)

    # Chart 2: Pie chart
    ax[1].pie(target.value_counts(), labels=target.unique(), autopct='%1.1f%%', startangle=90)
    ax[1].set_title('Target Distribution - Percentage')
    ax[1].axis('equal')

    plt.tight_layout()
    plt.show()

    return None
