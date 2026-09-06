# Audio Visualizer

Real-time audio waveform visualizer that processes uncompressed WAV files and renders frequency/amplitude streams.

## Overview

Parses raw PCM audio byte streams from `.wav` files, extracts channel amplitudes per frame buffer, and animates real-time waveform bars matching the audio envelope.

## Features

- Reads uncompressed multi-channel WAV streams.
- Amplitude normalization and frequency binning across playback frames.
- Real-time animated visualization using Pygame.

## Tech Stack

Python, Pygame, NumPy, Wave