import pandas as pd 

df = pd.read_csv('events.csv')

def clean(i):
    i = i.replace('https://dasreda.ru/learn/', '')
    if '/' in i:
        i = i[:i.index('/')]
    return i

df['URL_visited'] = df['URL_visited'].apply(clean)

print('Топ 3 популярные категории на сайте:\n' + 'Курсы. Кол-во посещений:', df['URL_visited'].value_counts()['courses'], '\n',
'Блог. Кол-во посещений:', df['URL_visited'].value_counts()['blog'], '\n',
'Видео. Кол-во посещений:', df['URL_visited'].value_counts()['video'])

# print(df['user_id'].value_counts())

print('Самый активный пользователь(id): 6101')
print('Кол-во его посещений:', df['user_id'].value_counts().max())

# Для более детального анализа нехватает данных о том, кто из пользователей учился на курсах и кто закончил, 
# информации о возрасте пользователей, их поле и увлечениях.