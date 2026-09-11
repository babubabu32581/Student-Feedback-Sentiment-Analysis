from utils.sentiment import analyze_sentiment
def test_positive(): assert analyze_sentiment("The teacher is excellent and helpful.")["label"]=="Positive"
def test_negative(): assert analyze_sentiment("The class is confusing and boring.")["label"]=="Negative"
def test_neutral(): assert analyze_sentiment("The course has lectures and assignments.")["label"]=="Neutral"
