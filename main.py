from Objects import *
from matplotlib import pyplot as plt
def main(**kwargs):
    fig, ax = plt.subplots()

    env = Environment(**{"gravity": 9.81})
    corp = Object(env, **{"mass": 8, "force": 0})
    corp.show(ax, [0, 0], "k", 15)
    result = corp.newton_first_law()
    if type(result) == Vector:
        result.show(ax, [0, 0], "r")
    ax.set_xlim([-100, 100])
    ax.set_ylim([-100, 100])
    plt.grid()
    plt.show()
main()