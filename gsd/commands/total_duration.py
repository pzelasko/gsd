#!/usr/bin/env python

import click
import pandas as pd


@click.command()
@click.argument('segments', type=click.File())
def main(segments):
    durations = []
    for line in segments:
        parts = line.strip().split()
        begin, end = float(parts[2]), float(parts[3])
        durations.append(end - begin)
    durations = pd.DataFrame(durations)
    total = float(durations.sum())
    print('Total duration:', total, 'seconds')
    print('Total duration:', total / 3600, 'hours')
    print('Statistics:')
    print(durations.describe())


if __name__ == '__main__':
    main()