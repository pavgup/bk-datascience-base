import numpy as np
import pandas as pd

# Heavily modified from: https://towardsdatascience.com/pandas-equivalent-of-10-useful-sql-queries-f79428e60bd9 and also a GREAT resource

# Reading the csv file into a DataFrame
df = pd.read_csv('USvideos.csv')
print("#######################################")
print("# Reading the csv file into a DataFrame")
print("#######################################")
print(df)
print('\n\n\n\n\n')

# SELECT col1, col2, ... FROM table
selectResult = df[['video_id', 'title']]
print("###################################")
print("# SELECT col1, col2, ... FROM table")
print("###################################")
print(selectResult)
print('\n\n\n\n\n')

# SELECT col1, col2, ... FROM table WHERE condition
selectResultWhere = df.loc[df['likes'] >= 1000000, ['video_id', 'title']]
print("###################################################")
print("# SELECT col1, col2, ... FROM table WHERE condition")
print("###################################################")
print(selectResultWhere)
print('\n\n\n\n\n')

# SELECT col1, col2, ... FROM table ORDER BY col1, col2 ASC|DESC
selectResultOrderBy = df.loc[df['likes'] >= 2000000, ['video_id', 'title'] ].sort_values(by=['title'], ascending=True).drop_duplicates()
print("################################################################")
print("# SELECT col1, col2, ... FROM table ORDER BY col1, col2 ASC|DESC")
print("################################################################")
print(selectResultOrderBy)
print('\n\n\n\n\n')

# SELECT col1, col2, ... FROM table GROUP BY colN
df.loc[:, ['channel_title', 'views', 'likes', 'dislikes'] ].groupby(['channel_title']).sum()
print("#################################################")
print("# SELECT col1, col2, ... FROM table GROUP BY colN")
print("#################################################")
print(df.loc[:, ['channel_title', 'views', 'likes', 'dislikes'] ].groupby(['channel_title']).sum())
print('\n\n\n\n\n')

# SELECT col1, col2, ... FROM table GROUP BY colN HAVING condition
g = df.groupby(['channel_title'])
g = g.filter(lambda x: x['video_id'].count() > 100)
g = g.loc[:, ['channel_title', 'views', 'likes', 'dislikes']]
groupByFinalResult = g.groupby(['channel_title']).mean()
print("#################################################X#################")
print("# SELECT col1, col2, ... FROM table GROUP BY colN HAVING condition")
print("##################################################################")
print(groupByFinalResult)
print('\n\n\n\n\n')

# INSERT INTO table (column1, column2, ...) VALUES (value1, value2, ...)
new_row = pd.DataFrame({'video_id': ['EkZGBdY0vlg'],
                        'channel_title': ['Professor Leonard'],
                        'title': ['Calculus 3 Lecture 13.3: Partial Derivatives']})
dfInsertResult = pd.concat([df, new_row], ignore_index=True,  axis = 0)
print("#################################################X######################")
print("# INSERT INTO table (column1, column2, ...) VALUES (value1, value2, ...)")
print("########################################################################")
print(dfInsertResult)
print('\n\n\n\n\n')

# DELETE FROM table WHERE condition
dfDeleted = df.drop(np.where(df['channel_title'] != '3Blue1Brown')[0])
print("###################################")
print("# DELETE FROM table WHERE condition")
print("###################################")
print(dfDeleted)
print('\n\n\n\n\n')

# ALTER TABLE table ADD column
df['like_ratio'] = df['likes'] / (df['likes'] + df['dislikes'])
print("##############################")
print("# ALTER TABLE table ADD column")
print("##############################")
print(df)
print('\n\n\n\n\n')

# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;
df.loc[df['channel_title'] == 'Veritasium', ['title', 'likes']]
print("#############################################")
print("# UPDATE table_name")
print("# SET column1 = value1, column2 = value2, ...")
print("# WHERE condition;")
print("#############################################")
print(df)
print('\n\n\n\n\n')


# SELECT *
# FROM df_titles
# INNER JOIN df_stats
# ON df_titles.video_id = df_stats.video_id;
df_titles = df.loc[:, ['video_id', 'title']].drop_duplicates()
df_stats = df.loc[:, ['video_id', 'views', 'likes', 'dislikes'] ].groupby('video_id').max()
# transform video_id from index to column
df_stats = df_stats.reset_index()
finalJoin = df_titles.join(df_stats.set_index('video_id'), on='video_id', how='inner')

print("############################################")
print("# SELECT *")
print("# FROM df_titles")
print("# INNER JOIN df_stats")
print("# ON df_titles.video_id = df_stats.video_id;")
print("############################################")
print(finalJoin)
print('\n\n\n\n\n')

print("##############################################")
print("Contact Pavan Gupta and Lu Chen for more help!")
print("##############################################")
