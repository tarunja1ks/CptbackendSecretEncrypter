import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

class aienglish:
    def __init__(self): # this function just reads in the dataset

       self. df = pd.read_csv('AIcodebyme/datatrainisenglish.csv')
    
    def preprocess(self): # this perfroms basic preprocessing of the text data including splitting it into testing/training cateogories, and also converting the text into numbers for the model with TfidfVectorizer()

        self.X = self.df['Text']
        self.y = self.df['IsEnc']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        self.tfidf_vectorizer = TfidfVectorizer()
        self.X_train_tfidf = self.tfidf_vectorizer.fit_transform(self.X_train)
        self.X_test_tfidf = self.tfidf_vectorizer.transform(self.X_test)
    def train(self): #Training the model with LogisticRegression and outputting score reports for the model on testing data
        self.model = LogisticRegression()
        self.model.fit(self.X_train_tfidf, self.y_train)
        y_pred =self.model.predict(self.X_test_tfidf)
        accuracy = accuracy_score(self.y_test, y_pred)
        report = classification_report(self.y_test, y_pred)
        print("Accuracy:", accuracy)
    def export(self): # exporting the models of the training for quick use in the future
        joblib.dump(self.model, "Checkingenglishmodel.joblib")
        joblib.dump(self.tfidf_vectorizer, "vectorizerenglish.joblib")

