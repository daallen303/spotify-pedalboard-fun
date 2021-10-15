from pedalboard import Chorus

class ChorusPlugin:
  def __init__(self):
    self.chorus = Chorus()
    self.options = [
      { 'name': "rate_hz", 'type': float, 'default': self.chorus.rate_hz, },
      { 'name': "depth", 'type': float, 'default': self.chorus.depth, },
      { 'name': "centre_delay_ms", 'type': float, 'default': self.chorus.centre_delay_ms, },
      { 'name': "feedback", 'type': float, 'default': self.chorus.feedback, },
      { 'name': "mix", 'type': float, 'default': self.chorus.mix, 'help': "value must be between 0.0 and 1.0" }
      ]