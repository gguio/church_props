from transcript.py import get_large_audio_transcription_on_silence 
from clean_trs.py import get_cleaned_prop_text

if __name__ == '__main__':
    file = sys.argv[1]
    f = open(f'{file}_raw.txt', 'w')
    f.write(get_large_audio_transcription_on_silence(file))
    f.close()

    f = open(f'{file}.txt', 'w')
    f.write(get_cleaned_prop_text(f'{file}_raw.txt'))
    f.close()
