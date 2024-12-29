import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import subprocess
import math
import random
import csv
import sys
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import ast

# Increase recursion limit to handle large arrays
sys.setrecursionlimit(3000)

result_file = None
arrays_data_file = None  # Global variable to store the CSV file for arrays


def generate_result_file():
    # Generate a unique filename based on the current timestamp.
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"sorting_results_{timestamp}.csv"


def save_results_to_csv(result_file, method_names, array_size, steps_array, expected_steps=None, min_steps=None):
    with open(result_file, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the header row if the file is empty
        if file.tell() == 0:
            header = ["ArraySize"] + method_names
            if expected_steps is not None:
                header.append("ExpectedSteps")
            if min_steps is not None:
                header.append("MinSteps")
            writer.writerow(header)

        # Write the data row
        row = [array_size] + steps_array
        if expected_steps is not None:
            row.append(expected_steps)
        if min_steps is not None:
            row.append(min_steps)
        writer.writerow(row)


def insertion_sort(arr, steps):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            steps[0] += 1
        arr[j + 1] = key
        steps[0] += 1


def merge_sort(arr, steps):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, steps)
        merge_sort(right, steps)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            steps[0] += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            steps[0] += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            steps[0] += 1
            k += 1


def bubble_sort(arr, steps):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            steps[0] += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps[0] += 1


def quick_sort(arr, steps):
    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high, steps)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)


def partition(arr, low, high, steps):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        steps[0] += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps[0] += 1
    return i + 1


def heap_sort(arr, steps):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
            steps[0] += 1

        if right < n and arr[right] > arr[largest]:
            largest = right
            steps[0] += 1

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            steps[0] += 1
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        steps[0] += 1
        heapify(arr, i, 0)


def radix_sort(arr, steps):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp, steps)
        exp *= 10


