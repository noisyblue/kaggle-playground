#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
from pydub.playback import play

from beep_generator import BeepGenerator, BeepConfig

config = BeepConfig(duration_millis=1000, q_bits=16, freq=100, sample_rate=4000)

beep = BeepGenerator.create_beep(config)

play(AudioSegment(
    beep.tobytes(),
    frame_rate=config.sample_rate,
    sample_width=int(config.q_bits / 8),
    channels=1
))

sample_indices = np.arange(len(beep))
plt.style.use('ggplot')
plt.stem(sample_indices, beep, linefmt='r')
plt.plot(sample_indices, beep)
plt.show()
