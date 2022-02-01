"""
Kommandolinje-modul til Kalkulator

"""

from typing import Iterable

import click

import kalk


@click.command()
@click.argument('operation', type=str)
@click.argument('arguments', nargs=-1, required=True, type=float)
def main(operation: str, arguments: float):
    do = getattr(kalk, operation)
    result = do(*arguments)
    click.echo(result)