def counting_sort_for_radix(arr, exp, steps):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        count[(arr[i] // exp) % 10] += 1
        steps[0] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]
        steps[0] += 1

    for i in range(n - 1, -1, -1):
        output[count[(arr[i] // exp) % 10] - 1] = arr[i]
        count[(arr[i] // exp) % 10] -= 1
        steps[0] += 1

    for i in range(n):
        arr[i] = output[i]
        steps[0] += 1


def input_array(arr, num_elements):
    arr.clear()
    arr.extend(range(1, num_elements + 1))


def input_array_worst(arr, num_elements):
    arr.clear()
    arr.extend(range(num_elements, 0, -1))


def input_array_average(arr, num_elements):
    arr.clear()
    arr.extend(range(1, num_elements + 1))

    for start in range(0, num_elements, 20):
        end = min(start + 20, num_elements)  # Ensure we don't go out of bounds

        if end - start == 20:
            # Apply the specified pattern for 20 elements
            arr[start + 1], arr[start + 17] = arr[start + 17], arr[start + 1]  # 2nd <-> 18th
            arr[start + 3], arr[start + 8] = arr[start + 8], arr[start + 3]  # 4th <-> 9th
            arr[start + 2], arr[start + 6] = arr[start + 2], arr[start + 6]  # 3rd <-> 7th
            arr[start + 4], arr[start + 12] = arr[start + 12], arr[start + 4]  # 5th <-> 13th
            arr[start + 5], arr[start + 14] = arr[start + 14], arr[start + 5]  # 6th <-> 15th
            arr[start + 10], arr[start + 16] = arr[start + 16], arr[start + 10]  # 11th <-> 17th
        elif end - start == 15:
            # Apply the specified pattern for 15 elements
            arr[start + 1], arr[start + 10] = arr[start + 10], arr[start + 1]  # 2nd <-> 11th
            arr[start + 3], arr[start + 7] = arr[start + 7], arr[start + 3]  # 4th <-> 8th
            arr[start + 5], arr[start + 12] = arr[start + 12], arr[start + 5]  # 6th <-> 13th
            arr[start + 6], arr[start + 14] = arr[start + 14], arr[start + 6]  # 7th <-> 15th

        # If the chunk has exactly 10 elements
        if end - start == 10:
            # Apply the specified pattern for 10 elements
            arr[start + 1], arr[start + 7] = arr[start + 7], arr[start + 1]  # 2nd <-> 8th
            arr[start + 3], arr[start + 8] = arr[start + 8], arr[start + 3]  # 4th <-> 9th
            arr[start + 6], arr[start + 2] = arr[start + 2], arr[start + 6]  # 3rd <-> 7th

        # If the chunk has fewer than 10 elements (e.g., the last group)
        elif end - start == 5:
            # Apply the specified pattern for 5 elements
            arr[start + 1], arr[start + 3] = arr[start + 3], arr[start + 1]  # 2nd <-> 4th
            arr[start + 2], arr[start + 4] = arr[start + 4], arr[start + 2]  # 3nd <-> 5th


def calculate_asymptotic_steps(method_index, num_elements, case):
    if method_index == 0:  # Insertion Sort
        if case == 1:  # Best Case
            return int(num_elements - 1)
        elif case == 2:  # Average Case
            return int((num_elements * (num_elements - 1)) // 4)
        elif case == 3:  # Worst Case
            return int((num_elements * (num_elements - 1)) // 2)
    elif method_index == 1:  # Merge Sort
        return int(num_elements * math.log2(num_elements))
    elif method_index == 2:  # Bubble Sort
        if case == 1:  # Best Case
            return int(num_elements - 1)
        elif case == 2:  # Average Case
            return int((num_elements * (num_elements - 1)) // 4)
        elif case == 3:  # Worst Case
            return int((num_elements * (num_elements - 1)) // 2)
    elif method_index == 3:  # Quick Sort
        if case == 1 or case == 2:  # Best or Average Case
            return int(num_elements * math.log2(num_elements))
        elif case == 3:  # Worst Case
            return int((num_elements * (num_elements - 1)) // 4)
    elif method_index == 4:  # Heap Sort
        return int(num_elements * math.log2(num_elements))
    elif method_index == 5:  # Radix Sort
        max_elem = num_elements
        num_digits = 0
        while max_elem > 0:
            max_elem //= 10
            num_digits += 1
        return int(num_elements * num_digits)
    return 0  # Default for invalid method_index


def user_sort_selection(result_file, arr, chosen_methods, num_elements, case):
    methods = [insertion_sort, merge_sort, bubble_sort, quick_sort, heap_sort, radix_sort]
    method_names = ["Insertion Sort", "Merge Sort", "Bubble Sort", "Quick Sort", "Heap Sort", "Radix Sort"]

    steps_array = []
    for method_index in chosen_methods:
        steps = [0]  # Initialize steps for each method
        methods[method_index](arr[:], steps)  # Use a copy of the array
        steps_array.append(steps[0])

    if len(chosen_methods) == 1:
        # Compare with asymptotic efficiency if only one method is selected
        asymptotic_steps = calculate_asymptotic_steps(chosen_methods[0], num_elements, case)

        # Save results to CSV, include expected steps
        save_results_to_csv(
            result_file,
            [method_names[chosen_methods[0]]],
            num_elements,
            [steps_array[0]],

            expected_steps=asymptotic_steps
        )
    else:
        # Compare multiple methods
        min_steps = min(steps_array)  # Identify the method with the minimum steps

        # Save results to CSV
        save_results_to_csv(
            result_file,
            [method_names[i] for i in chosen_methods],
            num_elements,
            steps_array,
            min_steps=min_steps
        )


def detect_case(array):
    global case2
    """
    Detects if the array is in Best Case, Worst Case, or Average Case for sorting.   """

    if array == sorted(array):
        case2 = 1  # Best Case
        return "Best Case"  # Already sorted in ascending order
    elif array == sorted(array, reverse=True):
        case2 = 3  # Worst Case
        return "Worst Case"  # Sorted in descending order
    else:
        case2 = 2  # Average Case
        return "Average Case"  # Randomized order


arrays_data = []


def process_excel_file(file_path):
    """
    Reads an Excel file and extracts arrays from the 'Array' column.
    """
    global arrays_data
    arrays_data = []  # Reset global variable
    try:
        df = pd.read_excel(file_path)

        # Check if the required column exists
        if "Array" not in df.columns:
            messagebox.showerror("Error", "The Excel file must contain an 'Array' column.")
            print("Error: 'Array' column not found in the Excel file.")
            return None

        print("Raw 'Array' Column Data:", df["Array"].tolist())

        # Process each row in the "Array" column
        for idx, value in df["Array"].dropna().items():
            try:
                # Use _eval to validate and convert the value
                array = ast.literal_eval(value)
                if isinstance(array, list):  # Ensure it's a list
                    arrays_data.append(array)
                else:
                    print(f"Row {idx} is not a valid list: {value}")
            except (ValueError, SyntaxError) as e:
                print(f"Error processing row {idx}: {value}. Error: {e}")

        print("Extracted Arrays Data:", arrays_data)

        if not arrays_data:
            messagebox.showerror("Error", "No valid arrays found in the file.")
            print("Error: No valid arrays found in the Excel file.")
            return None

        return arrays_data

    except Exception as e:
        messagebox.showerror("Error", f"Failed to process Excel file: {e}")
        print(f"Exception while processing Excel file: {e}")
        return None


def process_csv_file(file_path):
    """
    Reads a CSV file and extracts arrays from the 'Array' column.
    """
    global arrays_data
    arrays_data = []  # Reset global variable
    try:
        df = pd.read_csv(file_path)

        # Check if the required column exists
        if "Array" not in df.columns:
            messagebox.showerror("Error", "The CSV file must contain an 'Array' column.")
            print("Error: 'Array' column not found in the CSV file.")
            return None

        print("Raw Array Column Data:", df["Array"].tolist())

        # Process each row in the "Array" column
        for idx, value in df["Array"].dropna().items():
            try:
                # Use eval to validate and convert the value
                array = ast.literal_eval(value)
                if isinstance(array, list):
                    arrays_data.append(array)
                else:
                    print(f"Row {idx} is not a valid list: {value}")
            except (ValueError, SyntaxError) as e:
                print(f"Error processing row {idx}: {value}. Error: {e}")

        print("Extracted Arrays Data:", arrays_data)

        if not arrays_data:
            messagebox.showerror("Error", "No valid arrays found in the file.")
            print("Error: No valid arrays found in the CSV file.")
            return None

        return arrays_data

    except Exception as e:
        messagebox.showerror("Error", f"Failed to process CSV file: {e}")
        print(f"Exception while processing CSV file: {e}")
        return None


excel_data = None  # Global variable to store the extracted data


def extract_data_from_file():
    global excel_data
    file_path = filedialog.askopenfilename(
        title="Select File",
        filetypes=[("Excel and CSV Files", ".xlsx *.csv"), ("All Files", ".*")]
    )
    if file_path:
        # Determine the file type based on the extension
        if file_path.endswith(".xlsx"):
            excel_data = process_excel_file(file_path)  # Process Excel file
        elif file_path.endswith(".csv"):
            excel_data = process_csv_file(file_path)  # Process CSV file
        else:
            messagebox.showerror("Error", "Unsupported file format. Please select an Excel or CSV file.")
            return

        print("Extracted Data:", excel_data)

        if excel_data is not None:
            messagebox.showinfo("Success", "File data has been loaded successfully!")
        else:
            messagebox.showerror("Error", "Failed to load data from the file.")


def run_sorting_program():
    global result_file, arrays_data_file, excel_data, arrays_data
    try:
        result_file = generate_result_file()  # Generate a new file name for every run

        chosen_methods = list(listbox_sort_methods.curselection())

        if not chosen_methods:
            raise ValueError("Please select at least one sorting method.")

        # Check if Excel data was loaded
        if excel_data is not None:

            # Use the extracted data from Excel
            arr2 = arrays_data
            print("Loaded arrays_data:", arr2)

            arrays_data_file = f"generated_arrays_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

            try:
                with open(arrays_data_file, 'w', newline='') as file:
                    writer = csv.writer(file)

                    writer.writerow(["Array Size", "Original Array"])

                    # Process each array from the Excel sheet
                    for idx, array in enumerate(arr2):
                        steps = []
                        detect_case(array)
                        # Perform sorting and record the number of steps
                        user_sort_selection(result_file, array, chosen_methods, len(array), case2)
                        # Write the results to the file
                        writer.writerow([len(array), array])

                messagebox.showinfo(
                    "Success",
                    f"Sorting completed. Results saved to {result_file}!\nGenerated arrays saved to {arrays_data_file}."
                )


            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            # return this  none to remove the Excel sheet and enter automatic results if needed
            excel_data = None
            arrays_data = []
            return

        else:
            size = int(size_entry.get())

            case = sorting_cases.index(case_selection.get()) + 1
            # Generate arrays based on selected case
            arrays_data_file = f"generated_arrays_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

            try:
                # Open the CSV file for writing
                with open(arrays_data_file, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Array Size", "Generated Array"])

                    # Generate arrays and write to the file
                    for num_elements in range(5, size + 1, 5):
                        arr = []  # Reinitialize arr for each iteration
                        if case == 1:
                            input_array(arr, num_elements)
                        elif case == 2:
                            input_array_average(arr, num_elements)
                        elif case == 3:
                            input_array_worst(arr, num_elements)

                            # Write the array size and the generated array to the CSV file
                        writer.writerow([num_elements, arr[:]])
                        arrays_data.append(arr)
                        # Perform sorting for each generated array
                        user_sort_selection(result_file, arr, chosen_methods, num_elements, case)

                messagebox.showinfo(
                    "Success",
                    f"Sorting completed. Results saved to {result_file}!\nGenerated arrays saved to {arrays_data_file}."
                )

            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")

    finally:

        print("Array generation and sorting attempt completed.")
        # Break out of the function to enable automatic results
        return  # Exit the function here


def open_csv(file_path):
    try:
        if file_path and os.path.exists(file_path):
            if os.name == "nt":  # For Windows
                os.startfile(file_path)
        else:
            messagebox.showerror("Error", "No file found or file doesn't exist.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file: {e}")


def generate_graph():
    try:
        if not result_file or not os.path.exists(result_file):
            messagebox.showerror("Error", "No results found. Please run the sorting program first.")
            return

        data = pd.read_csv(result_file)

        def confirm_columns():
            selected_columns = [listbox_columns.get(i) for i in listbox_columns.curselection()]
            if not selected_columns:
                messagebox.showerror("Error", "Please select at least one column to plot.")
                return

            column_window.destroy()
            plt.figure(figsize=(10, 6))

            for column in selected_columns:
                plt.plot(data["ArraySize"], data[column], marker='o', label=f"{column} Steps")

            plt.title("Comparison of Sorting Algorithms", fontsize=16, fontweight='bold')
            plt.xlabel("Array Size", fontsize=12)
            plt.ylabel("Number of Steps", fontsize=12)
            plt.legend(loc="best")
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.tight_layout()

            plt.show()

            plot_file = result_file.replace(".csv", ".png")
            plt.savefig(plot_file)
            messagebox.showinfo("Success", f"Graph saved to {plot_file}")

        column_window = tk.Toplevel(root)
        column_window.title("Select Columns for Graph")

        tk.Label(column_window, text="Select Columns to Include in the Graph:").pack(padx=10, pady=5)

        listbox_columns = tk.Listbox(column_window, selectmode=tk.MULTIPLE, height=10)
        for column in data.columns[1:]:
            listbox_columns.insert(tk.END, column)
        listbox_columns.pack(padx=10, pady=5)

        confirm_button = tk.Button(column_window, text="Generate Graph", command=confirm_columns, bg="green",
                                   fg="white")
        confirm_button.pack(padx=10, pady=10)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate graph: {e}")


root = tk.Tk()
root.title("Sorting Algorithm GUI")
root.configure(bg="#f0f0f0")

default_font = ("Arial", 12)
header_font = ("Arial", 14, "bold")

size_frame = tk.Frame(root, bg="#e6f7ff", bd=2, relief="ridge", padx=10, pady=10)
size_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
tk.Label(size_frame, text="Maximum Array Size:", font=default_font, bg="#e6f7ff").grid(row=0, column=0, padx=5, pady=5)
size_entry = tk.Entry(size_frame, font=default_font, width=10)
size_entry.grid(row=0, column=1, padx=5, pady=5)

case_frame = tk.Frame(root, bg="#e6f7ff", bd=2, relief="ridge", padx=10, pady=10)
case_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
tk.Label(case_frame, text="Sorting Case:", font=default_font, bg="#e6f7ff").grid(row=0, column=0, padx=5, pady=5)
sorting_cases = ["Best Case", "Average Case", "Worst Case"]
case_selection = ttk.Combobox(case_frame, values=sorting_cases, state="readonly", font=default_font, width=15)
case_selection.grid(row=0, column=1, padx=5, pady=5)

method_frame = tk.Frame(root, bg="#e6f7ff", bd=2, relief="ridge", padx=10, pady=10)
method_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
tk.Label(method_frame, text="Select Sorting Methods:", font=default_font, bg="#e6f7ff").grid(row=0, column=0, padx=5,
                                                                                             pady=5)
listbox_sort_methods = tk.Listbox(method_frame, selectmode=tk.MULTIPLE, height=6, font=default_font, width=20)
sorting_methods = ["Insertion Sort", "Merge Sort", "Bubble Sort", "Quick Sort", "Heap Sort", "Radix Sort"]
for method in sorting_methods:
    listbox_sort_methods.insert(tk.END, method)
listbox_sort_methods.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

note_frame = tk.Frame(root, bg="#fff2e6", bd=2, relief="ridge", padx=10, pady=10)
note_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
note_label = tk.Label(
    note_frame,
    text="Note: If a single sorting method is selected, it will be compared to its asymptotic complexity.",
    wraplength=400,
    font=("Arial", 10, "italic"),
    bg="#fff2e6",
    fg="#cc5500"
)
note_label.pack(padx=5, pady=5)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

run_button = tk.Button(button_frame, text="Run Sorting Program", command=run_sorting_program, bg="#4caf50", fg="white",
                       font=default_font, padx=10, pady=5)
run_button.grid(row=0, column=0, padx=10, pady=5)

open_csv_button = tk.Button(button_frame, text="Open Results CSV", command=lambda: open_csv(result_file), bg="#2196f3",
                            fg="white",
                            font=default_font, padx=10, pady=5)
open_csv_button.grid(row=0, column=1, padx=10, pady=5)

open_arrays_csv_button = tk.Button(button_frame, text="Open Test Data", command=lambda: open_csv(arrays_data_file),
                                   bg="#ffa500", fg="white",
                                   font=default_font, padx=10, pady=5)
open_arrays_csv_button.grid(row=0, column=2, padx=10, pady=5)

graph_button = tk.Button(button_frame, text="Generate Graph", command=generate_graph, bg="#9c27b0", fg="white",
                         font=default_font, padx=10, pady=5)
graph_button.grid(row=0, column=3, padx=10, pady=5)
excel_button = tk.Button(button_frame, text="Extract data from Excel Sheet", command=lambda: extract_data_from_file(),
                         bg="#ff5722", fg="white",
                         font=default_font, padx=10, pady=5)
excel_button.grid(row=0, column=4, padx=10, pady=5)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()