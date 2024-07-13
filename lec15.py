#lab15
import plotly 
import plotly.graph_objs as G
import numpy as np

# #task 1
# num =100
# x=np.random.randn(num)
# y=np.random.randn(num)
# print(x)
# print(y)
# #create a trace
# follow = G.Scatter(
#     x = x,
#     y = y,
#     mode = 'markers'
# )
# output = [follow]
# plotly.offline.plot(output, filename='scatter.html')


# #task 2 to represent the data using combination of lines and scatter plot
# N=20
# x=np.linspace(0,1,N)
# one_y=np.random.randn(N)+10
# two_y=np.random.randn(N)
# three_y=np.random.randn(N)-10
# #create trace
# plot0=G.Scatter(
#     x=x,
#     y=one_y,
#     mode='markers'
# )
# plot1=G.Scatter(
#     x=x,
#     y=two_y,
#     mode = 'lines+markers'
# )
# plot2=G.Scatter(
#     x=x,
#     y=three_y,
#     mode = 'lines'
# )
# output=[plot0,plot1,plot2]
# plotly.offline.plot(output, filename='line_scatterinf_fashion.html')


# #task 3 bubble scatter plot
# img = G.Figure(data=G.Scatter(
#     x = [10,20,30,40,50],
#     y = [3,6,9,12,15],
#     mode='markers',
#     marker=dict(size=[10,20,30,40,50],
#                 color=[1,2,3,4,5])
# ))
# img.show()


# #task 4 box plot
# a=np.random.randn(100)-10
# b=np.random.randn(100)+10
# output=G.Figure()
# output.add_trace(G.Box(y=a))
# output.add_trace(G.Box(y=b))
# output.show()


# #task 5 histogram
# x=np.random.randn(100)
# output=G.Figure(data=(G.Histogram(x=x)))
# output.show()




































































































































































































