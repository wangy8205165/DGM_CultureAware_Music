"""
Linear mix of two mono waveforms (used by data augmentation in torch_tools).

Compatible with declare-lab/Tango-style API: mix(sound1, sound2, mix_ratio, sr).
"""

import numpy as np


def mix(sound1, sound2, mix_ratio, sr):
    """
    Mix two 1D audio signals with linear weights.

    Parameters
    ----------
    sound1, sound2 : array-like
        Mono samples. Typically already normalized and at the same rate as ``sr``.
    mix_ratio : float
        Weight on ``sound1``; ``sound2`` uses ``(1 - mix_ratio)``.
        E.g. ``0.5`` gives equal-power blend: 0.5 * s1 + 0.5 * s2.
    sr : int
        Sample rate in Hz. Both inputs should already match this rate; kept for
        API compatibility with the original Tango helper.

    Returns
    -------
    np.ndarray
        1D ``float32`` mixed waveform, length ``max(len(s1), len(s2))`` (shorter
        signal is zero-padded at the end).
    """
    del sr  # callers pass 16000; waveforms are already resampled in read_wav_file

    s1 = np.asarray(sound1, dtype=np.float64).reshape(-1)
    s2 = np.asarray(sound2, dtype=np.float64).reshape(-1)

    n = max(s1.size, s2.size)
    if s1.size < n:
        s1 = np.pad(s1, (0, n - s1.size), mode="constant", constant_values=0.0)
    if s2.size < n:
        s2 = np.pad(s2, (0, n - s2.size), mode="constant", constant_values=0.0)

    w1 = float(mix_ratio)
    w2 = 1.0 - w1
    out = w1 * s1 + w2 * s2

    return out.astype(np.float32)
