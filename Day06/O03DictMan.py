
players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}

print(f"players :{players}")
print("-" * 60)

print(f"sachin :{players['sachin']}")
print("-" * 60)

print(f"sachin :{sum(players['sachin'])}")
print("-" * 60)

scores = {k: sum(v) for k, v in players.items()}
print(f"scores :{scores}")
print("-" * 60)

# implement lambdas
scores = {k: (lambda scores: sum(scores) / len(scores))(v)
for k, v in players.items()}
print(f"scores :{scores}")
print("-" * 60)

def average_score(score):
    return sum(score) / len(score)

scores = {k: average_score(score) for k, score in players.items()}
print(scores)
print("-" * 60)

basic1 = [{x: (lambda par: "Mr." + par)("sachin {}".format(x))}
for x in range(1, 6)]
print(basic1)
print("-" * 60)

vals = {(lambda par: par * 10)(k): (lambda par: par * par)(v)
for k, v in {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}.items()}
print(vals)
print("-" * 60)


players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}

scores = [score for score in players.values()]
print(f"scores :{scores}")
print("-" * 60)

scores = [scr for score in players.values() for scr in score]
print(scores)
print("-" * 60)

scores = [scr for score in players.values() for scr in score if scr > 200]
print(scores)
print("-" * 60)

scores = {name : [scr for scr in score if scr > 200]
          for name,  score in players.items()}
print(scores)
