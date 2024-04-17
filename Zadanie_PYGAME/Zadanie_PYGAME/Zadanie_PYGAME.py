import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon, Rectangle, Circle, Polygon
from matplotlib.lines import Line2D
from matplotlib.collections import PatchCollection
from matplotlib import cm
import numpy as np

class PolygonDrawer:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim(0, 600)
        self.ax.set_ylim(0, 600)
        self.ax.set_aspect('equal')
        self.ax.set_axis_off()
        self.polygon = self.draw_polygon(6)  # Draw hexagon initially
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)

    def draw_polygon(self, n):
        center = (300, 300)
        radius = 150
        verts = [
            (center[0] + radius * np.cos(2 * np.pi * i / n),
             center[1] + radius * np.sin(2 * np.pi * i / n))
            for i in range(n)
        ]
        polygon = Polygon(verts, closed=True, edgecolor='black', facecolor='none')
        self.ax.add_patch(polygon)
        self.fig.canvas.draw()
        return polygon

    def on_key_press(self, event):
        if event.key.isdigit():
            n = int(event.key)
            if 1 <= n <= 9:
                self.polygon.remove()
                self.polygon = self.draw_polygon(n)
                self.fig.canvas.draw()

if __name__ == "__main__":
    drawer = PolygonDrawer()
    plt.show()
