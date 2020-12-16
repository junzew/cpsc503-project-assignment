from pydub import AudioSegment
from pydub.playback import play
import cmudict
import os
import argparse
from g2p_en import G2p

from phone_mapping import phone_map

DST_DIR = "waveforms/"
WORDS_DIR = "words/"
PHONEMES_DIR = "phonemes/"

class TextToSpeech:
    """A simple speech synthesizer based on concatenation"""

    def __init__(self):
        # ensure DST_DIR exists
        if not os.path.exists(DST_DIR):
            os.makedirs(DST_DIR)

    def word_synthesize(self, text):
        """
        Synthesize speech from text by concatenating words
        selected from the database
        """
        #TODO Concatenate words selected from WORDS_DIR
        #TODO Write the synthesized .wav file to DST_DIR
        pass

    def phone_synthesize(self, text):
        """
        Synthesize speech from text by concatenating phonemes
        selected from the database
        """
        #TODO Use cmudict get phonemic representation
        #TODO If word not found, use g2p instead
        #TODO Concatenate phonems selected from PHONEMES_DIR
        #TODO Write the synthesized .wav file to DST_DIR
        pass

    def word_synthesize_solution(self, text):
        """
        Synthesize speech from text by concatenating words
        selected from the database
        """
        # Convert all words to lower case
        words = [word.lower() for word in text.split()]
        # Initialize an empty audio segment
        result = AudioSegment.empty()
        for word in words:
            path = WORDS_DIR + word + ".mp3"
            try:
                # Concatenate words selected from WORDS_DIR
                audio = AudioSegment.from_mp3(path)
                result += audio
            except Exception as e:
                print(e)
        # Write the synthesized .wav file to DST_DIR
        result.export(DST_DIR + "gen.wav", format="wav")
        play(result)

    def phone_synthesize_solution(self, text):
        """
        Synthesize speech from text by concatenating phonemes
        selected from the database
        """
        # Convert all words to lower case
        words = [word.lower() for word in text.split()]
        phones = []
        for word in words:
            try:
                # Use cmudict get phonemic representation
                phones.extend(cmudict.dict()[word][0])
            except IndexError:
                # If word not found in dictionary, use g2p instead
                g2p = G2p()
                phones.extend(g2p(word))
        print(phones)

        # Initialize an empty audio segment
        result = AudioSegment.empty()
        # Concatenate phonems selected from PHONEMES_DIR
        for phone in phones:
            # Ignore accent marker
            phone = phone[0:-1] if phone[-1].isdigit() else phone
            # Look up phoneme wav file using phone_map
            sound_label = phone_map[phone]
            sound_path = PHONEMES_DIR + str(sound_label) + ".wav"
            audio = AudioSegment.from_wav(sound_path)
            result += audio
        # Write the synthesized .wav file to DST_DIR
        result.export(DST_DIR + "gen.wav", format="wav")
        play(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-w', help='word synthesis', action="store_true")
    group.add_argument('-p', help='phoneme synthesis', action="store_true")
    args = parser.parse_args()
    tts = TextToSpeech()
    while True:
        text = input("> ")
        if args.w:
            tts.word_synthesize_solution(text)
        elif args.p:
            tts.phone_synthesize_solution(text)
