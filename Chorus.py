from pedalboard import Chorus

default_chorus = Chorus()

class ChorusPlugin:
  def __init__(self):
    self.chorus = Chorus
    self.options = [
      { 'name': "rate_hz", 'type': float, 'default': default_chorus.rate_hz, },
      { 'name': "depth", 'type': float, 'default': default_chorus.depth, },
      { 'name': "centre_delay_ms", 'type': float, 'default': default_chorus.centre_delay_ms, },
      { 'name': "feedback", 'type': float, 'default': default_chorus.feedback, },
      { 'name': "mix", 'type': float, 'default': default_chorus.mix, 'help': "value must be between 0.0 and 1.0" }
      ]