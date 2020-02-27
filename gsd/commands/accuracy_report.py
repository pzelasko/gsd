#!/usr/bin/env python

import click
import pandas as pd


@click.command()
@click.argument('report', type=click.Path(exists=True))
def main(report):
    df = pd.read_csv(report, sep='\t')
    df = df[:-1]
    df[['train_objective', 'valid_objective']].plot()


if __name__ == '__main__':
    main()
