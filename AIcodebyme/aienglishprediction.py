from aienglish import aienglish
import joblib
class aienglishprediction:
    def __init__(self):
        self.predictor=aienglish()
    def predict(self,text):
        text=[text]
        model_filename = "Checkingenglishmodel.joblib"
        vectorizer_filename = "vectorizerenglish.joblib"
        trained_model = joblib.load(model_filename)
        tfidf_vectorizer = joblib.load(vectorizer_filename)
        value=trained_model.predict(tfidf_vectorizer.transform(text))
        predicted_probabilities = trained_model.predict_proba(tfidf_vectorizer.transform(text))
        print(predicted_probabilities)
        print(value)
        return int(value[0])