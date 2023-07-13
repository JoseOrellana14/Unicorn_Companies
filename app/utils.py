from collections import Counter

def get_valuation_country(data):
    valuation_dict = {
        item['Company']: float(item['Valuation ($B)'].replace('$','')) for item in data
    }
    sorted_valuation_dict = {
        key: value for key, value in sorted(valuation_dict.items(), key=lambda item: item[1])
        }
    modified_dict = {
        key: '$'+ str(value) for key, value in sorted_valuation_dict.items()
    }
    labels = modified_dict.keys()
    values = modified_dict.values()
    print(modified_dict)

    return labels, values
    
def count_frequencies(data):
    countries_dict = [key['Country'] for key in data if key != '']
    frequency = Counter(countries_dict)
    print(frequency)
    labels = frequency.keys()
    values = frequency.values()
    return labels, values
