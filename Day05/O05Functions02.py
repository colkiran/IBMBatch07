
from collections import namedtuple

def results():
    phy = 83
    maths = 90
    che = 95
    bio = 97
    nmdTpl = namedtuple("Marks", "p m c b")
    mks = nmdTpl(p = phy, m = maths, c = che, b = bio)
    return mks

marks = results()
print(marks)
print(f"Physics   :{marks.p}")
print(f"Maths     :{marks.m}")
print(f"Chemistry :{marks.c}")
print(f"Biology   :{marks.b}")

# marks.p = 100

# immutable dictionary =