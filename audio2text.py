import speech_recognition as sr
import spacy
from datetime import datetime as dt

AUDIO_FILE = './flightsearch.wav'

def audio2text(audiofile):
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


#audiotext = audio2text(AUDIO_FILE)
audiotext = "I am looking for flight from Singapore to Beijing on November 1st 2019 and returning on November 5th 2019 for 2 adults and 2 children Age 3 and 10"

# run the following line before running the rest of the code
# python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")
doc = nlp(audiotext)

city = []
dates = []
adult = 0
child_age = []
for noun_chunk in doc.noun_chunks:
    if 'adult' in noun_chunk.lemma_:
        adult = int(noun_chunk.ents[0].text)
    if 'child' in noun_chunk.lemma_:
        num_child = int(noun_chunk.ents[0].text)


for ent in doc.ents:
    #print('text: ',ent.text)
    if ent.label_ == 'GPE':
        city.append(ent.text)
    elif ent.label_ == 'DATE':
        raw_date = (ent.text).split(" ")
        if len(raw_date) == 3:
            dateday = (((raw_date[1].replace('st','')).replace('nd','')).replace('rd','')).replace('th','')
            datemonth = raw_date[0]
            dateyear = raw_date[2]
            final_date = dt.strptime(dateday+" "+datemonth+" "+dateyear,'%d %B %Y')
            dates.append(final_date.strftime('%d/%m/%Y'))

num_list = []
for token in doc:
    if token.pos_ == 'NUM':
        num_list.append(token.text)
for i in range(num_child):
    child_age.append(num_list[-i-1])

#print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,token.shape_, token.is_alpha, token.is_stop)


print('city: ',city)
print('dates: ',dates)
print('adult: ',adult)
print('children: ',child_age)