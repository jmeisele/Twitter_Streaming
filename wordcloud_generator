import pandas as pd
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


#Create the dataframe from the json file
df = pd.read_json(path_or_buf = 'tweets.json', lines = True)

#Extract only the text column
text = df['text']

#Create a single string from all text
words = ' '.join(text)

#Words to ignore
ignored_words =['http','RT','the','CO','and','to','https']

#Generate an instance of WordCloud
wordcloud = WordCloud(stopwords = ignored_words)
wordcloud.generate(text = words)

#Plot the wordcloud
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
