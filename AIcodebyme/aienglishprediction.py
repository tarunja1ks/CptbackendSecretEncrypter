from AIcodebyme.aienglish import aienglish
import joblib
class aienglishprediction:
    def __init__(self): # making an object of aienglish.py
        self.predictor=aienglish()
    def predict(self,text): # this just loads in the file and uses the model to predict quickly rather than retraining every time for prediction
        text=[text]
        model_filename = "Checkingenglishmodel.joblib"
        vectorizer_filename = "vectorizerenglish.joblib"
        trained_model = joblib.load(model_filename)
        tfidf_vectorizer = joblib.load(vectorizer_filename)
        value=trained_model.predict(tfidf_vectorizer.transform(text))
        predicted_probabilities = trained_model.predict_proba(tfidf_vectorizer.transform(text))
        return float(predicted_probabilities[0][0])
aithing=aienglishprediction()
print(aithing.predict("i love to eat food"))