Plotting Test Specimen Graphs
This repository contains Python scripts that allow plotting graphs from experimental data of test specimens. The data is loaded from CSV files, and the graphs are generated for the analysis of force, deformation, stress, displacement, and other parameters related to mechanical tests. This README describes the functionality of each script and provides usage instructions.

General Functionality
The scripts in this repository are designed to:

Load multiple CSV files.
Process and clean the data by removing duplicate values and allowing the user to exclude unwanted end points.
Plot graphs of multiple tests, highlighting maximum values and calculating the mean and standard deviation when applicable.
Export the mean of the data to CSV files.
Adjust axis scales and customize the titles and legends of the graphs.
Scripts
1. Provetes_cod_melhorado_Graph_melhorado.py
This script loads multiple CSV files and generates comparative graphs of deformation and stress or other measurement parameters. The user can:

Select columns for the X and Y axes.
Manually remove end points from the graphs.
Highlight the maximum value of each test.
Plot the mean and standard deviation of the values in additional graphs.
How to use:
Run the script and select the CSV files that contain the data of interest.
Choose the columns to be plotted on the X and Y axes.
Adjust the graph title, and if necessary, remove the end points.
The graph will be displayed with the selected options, including the mean and standard deviation (if enabled).
The user can save the results as CSV files containing the mean values.
2. Provetes_cod_melhorado_Graph_melhorado_Força_Desloc.py
Similar to the previous script, this one is specific to plotting force vs displacement graphs. It also allows:

Plotting selected tests.
Calculating and displaying the mean and standard deviation.
Adjusting the axis scales for force and displacement with predefined intervals.
How to use:
The usage procedure is similar to the first script, but this script is optimized for plotting force and displacement, with specific intervals and adjustments for these parameters.

3. teste_media_melhorado.py
This script focuses on generating the mean of different tests and visualizing it in a graph. The code:

Allows the user to select multiple CSV files.
Generates a graph of force and deformation means for the selected tests.
How to use:
The user selects the CSV files and defines the graph title.
The script processes the files and plots the mean of the selected tests.
The mean can be saved in a CSV file.
4. testes_praticos_melhorado.py
This script is aimed at practical analysis of mechanical tests, allowing comparison of various tests and displaying results of force and displacement. It includes functions to highlight the maximum value of each test and calculate means and standard deviations.

How to use:
The user selects the CSV files containing the test data.
The script allows selecting columns for plotting, removing end points, and viewing the results.
It includes options to display the mean and standard deviation in graphs.
5. Cod_Provetes_2x_Graph_melhorado.py
This script allows plotting graphs of grouped tests. Each pair of tests is grouped and plotted on a single line, allowing comparison of two tests at a time. This is useful for comparing similar series of tests.

How to use:
The script groups the tests in pairs, comparing them side by side.
It allows saving the mean of the grouped results.
6. medias_garras_testes_praticos_melhorado.py
This script is dedicated to comparing different grip formats in mechanical tests. It allows plotting and comparing data from tests performed with different grip configurations.

How to use:
The user selects the CSV files corresponding to the tests of each type of grip.
The script plots the results for comparison and calculates the mean for each grip type.
Dependencies
The scripts use the following Python libraries:

pandas: For data manipulation and analysis of CSV files.
matplotlib: For generating graphs.
numpy: For mathematical calculations such as interpolation and calculating mean and standard deviation.
tkinter: For graphical interfaces that allow the user to select files and adjust plotting settings.
To install the dependencies, run:


pip install pandas matplotlib numpy
How to Run the Scripts
Clone this repository to your local machine.
Install the dependencies listed above.
Run the desired script using Python:

cd path_to_code_folder
python script_name.py
Follow the graphical interface instructions to load the CSV files and generate the graphs.

Made by Luan Matheus Capeletti Lang
