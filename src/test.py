import librosa
import numpy as np
import soundfile as sf

def down_sample(input_wav, origin_sr, resample_sr):
    y, sr = librosa.load(input_wav, sr=origin_sr)
    resample = librosa.resample(y, sr, resample_sr)
    print("original wav sr: {}, original wav shape: {}, resample wav sr: {}, resmaple shape: {}".format(origin_sr, y.shape, resample_sr, resample.shape))

    sf.write('./' + '16k.wav' , y, origin_sr, format='WAV', endian='LITTLE', subtype='PCM_16')

man_original_data = './ASR_exam.wav'
down_sample(man_original_data, 40000, 16000)