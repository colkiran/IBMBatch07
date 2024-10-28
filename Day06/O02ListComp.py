
fruits = [
    ('apple',  385),
    ('grapes', 250),
    ('orange', 120),
    ('pineapple', 75),
    ('gauva', 110),
    ('watermelon', 60),
    ('banana', 55),
    ('pears', 210)
]

print(f"fruits :{fruits}")
print("-" * 60)

price = ["fruit" for friut in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit for fruit in fruits]
print(price)
print("-" * 60)

price = [fruit[0] for fruit in fruits]
print(price)
print("-" * 60)

price = [fruit[1] for fruit in fruits]
print(price)
print("-" * 60)

price = [fruit[1] * 0.9 for fruit in fruits]
print(price)
print("-" * 60)

price = [fruit[1] * 0.75 for fruit in fruits]
print(price)
print("-" * 60)

exp_items = [fruit[1] for fruit in fruits if fruit[1] > 100]
print(exp_items)
print("-" * 60)

exp_items = [[fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75]
             for fruit in fruits if fruit[1] > 100]
print(exp_items)

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(sentence)
print("-" * 60)

words = [word for word in sentence.split()]
print(words)
print("-" * 60)

words = [(word, len(word)) for word in sentence.split()]
print(words)
print("-" * 60)

words = [(word, len(word)) for word in sentence.split() if len(word) <= 4]
print(words)
print("-" * 60)

squares  = [i ** 2 for i in range(1, 11)]
print(squares)
print("-" * 60)


boys = ['James', 'Jack', "Mike", 'Ben', 'Kevin', 'Peter']
girls = ['Tina', 'Mary', 'alisha', 'Emma', 'Olivia', 'Ellie']

combine = [(boy, girl) for boy in boys for girl in girls]
print(combine)
