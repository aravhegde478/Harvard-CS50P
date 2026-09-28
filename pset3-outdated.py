import re


def main():
    date = input("Date: ")
    print(convert(date))


def convert(date):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # Format 1: 9/8/1636  (month/day/year)
    match = re.search(r"^(\d{1,2})/(\d{1,2})/(\d{4})$", date)
    if match:
        month = int(match.group(1))
        day = int(match.group(2))
        year = int(match.group(3))
        if 1 <= month <= 12 and 1 <= day <= 31:
            return f"{year}-{month:02}-{day:02}"

    # Format 2: September 8, 1636
    match = re.search(r"^([A-Za-z]+) (\d{1,2}), (\d{4})$", date)
    if match:
        month_name = match.group(1)
        day = int(match.group(2))
        year = int(match.group(3))
        if month_name in months and 1 <= day <= 31:
            month = months.index(month_name) + 1
            return f"{year}-{month:02}-{day:02}"

    raise ValueError("Invalid date format")


if __name__ == "__main__":
    while True:
        try:
            print(convert(input("Date: ")))
            break
        except ValueError:
            pass
