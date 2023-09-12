# Library for applying some basic visualizations to numerical features

import matplotlib.pyplot as plt
import seaborn as sns


def basic_eda_num(df, feature, target=None, vlines_stats=False, vlines_manual=None):
    # 2 charts in 1 row: Histogram and Boxplot
    fig, ax = plt.subplots(1, 2, figsize=(15, 5), gridspec_kw={'width_ratios': [3, 1]})

    num_data = df[feature]

    # Get main stats: - Mean - Median - Standard deviation - Min - Max - Range
    mean = num_data.mean()
    median = num_data.median()
    std = num_data.std()
    minimum = num_data.min()
    maximum = num_data.max()
    range_ = maximum - minimum
    IQR = num_data.quantile(0.75) - num_data.quantile(0.25)

    # Chart 1: Histogram
    if target is not None:
        sns.histplot(df, x=feature, hue=target, ax=ax[0], kde=True)
    else:
        sns.histplot(num_data, ax=ax[0], kde=True)
    ax[0].set_title('Histogram: {}'.format(feature))
    ax[0].set_xlabel(feature)
    ax[0].set_ylabel('Count')

    # Add vertical lines if necessary along the value as a text
    if vlines_stats:
        stats = {'Mean': mean, 'Median': median, 'IQR': IQR}
        colors = {'Mean': 'r', 'Median': 'g', 'IQR': 'b'}
        for k, v in stats.items():
            ax[0].axvline(v, color=colors[k], linestyle='--', label='{}: {:.2f}'.format(k, v))
            # Show as text the stat name in vertical orientation, middle of the line
            ax[0].text(v, ax[0].get_ylim()[1], k, color='k', ha='center', va='bottom', rotation=90)

    if vlines_manual is not None:
        for vline in vlines_manual:
            ax[0].axvline(vline, color='k', linestyle='--', label='Limit: {:.2f}'.format(vline))
            ax[0].text(vline, ax[0].get_ylim()[1], '{:.2f}'.format(vline), color='k', ha='center', va='bottom')

    # Remove top and right borders
    ax[0].spines['top'].set_visible(False)
    ax[0].spines['right'].set_visible(False)

    # Add some padding
    ax[0].margins(0.05)

    # Chart 2: Boxplot
    if target is not None:
        try:
            # If target is not numerical or categorical, transform it to categorical
            df[target] = df[target].astype('category')
            sns.boxplot(data=df, x=feature, y=target, ax=ax[1])
        except:
            print('Check the target variable. It should be categorical or int')
    else:
        sns.boxplot(num_data, ax=ax[1])
    ax[1].set_title('Boxplot: {}'.format(feature))
    ax[1].set_xlabel(feature)

    # Remove top and right borders
    ax[1].spines['top'].set_visible(False)
    ax[1].spines['right'].set_visible(False)

    # Add some padding
    ax[1].margins(0.05)

    plt.tight_layout()
    plt.show()

    # Print main stats
    print('Mean: {}'.format(mean))
    print('Median: {}'.format(median))
    print('Standard Deviation: {}'.format(std))
    print('Minimum: {}'.format(minimum))
    print('Maximum: {}'.format(maximum))
    print('Range: {}'.format(range_))
    # This is the interquartile range. It is the difference between the 75th percentile and the 25th percentile of the data. It is also called the midspread or middle 50%.
    # The goal of the IQR is to measure the spread of the data and to identify outliers. The IQR is robust to outliers.
    print('Interquartile Range: {}'.format(IQR))
    print('-----------------------------------')
    analyze_skewness_kurtosis(num_data)

    return None


def analyze_skewness_kurtosis(num_data):
    # Check if distribution is normal, skewed (right or left) or kurtosis
    skewness = num_data.skew()
    kurtosis = num_data.kurtosis()

    if skewness > 0:
        skewness_type = 'right'
    elif skewness < 0:
        skewness_type = 'left'
    else:
        skewness_type = 'normal'

    if kurtosis > 0:
        kurtosis_type = 'heavy-tailed'
    elif kurtosis < 0:
        kurtosis_type = 'light-tailed'
        kurtosis = abs(kurtosis)
    else:
        kurtosis_type = 'normal'

    print('Skewness: {:.2f} ({})'.format(skewness, skewness_type))
    print('Kurtosis: {:.2f} ({})'.format(kurtosis, kurtosis_type))

    return None
