import matplotlib.pyplot as plt
import csv


def calculate(csv_data):
    """This fuction is used to store the asean countries name in set and this
    set is used to store the data in dictionary of asean countries name and
    their population in 2014.
    """

    asean_country_set = {"Brunei Darussalam", "Cambodia", "Indonesia", "Lao People's Democratic Republic",
                         "Malaysia", "Myanmar", "Philippines", "Singapore", "Thailand", "Viet Nam"}
    asean_pop_2014 = {}
    for line in csv_data:
        if line['Year'] == '2014' and line['Region'] in asean_country_set:
            asean_pop_2014[line['Region']] = float(line['Population'])
    return asean_pop_2014


def transfer(asean_pop_2014):
    """This function transfers dictionary into lists."""

    country = list(asean_pop_2014.keys())
    population = list(asean_pop_2014.values())
    return country, population


def graph_plot(country, population):
    """This fuction plots bar chart of asean countries name and their population in 2014."""

    plt.bar(country, population)
    plt.xlabel("Asean Country")
    plt.ylabel("Population in 2014")
    plt.title("For the year 2014. Bar Chart of population of ASEAN countries")
    plt.xticks(fontsize = 7, rotation = 90)
    plt.show()


def main():
    file = open('population-estimates_csv.csv', 'r')
    csv_data = csv.DictReader(file)
    asean_pop_2014 = calculate(csv_data)
    country, population = transfer(asean_pop_2014)
    graph_plot(country, population)


if __name__ == "__main__":
    main()
