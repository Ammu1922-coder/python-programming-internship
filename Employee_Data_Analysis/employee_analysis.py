import pandas as pd

def load_data(file_path):
    """
    Load employee data from CSV file.
    """
    try:
        df = pd.read_csv(file_path)
        print("Employee dataset loaded successfully.\n")
        return df

    except FileNotFoundError:
        print("Error: employees.csv file not found.")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None


def average_salary(df):
    """
    Calculate average salary.
    """
    avg_salary = df["Salary"].mean()
    print(f"\nAverage Salary: {avg_salary:.2f}")


def department_count(df):
    """
    Count employees in each department.
    """
    print("\nDepartment Count:")
    print(df["Department"].value_counts())


def filter_employees(df):
    """
    Filter employees above salary threshold.
    """
    while True:

        try:

            threshold = float(input("\nEnter Salary Threshold: "))

            filtered = df[df["Salary"] > threshold]

            print("\nFiltered Employees:\n")

            print(filtered)

            filtered.to_csv("filtered_employees.csv", index=False)

            print("\nFiltered data exported successfully as 'filtered_employees.csv'.")

            break

        except ValueError:
            print("Please enter a valid salary.")


def main():

    file_path = "employees.csv"

    df = load_data(file_path)

    if df is not None:

        print(df.head())

        average_salary(df)

        department_count(df)

        filter_employees(df)


if __name__ == "__main__":
    main()