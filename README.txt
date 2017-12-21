
Final project for BMI 6018
Project by:
Anwar Alsanea
Ryan Williams
Md Imdadul Islam


Project background:

Visual:
The first graph was created using plot method under pandas dataframe with specific paramter kind="hist". A new dataframe called DF_1 was created with only column of "egg1_gasproduced" and "egg2_gasproduced"". This code produces a histogram of the two column value in the dataframe. Our graph showed that most of the time the gas production was in the range of 375,000 to 410,000 trillion cubic feet (tcf).

The next plot was a boxplot using same plot method under pandas dataframe. This showed that the median value as well as first and third quartile is greater for the gas production in egg1 compared to egg2.
Now we are going to use the class stats_data from the module called aclass to verify the above findings. The normalized gas production (i.e. gas produced divided by the amount of feed) value was 4.9 for egg1 and 4.7 for egg2, which proves that digester 1 is more efficient.

Next we created a scatter plot using DataFrame.plot() function and kind = 'scatter', but our scatter plot looked so dense. That is why we decided to use hexabin plot. Hexabin plot was created using DataFrame.plot() function and kind = 'hexbin'.

In the next plot we have two scatter plot of gas production vs feed for both of the digester. This graph was created using DataFrame.plot.scatter(). The graph showed that both the digester produces maximum gas when the feed is about 100,000 gallons.

The plot next is an interactive plot created using the function called daily_variation_by_month which is under the module named imdadplot.py. The function goes into another function called interact imported from ipwidget. Function daily_variation_by_month takes two keyword arguments: df_glob and month. In this plot we can choose the month that we want to visualize and the graph shows the daily variation of gas produced in egg1.

Finally we created another interactive plot using the function monthly_boxplot_by_egg from the same previous module imdaplot.py. This also takes help of interact function. The function monthly_boxplot_by_egg function takes two keyword argument: df_glob and egg. In this plot we can choose the number of egg from the widget and the graph shows boxplot of gas production in different month. 