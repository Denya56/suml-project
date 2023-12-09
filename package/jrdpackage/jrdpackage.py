def clean_data(data, re_letters):
    data['text'] = data['text'].apply(lambda x: x.lower())
    data['text'] = data['text'].apply(lambda x: re_letters.sub('', x))


def remove_stopwords(text):
    return ' '.join(filter(lambda x: x not in nlp.Defaults.stop_words, text.split()))


def lemmatize(text):
    return ' '.join([x.lemma_ for x in nlp(text)])


def build_wordcloud(data, label_type, max_words, c_width, c_height):
    text = ' '.join(data['text'][data['label'] == label_type])
    wc = WordCloud(max_words=max_words, width=c_width, height=c_height, collocations=False).generate(text)
    return wc.to_image()
    
y = 5
