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
        plt.plot(self.data, self.x, 'o-')
        plt.plot(self.data, self.y, 'bo-')
        plt.title(self.title)
        plt.xlabel('data')
        plt.ylabel('x, y')
        plt.show()

class Description:
    def __init__(self, text):
        self.text = text

class App:
    def __init__(self, data, x, y, i):
        self.window = tk.Tk()
        self.window.title("Graph Plotter")

        self.button = tk.Button(self.window, text="Plot Graph", command=self.plot_graph)
        self.button.pack()

        self.graph = Graph(data, x, y, "Graph")

        if i == 1:
            dollar_max_gain = 0
            dollar_max_loss = 0
            euro_max_gain = 0
            euro_max_loss = 0
            for j in range(2,len(x)):
                dif_usd = float(x[j-1])-float(x[j])
                dif_euro = float(y[j-1])-float(y[j])
                if dif_usd>dollar_max_gain:
                    dollar_max_gain = dif_usd
                    dollar_max_gain_day = data[j]
                if dif_usd<dollar_max_loss:
                    dollar_max_loss = dif_usd
                    dollar_max_loss_day = data[j]
                if dif_euro > euro_max_gain:
                    euro_max_gain = dif_euro
                    euro_max_gain_day = data[j]
                if dif_euro < euro_max_loss:
                    euro_max_loss = dif_euro
                    euro_max_loss_day = data[j]
            result = f"Dollar max up on {dollar_max_gain} - {dollar_max_gain_day}\n Euro max up on {euro_max_gain} - {euro_max_gain_day}\n Dollar max down on {dollar_max_loss} - {dollar_max_loss_day}\n Euro max down on {euro_max_loss} - {euro_max_loss_day}"
            #print(result)
        elif i==2:
            tmp1 = [int(x[k].split()[0]) * 1000 for k in range(1, len(x))]

            tmp2 = [int(y[k].split()[0]) * 1000 for k in range(1, len(y))]

            if max(sum(tmp1), sum(tmp2)) > sum(tmp1):
                result = f"Asia win {sum(tmp2)} is {sum(tmp1)}"
                #print(result)
            else:
                result = f"Europe win {sum(tmp1)} is {sum(tmp2)}"
                #print(result)

        self.description = Description(result)
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
app = App(data, x, y, int(i))