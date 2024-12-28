# Sorting Algorithm Performance Evaluation Application (Sortify Analyzer).

# Overview

This Sorting Algorithm GUI tool is a live Python application with a user interface, built to compare the efficiency of different sorting techniques. They allow flexible configuration of tests, generation of test data and the last but not the least-visualization of the results. The application is ideal for students, educators as well as developers who need to study performance and analyze various sorting strategies under various constraints.

---------------------------------------------------------------------------------------------

# Prerequisites

Before you begin, ensure that you have the following installed on your system:

**1. Python**

The application requires Python to run.

Download and install Python from the official Python website.

During installation, make sure to check the box that says "Add Python to PATH".

To verify the installation, open a terminal or command prompt and type:

python --version

This should display the installed Python version.

**2. Visual Studio Code (VS Code) (Optional but Recommended)**

Download and install VS Code from the official VS Code website.

Install the Python extension in VS Code for better support:

Open VS Code.

Go to the Extensions tab (or press Ctrl+Shift+X).

Search for "Python" and install the extension provided by Microsoft.

---------------------------------------------------------------------------------------------

# How to Set Up and Run the Application

**Step 1**: Extract the ZIP File

Get the path to the folder which contains the program in ZIP format.

For Windows user, right click directly on the file and then you option “Extract All”.

Select a desired folder and click on “Extract”.

**Step 2**: Open the Application Folder

User should open the extracted folder.

In this case, you should see at least one plain text JS file which is our main program script, and a few other files that may be linked to it.

**Step 3** : Launch the Application

*Option 1*: Using Python

In the terminal, run the following command to start the application:

python sorting_gui.py

This means that once the application is launched; you will see the GUI window through which you will be running the tool.

*Option 2*: So, I decided to try and use the precompiled executable that I had downloaded from a website.

If the ZIP file includes an executable (.exe) file:

To run the program double-click on the executable file.

There is no further configuration if this option is chosen.

---------------------------------------------------------------------------------------------

# Features

## Sorting Algorithms: Contains six important types of sorting program:

(1) Insertion Sort

(2) Merge Sort

(3) Bubble Sort

(4) Quick Sort

(5) Heap Sort

(6) Radix Sort

---------------------------------------------------------------------------------------------

## Sorting Cases:

(1) Best Case (Pre-sorted array)

(2) Average Case (Randomly shuffled array is chosen)

(3) Worst Case (Reverse-sorted array)

---------------------------------------------------------------------------------------------

## Performance Metrics:

(1) Keeps record of how many steps (operations) performed by each algorithm.

(2) Compared with actual efficiency to the asymptotic counterpart.

---------------------------------------------------------------------------------------------

## Result Export

(1) Allows saving the sorting results to a CSV file to provide more detailed results analysis.

(2) Saves generated array and sizes of array in a separate CSV file.

---------------------------------------------------------------------------------------------

## Graphical Analysis:

(1) Creates graphical representations of the trends of the performance with standard deviations as well as array sizes and sorting methods.

(2) Interactive GUI: Developed with Tkinter to offer a pleasant drive for the users.

---------------------------------------------------------------------------------------------

# How to Use

## Step 1: Configure Input

Maximum Array Size: Enter the maximum size of the arrays to be tested.

**(A) Sorting Case** Select one of the three available cases:

(A.1) Best Case

(A.2) Average Case

(A.3) Worst Case

**(B) Sorting Methods**: Choose one or more sorting methods from the list.

## Step 2: Run the Sorting Program

Click the "Run Sorting Program" button. The application will:

Generate test data based on your chosen sorting case.

Execute the selected sorting algorithms on arrays of increasing size.

Save the results to a CSV file (e.g., sorting_results_<timestamp>.csv).

Save the generated arrays to a separate CSV file (e.g., generated_arrays_<timestamp>.csv).

## Step 3: Analyze Results

Open Results CSV:

Use the "Open Results CSV" button to view the sorting performance data.

Open Test Data:

Use the "Open Test Data" button to inspect the generated arrays.

Generate Graph:

Click "Generate Graph" to visualize sorting performance. You can select specific algorithms to include in the graph.

---------------------------------------------------------------------------------------------

# File Details

(A) sorting_results_<timestamp>.csv: It provides performance measures for all the sorting algorithms chosen for evaluation in this research.

(B) generated_arrays_<timestamp>.csv: Covers the test arrays for sorting purpose.

(C) <timestamp>.png: Data points used for trend-line calculation (see point #1), as well as generated performance graph (sent to your inbox after plotting).

---------------------------------------------------------------------------------------------

# How to Use the GUI

**Step 1**: Set the Maximum Array Size

Key in the maximum size of the array in the Maximum Array Size input box.

This determines the number of elements within an array to be generated for sorting analysis by the program.

**Step 2**: Select a Sorting Case

Choose a case from the "Sorting Case" dropdown menu:

Best Case: Pre-sorted array.

Average Case: Randomized array.

Worst Case: Reverse-sorted array.

**Step 3**: Select Sorting Methods

From the given list of sorting, choose one or more strategies to work out.

If you want to choose two or more methods, right-click on top of it, or with your keyboard, use CTRL and click on the desired methods.

**Step 4**: Run the Sorting Program

Now click on the “Run Sorting Program” button that is shown at the end of the screen.

As a result, the arrays will be generated, the required sorting analysis is to be conducted and the outcome is that all results should be saved to a CSV file.

**Step 5**: View Results

To view the results:

When you are ready click on “Open Results CSV” to view the sorting analysis report.

Press “Open Test Data” button as a result of which you will see the generated arrays.

**Step 6**: Generate a Graph

To edit the graph or to generate a new graph, simply click on “Generate Graph”.

Choose which bring out which columns you want to have in the graph (for instance, sorting steps of certain algorithms).

A graph will be shown, and it will be exported also as a PNG image in the results folder.

---------------------------------------------------------------------------------------------

# Note

-- If only one of the sorting methods is chosen, then this methods’ run time will be compared to the theoretical best estimate of its complexity.

-- The feature means that the name of the result and data file is generated in accord to the time of the program’s executing.

# About the Project

-- Due to the practical implementation of the project a unique connection between theoretical comprehension of the sorting algorithm and testing of their performance could be made. It evolved from an attempt to improve algorithm instruction within an educational platform.

---------------------------------------------------------------------------------------------
# Screenshots
-- To be added soon

---------------------------------------------------------------------------------------------
# Simulation
-- To be added soon 

---------------------------------------------------------------------------------------------

# Troubleshooting

1. Python Not Found

Make sure you have installed Python on your machine, and it is set in your system’s Path.

After the installation most application to be run requires that the terminal or the command prompt has to be restarted.

2. Missing Dependencies

Run the following command to reinstall dependencies:

It can be used by typing pips install -r requirements.txt

3. GUI Not Opening

Make sure you are executing the right script with the name sorting_gui.py and with Python 3.

4. CSV or Graph File Not Found

The program requires that it has finished the execution process before opening the files.

---------------------------------------------------------------------------------------------

# Contact

For any further inquiries, comments and contribution, feel free to contact me on twitter (@0xtkmo).

----------------------------------------------------------------------------------------------

Thank you for using our application. Happy Learning! 
