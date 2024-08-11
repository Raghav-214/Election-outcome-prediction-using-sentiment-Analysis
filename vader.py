from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax
import pandas as pd
import torch
from transformers import AutoModel, AutoTokenizer


roberta = "cardiffnlp/twitter-roberta-base-sentiment"


model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)
max_length = tokenizer.model_max_length
labels = ['Negative','Neutral','Positive']
def preprocessing_cong():
    tweet_words = []
    tweet_char = []
    df = pd.read_csv('congfinal1')
    tweet_words = df.values.tolist()
    my_1d_list = [item for sublist in tweet_words for item in sublist]
    new_list = [item for item in my_1d_list if not isinstance(item, int)]
    # print(my_1d_list)

    processed_list_cong = []

    for string in new_list:
        word_list = string.split(' ')
        processed_words = []
        for word in word_list:
            if word.startswith('@') and len(word) > 1:
                word = '@user'
            elif word.startswith('http'):
                word = "http"
            elif word.startswith('https'):
                word = 'https'
            processed_words.append(word)
        processed_string = ' '.join(processed_words)

        processed_list_cong.append(processed_string)
    #print(processed_list_cong)
    return processed_list_cong




def bjp_preprocessing():
    tweet_words = []
    tweet_char = []
    df = pd.read_csv('bjpfinal1')
    tweet_words = df.values.tolist()
    #print(tweet_words)
    my_1d_list = [item for sublist in tweet_words for item in sublist]
    new_list = [item for item in my_1d_list if not isinstance(item, int)]
    # print(my_1d_list)

    processed_list_bjp = []

    for string in new_list:
        word_list = string.split(' ')
        processed_words = []
        for word in word_list:
            if word.startswith('@') and len(word) > 1:
                word = '@user'
            elif word.startswith('http'):
                word = "http"
            elif word.startswith('https'):
                word ='https'
            processed_words.append(word)
        processed_string = ' '.join(processed_words)
        processed_list_bjp.append(processed_string)
    #print(processed_list_bjp)
    return processed_list_bjp


processed_list_bjp = bjp_preprocessing()
processed_list_cong = preprocessing_cong()


df5 = pd.DataFrame(processed_list_bjp,columns=['headline'])
df5.to_csv('bjpprocess')
df6 = pd.DataFrame(processed_list_cong,columns=['headline'])
df6.to_csv('congprocess')
#print(df5)
#print(df5.isnull().sum())

#print(tweet_proc_cong)
#print(tweet_proc_bjp)



from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
positive =[]
negative =[]

#print(a)
for n in range(df5.shape[0]):
    title = df5.iloc[n,0]
    title_analysed = analyzer.polarity_scores(title)
    negative.append((title_analysed['neg']))
    positive.append((title_analysed['pos']))
df5["Negative"] = negative
df5["Positive"] = positive
# print(df5)
#df5.to_csv("analysedbjp.csv")
mean_negative = df5["Negative"].mean()
mean_positive = df5["Positive"].mean()

# print the overall sentiment scores
# print("Mean Negative Score bjp:", mean_negative)
# print("Mean Positive Score bjp:", mean_positive)

# classify the overall sentiment as positive, negative, or neutral based on the average scores
# if mean_positive > mean_negative:
#     print("Overall Sentiment: Positive")
#
# elif mean_positive < mean_negative:
#     print("Overall Sentiment: Negative")
# else:
#     print("Overall Sentiment: Neutral")


positive1 =[]
negative1=[]
for n in range(df6.shape[0]):
    title1 = df6.iloc[n,0]
    title_analysed1 = analyzer.polarity_scores(title1)
    negative1.append((title_analysed1['neg']))
    positive1.append((title_analysed1['pos']))
df6["Negative"] = negative1
df6["Positive"] = positive1

#df6.to_csv("analysedcong.csv")
mean_negative1 = df6["Negative"].mean()
mean_positive1 = df6["Positive"].mean()

# print the overall sentiment scores
# print("Mean Negative Score cong:", mean_negative1)
# print("Mean Positive Score cong:", mean_positive1)

# classify the overall sentiment as positive, negative, or neutral based on the average scores
# if mean_positive1 > mean_negative1:
#     print("Overall Sentiment: Positive")
# elif mean_positive1 < mean_negative1:
#     print("Overall Sentiment: Negative")
# else:
#     print("Overall Sentiment: Neutral")

def pred_model_vader():
    if (mean_positive - mean_negative) > (mean_positive1 - mean_negative1):
        print("bjp wins acc to vader model")
    else:
        print("congress wins")