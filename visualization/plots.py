import matplotlib.pyplot as plt


def plot_all(time, velocity, current, loss, title_prefix=""):
    plt.figure()
    plt.plot(time, velocity)
    plt.title(f"{title_prefix} Velocity")
    plt.grid()
    plt.savefig("velocity.png")
    plt.close()

    plt.figure()
    plt.plot(time, current)
    plt.title(f"{title_prefix} Current")
    plt.grid()
    plt.savefig("current.png")
    plt.close()

    plt.figure()
    plt.plot(time, loss)
    plt.title(f"{title_prefix} Energy Loss")
    plt.grid()
    plt.savefig("loss.png")
    plt.close()
