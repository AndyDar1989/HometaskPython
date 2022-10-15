# 5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого)
from random import choice, randrange
from itertools import repeat
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра",
           "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# in  10 True
# out  ['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 'автомобиль сегодня веселый', 'город позавчера утопичный']


def joke_generator(count: int, nouns, adj, adv: list):
    new_list = []
    min_size = min(nouns, adj, adv)
    for i in range(len(min_size)):
        n = randrange(len(min_size))
        new_list.append(f"{nouns.pop(n)} {adj.pop(n)} {adv.pop(n)}" if repeat else
                        f'{choice(nouns)} {choice(adj)} {choice(adv)}')
    return new_list


print(joke_generator(5, nouns, adjectives, adverbs))
