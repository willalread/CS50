from datetime import date
import inflect
p = inflect.engine()
import sys


def main():
    try:
        birth = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    time = int((date.today() - birth).total_seconds()/60)
    print(p.number_to_words(time))

if __name__ == "__main__":
    main()
