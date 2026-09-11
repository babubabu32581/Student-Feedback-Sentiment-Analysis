import re
POSITIVE={"excellent","great","good","helpful","clear","clearly","easy","amazing","interesting","enjoy","enjoyed","love","liked","useful","friendly","supportive","understand","understood","effective","best","positive","improved","impressive","well","awesome","satisfied","engaging"}
NEGATIVE={"bad","poor","difficult","hard","confusing","confused","boring","hate","dislike","slow","unclear","unhelpful","problem","problems","worst","negative","stress","stressed","late","lack","lacking","weak","complicated","unsatisfied","disappointed","disappointing"}
NEGATIONS={"not","no","never","hardly","isn't","wasn't","don't","didn't","can't"}

def tokenize(text): return re.findall(r"[a-zA-Z']+",text.lower())

def analyze_sentiment(text):
    t=tokenize(text); pos=neg=0
    for i,w in enumerate(t):
        negated=any(x in NEGATIONS for x in t[max(0,i-3):i])
        if w in POSITIVE: neg+=1 if negated else 0; pos+=0 if negated else 1
        elif w in NEGATIVE: pos+=1 if negated else 0; neg+=0 if negated else 1
    score=(pos-neg)/max(pos+neg,1)
    label="Positive" if score>0.15 else "Negative" if score<-0.15 else "Neutral"
    confidence=min(99,50+abs(score)*45) if pos+neg else 50
    explanation={"Positive":"More positive signals were detected.","Negative":"More negative signals were detected.","Neutral":"Positive and negative signals are balanced or limited."}[label]
    keywords=list(dict.fromkeys([w for w in t if w in POSITIVE or w in NEGATIVE]))
    return {"label":label,"score":round(score,2),"confidence":round(confidence,1),"explanation":explanation,"keywords":keywords}
