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

df = pd.read_csv('bjpprocess')
df1 =pd.read_csv('congprocess')
proc_bjp =''.join(df['headline'])
proc_cong =''.join(df1['headline'])
#print(proc_bjp)

encoded_tweet = tokenizer(proc_bjp,max_length=128, padding="max_length", truncation=True, return_tensors='pt')
output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])
output = model(**encoded_tweet)
#print(output)
scores = output[0][0].detach().numpy()
scores = softmax(scores)
#print(scores[2])

encoded_tweet1 = tokenizer(proc_cong,max_length=128, padding="max_length", truncation=True, return_tensors='pt')
output1 = model(encoded_tweet1['input_ids'], encoded_tweet['attention_mask'])
output1 = model(**encoded_tweet1)
#print(output)
scores1 = output1[0][0].detach().numpy()
scores1 = softmax(scores1)

def pred_model_roberta():
    #adding neutral in positive too cuz too much neutral
    if (scores[1] + scores[2] - scores[0] < scores1[1] + scores1[2] - scores1[0]):
        print("bjp wins acc to roberta")
    else:
        print("cong wins acc to roberta")

for i in range(len(scores)):
    l = labels[i]
    s = scores[i]
    #print(l, s)
#pred_model_roberta()