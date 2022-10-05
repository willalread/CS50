from datetime import date
import sys


def main():
    try:
        birth = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    print(birth)

if __name__ == "__main__":
    main()
