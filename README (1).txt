# Sorting Algorithm Performance Evaluation Application (Sortify Analyzer).

# Overview

This Sorting Algorithm GUI tool is a live Python application with a user interface, built to compare the efficiency of different sorting techniques. They allow flexible configuration of tests, generation of test data and the last but not the least-visualization of the results. The application is ideal for students, educators as well as developers who need to study performance and analyze various sorting strategies under various constraints.

---------------------------------------------------------------------------------------------

# Features

## Sorting Algorithms: Contains six important types of sorting program:

### Insertion Sort

### Merge Sort

### Bubble Sort

### Quick Sort

### Heap Sort

### Radix Sort

---------------------------------------------------------------------------------------------

##Sorting Cases:

### Best Case (Pre-sorted array)

### Average Case (Randomly shuffled array is chosen)

### Worst Case (Reverse-sorted array)

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

(A) Sorting Case: Select one of the three available cases:

Best Case

Average Case

Worst Case

(B) Sorting Methods: Choose one or more sorting methods from the list.

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
-------------------------------------------------------------------------------------------------------------------------------------------
# Prerequisites

Before you begin, ensure that you have the following installed on your system:

1. Python

The application requires Python to run.

Download and install Python from the official Python website.

During installation, make sure to check the box that says "Add Python to PATH".

To verify the installation, open a terminal or command prompt and type:

python --version

This should display the installed Python version.

2. Visual Studio Code (VS Code) (Optional but Recommended)

VS Code is a powerful code editor for running and debugging Python applications.

Download and install VS Code from the official VS Code website.

Install the Python extension in VS Code for better support:

Open VS Code.

Go to the Extensions tab (or press Ctrl+Shift+X).

Search for "Python" and install the extension provided by Microsoft.

---------------------------------------------------------------------------------------------

# How to Set Up and Run the Application

Step 1: Extract the ZIP File

Get the path to the folder which contains the program in ZIP format.

For Windows user, right click directly on the file and then you option “Extract All”.

Select a desired folder and click on “Extract”.

Step 2: Open the Application Folder

User should open the extracted folder.

In this case, you should see at least one plain text  file which is our main program script, and a few other files that may be linked to it.

Step 3 :download the desired libraries Launch the Application

Option 1: Using Python

In the terminal, run the following command to start the application:

python project.py

This means that once the application is launched; you will see the GUI window through which you will be running the tool.

 





