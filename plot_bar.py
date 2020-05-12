import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import sys

def counts(data):    
    ax = sns.countplot(data, order=range(100))
    plt.xlabel('Age')
    return ax

def bars(data, cr, df):
    freq = lambda i: len(i) / float(len(df))
    ax = sns.barplot(x=data, y=data, estimator=freq, order=range(100), alpha=0.7, color= cr)
    plt.ylabel('Frequency')
    return ax

def specific(cc):
    files = ('gan_morph_wgangp_z512_arcface_10llr_Din_flip_0001l2_0_3_stargan_GBN_age.csv', \
            'morph_3_age.csv', \
            )

    for i, file in enumerate(files):
        df = pd.read_csv(file)
        
        data = df.iloc[:,2]
        ax = bars(data, cc[i])

        ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
        ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
        plt.axvline(data.mean(), color=cc[i], linestyle='dashed')
    plt.savefig('bar_{}.png'.format(file.split('.')[0], dpi=120))
    plt.close()

def single(cc):
    file = sys.argv[1]
    df = pd.read_csv('gmm/'+file)
    labels = df['label']
    ages = df['age']
    ls = set(labels)
    for i, l in enumerate(ls):
        data = ages[labels == l]
        ax = bars(data, cc[i], df)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
        ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
        plt.axvline(data.mean(), color=cc[i], linestyle='dashed')
        plt.ylim(0,0.04)
    plt.savefig('bar_{}.png'.format(file.split('.')[0], dpi=240))
    plt.close()

if __name__ == '__main__':
    color_code = ('#496e76', '#b8c57a', '#afcbcc', '#bf3a7c', '#6b6787', \
                    '#df8149', '#a6cea0', '#3a2068', '#437c17', '#bf5e64', '#63110e', '#32212a')
    # specific(color_code) 
    single(color_code) 
