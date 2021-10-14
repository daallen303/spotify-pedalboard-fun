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
options = [
  { 'name': "rate_hz", 'type': float, 'default': chorus.rate_hz, },
  { 'name': "depth", 'type': float, 'default': chorus.depth, },
  { 'name': "centre_delay_ms", 'type': float, 'default': chorus.centre_delay_ms, },
  { 'name': "feedback", 'type': float, 'default': chorus.feedback, },
  { 'name': "mix", 'type': float, 'default': chorus.mix, 'help': "value must be between 0.0 and 1.0" }
  ]

click_options = []
for option in options:
    help = option['help'] if 'help' in option.keys() else None
    click_options.append(click.Option(["--" + option['name']], type=option['type'], default=option['default'], help=help))

def addchorus_callback(rate_hz, depth, centre_delay_ms, feedback, mix, input, output):
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

addchorus = click.Command('addChorus', callback=addchorus_callback, params=click_options)

cli.add_command(hello)
cli.add_command(addchorus)

def main():
  cli()

def get_version():
  return 1