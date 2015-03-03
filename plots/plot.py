#!/usr/bin/env python
from __future__ import division, print_function


def main(filename):
    print(filename)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Render PDF of the csv data')
    parser.add_argument('filename', metavar='filename', type=str)

    args = parser.parse_args()

    main(
        filename=args.filename,
    )
