# Dinner statistics visualization

## Running the visualizer
To run the program, simply run the command "python3 main.py" in the root folder
Make sure all of the dependencies are installed, using pip3

## Note on the graphs created
The graphs the program creates are the ones listed in the graph_types list, in the main function.
For each of these, there must be an if-case, in the plot function, to run it. i.e if we want to display 'graph_x', we must include it in the list, 
and create an if-case for 'graph_x' in which lies the code to plot and display said graph