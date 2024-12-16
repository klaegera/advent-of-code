with open("input") as f:
    input = [line.strip() for line in f.readlines()]

w, h = 101, 103

import re

robots = []
pattern = re.compile(r"p=(.+),(.+) v=(.+),(.+)")
for line in input:
    robots.append([int(x) for x in re.match(pattern, line).groups()])

from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
scatter = ax.scatter([0, w], [0, h])
fig.subplots_adjust(bottom=0.15)
ax_iter = fig.add_axes([0.1, 0.05, 0.8, 0.03])
slider = Slider(ax=ax_iter, valmin=0, valmax=max(w, h), valstep=1, label="")


def update(val):
    scatter.set_offsets(
        [((px + val * vx) % w, (py + val * vy) % h) for px, py, vx, vy in robots]
    )
    fig.canvas.draw_idle()


slider.on_changed(update)

update(0)
plt.show()
