import plotext as plt

l = 1000
frames = 200

plt.title("Streaming Data")

y = plt.sin(periods = 2, length = l, phase = 2 * 1  / frames)
plt.scatter(y, marker="sd")
plt.show()