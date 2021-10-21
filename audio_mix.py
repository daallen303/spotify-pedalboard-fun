from typing import Text
import click
from numpy import string_
from pedalboard import Pedalboard
import soundfile as sf
import os
from Chorus import ChorusPlugin
from Reverb import ReverbPlugin
chorus = ChorusPlugin()
reverb = ReverbPlugin()

def write_output(output, sample_rate, audio):
  output_directory = os.path.dirname(output)
  if not os.path.exists(output_directory):
      os.mkdir(output_directory)
  with sf.SoundFile(
      output, 'w', samplerate=sample_rate, channels=len(audio.shape)
  ) as f:
      f.write(audio)

def init_pedalboard(plugins, sample_rate):
  return Pedalboard(
      plugins,
      sample_rate=sample_rate,
  )

def write_audio(input, plugins, output):
  audio, sample_rate = sf.read(input)
  pedalboard = init_pedalboard(plugins, sample_rate)
  effected = pedalboard(audio)
  write_output(output, sample_rate, audio=effected)

def create_options(plugin):
    options = []
    for option in plugin.options:
        help = option['help'] if 'help' in option.keys() else None
        options.append(click.Option(['--' + option['name']], type=option['type'], default=option['default'], help=help))
    options.append(click.Option(['--input']))
    options.append(click.Option(['--output']))
    return options

def add_chorus_callback(rate_hz, depth, centre_delay_ms, feedback, mix, input, output):
  plugins = [ chorus.chorus(rate_hz, depth, centre_delay_ms, feedback, mix) ]
  write_audio(input, plugins, output)

def add_reverb_callback(room_size, damping, wet_level, dry_level, width, freeze_mode,  input, output):
  plugins = [ reverb.reverb(room_size, damping, wet_level, dry_level, width, freeze_mode) ]
  write_audio(input, plugins, output)

@click.group()
def cli():
  pass

chorus_options = create_options(chorus)
addchorus = click.Command('chorus', callback=add_chorus_callback, params=chorus_options)
cli.add_command(addchorus)

reverb_options = create_options(reverb)
addreverb = click.Command('reverb', callback=add_reverb_callback, params=reverb_options)
cli.add_command(addreverb)

def main():
  cli()

def get_version():
  return 1