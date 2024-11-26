from Objects import *
from matplotlib import pyplot as plt
def main(**kwargs):
    fig, ax = plt.subplots()
    '''Guide:
    - Create an ENVIRONMENT. It takes in the constructor a kwargs where you have to put:
    1. gravity
    2. steepness of the plane the object is put on
    ex: env = Environment(**{"gravity": 9.81, "steepness": 30})
    - create you OBJECT. It takes in the constructor a kwargs where you have to put:
    1. mass
    2. environment
    ex: corp1 = Object(**{"mass": 110, "environment": env})
    - now you can use the functions inside of Object to create your forces. 
    ex: weight = corp1.newton_first_law()
    - if steepness is != 0, you can calculate the components of a force
    ex: comps = weight.get_comps(env)
    - by creating a plot with fig, ax = subplots() you can put it into a .show(ax, origin, color:str) function of the Vector to plot the vector
    Inverse formulas have been added but require further testing.'''
    env = Environment(**{"gravity": 9.81, "steepness": 30})
    corp1 = Object(**{"mass": 110, "environment": env})
    weight = corp1.newton_first_law()
    comps1 = weight.get_comps(env)
    print(comps1.get("x"))

    weight.show(ax, [0, 0], "r")
    comps1.get("x").show(ax, [0, 0], "b")
    comps1.get("y").show(ax, [0, 0], "b")

    ax.set_xlim([-1500, 1500])
    ax.set_ylim([-1500, 1500])

    plt.grid()
    plt.show()

main()