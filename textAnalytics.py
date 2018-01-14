from polyglot.text import Text as T

import indicoio
class Analyze():

    def __init__(self,text="",analyticsType="bylib"):
        self._text = text
        self._type = analyticsType

    def get_text_analyze(self):
        if self._type=="bylib":
             text = T(self._text)
             print("Text analyze by lib : {}".format(text.polarity))

            # analyze by word eg : Good : 1.0
            # for w in text.words:
            #     print("{:<16}{:>2}".format(w, w.polarity))
        else:
            indicoio.config.api_key = '799b2dbda4132e1553a94467eb0e890f'
            print("Text analyze by api: {}".format(indicoio.sentiment(self._text, language='ru')))
