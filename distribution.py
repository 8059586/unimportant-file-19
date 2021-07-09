import plotly.figure_factory as ff
import random

result = []
for i in range(0,100):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    result.append(d1+d2)

fig = ff.create_distplot([result],["Result"])
fig.show()