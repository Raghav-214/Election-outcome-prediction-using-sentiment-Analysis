import pandas as pd
df = pd.read_csv('headlines_news18.csv')
df['headline'] = df['headline'].str.replace('|', '')
#print(df.head())
#df.to_csv('headline_filter')
df1 = pd.read_csv('headline_filter')
df1 = df1.applymap(lambda s: s.lower() if type(s) == str else s)
#print(df1.head())
list =['bjp','modi']
list1 = ['congress','gandhi']
list2 =[]
list3 =[]
#names = df1['headline'].tolist()
filter = '|'.join(list1) #list of keywords joined by or filter
filter1 = '|'.join(list)
df_cong18 = df1[df1['headline'].str.contains(filter)]
#print(df_cong18.head())
df_bjp18 = df1[df1['headline'].str.contains(filter1)]
#print(df_bjp18.head())

#print(names)
#print(article)


#print(df.head())
#print(list2)
df2 = pd.read_csv('headlines_times.csv')
df2 = df2.applymap(lambda s: s.lower() if type(s)==str else s)
filter = '|'.join(list1) #list of keywords joined by or filter
filter1 = '|'.join(list)
df_congtimes = df2[df2['headlines'].str.contains(filter)]
#print(df_congtimes.head())
df_bjptimes = df2[df2['headlines'].str.contains(filter1)]
#print(df_bjptimes.head())

df3 = pd.read_csv('reddit.csv')
df4 = pd.read_csv('reddit1.csv')
df5 = pd.read_csv('reddit2.csv')

df6 = pd.concat([df3['reddit_posts'],df4['reddit_posts'],df5['reddit_posts']],ignore_index=True).drop_duplicates()

#df6.to_csv('redditfinal.csv')
#print(df6.head())
df7 = pd.read_csv('redditfinal.csv')

filter = '|'.join(list1) #list of keywords joined by or filter
filter1 = '|'.join(list)
df_congreddit = df7[df7['reddit_posts'].str.contains(filter)]
#print(df_congreddit.head())
df_bjpreddit = df7[df7['reddit_posts'].str.contains(filter1)]
#print(df_bjpreddit.head())

df8 = pd.read_csv('RahulGandhi_data.csv')
df8 = df8.iloc[2:95,2:3]
#df8['Tweet'] = df8['Tweet'].str.replace('@', '')
mask = df8['Tweet'].str.contains('https')
print(type(mask))
#df8 = df8[~mask]
#print(df8.head())
#df8.to_csv('congtwitter')

df9 = pd.read_csv('bjp.csv')
df9 = df9.iloc[2:250,2:3]
#df9['Tweet'] = df9['Tweet'].str.replace('@', '') #replacing @ with emptyspace
mask = df9['Tweet'].str.contains('https') #droping columns containg https with ~
#df9 = df9[~mask]
#print(df9.head())
#df9.to_csv('bjptwitter')

df_congfinal = pd.concat([df_cong18['headline'],df_congtimes['headlines'],df_congreddit['reddit_posts'],df8['Tweet']],ignore_index=True)
#df_congfinal.to_csv('congfinal1')

df_bjpfinal = pd.concat([df_bjp18['headline'],df_bjptimes['headlines'],df_bjpreddit['reddit_posts'],df9['Tweet']],ignore_index=True)
df_bjpfinal.to_csv('bjpfinal1')