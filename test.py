import csv

def count_column_b(csv_path):
    counts = {}
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            value_a = row[0]  # Assuming column A is at index 0
            value_b = row[1]  # Assuming column B is at index 1
            counts[value_a] = counts.get(value_a, 0) + int(value_b)
    return counts

def update_csv(csv1_path, csv2_path):
    counts = count_column_b(csv1_path)

    with open(csv2_path, 'r') as file:
        rows = list(csv.reader(file))

    for row in rows:
        value_a = row[0]  # Assuming column A is at index 0
        if value_a in counts:
            row.append(str(counts[value_a]))
        else:
            row.append("0")

    with open(csv2_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def main():
    csv1_path = input("Enter the path of the first CSV file (csv1): ")
    csv2_path = input("Enter the path of the second CSV file (csv2): ")

    update_csv(csv1_path, csv2_path)

    print("CSV2 updated successfully.")

if __name__ == "__main__":
    main()
