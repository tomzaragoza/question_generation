from pipelines import pipeline
import wikipedia

nlp = pipeline("question-generation")

topic = "Cricket World Cup"
summary = wikipedia.summary(topic)
summary = summary.replace("\n", "")

json_result = nlp(summary)
