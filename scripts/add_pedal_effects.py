import os
import sys
import soundfile as sf

from pedalboard import (
    Pedalboard,
    Convolution,
    Compressor,
    Chorus,
    Distortion,
    Gain,
    Reverb,
    Limiter,
    LadderFilter,
    HighpassFilter,
    LowpassFilter,
    Phaser,
)

plugins = [
  # Non default constructor, currently throws error
  # {
  # 'name': 'convolution',
  # 'plugin': Convolution
  # },
  {
  'name': 'compressor',
  'plugin': Compressor
  },
  {
    'name': 'chorus',
    'plugin': Chorus
  },
  {
    'name': 'gain',
    'plugin': Gain
  },
  {
    'name': 'distortion',
    'plugin': Distortion
  },
  {
    'name': 'reverb',
    'plugin': Reverb
  },
  {
    'name': 'limiter',
    'plugin': Limiter
  },
  {
    'name': 'ladder_filter',
    'plugin': LadderFilter
  },
  {
    'name': 'highpass_filter',
    'plugin': HighpassFilter
  },
  {
    'name': 'lowpass_filter',
    'plugin': LowpassFilter
  },
  {
    'name': 'phaser',
    'plugin': Phaser
  },
]

filepath = sys.argv[1]
filename = filepath.split('/')[-1].split('.')[0]
audio, sample_rate = sf.read(filepath)

for plugin in plugins:
    plugin['board'] = Pedalboard([
        plugin['plugin'](),
      ], sample_rate=sample_rate)

for plugin in plugins:
  effected = plugin['board'](audio)
  outputDirectory = 'audio/output_files/' + filename + '/'
  outputFilePath =  outputDirectory + plugin['name']+'_'+filename+'.wav'
  if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

  with sf.SoundFile(outputFilePath, 'w', samplerate=sample_rate, channels=len(effected.shape)) as f:
        f.write(effected)