#BASEADO EM UM ARQUIVO FEITO PELO PROFESSOR FEZ EM SALA

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataVisualizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Visualization Interface")
        self.root.geometry("1000x600")

        # Dados de exemplo
        self.create_sample_data()

        # Configurar layout
        self.setup_layout()

    def create_sample_data(self):
        """Criar DataFrame de exemplo"""
        data = {
            'total_bill': [16.99, 10.34, 21.01, 23.68, 24.59],
            'tip': [1.01, 1.66, 3.50, 3.31, 3.61],
            'day': ['Sun', 'Sun', 'Sun', 'Sat', 'Sat'],
            'size': [2, 3, 3, 2, 4]
        }
        self.tips = pd.DataFrame(data)

    def setup_layout(self):
        """Configurar layout da interface"""
        # Título
        title_label = tk.Label(self.root, text="Data Visualization", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Quadro principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Menu lateral
        menu_frame = tk.Frame(main_frame, width=200, bg="lightgrey")
        menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        menu_label = tk.Label(menu_frame, text="Select Graph Type", bg="lightgrey")
        menu_label.pack(pady=10)

        # Tipos de gráficos
        graph_types = ["Scatter Plot", "Bar Chart", "Pie Chart", "Line Chart", "Histogram"]
        for graph in graph_types:
            button = tk.Button(menu_frame, text=graph, 
                               command=lambda g=graph: self.update_graph(g))
            button.pack(fill=tk.X, padx=10, pady=5)

        # Quadro de dados
        self.data_frame = tk.Frame(main_frame)
        self.data_frame.pack(fill=tk.X)
        self.display_dataframe()

        # Quadro de gráficos
        self.graph_frame = tk.Frame(main_frame)
        self.graph_frame.pack(fill=tk.BOTH, expand=True)

        # Gráfico inicial
        self.update_graph("Scatter Plot")

    def update_graph(self, selected_graph):
        """Atualizar gráfico com base na seleção"""
        # Limpar gráficos existentes
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        # Criar novo gráfico
        fig, ax = plt.subplots(figsize=(8, 5))
        
        # Seleção de gráfico
        graph_methods = {
            "Scatter Plot": self.create_scatter_plot,
            "Bar Chart": self.create_bar_chart,
            "Pie Chart": self.create_pie_chart,
            "Line Chart": self.create_line_chart,
            "Histogram": self.create_histogram
        }
        
        # Chamar método do gráfico selecionado
        graph_methods.get(selected_graph, self.create_scatter_plot)(ax)
        
        # Renderizar gráfico
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def create_scatter_plot(self, ax):
        """Criar gráfico de dispersão"""
        sns.scatterplot(data=self.tips, x='total_bill', y='tip', 
                        hue='day', size='size', ax=ax)
        ax.set_title("Scatter Plot - Bills and Tips")

    def create_bar_chart(self, ax):
        """Criar gráfico de barras"""
        categories = ['A', 'B', 'C', 'D']
        values = [4, 7, 1, 8]
        ax.bar(categories, values)
        ax.set_title("Bar Chart Example")

    def create_pie_chart(self, ax):
        """Criar gráfico de pizza"""
        labels = ['A', 'B', 'C', 'D']
        sizes = [15, 30, 45, 10]
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.set_title("Pie Chart Distribution")

    def create_line_chart(self, ax):
        """Criar gráfico de linha"""
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]
        ax.plot(x, y, marker='o')
        ax.set_title("Line Chart Progression")

    def create_histogram(self, ax):
        """Criar histograma"""
        sns.histplot(data=self.tips['total_bill'], kde=True, ax=ax)
        ax.set_title("Histogram of Bill Totals")

    def display_dataframe(self):
        """Exibir DataFrame em uma tabela"""
        # Limpar quadro anterior
        for widget in self.data_frame.winfo_children():
            widget.destroy()
        
        # Criar Treeview
        columns = list(self.tips.columns)
        tree = ttk.Treeview(self.data_frame, columns=columns, show="headings")
        
        # Configurar colunas
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='center')
        
        # Adicionar dados
        for _, row in self.tips.iterrows():
            tree.insert("", "end", values=list(row))
        
        # Adicionar scrollbar
        scrollbar = ttk.Scrollbar(self.data_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        
        # Renderizar
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

def main():
    root = tk.Tk()
    app = DataVisualizationApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
