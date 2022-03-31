import numpy as np
import pandas as pd

# Lifted from: https://towardsdatascience.com/pandas-equivalent-of-10-useful-sql-queries-f79428e60bd9 and a GREAT resource

# Reading the csv file into a DataFrame
df = pd.read_csv('USvideos.csv')

# SELECT col1, col2, ... FROM table
df[['video_id', 'title']]

# SELECT col1, col2, ... FROM table WHERE condition
df.loc[df['likes'] >= 1000000, ['video_id', 'title']]

# SELECT col1, col2, ... FROM table ORDER BY col1, col2 ASC|DESC
df.loc[df['likes'] >= 2000000, ['video_id', 'title'] ].sort_values(by=['title'], ascending=True).drop_duplicates()

# SELECT col1, col2, ... FROM table GROUP BY colN
df.loc[:, ['channel_title', 'views', 'likes', 'dislikes'] ].groupby(['channel_title']).sum()

# SELECT col1, col2, ... FROM table GROUP BY colN HAVING condition
g = df.groupby(['channel_title'])
g = g.filter(lambda x: x['video_id'].count() > 100)
g = g.loc[:, ['channel_title', 'views', 'likes', 'dislikes']]
g = g.groupby(['channel_title']).mean()

# INSERT INTO table (column1, column2, ...) VALUES (value1, value2, ...)
new_row = pd.DataFrame({'video_id': ['EkZGBdY0vlg'],
                        'channel_title': ['Professor Leonard'],
                        'title': ['Calculus 3 Lecture 13.3: Partial Derivatives']})
df = df.append(new_row, ignore_index=True)

# DELETE FROM table WHERE condition
df = df.drop(np.where(df['channel_title'] != '3Blue1Brown')[0])

# ALTER TABLE table ADD column
df['like_ratio'] = df['likes'] / (df['likes'] + df['dislikes'])

# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
df.loc[df['channel_title'] == 'Veritasium', ['title', 'likes']]

# SELECT *
# FROM df_titles
# INNER JOIN df_stats
# ON df_titles.video_id = df_stats.video_id;
df_titles = df.loc[:, ['video_id', 'title']].drop_duplicates()
df_stats = df.loc[:, ['video_id', 'views', 'likes', 'dislikes'] ].groupby('video_id').max()
# transform video_id from index to column
df_stats = df_stats.reset_index()
df_titles.join(df_stats.set_index('video_id'), on='video_id', how='inner')








