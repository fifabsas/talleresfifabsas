# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 11:42:31 2014, para la práctica de cristales sónicos de Labo 5.

@author: Juan Beiroa.
@authorofauthor: Mark Jones.
Pueden ver el programa original que sirvió como base de este en la web de Mark 
Jones: http://markjones112358.co.nz/projects/Python-Tone-Generator/ . 

Este script utiliza PyAudio (bindings de PortAudio) y NumPy para reproducir 
generar y reproducir sonido en la PC. Recomiendo que instalen PyAudio via pip
(incluso con Anaconda) y PortAudio con su sogüar manayer de elección. Si tienen
Windows, PyAudio debería instalar PortAudio.

Terminología:
Buffer: Espacio de memoria de la placa de sonido donde va guardando frames.
Frame: Muestra de amplitud (intensidad del sonido) a un dado tiempo.
Sample rate: Frecuencia de muestreo (cada cuánto toma un frame).
"""

import numpy as np
import pyaudio


class ToneGenerator(object):


    def __init__(self, samplerate=48100, frames_per_buffer=4810):
        """
        Por prueba y error, todo funciona mejor cuando frames_per_buffer es 
        algún submúltiplo del samplerate.
        """
        self.p = pyaudio.PyAudio()
        self.samplerate = samplerate
        self.frames_per_buffer = frames_per_buffer
        self.streamOpen = False


    def sinewave(self):
        """
        Crea tonos senoidales acorde al tamaño del buffer.
        """
        if self.buffer_offset + self.frames_per_buffer - 1 > self.x_max:
            #relleno con ceros al final si es necesario
            xs = np.arange(self.buffer_offset, self.x_max)
            tmp = self.amplitude * np.sin(xs * self.omega) #tono
            out = np.append(tmp, np.zeros(self.frames_per_buffer-len(tmp)))
        else:
            xs = np.arange(self.buffer_offset,
                           self.buffer_offset + self.frames_per_buffer)
            out = self.amplitude * np.sin(xs * self.omega)
        self.buffer_offset += self.frames_per_buffer
        return out

    def callback_sine(self, in_data, frame_count, time_info, status):
        """
        Función callback implementada según docs de PyAudio.
        """
        if self.buffer_offset < self.x_max:
            data = self.sinewave().astype(np.float32)
            return (data.tostring(), pyaudio.paContinue)
        else:
            return (None, pyaudio.paComplete)

    def play_sine(self, frequency, duration, amplitude):
        self.omega = float(frequency) * (np.pi * 2) / self.samplerate
        self.amplitude = amplitude
        self.buffer_offset = 0
        self.streamOpen = True
        self.x_max = np.ceil(self.samplerate * duration) - 1
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=self.samplerate,
                                  output=True,
                                  frames_per_buffer=self.frames_per_buffer,
                                  stream_callback=self.callback_sine)


    def noise(self):
        """
        Usamos np.random.random_sample para crear ruido (no es estrictamente
        ruido blanco) y lo adecuamos al buffer igual que en sinewave.
        """
        if self.buffer_offset + self.frames_per_buffer - 1 > self.x_max:
            #relleno con ceros al final si es necesario
            xs = np.arange(self.buffer_offset, self.x_max)
            tmp = np.random.random_sample(len(xs)) #ruido
            out = np.append(tmp, np.zeros(self.frames_per_buffer-len(tmp)))
        else:
            xs = np.arange(self.buffer_offset,
                           self.buffer_offset + self.frames_per_buffer)
            out = np.random.random_sample(len(xs))
        self.buffer_offset += self.frames_per_buffer
        return out

    def callback_noise(self, in_data, frame_count, time_info, status):
        if self.buffer_offset < self.x_max:
            data = self.noise().astype(np.float32)
            return (data.tostring(), pyaudio.paContinue)
        else:
            return (None, pyaudio.paComplete)

    def play_noise(self, duration):
        self.buffer_offset = 0
        self.streamOpen = True
        self.x_max = np.ceil(self.samplerate * duration) - 1
        self.stream = self.p.open(format=pyaudio.paFloat32,
                                  channels=1,
                                  rate=self.samplerate,
                                  output=True,
                                  frames_per_buffer=self.frames_per_buffer,
                                  stream_callback=self.callback_noise)


    def is_playing(self):
        """
        Cierra el Stream si ya terminó la reproducción.
        """
        if self.stream.is_active():
            return True
        else:
            if self.streamOpen:
                self.stream.stop_stream()
                self.stream.close()
                self.streamOpen = False
            return False


class Recorder(object):
    """
    Clase para grabar con pyaudio.
    """
    
    def __init__(self, samplerate=48100, frames_per_buffer=4810):
        self.samplerate = samplerate
        self.frames_per_buffer = frames_per_buffer
        self.rec = pyaudio.PyAudio()
        self.stream = self.rec.open(format=pyaudio.paInt16,
                               channels=1,
                               rate=self.samplerate,
                               input=True,
                               frames_per_buffer=self.frames_per_buffer)
    
    def record(self, frames, duration):
        samples = int(self.samplerate / self.frames_per_buffer * duration)
        for i in range(0, samples):
            data = self.stream.read(self.frames_per_buffer)
            frames.append(data)
        return frames
    
    def end_recorder(self):
        self.stream.stop_stream()
        self.stream.close()
        self.rec.terminate()
        

if __name__ == "__main__":
    from time import sleep
    from pyaudio import paInt16, get_sample_size
    import wave
    #probemos primero el ruido
    timestep = 1    #duración de los tonos en seg
    generator = ToneGenerator()
    generator.play_noise(timestep * 5)
    while generator.is_playing():
        print('Esto está andando')
        sleep(1)
    #bucleemos sobre tonos y hagamos algo más últil en el while
    freq_start = 200
    freq_end = 15000
    num_freqs = 10
    amplitude = 0.5
    frames = []
    recorder = Recorder()
    #frecuencias equiespaciadas en escala log
    logs = np.logspace(np.log10(freq_start), np.log10(freq_end), num_freqs)
    for freq in logs:
        print("Reproduciendo tono a {0:0.2f} Hz".format(freq))
        generator.play_sine(freq, timestep, amplitude)
        while generator.is_playing():
            frames = recorder.record(frames, 2)
    recorder.end_recorder()
    #y ahora guardemos lo grabado en un .wav
    wf = wave.open("outtest.wav", 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(get_sample_size(paInt16))
    wf.setframerate(48100)
    wf.writeframes(b''.join(frames))
    wf.close()
