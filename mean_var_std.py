"""This module uses numpy to analyze data in a 3x3 matrix"""
import numpy as np

def calculate(input_list):
    """This function calculates the mean, median, sum, std dev, min and sum of a 3x3 matrix"""
    try:
        if len(input_list) != 9:
            raise ValueError("List must contain nine numbers.")

        # Creating the 3x3 matrix
        a = np.array([input_list[0], input_list[1], input_list[2]])
        b = np.array([input_list[3], input_list[4], input_list[5]])
        c = np.array([input_list[6], input_list[7], input_list[8]])

        matrix = np.array([a, b, c])

        # dictionary that returns the values
        matrix_dict = {}

        # setting the required values to the dictionary keys

        matrix_dict['mean'] = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix.flatten()).tolist()] 
        matrix_dict['variance'] = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix.flatten()).tolist()]
        matrix_dict['standard deviation'] = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix.flatten()).tolist()]
        matrix_dict['max'] = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix.flatten()).tolist()]
        matrix_dict['min'] = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix.flatten()).tolist()]
        matrix_dict['sum'] = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix.flatten()).tolist()]

        return matrix_dict

    except ValueError as e:
        print(e) 


print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))