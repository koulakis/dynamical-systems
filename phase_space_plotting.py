import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def plot_traj(x0, dx_dt, fw=0, bw=0, n_time_samples=100, ax=None, color=None):
    if color is None:
        color='red'
    xs = odeint(dx_dt, x0, np.linspace(0, fw, n_time_samples))
    (ax if ax else plt).plot(xs[:, 0], xs[:, 1], linewidth=1, color=color)
    
    xs = odeint(dx_dt, x0, np.linspace(0, -bw, n_time_samples))
    (ax if ax else plt).plot(xs[:, 0], xs[:, 1], linewidth=1, color=color)
    

def plot_field(dx_dt, xlim, ylim, scale=100, ax=None, polar=False):
    X, Y = np.mgrid[xlim[0]:xlim[1]:15j, ylim[0]:ylim[1]:15j]
    u, v = dx_dt([X, Y], None)
    if polar:
        u, v = v*np.cos(X) - Y*u*np.sin(X), v*np.cos(X) + Y*u*np.cos(X)
    (ax if ax else plt).quiver(X, Y, u, v, color='b', scale=scale)

def plot_phase_portrait(
    dx_dt, ts, 
    xlim=np.array([-3, 3]), 
    ylim=np.array([-3, 3]), 
    title=None,
    ic_x = np.linspace(*[-3, 3], 9),
    ic_y = np.linspace(*[-3, 3], 9),
    linewidth=1,
    scale=None):

    for r in ic_x:
        for s in ic_y:
            x0 = [r, s]
            xs = odeint(dx_dt, x0, ts)
            plt.plot(xs[:, 0], xs[:, 1], 'r-', linewidth=linewidth)

    X, Y = np.mgrid[xlim[0]:xlim[1]:15j, ylim[0]:ylim[1]:15j]
    u, v = dx_dt([X, Y], None)
    plt.quiver(X, Y, u, v, color='b', scale=scale)

    plt.title(title)
    plt.xlim(np.array(xlim) * 1.1)
    plt.ylim(np.array(ylim) * 1.1)
