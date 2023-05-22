import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import ArrayLike
from typing import Any, Union, Iterable

class GaussBuilder:
    def __init__(self):
        self.name = 2
        plt.style.use("ggplot")

    #util
    def create_empty_array(self, rows: int, columns: int) -> ArrayLike:
        return np.zeros((rows,columns))

    #trigonometric
    def sine(self, x) -> Any:
        return np.sin(x)

    def cosine(self, x) -> Any:
        return np.cos(x)

    def tangent(self, x) -> Any:
        return np.tan(x)

    #graphic
    def single_plot(self,
                    X: Union[Iterable, ArrayLike],
                    y: Union[Iterable, ArrayLike],
                    labelX: str = "x_axis",
                    labely: str = "y_axis",
                    name: str = "single_plot") -> None:
        fig, ax = plt.subplots()
        ax.plot(X,y)
        ax.set(title=name, xlabel=labelX, ylabel=labely)
        plt.show()

    def scatter_plot(self,
                    X: Union[Iterable, ArrayLike],
                    y: Union[Iterable, ArrayLike],
                    labelX: str = "x_axis",
                    labely: str = "y_axis",
                    name: str = "scatter_plot") -> None:
        fig, ax = plt.subplots()
        ax.scatter(X,y)
        ax.set(title=name, xlabel=labelX, ylabel=labely)
        plt.show()

    def hist_plot(self,
                    X: Union[Iterable, ArrayLike],
                    labelX: str = "x_axis",
                    labely: str = "y_axis",
                    name: str = "hist_plot") -> None:
        fig, ax = plt.subplots()
        ax.scatter(X)
        ax.set(title=name, xlabel=labelX, ylabel=labely)
        plt.show()
        
    def pie_chart_plot(self,
                    sizes: Union[Iterable, ArrayLike],
                    labels: Union[Iterable, ArrayLike],
                    name: str = "pie_chart_plot") -> None:
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels)
        ax.set(title=name)
        plt.show()
         
    #random
    def random_g(x_shape: int =None, y_shape: int = None) -> Union[float, ArrayLike]:
        if x_shape:
            if y_shape:
                return np.random.rand(x_shape,y_shape)
            return np.random.rand(x_shape)
        return np.random.rand()

    #lineal algebra
    def add_matrices(self,
    matrix1: ArrayLike,
    matrix2: ArrayLike) -> ArrayLike:
        return np.add(matrix1, matrix2)
    
    def subtract_matrices(self,
    matrix1: ArrayLike,
    matrix2: ArrayLike) -> ArrayLike:
        return np.subtract(matrix1, matrix2)
    
    def multiply_matrices(self,
    matrix1: ArrayLike,
    matrix2: ArrayLike) -> ArrayLike:
        return np.matmul(matrix1, matrix2)
    
    def dot_product(self,
    matrix1: ArrayLike,
    matrix2: ArrayLike) -> ArrayLike:
        return np.dot(matrix1, matrix2)
    
    def transpose_matrix(self, matrix: ArrayLike) -> ArrayLike:
        return np.transpose(matrix)
    
    def inverse_matrix(self, matrix: ArrayLike) -> ArrayLike:
        return np.linalg.inv(matrix)

Gauss = GaussBuilder()        