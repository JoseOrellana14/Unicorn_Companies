import csv
import os

# Directorio al que deseas cambiar
new_directory = 'C:/Documents/PLATZI/RUTA_Data_Scientist_Python/2.StartUpVisualizationProject'

# Cambiar al nuevo directorio
os.chdir(new_directory)

# Verificar el directorio actual después del cambio
current_directory = os.getcwd()
print("Directorio actual:", current_directory)


def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            unicorn_company_dict = {key: value for key, value in iterable}
            data.append(unicorn_company_dict)
    return data

if __name__ == '__main__':
    data = read_csv('./StartUpsession/app/Unicorn_Companies.csv')
    print(data[0])
