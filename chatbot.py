import aiml
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Initialize AIML Kernel and load AIML file
kernel = aiml.Kernel()
kernel.learn("aiml.xml")

# NLP Setup
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return set(synonyms)

def get_antonyms(word):
    antonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
    return set(antonyms)

training_data = [
    ("Tell me a joke", "humor"),
    ("What's the weather like?", "weather"),
    # Add more training examples for different categories
]

X_train = [data[0] for data in training_data]
y_train = [data[1] for data in training_data]

classifier = make_pipeline(TfidfVectorizer(), MultinomialNB())
classifier.fit(X_train, y_train)

def chatbot_response(user_input):
    aiml_response = kernel.respond(user_input)

    tokens = word_tokenize(user_input)
    pos_tags = pos_tag(tokens)


    ml_response = classifier.predict([user_input])[0]

    final_response = aiml_response + " " + ml_response
    return final_response

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chatbot_response(user_input)
    print("ChatBot:", response)
