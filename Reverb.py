from pedalboard import Reverb
from soundfile import default_subtype
default_reverb = Reverb()

class ReverbPlugin:
  def __init__(self):
    self.reverb = Reverb
    self.options = [
      { 'name': "room_size", 'type': float, 'default': default_reverb.room_size, 'help': "value must be between 0.0 and 1.0"},
      { 'name': "damping", 'type': float, 'default': default_reverb.damping, 'help': "value must be between 0.0 and 1.0"},
      { 'name': "wet_level", 'type': float, 'default': default_reverb.wet_level, 'help': "value must be between 0.0 and 1.0"},
      { 'name': "dry_level", 'type': float, 'default': default_reverb.dry_level, 'help': "value must be between 0.0 and 1.0"},
      { 'name': "width", 'type': float, 'default': default_reverb.width, 'help': "value must be between 0.0 and 1.0"},
      { 'name': "freeze_mode", 'type': float, 'default': default_reverb.freeze_mode, 'help': "value must be between 0.0 and 1.0"},
      ]