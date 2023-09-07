# Создайте класс Матрица.
# Добавьте методы для: - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц

class Matrix:
    """
    Класс Матрица содержит методы для:
    - вывода на печать,
    - сравнения,
    - сложения,
    - умножения матриц
    """
    def __init__(self, matrix_data):
        self.matrix = matrix_data
        self.rows = len(matrix_data)
        self.columns = len(matrix_data[0])

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError('Количество строк в матрицах не совпадает')
        result_matrix = []
        for i in range(self.rows):
            result_row = [x + y for x, y in zip(self.matrix[i], other.matrix[i])]
            result_matrix.append(result_row)
        return Matrix(result_matrix)

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError('Количество столбцов в матрицах не совпадает')
        result_matrix = []
        for i in range(self.rows):
            result_row = []
            for j in range(other.columns):
                result_element = 0
                for k in range(self.columns):
                    result_element += self.matrix[i][k] * other.matrix[k][j]
                result_row.append(result_element)
            result_matrix.append(result_row)
        return Matrix(result_matrix)


# Пример использования класса Matrix
if __name__ == "__main__":
    matrix1_data = [[1, 2], [3, 4]]
    matrix2_data = [[5, 6], [7, 8]]

    matrix1 = Matrix(matrix1_data)
    matrix2 = Matrix(matrix2_data)

    print("Матрица 1:")
    print(matrix1)

    print("Матрица 2:")
    print(matrix2)

    print("Матрица 1 == Матрица 2:", matrix1 == matrix2)

    sum_matrix = matrix1 + matrix2
    print("Сумма Матрицы 1 и Матрицы 2:")
    print(sum_matrix)

    product_matrix = matrix1 * matrix2
    print("Произведение Матрицы 1 и Матрицы 2:")
    print(product_matrix)
