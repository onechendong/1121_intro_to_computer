import matplotlib.pyplot as plt
import numpy as np

with open("oddExperiment.txt") as file:
    x_list = []
    y_list = []
    for line in file:
        row_data = line.strip().split(' ')
        if row_data[0] != "y":
            y_list.append(float(row_data[0]))
            x_list.append(int(row_data[1]))

coefficients_1 = np.polyfit(x_list, y_list, 1)
poly_1 = np.poly1d(coefficients_1)

coefficients_2 = np.polyfit(x_list, y_list, 2)
poly_2 = np.poly1d(coefficients_2)

mse_1 = np.mean((y_list - poly_1(x_list))**2)
mse_2 = np.mean((y_list - poly_2(x_list))**2)

x_fit = np.linspace(min(x_list), max(x_list), 100)
y_fit_1 = poly_1(x_fit)
y_fit_2 = poly_2(x_fit)

scatter = plt.scatter(x_list, y_list, label='data')  
plt.plot(x_fit, y_fit_1, label=f'Fit of degree 1, LSE: {mse_1:.5f})', color='red')  
plt.plot(x_fit, y_fit_2, label=f'Fit of degree 2, LSE: {mse_2:.5f})', color='purple')  

plt.title('oddExperiment Data')
plt.legend()
plt.show()
