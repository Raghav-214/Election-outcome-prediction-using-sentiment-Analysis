import pandas as pd
import torch
from transformers import AutoModel, AutoTokenizer



# Load the dataset into a Pandas DataFrame
df = pd.read_csv("bjpprocess")
df1 = pd.read_csv("congprocess")


from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("ganeshkharad/gk-hinglish-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("ganeshkharad/gk-hinglish-sentiment")

# example sentence
# sentence = "tu pagal hai kya"
#
# # tokenize the sentence
# inputs = tokenizer(sentence, padding=True, truncation=True, return_tensors="pt")
#
# # make a prediction
# outputs = model(**inputs)
# predictions = outputs.logits.argmax(dim=-1)
#
# # print the predicted sentiment label
# if predictions == 0:
#     print("Negative")
# elif predictions == 1:
#     print("Neutral")
# else:
    #print("Positive")

def analyze_sentiment(row):
    text = row["headline"]
    encoding = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        output = model(**encoding)
    scores = output.logits.softmax(dim=1).tolist()[0]
    row["positive_score"] = scores[1]
    row["negative_score"] = scores[0]
    return row


# Apply the sentiment analysis function to the DataFrame
df = df.apply(analyze_sentiment, axis=1)
df1 = df1.apply(analyze_sentiment, axis=1)
# Print the results
#print(df)
df.to_csv('bjpabi')
df1.to_csv('congabi')

mean_negative = df["negative_score"].mean()
mean_positive = df["positive_score"].mean()


mean_negative1 = df1["negative_score"].mean()
mean_positive1 = df1["positive_score"].mean()

# print the overall sentiment scores
# print("Mean Negative Score bjp:", mean_negative)
# print("Mean Positive Score bjp:", mean_positive)
#
# print("Mean Negative Score cong:", mean_negative1)
# print("Mean Positive Score cong:", mean_positive1)


def predic_model_hinglish():
    if (mean_positive - mean_negative) > (mean_positive1 - mean_negative1):
        print("bjp wins acc to hinglish model")
    else:
        print("congress wins")