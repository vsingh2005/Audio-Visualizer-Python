# Audio Visualizer

A real-time audio waveform and frequency visualizer in Python that parses uncompressed `.wav` audio files and renders visual waveform streams.

## Overview

This project reads raw PCM audio streams from `.wav` files, performs amplitude extraction across audio frames, and renders animated visual waveform bars synchronized with playback.

## Features

- **WAV Stream Parsing**: Reads uncompressed PCM audio channels, sample rates, and bit depths.
- **Amplitude Normalization**: Converts raw byte streams into normalized frequency and amplitude vectors.
- **Visual Waveform Rendering**: Generates dynamic animated visual bars matching audio amplitude envelopes.

## Tech Stack

- **Language**: Python 3
- **Libraries**: Pygame / Matplotlib, Wave, NumPy

## Getting Started

```bash
# Clone repository
git clone https://github.com/vsingh2005/Audio-Visualizer-Python.git
cd Audio-Visualizer-Python

# Install dependencies
pip install pygame numpy

# Run visualizer
python visualizer.py
```