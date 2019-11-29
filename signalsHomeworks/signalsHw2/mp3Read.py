from pydub import AudioSegment

def convert(srcfile, destfile):
    signal = AudioSegment.from_mp3(srcfile)
    signal.export(destfile, format = "wav")