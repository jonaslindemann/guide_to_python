# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

class QuadraticFunction:
    def __init__(self, a=1.0, b=0.0, c=0.0):
        self.__a = a
        self.__b = b
        self.__c = c

    def __call__(self, x):
        return self.__a * x**2 + self.__b * x + self.__c

    def __str__(self):
        return f"QuadraticFunction(a={self.__a}, b={self.__b}, c={self.__c})"


class NumericalDerivative:
    def __init__(self, function, h=1e-5):
        """
        Initialize numerical derivative calculator.
        
        Args:
            function: A callable function to differentiate
            h: Step size for numerical differentiation (default: 1e-5)
        """
        self.__function = function
        self.__h = h
    
    def __call__(self, x):
        """
        Calculate the derivative at point x using central difference method.
        f'(x) ≈ (f(x+h) - f(x-h)) / (2h)
        """
        return (self.__function(x + self.__h) - self.__function(x - self.__h)) / (2 * self.__h)
    
    def __str__(self):
        return f"NumericalDerivative(h={self.__h})"

    
# Example usage:
if __name__ == "__main__":
    qf = QuadraticFunction(1, -3, 2)

    x = np.linspace(-10, 10, 400)
    y = qf(x)

    # Create numerical derivative of the quadratic function
    qf_prime = NumericalDerivative(qf)
    y_prime = qf_prime(x)

    # Plot both the function and its derivative
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=f"f(x) = {qf}", linewidth=2)
    plt.plot(x, y_prime, label="f'(x) (numerical)", linewidth=2, linestyle='--')
    plt.plot(x, 2*x - 3, label="f'(x) = 2x - 3 (analytical)", linewidth=1, linestyle=':')
    plt.title("Quadratic Function and Its Derivative")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.show()
