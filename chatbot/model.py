from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import json

class ChatbotModel:
    def __init__(self, data_path="data/intents.json"):
        with open(data_path, "r") as f:
            self.intents = json.load(f)

        phrases, labels = [], []
        for intent, examples in self.intents.items():
            for ex in examples:
                phrases.append(ex)
                labels.append(intent)

        self.vectorizer = CountVectorizer()
        X = self.vectorizer.fit_transform(phrases)
        self.model = MultinomialNB()
        self.model.fit(X, labels)

    def predict(self, text):
        X_test = self.vectorizer.transform([text])
        return self.model.predict(X_test)[0]
