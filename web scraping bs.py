from bs4 import BeautifulSoup
import requests
import praw
import pandas as pd
def indiatimes():
    url = 'https://timesofindia.indiatimes.com/politics/news'

    # send a request to the webpage and get its HTML content
    response = requests.get(url)
    html_content = response.content
    pr=[]

    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')
    # for headline in  soup.find_all('div',class_ ='container clearfix wrapper'):
    head = soup.find_all('span', class_='w_tle')
    for articles in head:
        # head = articles.find_all('a',{'class':'title'})
        headlines = articles.find('a')['title']
        pr.append(headlines)
    df = pd.DataFrame(pr,columns =['headlines'])
    print(df)
    df.to_csv('headlines_times.csv')

def news18_article():
    url = "https://www.news18.com/politics/"
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'lxml')
    links = []

    for news in soup.find_all('div', class_='jsx-3621759782 blog_list_row'):
        links.append(news.a['href'])
        for link in links:
            page = requests.get(link)
            bsop = BeautifulSoup(page.content, 'lxml')
            for new in bsop.find_all('div', class_='jsx-2637209261'):
                for para in new.find_all("p"):
                    a = para.get_text()
                    print(a)
            #print(new.text.strip())
def news18_headline():
    url = "https://www.news18.com/politics/"
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'lxml')
    data = []
    for headline in soup.find_all('div', class_='jsx-3621759782 blog_list_row'):
        # articles = headline.find_all('figcaption',class_='jsx-3621759782')
        for articles in headline.find_all('h4', class_='jsx-3621759782'):
            article = articles.text.strip()

            data.append(article)

        # for i
        # df = pd.DataFrame(data,columns=['headline'])
        # for i in range(len(df)):
        # print(data)
        # df.to_csv('headlines.csv')
        # print(article)
        # article = articles.get(text)

    df = pd.DataFrame(data, columns=['headline'])
    # print(article)
    print(df)
    df.to_csv('headlines_news18.csv')

#indiatimes()
#news18_headline()

def twitternews():
    import snscrape.modules.twitter as sntwitter
    val = input('type political party:' )
    scraper = sntwitter.TwitterSearchScraper(val)
    tweets = []
    for i, tweet in enumerate(scraper.get_items()):
        data = tweet.rawContent
        tweets.append(data)
        if i > 50:
            break
    # print(tweets)
    df = pd.DataFrame(tweets, columns=['tweets'])
    # print(df)
    df.to_csv('tweets.csv')

#twitternews()



def redditapi():
    reddit = praw.Reddit(
        client_id="DV1woBLefNGvd71XdYUaVw",
        client_secret="-Rh2pTvtq-w2rqCQOrVVuno1CgpkCQ",
        # redirect_uri="http://localhost:8080",
        user_agent="my user agent",

    )
    # print(reddit.auth.url(scopes=["identity"], state="...", duration="permanent"))
    # print(reddit.auth.authorize(code))
    subreddit = reddit.subreddit("india").hot(limit=300)
    # subr = reddit.subreddit("religion").hot(limit=100)
    list1 = []
    list2 = []
    list3 = ["bjp", "rahul gandhi", "congress", "Modi"]
    list4 = ['party']
    for submission in subreddit:
        subr1 = submission.title.lower()

        for question_phrase in list3:
            if question_phrase in subr1:
                # subr1 = subr1
                list1.append(subr1)
                for top_level_comment in submission.comments:
                    if hasattr(top_level_comment, 'body'):
                        comment = top_level_comment.body

                # print(user_comments)

                #list2.append(comment)

    '''for i in subr:
        subr2= i.title
        list2.append(subr2)
    for a in range(1,100):
        if (list1[a] == list2[a]):
            list3.append(list1[a])'''

    # print(list1)
    print("-----")

    # list2 = filter(lambda x: 'modi' , list2)

    # print(list(list2))

    # result = [element for element in list2 if element in list3]
    #print(result)
    # print(list2)

    df = pd.DataFrame(list1,columns=['reddit_posts'])
    df.to_csv('reddit2.csv')

#indiatimes()
#news18_headline()
#twitternews()
#redditapi()

'''from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
df1 = pd.read_csv('reddit.csv')
analyzer = SentimentIntensityAnalyzer()
positive =[]
negative =[]
a = analyzer.polarity_scores("what a good day")
print(a)
for n in range(df1.shape[0]):
    title = df1.iloc[n,1]
    title_analysed = analyzer.polarity_scores(title)
    negative.append((title_analysed['neg']))
    positive.append((title_analysed['pos']))
df1["Negative"] = negative
df1["Positive"] = positive
print(df1)
df1.to_csv("analysed.csv")'''