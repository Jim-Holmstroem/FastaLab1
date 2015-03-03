#!/usr/bin/env python
from __future__ import division, print_function

import os

import pandas


data_location = '../data/'
plot_location = '.'


def read_csv(plotname):
    return pandas.read_csv(
        os.path.join(data_location, '{}.csv'.format(plotname)),
        index_col=0,
    )


def main(plotname):
    ax = read_csv(plotname).plot()

    ax.get_figure().savefig(
        os.path.join(
            plot_location,
            '{}.pdf'.format(plotname),
        )
    )


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Render PDF of the csv data')
    parser.add_argument('plotname', metavar='plotname', type=str)

    args = parser.parse_args()

    main(
        plotname=args.plotname,
    )
