import click
from pedalboard import Pedalboard, Chorus
import soundfile as sf
import os


@click.group()
def cli():
  pass

@click.command()
@click.option('-n', '--name', type=str, help='Name to greet', default='Danny')
def hello(name):
  click.echo(f'Hello {name}')


chorus = Chorus()
@click.command()
@click.option("--rate_hz", type=float, default=chorus.rate_hz)
@click.option("--depth", type=float, default=chorus.depth)
@click.option("--centre_delay_ms", type=float, default=chorus.centre_delay_ms)
@click.option("--feedback", type=float, default=chorus.feedback)
@click.option("--mix", type=float, default=chorus.mix, help="value must be between 0.0 and 1.0")
@click.option("--input", type=str, help="input file path")
@click.option("--output", type=str, help="output file path")
def addchorus(rate_hz, depth, centre_delay_ms, feedback, mix, input, output):
  audio, sample_rate = sf.read(input)
  pedalboard = Pedalboard(
      [
          Chorus(rate_hz, depth, centre_delay_ms, feedback, mix),
      ],
      sample_rate=sample_rate,
  )

  effected = pedalboard(audio)

  output_directory = os.path.dirname(output)
  if not os.path.exists(output_directory):
      os.mkdir(output_directory)

  with sf.SoundFile(
      output, "w", samplerate=sample_rate, channels=len(effected.shape)
  ) as f:
      f.write(effected)

cli.add_command(hello)
cli.add_command(addchorus)

def main():
  cli()