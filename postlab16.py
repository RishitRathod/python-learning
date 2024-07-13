import plotly 
import plotly.graph_objs as G
import numpy as np

num =100
x=np.random.randn(num)
y=np.random.randn(num)
print(x)
print(y)

#create a trace
follow = G.Scatter(
    x = x,
    y = y,
    mode = 'markers'
)
output = [follow]

plotly.offline.plot(output, filename='scatter.html')

img = G.Figure(data=G.Scatter(
    x = [10,20,30,40,50],
    y = [3,6,9,12,15],
    mode='markers',
    marker=dict(size=[10,20,30,40,50],
                color=[1,2,3,4,5])
))
img.show()