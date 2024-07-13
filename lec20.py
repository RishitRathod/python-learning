import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sg

# # Task 1:  Sine wave
freq = 2
amp = 2
t = np.linspace(0,2,1000)
# sig_sine = amp*np.sin(2*np.pi*freq*t)
# plt.figure(figsize = (10,8)) # set the size of figure
# plt.title('Sine Wave',fontsize=20)
# plt.plot(t,sig_sine, linewidth=3,label= 'x(t) = sin(wt)')
# plt.xlabel('time',fontsize=15)
# plt.ylabel('Amplitude',fontsize=15)
# plt.legend(loc='upper right')
# plt.grid()
# plt.show()

# #task 2 square wave
# t = np.linspace(0,2,1000)
# sig_square = amp*sg.square(2*np.pi*freq*t, duty=0.3)
# plt.figure(figsize = (10,8)) # set the size of figure
# plt.title('Square Wave',fontsize=20)
# plt.plot(t,sig_square, linewidth=3,label= 'x(t) = square(wt)')
# plt.xlabel('time',fontsize=15)
# plt.ylabel('Amplitude',fontsize=15)
# plt.legend(loc='upper right')
# plt.grid()
# plt.show()

# #task 3 triangle wave
# t = np.linspace(0,2,1000)
# sig_triangle = amp*sg.sawtooth(2*np.pi*freq*t, width=0.3)
# plt.figure(figsize = (10,8)) # set the size of figure
# plt.title('triangle Wave',fontsize=20)
# plt.plot(t,sig_triangle, linewidth=3,label= 'x(t) = tri(wt)')
# plt.xlabel('time',fontsize=15)
# plt.ylabel('Amplitude',fontsize=15)
# plt.legend(loc='upper right')
# plt.grid()
# plt.show()


# #task 4 sinc function
# # t1=np.linspace(-2*np.pi,2*np.pi,0.01)
# t1=np.linspace(-8,8,1000000)
# sig_sinc = np.sinc(t1)
# # plt.figure(figsize = (10,8)) # set the size of figure
# plt.title('sinc function',fontsize=20)
# plt.plot(t1,sig_sinc, linewidth=3,label= 'x(t) = sinc(t)')
# plt.xlabel('time',fontsize=15)
# plt.ylabel('Amplitude',fontsize=15)
# plt.legend(loc='upper right')
# plt.axhline(y=0, color='k')
# plt.axvline(x=0, color='k')
# plt.grid()
# plt.show()

# #task 5 basic function
# def p(t):
#     """Basic rectangular pulse"""
#     return 1 * (abs(t) < 0.5)

# def pt(t):
#     """ Basic triangular pulse"""
#     return (1 - abs(t)) * (abs(t) < 1)

# def sgn(t):
#     """Sign function"""
#     return 1 * (t >= 0) - 1 * (t < 0)

# def u(t):
#     """Unit step function"""
#     return 1 * (t >= 0)

# functions = [p, pt, sgn, u]

# t = np.linspace(-2, 2, 1000)

# plt.figure()
# for i, function in enumerate(functions, start=1):
#     plt.subplot(2, 2, i)
#     plt.plot(t, function(t), '-b')
#     plt.ylim((-1.1, 1.1))
#     plt.title(function.__doc__)
# plt.tight_layout()
# plt.show()


# Post lab work 
# # Task 1: Plot Discrete-time signals
# F0 = 0.1
# L = 100
# n = np.arange(L)
# x = np.cos(2*np.pi*F0*n)
# plt.stem(x) 
# plt.title('Discrete-time sinusoid of F0=0.1')
# plt.xlabel('n')
# from fractions import Fraction

# n = np.arange(50)
# frequencies = [0, 1/2, 1/4, 3/4, 1/16, 15/16]

# for i, F0 in enumerate(frequencies, start=1):
#     plt.subplot(3, 2, i)
#     plt.stem(np.cos(2*np.pi*F0*n))
#     plt.title(r'$\cos(2\pi {}n)$'.format(Fraction(F0)))

# plt.tight_layout()






# # Task 2: Basic transformations

# def x(t):
#     return np.exp(-0.2 * t) * (t >= 0)

# t = np.linspace(-10, 10, 1000)

# f, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True, sharey=True)
# plt.subplots_adjust(hspace=1)
# ax1.set_ylim([-0.2, 1.2])

# ax1.plot(t, x(t))
# ax1.set_title(r'x(t)')

# ax2.plot(t, x(2-t))
# ax2.set_title(r'x(2 - t)')

# ax3.plot(t, x(4*t))
# ax3.set_title(r'x(4t)')

# ax4.plot(t, x(0.25*t))
# ax4.set_title(r'x(\frac{1}{4}t)')
# ax4.set_xlabel('t (in s)')

# L = 20
# n = np.arange(L)

# x = np.exp(-0.2 * n) * (n >= 0)
# x2 = x[::2]  # Decimation by 2: Remove one from every 2 points
# v = np.zeros((2*L))
# v[::2] = x   # v = x(n/2) for even n, 0 otherwise

# f, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, sharey=True)
# plt.subplots_adjust(hspace=1)
# ax1.set_ylim([-0.2, 1.2])

# ax1.stem(x)
# ax1.set_title(r'x[n]')

# ax2.stem(x2)
# ax2.set_title(r'x[2n]')

# ax3.stem(v)
# ax3.set_title(r'v[n]')

# # The discrete signals are represented versus n, not versus t
# ax3.set_xlabel('n')
