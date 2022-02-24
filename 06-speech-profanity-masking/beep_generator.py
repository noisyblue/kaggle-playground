from dataclasses import dataclass

import numpy as np


@dataclass()
class BeepConfig:
    duration_millis: float
    freq: int
    volume: float = 1.0
    q_bits: int = 16
    sample_rate: int = 44100


class BeepGenerator:
    @staticmethod
    def create_beep(config: BeepConfig):
        sample_count = int(config.duration_millis / 1000 * config.sample_rate)
        multipliers = np.arange(sample_count)

        waveform = np.sin(2 * np.pi * multipliers * (config.freq / config.sample_rate)) * config.volume

        abs_max_value = 2 ** (config.q_bits - 1)
        waveform_int = np.clip(waveform * abs_max_value, -abs_max_value, abs_max_value - 1)

        if config.q_bits == 8:
            waveform_int = np.int8(waveform_int)
        elif config.q_bits == 16:
            waveform_int = np.int16(waveform_int)
        elif config.q_bits == 24:
            waveform_int = np.int32(waveform_int)
        elif config.q_bits == 32:
            waveform_int = np.int32(waveform_int)
        else:
            raise RuntimeError("Not supported!")

        return waveform_int
