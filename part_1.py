import matplotlib.pyplot as plt
import csv


def calculate(csv_data):
    """This function is used to store the data in dictionary of every year Indian population."""

    india_pop_over_years = {}
    for line in csv_data:
        india_pop_over_years[line['Year']] = float(line['Population'])

    return india_pop_over_years


def transfer(india_pop_over_years):
    """This function is used to transfer the dictionary into lists."""

    years = list(india_pop_over_years.keys())
    population = list(india_pop_over_years.values())

    return years, population


def graph_plot(years, population):
    """This fuction plots bar chart graph of years v/s India population."""

    plt.bar(years, population)
    plt.xlabel("Years")
    plt.ylabel("India population")
    plt.title("India population over years - Bar Plot")
    plt.xticks(rotation = 90)
    plt.show()


def main():
    file = open('population-estimates_csv.csv', 'r')
    csv_data = csv.DictReader(file)
    india_pop_over_years = calculate(csv_data)
    years, population = transfer(india_pop_over_years)
    graph_plot(years, population)


if __name__ == "__main__":
    main()
