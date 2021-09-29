#! /usr/local/bin/python3
import argparse
from pedalboard import Pedalboard, Chorus
import os
import soundfile as sf

chorus = Chorus()
options = [
  { 'name': "rate_hz", 'type': float, 'default': chorus.rate_hz, },
  { 'name': "depth", 'type': float, 'default': chorus.depth, },
  { 'name': "centre_delay_ms", 'type': float, 'default': chorus.centre_delay_ms, },
  { 'name': "feedback", 'type': float, 'default': chorus.feedback, },
  { 'name': "mix", 'type': float, 'default': chorus.mix, 'help': "value must be between 0.0 and 1.0" }
  ]

parser = argparse.ArgumentParser()
parser.add_argument("--input_file", help="The input file to add chorus to.")
parser.add_argument("--output_file", help="Path for the output file")

for option in options:
    help = option['help'] if 'help' in option.keys() else None
    parser.add_argument("--" + option['name'], type=option['type'], default=option['default'], help=help, metavar='')

args = parser.parse_args()
input_filepath = getattr(args, "input_file")
output_filepath = getattr(args, "output_file")

if not input_filepath:
    raise Exception("input_file is required")
if not output_filepath:
    raise Exception("output_file is required")

for option in options:
    setattr(chorus, option['name'], getattr(args, option['name']))

audio, sample_rate = sf.read(input_filepath)
pedalboard = Pedalboard(
    [
        chorus,
    ],
    sample_rate=sample_rate,
)

effected = pedalboard(audio)

output_directory = os.path.dirname(output_filepath)
if not os.path.exists(output_directory):
    os.mkdir(output_directory)

with sf.SoundFile(
    output_filepath, "w", samplerate=sample_rate, channels=len(effected.shape)
) as f:
    f.write(effected)
