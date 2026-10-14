"""Student Performance Analytics System."""
from pathlib import Path
import numpy as np
import pandas as pd

DATA_FILE = Path(__file__).with_name("students.csv")

def load_data(file_path=DATA_FILE):
    """Load and validate the student dataset."""
    df = pd.read_csv(file_path)
    required = {"Student_ID", "Name", "Maths", "Python", "DBMS", "Attendance"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
    return df

def analyze_data(df):
    """Calculate student averages and summary statistics."""
    subjects = ["Maths", "Python", "DBMS"]
    result = df.copy()
    result["Average_Marks"] = np.round(result[subjects].mean(axis=1), 2)
    subject_averages = result[subjects].mean().round(2)
    overall_average = round(float(result["Average_Marks"].mean()), 2)
    attendance_average = round(float(result["Attendance"].mean()), 2)
    return result, subject_averages, overall_average, attendance_average

def main():
    df = load_data()
    result, subject_averages, overall_average, attendance_average = analyze_data(df)
    print("STUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 38)
    print(f"Total students: {len(result)}")
    print("\nAverage marks by subject:")
    for subject, average in subject_averages.items():
        print(f"- {subject}: {average:.2f}")
    print(f"Overall average marks: {overall_average:.2f}")
    print(f"Average attendance: {attendance_average:.2f}%")
    print("\nStudent averages (first 5 rows):")
    print(result[["Student_ID", "Name", "Average_Marks", "Attendance"]].head().to_string(index=False))

if __name__ == "__main__":
    main()
