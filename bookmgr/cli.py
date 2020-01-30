import os
import sys

import click

from bookmgr.bookmgr import deploy_book
from bookmgr.config import write_config, get_store


@click.group()
def cli():
    """A simple eBook manager."""
    pass


@cli.command()
@click.option("--config", default=".bookmgr.yaml")
@click.option("--store", default=".store")
def init(config, store):
    click.echo("Initialising...")
    try:
        write_config(config, store)
        click.echo("Config written")
    except FileExistsError:
        click.echo(
            "Failed to initialise, config file '{}' exists".format(config), err=True
        )
        sys.exit(1)

    try:
        os.makedirs(os.path.abspath(store))
        click.echo("Store created")
    except FileExistsError:
        click.echo(
            "Failed to initialise, store '{}' already exists".format(store), err=True
        )
        sys.exit(1)


@cli.command()
@click.option("--config", default=".bookmgr.yaml")
def build(config):
    click.echo("Building...")
    if (store := get_store(config)) :
        store_path = os.path.abspath(store)
        if not os.path.isdir(store):
            click.echo("Failed to locate store '{}'".format(store), err=True)
            exit(1)

        books = [os.path.abspath(os.path.join(store, x)) for x in os.listdir(store)]
        for book in books:
            deploy_book(book)

    else:
        click.echo(
            "Failed to build, config file '{}' could not be read".format(config),
            err=True,
        )
        sys.exit(1)
