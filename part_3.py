import matplotlib.pyplot as plt
import csv


def calculate(csv_data):
    """This fuction is used to store the saarc countries name in set and this
    set is used to store the data in dictionary of saarc countries population and year.
    """

    saarc_contries = {"Afghanistan", "Bangladesh", "Bhutan",
                      "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"}
    year_and_pop_of_saarc = {}
    for line in csv_data:
        if line['Region'] in saarc_contries:
            if year_and_pop_of_saarc.get(line['Year']) == None:
                year_and_pop_of_saarc[line['Year']] = float(line['Population'])
            else:
                year_and_pop_of_saarc[line['Year']
                                      ] += float(line['Population'])
    return year_and_pop_of_saarc


def transfer(year_and_pop_of_saarc):
    """This fuction plots bar chart of year and saarc countries population."""

    year = list(year_and_pop_of_saarc.keys())
    population = list(year_and_pop_of_saarc.values())
    return year, population


def graph_plot(year, population):
    plt.bar(year, population)
    plt.xlabel("Year")
    plt.ylabel("Saarc countries population")
    plt.title("Over the years, TOTAL population of SAARC countries")
    plt.xticks(rotation = 90)
    plt.show()


def main():
    file = open('population-estimates_csv.csv', 'r')
    csv_data = csv.DictReader(file)
    year_and_pop_of_saarc = calculate(csv_data)
    year, population = transfer(year_and_pop_of_saarc)
    graph_plot(year, population)


if __name__ == "__main__":
    main()
