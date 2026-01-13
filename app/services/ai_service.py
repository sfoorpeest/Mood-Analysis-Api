from transformers import pipeline

class MoodAnalyzer:
    def __init__(self):
        self.classifier = None

    def load_model(self):
        if self.classifier is None:
            self.classifier = pipeline(
                "sentiment-analysis",
                model="distilbert-base-uncased-finetuned-sst-2-english"
            )

    def analyze(self, text: str):
        self.load_model()
        result = self.classifier(text)[0]
        return {
            "emotion": result["label"].lower(),
            "confidence": result["score"]
        }
