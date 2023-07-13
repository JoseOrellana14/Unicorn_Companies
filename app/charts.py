import matplotlib.pyplot as plt

labels = []
values = []

def generate_bar_charts(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_charts(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

if __name__=='__main__':
    generate_bar_charts()
    generate_pie_charts()
    