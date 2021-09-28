# rate_hz default 1
# depth default .25
# centre_delay_ms default 7
# feedback default 0
# mix value 0.0 - 1.0 default 0.5

# This file defines the chorus arguments

import argparse
from pedalboard import  Pedalboard, Chorus
import os
import sys
import soundfile as sf

# Instantiate the Chorus object early so we can read its defaults for the argparser --help:
chorus = Chorus()

options = ['rate_hz', 'depth', 'centre_delay_ms', 'feedback']
parser = argparse.ArgumentParser()
parser.add_argument('--mix', help='value must be between 0.0 and 1.0', type=float, default=chorus.mix) # can also be contained in file just need a dictionary for options

parser.add_argument('--input_file', help='The input file to add chorus to.')
parser.add_argument('--output_file', help='Path for the output file')
for option in options:
  parser.add_argument('--' + option, type=float, default=getattr(chorus, option))
  
args = parser.parse_args()
filepath = getattr(args, 'input_file')
outputfilepath = getattr(args, 'output_file')

if not filepath:
  raise Exception('input_file is required')
if not outputfilepath:
  raise Exception('output_file is required')

for option in options:
    setattr(chorus, option, getattr(args, option))

audio, sample_rate = sf.read(filepath)
pedalboard = Pedalboard([
        chorus,
      ], sample_rate=sample_rate)

effected = pedalboard(audio)

outputDirectory = os.path.dirname(outputfilepath)
if not os.path.exists(outputDirectory):
  os.mkdir(outputDirectory)

with sf.SoundFile(outputfilepath, 'w', samplerate=sample_rate, channels=len(effected.shape)) as f:
      f.write(effected)