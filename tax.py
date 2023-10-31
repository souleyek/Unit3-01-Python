import math


def main():
    # Get subtotal from
    subtotal = float(input("Enter the subtotal ($): "))
    # calculate area and perimeter
    Tax = subtotal * 0.07
    total = subtotal + Tax

    # shows Tax and Total
    print("")
    print("Tax = {} $".format(Tax))
    print("total = {} $".format(total))


if __name__ == "__main__":
    main()
