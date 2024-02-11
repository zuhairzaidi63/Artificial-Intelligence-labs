def calculate_area(length, width):     # write function for area
    return length * width         # area = length * width so returning a area


def calculate_volume(length, width, height):   # function for volume calculation
    return length * width * height             # volume = length * width * height  so return it


def main():
    length = int(input("Enter length : "))  # taking length from user
    width = int(input("Enter width : "))    # taking width from user
    height = int(input("Enter height : "))  # taking height from user
    print("Area is", calculate_area(length, width))  # call calculate area function
    print("Volume is", calculate_volume(length, width, height))  # call calculate volume function
    print("\nCleaning Starts............")


main()
