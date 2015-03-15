#!/usr/bin/env python
from __future__ import division, print_function

import os

import numpy as np
from matplotlib import pyplot
import pandas as pd

from scipy import signal


data_location = '../data/'
plot_location = '.'


def read_csv(plotname):
    return pd.read_csv(
        os.path.join(data_location, '{}.csv'.format(plotname)),
        index_col=0,
    )


def peaks(plotname, data):

    ax = data.plot()
    peaks = pd.Series(
        data.index[
            signal.find_peaks_cwt(
                data.intensity,
                widths=np.arange(1, 32)
            )
        ]
    )

    def postprocess(intensity, peaks):
        """
        Parameters
        ----------
        intensity : pd.Series
        peaks : pd.Series
            index is default enumeration
            values is the raw intensity peaks (which are to be corrected)

        Returns
        -------
        postprocessed_peaks : pd.Series
            index is default enumeration
            values is the corrected intensity peaks.

        """
        neighborhoods = pd.concat(
            {
                0.1: intensity.shift(-1),
                0.0: intensity.shift(0),
                -0.1: intensity.shift(1),
            },
            axis=1
        )
        peak_neighborhoods = neighborhoods.ix[peaks]
        peak_corrections = peak_neighborhoods.idxmax(axis=1)

        postprocessed_peaks = peaks + peak_corrections.reset_index()[0]

        return postprocessed_peaks

    postprocessed_peaks = postprocess(data.intensity, peaks)

    map(ax.axvline, postprocessed_peaks)

    ax.get_figure().savefig(
        os.path.join(
            plot_location,
            '{}_peaks.pdf'.format(plotname),
        )
    )


def ordinary(plotname, data):
    ax = data.plot()

    ax.get_figure().savefig(
        os.path.join(
            plot_location,
            '{}.pdf'.format(plotname),
        )
    )


def main(plotname):
    data = read_csv(plotname)
    ordinary(plotname, data)
    peaks(plotname, data)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Render PDF of the csv data')
    parser.add_argument('plotname', metavar='plotname', type=str)

    args = parser.parse_args()

    main(
        plotname=args.plotname,
    )
