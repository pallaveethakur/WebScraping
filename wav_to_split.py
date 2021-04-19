# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 12:22:45 2021

@author: 
"""

import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import moviepy.editor as mp
from pydub import AudioSegment
from pydub.utils import make_chunks


def convert_audio(audio_path, target_path, remove=False):
    """This function sets the audio `audio_path` to:
        - 16000Hz Sampling rate
        - one audio channel ( mono )
            Params:
                audio_path (str): the path of audio wav file you want to convert
                target_path (str): target path to save your new converted wav file
                remove (bool): whether to remove the old file after converting
        Note that this function requires ffmpeg installed in your system."""

    os.system(f"ffmpeg -i {audio_path} -ac 1 -ar 16000 {target_path}")
    # os.system(f"ffmpeg -i {audio_path} -ac 1 {target_path}")
    if remove:
        os.remove(audio_path)    
    
def split(audio):
    myaudio = AudioSegment.from_file(audio, "wav") 
#     chunk_length_ms = 10000 # pydub calculates in millisec
    chunks = make_chunks(myaudio, 30000) #Make chunks of one sec
    name=audio.split('_')[0].split('\\')[-1]
    #Export all of the individual chunks as wav files

    for i, chunk in enumerate(chunks):
        chunk_name = name+"_{0}.wav".format(i)
        print(chunk_name)
#         print("exporting", chunk_name)
        chunk.export('./Techno'+'//'+chunk_name, format="wav")
        
    
def convert(name,dir,start,end):

    audio_path = dir
    target_path = name+"_convert"   
    if os.path.isfile(audio_path) and audio_path.endswith(".wav"):
        if not target_path.endswith(".wav"):
            target_path += ".wav"
        convert_audio(audio_path, target_path, remove=False)  
    else:
        raise TypeError("The audio_path file you specified isn't appropriate for this operation")
    split(target_path)
    return 

if __name__ == "__main__":
    convert('Techno1',r"C:\Users\shree\Desktop\data\techno.wav", 0, 254)
    #split(r"C:\Users\nilof\Pictures\rock1_convert.wav")    