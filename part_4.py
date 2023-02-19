import matplotlib.pyplot as plt
import csv


def calculate(csv_data):
    """This fuction is used to store the asean countries name in set and this
    set is used to store the data in dictionary of dictionary of asean countries
    population in between year 2004 to 2014.
    """

    asean_country_set = {"Brunei Darussalam", "Cambodia", "Indonesia", "Lao People's Democratic Republic",
                         "Malaysia", "Myanmar", "Philippines", "Singapore", "Thailand", "Viet Nam"}
    asean_country_2004_to_2014_pop = {}
    for line in csv_data:
        if int(line['Year']) >= 2004 and int(line['Year']) <= 2014 and line['Region'] in asean_country_set:
            if asean_country_2004_to_2014_pop.get(line['Region']) == None:
                asean_country_2004_to_2014_pop[line['Region']] = {
                    2004: 0, 2005: 0, 2006: 0, 2007: 0, 2008: 0, 2009: 0, 2010: 0, 2011: 0, 2012: 0, 2013: 0, 2014: 0}
                asean_country_2004_to_2014_pop[line['Region']][int(
                    line['Year'])] += float(line['Population'])
            else:
                asean_country_2004_to_2014_pop[line['Region']][int(
                    line['Year'])] += float(line['Population'])

    return asean_country_2004_to_2014_pop


def graph_plot(asean_country_2004_to_2014_pop):
    """This function plots grouped bar chart of grouped by asean countries
    population on each year
    """
    
    bar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    clr = ["blue", "grey", "yellow", "green", "navy",
           "olive", "red", "pink", "purple", "black"]
    w = 0.1  # width of every bar
    j = 0
    for country in asean_country_2004_to_2014_pop:
        temp = []
        for i in range(11):
            temp.append(asean_country_2004_to_2014_pop[country][2004 + i])
        plt.bar(bar, temp, w, label=country, color=clr[j])
        j += 1
        for i in range(11):
            bar[i] += w
    x_ticks = [2004, 2005, 2006, 2007, 2008,
               2009, 2010, 2011, 2012, 2013, 2014]
    # now this bar list is used to point the middle position of every group bars
    bar[0] = 5 * w
    for i in range(1, 11):
        bar[i] = bar[i-1] + 10 * w   # (5*w+5*w = 10*w)
    plt.xticks(bar, x_ticks)
    plt.xlabel("Every year asean countries")
    plt.ylabel("Population")
    plt.title("4: Grouped Bar Chart - ASEAN population vs. years")
    plt.legend()
    plt.show()


def main():
    file = open('population-estimates_csv.csv', 'r')
    csv_data = csv.DictReader(file)
    asean_country_2004_to_2014_pop = calculate(csv_data)
    graph_plot(asean_country_2004_to_2014_pop)


if __name__ == "__main__":
    main()
