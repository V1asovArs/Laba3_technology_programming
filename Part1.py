import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd

class Graph:
    def __init__(self, data, x, y, title):
        self.data = data
        self.x = x
        self.y = y
        self.title = title

    def plot(self):
        pass

class Description:
    def __init__(self, text):
        self.text = text

class App:
    def __init__(self, data, x, y):
        self.window = tk.Tk()
        self.window.title("Graph Plotter")

        self.button = tk.Button(self.window, text="Plot Graph", command=self.plot_graph)
        self.button.pack()

        self.graph = Graph(data, x, y, "Graph")

        self.description = Description("")
        self.message = tk.Text(self.window)
        self.message.pack()

        self.window.mainloop()

    def plot_graph(self):
        self.graph.plot()
        self.message.insert(tk.END, "Привет!\n")
        self.message.insert(tk.END, self.description.text)

i = input('Введите номер графика (1 or 2): ')
df = pd.read_csv(f'data{i}.csv', sep=';')
data = df.iloc[1:, 0]
x = df.iloc[1:, 1]
y = df.iloc[1:, 2]
app = App(data, x, y)