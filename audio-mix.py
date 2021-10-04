import click

@click.group()
def cli():
  pass

@click.command()
def hello():
  click.echo('hello')

cli.add_command(hello)
