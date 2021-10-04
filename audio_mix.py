import click

@click.group()
def cli():
  pass

@click.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='Danny')
def hello(name):
  click.echo(f'Hello {name}')

cli.add_command(hello)

def main():
  cli()