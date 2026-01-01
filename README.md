# 📘 GradeBook Analyzer

A beginner-friendly Python CLI project that automates student grade analysis.
This mini project is built as part of the course **Programming for Problem Solving using Python**.

---

## 👤 Author

* **Name:** Krishyangi Dixit
---

## 🎯 Project Objective

Lecturers often need a quick way to calculate statistics and assign grades for student marks.
The **GradeBook Analyzer** simplifies this by:

* Accepting student marks (manual input or CSV file)
* Calculating statistical values
* Assigning grades automatically
* Displaying results in a clean tabular format

---

## 🧠 Features

* Manual entry of student names and marks
* CSV file import support
* Calculates:

  * Average
  * Median
  * Highest score
  * Lowest score
* Automatic grade assignment (A–F)
* Pass / Fail classification using list comprehension
* Menu-driven program with repeat execution

---

## 📁 Project Structure

```
gradebook_analyzer/
│
├── gradebook.py
├── marks.csv
└── README.md
```

---

## 📝 CSV File Format

The CSV file should contain **no headers** and follow this format:

```
Alice,78
Bob,92
Sam,55
Nina,88
Raj,39
```

---

## ▶️ How to Run the Program

1. Open the project folder in **VS Code**
2. Open the terminal
3. Run the program using:

```
python gradebook.py
```

(or `python3 gradebook.py` if required)

4. Choose an option from the menu:

   * `1` → Manual input
   * `2` → CSV file input
   * `3` → Exit program

---

## 📊 Sample Output

```
Name    Marks   Grade
------------------------
Alice   78      C
Bob     92      A
Sam     55      F
Nina    88      B
Raj     39      F
```

---

## 🧪 Concepts Used

* Dictionaries
* Functions
* Loops (`for`, `while`)
* Conditional statements (`if-elif-else`)
* List comprehension
* File handling (CSV)
* Basic statistics

---

## ✅ Submission Checklist

* [x] Working CLI program
* [x] Manual and CSV input
* [x] Statistical analysis
* [x] Grade assignment
* [x] Pass/Fail filtering
* [x] Formatted output table

---

## 🚀 Future Enhancements (Optional)

* Export results to CSV
* Add graphical analysis
* Handle CSV files with headers

---

Happy coding and stay curious! ✨
