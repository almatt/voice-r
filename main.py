import textAnalytics as tA
import pyAudioAnalysis as pAA
from pyAudioAnalysis.emotion import Emotion

def get_word_count(string=""):
    print("Word count : {}".format(len(string.split())))

#text analyze
analyze = tA.Analyze(text="лучше", analyticsType="bylib")
analyze.get_text_analyze()

#emotion analyze
emotion = Emotion(analyzeType="svm", pathFile="pyAudioAnalysis/data/dialog.wav",
                  pathModel = "pyAudioAnalysis/data/svmSpeechEmotion")
emotion.get_emotion()

get_word_count("дратути")
