#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument('filename')
@click.option("-p", "--punkt")
@click.option("-n", "--nomer")
@click.option("-t", "--time")
def add(filename, punkt, nomer, time):
    stations = open_file(filename)
    stations.append(
        {
            'punkt': punkt,
            'nomer': nomer,
            'time': time
        }
    )
    with open(filename, "w", encoding="utf-8") as out:
        json.dump(stations, out, ensure_ascii=False, indent=4)


@cli.command()
@click.argument('filename')
@click.option("-p", "--punkt")
def select(filename, name_station):
    stations = open_file(filename)
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "No",
            "Город прибытия",
            "Номер поезда",
            "Время отправления"
        )
    )
    print(line)
    result = []
    for idx, station in stations:
        if station.get('punkt', '') == name_station:
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                        idx,
                        station.get('punkt', ''),
                        station.get('nomer', ''),
                        station.get('time', '')
                    )
                )
    print(line)


@cli.command()
@click.argument('filename')
def display(filename):
    stations = open_file(filename)
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "No",
            "Город прибытия",
            "Номер поезда",
            "Время отправления"
        )
    )
    print(line)
    for idx, station in enumerate(stations, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                station.get('punkt', ''),
                station.get('nomer', ''),
                station.get('time', '')
            )
        )
    print(line)


def open_file(filename):
    with open(filename, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    cli()


if __name__ == '__main__':
    main()
