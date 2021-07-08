import wikipedia
topic = "Cricket World Cup"
summary = wikipedia.summary(topic)
summary = summary.replace("\n", "")
print(summary)
