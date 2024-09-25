# Sorting Algorithm Visualizer

### A Python-based visualization tool for exploring the behavior of various sorting algorithms.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [System Requirements](#system-requirements)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Sorting Algorithms Implemented](#sorting-algorithms-implemented)
- [Code Structure](#code-structure)
- [Future Enhancements](#future-enhancements)
---

## Project Overview

**Sorting Algorithm Visualizer** is a Python application that helps users visually explore how different sorting algorithms work. The tool uses the Pygame library to display graphical representations of sorting processes in real-time, allowing users to see how elements move and change throughout the execution of various algorithms. The project is aimed at helping learners and developers understand the inner workings of sorting algorithms through an intuitive and engaging visual interface.

---

## Features

- **Real-Time Visualizations**: Watch how sorting algorithms work in real-time with dynamically changing arrays.
- **Interactive Controls**: Start, stop, and reset sorting processes; switch between different algorithms using a dropdown menu.
- **Multiple Sorting Algorithms**: Compare different algorithms like Bubble Sort, Quick Sort, Merge Sort, and more.
- **Custom Sorting Order**: Choose between ascending or descending order to see how algorithms behave differently.
- **Dropdown Menu for Algorithm Selection**: Easily select sorting algorithms through a user-friendly dropdown interface.
- **Adjustable Speed**: Control the speed of the sorting animations.

---

## System Requirements

To run the **Sorting Algorithm Visualizer**, ensure you have the following system requirements:

- **Python**: Version 3.6 or later
- **Pygame**: Version 2.0 or later (can be installed via pip)
- **Operating System**: Compatible with Windows, macOS, and Linux
- **Memory**: 1GB of RAM or higher

---

## Installation and Setup

### Step 1: Clone the Repository

To get started, clone the repository using the following command:

```
git clone https://github.com/jacobchilds221/Sorting-Algorithm-Visualizer.git
```
## Step 2: Install Dependencies
Navigate to the project directory and install the necessary dependencies:
```
cd sorting-visualizer
pip install -r requirements.txt
```
Or manually install Pygame if it’s not included:
```
pip install pygame
```
## Step 3: Run the Application
After installing the dependencies, you can run the application with:
```
python sorting_visualizer.py
```
## Usage
Interface Overview:
Dropdown Menu: Select from different sorting algorithms to visualize.
Start Button: Begin the sorting process for the selected algorithm.
Reset Button: Reset the array and choose a new sorting algorithm or order.
Order Toggle: Choose between ascending or descending order for sorting.
Speed Control: Adjust the speed of the sorting process.

## Step-by-Step Guide:
Select Sorting Algorithm: Use the dropdown menu to choose which sorting algorithm to visualize.
Start Sorting: Press the space bar to start the selected sorting process.
Reset: Press "R" to reset the array to its original unsorted state, and choose a different sorting algorithm if desired.
Change Sorting Order: Press "A" for ascending order or "D" for descending order before starting the sorting process.
Pause/Resume: The sorting can be paused and resumed at any point.

## Sorting Algorithms Implemented
The following sorting algorithms have been implemented in the Sorting Algorithm Visualizer:

Bubble Sort: A simple comparison-based algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

Insertion Sort: Iterates through the array and inserts each element into its correct position, building the sorted array one element at a time.

Selection Sort: Divides the list into a sorted and unsorted part and repeatedly selects the smallest element from the unsorted part and swaps it with the first unsorted element.

Merge Sort: A divide-and-conquer algorithm that splits the array into smaller arrays, sorts each of them, and merges them back together.

Quick Sort: Selects a pivot element, partitions the array into elements less than and greater than the pivot, and recursively sorts the partitions.

Heap Sort: Builds a binary heap from the input data, and then repeatedly extracts the maximum element to build the sorted array.

## Code Structure
The Sorting Algorithm Visualizer project is structured as follows:

sorting_visualizer.py: The main file that runs the application and manages user interactions.
draw_info.py: Contains the DrawInformation class responsible for handling the drawing of the visualization window, including array blocks and labels.
sorting_algorithms.py: Contains all the sorting algorithm implementations, including Bubble Sort, Insertion Sort, Merge Sort, and more.
dropdown.py: Handles the implementation of the dropdown menu for selecting different sorting algorithms.
input_handler.py: Manages user inputs like algorithm selection, sorting order, and reset functionality.

## Future Enhancements
There are several potential features and improvements planned for future versions:

Additional Sorting Algorithms: Implement more advanced algorithms such as Radix Sort, Bucket Sort, and TimSort.
Performance Metrics: Display metrics like time complexity, memory usage, and runtime performance for each sorting algorithm.
Customization: Allow users to customize the size of the array, sorting speed, and color schemes for better user experience.
Step-by-Step Visualization: Add the ability to visualize each individual step of the sorting process in more detail.
Improved GUI: Build a more comprehensive and intuitive graphical user interface with sliders for input and algorithm comparisons.
