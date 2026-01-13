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


# Module-level analyzer and compatibility wrapper
_analyzer = MoodAnalyzer()

def analyze_sentiment(text: str):
    """Compatibility wrapper: returns a dict with `label` and `score` keys
    to match older code that imports `analyze_sentiment`.
    """
    res = _analyzer.analyze(text)
    return {"label": res["emotion"], "score": res["confidence"]}
