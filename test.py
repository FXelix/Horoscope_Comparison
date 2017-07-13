
import matplotlib.pyplot as plt
import pandas as pd


for v in range(1, 10):

    data = {"x": [],
            "y": []}

    g = 9.81  # m/s**2
    t = 0
    h = 100
    while True:
        height = h - 0.5 * g * t ** 2
        distance = t * v #height = h -0.5 * g * t ** 2  #!!! Fallzeitgleichung ! h(t) ,     h(x) = (2h/g)**1/2 * v==t*v
        if height <= int(0):
            print("hit the ground after {} seconds.".format(round(t, 3)))
            print("it flew {} metres.".format(round(v * (2*h/g)**(1/2), 3)))
            break
        data["x"].append(distance)
        data["y"].append(height)

        t += 1/100

    frame = pd.DataFrame(data["y"], data["x"])
    print(frame)
    plt.plot(frame, label="v={}".format(v))


plt.title("Velocity comparison")
plt.xlabel("Distance")
plt.ylabel("Height")
axes = plt.gca()
axes.set_xlim(0, )
axes.set_ylim(0,110)
plt.legend()
plt.show()