import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

def main():
    fig, ax = plt.subplots()
    plt.ylim([0, 10])
    plt.xlim([0, 5])
    radius = 0.25
    center = (0.5, 8)
    # theta1, theta2 = angle, angle + 180
    theta1 = 0
    theta2 = 180
    w1 = Wedge(center, radius, theta1, theta2, fc='black')
    ax.add_artist(w1)


    # ax.axis('equal')
    plt.show()


main()