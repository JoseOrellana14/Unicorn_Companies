import read_csv
import utils
import charts


def valuation_country():
    user_country = input('Ingrese el pais que desea conocer => ')
    data = read_csv.read_csv('./StartUpsession/app/Unicorn_Companies.csv')
    data = list(filter(lambda item: item['Country'] == user_country, data))

    labels, values = utils.get_valuation_country(data)
    charts.generate_bar_charts(labels, values)

def valuation_industry():
    user_industry = input('Ingrese la Industria que desea conocer => ')
    data = read_csv.read_csv('./StartUpsession/app/Unicorn_Companies.csv')
    data = list(filter(lambda item: item['Industry'] == user_industry, data))

    labels, values = utils.get_valuation_country(data)
    charts.generate_bar_charts(labels, values)

def world_pie_chart():
    data = read_csv.read_csv('./StartUpsession/app/Unicorn_Companies.csv')
    
    labels, values = utils.count_frequencies(data)
    charts.generate_pie_charts(labels, values)


if __name__=='__main__':
    
    print('*'*50)
    print('Unicorn Companies around the World')
    print('*'*50)
    print('Choose an option from this data set: \nValuation by Country \nValution by Industry \nWorld Pie Chart')
    option = input('=>')

    match option:
        case 'Valuation by Country':
            valuation_country()
        case 'Valuation by Industry':
            valuation_industry()
        case 'World Pie Chart':
            world_pie_chart()
        case _:
            print('Escoja una opcion valida')

