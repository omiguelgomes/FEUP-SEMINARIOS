import pandas as pd
import matplotlib.pyplot as plt
import csv
import seaborn as sns
import plotly.express as px


class Plotter:
    csv_path = "tips.csv"

    def __init__(self, graph_type):
        self.graph_type = graph_type
        self.data = pd.read_csv(self.csv_path)


    def add_tip_percentage(self):
        file = pd.read_csv(self.csv_path)

        for index, row in file.iterrows():
            file.at[index, 'tip_percentage'] = round((file.at[index, 'tip']/file.at[index, 'total_bill'])*100, 2)

        file.to_csv(self.csv_path)

    def plot(self):

        # scatter plot graph v1
        if self.graph_type == "scatter_simplified":
            plt.scatter(self.data['day'], self.data['tip'])
            plt.title('Scatter Plot (simplified)')
            plt.xlabel('Day')
            plt.ylabel('Tip')
            plt.savefig(self.graph_type)



        #scatter plot graph v2 - with bar color and dot size
        elif self.graph_type == "scatter_advanced":
            plt.scatter(self.data['day'], self.data['tip'], c=self.data['size'], s=self.data['total_bill'])
            plt.title('Scatter Plot (advanced)')
            plt.xlabel('Day')
            plt.ylabel('Tip')
            plt.colorbar()
            plt.savefig(self.graph_type)



        # line chart graph with day vs tip and day vs size
        elif self.graph_type == "line":
            plt.plot(self.data['tip'])
            plt.plot(self.data['size'])
            plt.title('Line Chart')
            plt.xlabel('Day')
            plt.ylabel('Tip')
            plt.savefig(self.graph_type)


        elif self.graph_type == "line_tip":
            # line chart graph with day vs tip only
            plt.plot(self.data['tip'])
            plt.title('Line Chart')
            plt.xlabel('Day')
            plt.ylabel('Tip')
            plt.savefig(self.graph_type)


        elif self.graph_type == "line_size":
            # line chart graph with day vs size only
            plt.plot(self.data['size'])
            plt.title('Line Chart')
            plt.xlabel('Day')
            plt.ylabel('Size')
            plt.savefig(self.graph_type)


        elif self.graph_type == 'barv':
            #bar chart vertical orientation
            plt.bar(self.data['day'], self.data['tip'])
            plt.title("Bar Chart")
            plt.xlabel('Day')
            plt.ylabel('Tip')
            plt.savefig(self.graph_type)


        elif self.graph_type == 'barh':
            # bar chart  horizontal orientation
            plt.barh(self.data['day'], self.data['tip'])
            plt.title("Bar Chart")
            plt.xlabel('Tip')
            plt.ylabel('Day')
            plt.savefig(self.graph_type)


        elif self.graph_type == 'bar_gender':
            # plotting the scatter chart
            fig = px.bar(self.data, x='day', y='tip', color='sex')
            fig.write_image(self.graph_type + ".png", format='png') 

            # showing the plot
            
        elif self.graph_type == 'histogram':
            # histogram counting men and women tip-givers according to bill amount
            ax = sns.histplot(x='total_bill', data=self.data, kde=True, hue='sex')
            ax.set(xlabel='Total Bill', ylabel="Count")
            plt.savefig(self.graph_type)

        elif self.graph_type == 'hexplot':
            # hexbin plot relating bill size and tip size
            sns.set_theme(style="ticks")
            plot = sns.jointplot(x=self.data['tip'], y=self.data['total_bill'], kind="hex", color="#4CB391")
            plot.savefig(self.graph_type)

        elif self.graph_type == 'kernel':
            # smooth kernel density plot relating bill size and tip size
            sns.set_theme(style="white")
            plot = sns.jointplot(data=self.data, x='tip', y='total_bill', space=0)
            plot.plot_joint(sns.kdeplot, fill=True, clip=((0, 10), (0, 75)), thresh=0, levels=100, cmap='rocket')
            plot.plot_marginals(sns.histplot, color="#03051A", alpha=1, bins=25)
            plot.savefig(self.graph_type)


        elif self.graph_type == 'scatterplot_smoker':
            plot = sns.swarmplot(data=self.data, x="tip", y="smoker")
            plot.get_figure().savefig(self.graph_type)
    

        elif self.graph_type == 'scatterplot_meal_time':
            plot = sns.swarmplot(data=self.data, x="tip", y="time", s=3)
            plot.get_figure().savefig(self.graph_type)

        elif self.graph_type == 'violin_plot':
            sns.set_theme(style='whitegrid')
            plot = sns.violinplot(data=self.data, x="day", y="total_bill", hue="smoker",
               split=True, inner="quart", linewidth=1,
               palette={"Yes": "b", "No": ".85"})
            sns.despine(left=True)
            plot.get_figure().savefig(self.graph_type)
            
        elif self.graph_type == 'tip_per_people':
            # draw lineplot
            plot = sns.lineplot(x="size", y="tip_percentage", data=self.data)
            plot.get_figure().savefig(self.graph_type)


        plt.figure().clear()


    def get_graph_type(self):
        return self.graph_type

    def set_graph_type(self, graph_type):
        self.graph_type = graph_type



def main():
    graph_types = ['scatter_simplified', 'scatter_advanced', 'line', 'line_size', 
    'line_tip', 'barv', 'barh', 'bar_gender', 'histogram', 'hexplot', 'scatterplot_smoker', 
    'scatterplot_meal_time', 'violin_plot', 'kernel', 'tip_per_people']

    plotter = Plotter("scatter_simplified")

    for type in graph_types:
        plotter.set_graph_type(type)
        plotter.plot()



if __name__ == '__main__':
    main()