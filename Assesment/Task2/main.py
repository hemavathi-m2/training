import csv
import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv

# File paths
base_path = Path(__file__).parent

# Requirement 1: Load API key from .envS
load_dotenv(base_path / ".env")
api_key = os.getenv("API_KEY")

# Requirement 2: Read employees.csv
employees = []

with open(base_path / "employees.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["salary"] = int(row["salary"])
        employees.append(row)

# Requirement 3: Save employee data to JSON
with open(base_path / "employees.json", "w", encoding="utf-8") as file:
    json.dump(employees, file, indent=4)

# Requirement 4: Find employees earning above 50000
high_earners = []

for employee in employees:
    if employee["salary"] > 50000:
        high_earners.append(employee)

print("Rows read:", len(employees), "| High earners:", len(high_earners))

# Requirement 5: Save high earners to CSV
if employees:
    with open(
        base_path / "high_earners.csv", "w", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=employees[0].keys())
        writer.writeheader()
        writer.writerows(high_earners)

# Requirement 6, 7 and 8: Get users from API
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
    response.raise_for_status()

    users = response.json()

    for user in users[:1]:
        print(user["id"], "-", user["name"], "-", user["email"])

    # Read nested JSON using get()
    user_data = []

    for user in users:
        address = user.get("address", {})

        user_data.append(
            {
                "id": user.get("id"),
                "name": user.get("name"),
                "city": address.get("city"),
            }
        )

    # Save API data to users.json
    with open(base_path / "users.json", "w", encoding="utf-8") as file:
        json.dump(user_data, file, indent=4)

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error")

except requests.exceptions.HTTPError as error:
    print("HTTP error:", error)

# Requirement 9: Check 404 error
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/9999", timeout=5
    )

    response.raise_for_status()

except requests.exceptions.HTTPError:
    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        print("HTTP error:", response.status_code)

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error")
