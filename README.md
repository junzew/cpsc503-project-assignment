# CPSC 503 Speech Synthesis Assignment

# Set up

Clone this repository with `git clone`.

Install python3 and pip3.

Install the required packages by running:

`pip3 install -r requirements.txt`

Install [ffmpeg](https://ffmpeg.org/)

Unzip two databases of audio files
* 1000words.zip: 1000 basic English words from Longman dictionary
* phonemes.zip: pre-recorded phonemes, indexed with phone_mapping.py

# Overview
You will implement a simplified version of concatenative synthesizer using two strategies:
* Word selection: select available words directly from database and concatenate them
* Phoneme selection: convert words to phonemes using the CMU Pronunciation Dictionary (cmudict package in python) and then generate speech from the phonemes. If a word is not present in the cmudict, use g2p package to obtain its phonemic representation.

# Usage
```
python3 synthesizer.py -h
usage: synthesizer.py [-h] (-w | -p)

optional arguments:
  -h, --help  show this help message and exit
  -w          word synthesis
  -p          phoneme synthesis
```

# Specific Task
* Implement the two functions `word_synthesize` and `phone_synthesize` in the `synthesizer.py` by completing the TODOs
* Make sure your code is easy to read and well-commented

# Useful resources
* cmudict: https://pypi.org/project/cmudict/ 
* g2p: https://github.com/Kyubyong/g2p
* pydub: https://github.com/jiaaro/pydub

# References
* List of 1000 Basic English Words: https://en.wiktionary.org/wiki/Appendix:1000_basic_English_words
* Audio files of 1000 Basic English words scraped from Longman online dictionary https://www.ldoceonline.com using scrape.py
* Phoneme recordings from https://github.com/stephengrice/synth-me

# Link to lecture recording
* https://youtu.be/sMWv5S678kA
