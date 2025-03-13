import numpy as np
random_array = np.random.randint(0, 100, (3, 3,))
print("The array is:")
print(random_array)

def mean():
    mean_value = np.mean(random_array)
    print(mean_value)
    return (mean_value)

def median(): 
    median_value = np.median(random_array)
    print(median_value)
    return (median_value)


def variance():
    variance_value = np.var(random_array)
    print(variance_value)
    return (variance_value)


def deviation():
    standard_deviation_value = np.std(random_array)
    print(standard_deviation_value)
    return (standard_deviation_value)


def min():
    min_value = np.min(random_array)
    print(min_value)
    return (min_value)  


def max():
    max_value = np.max(random_array)
    print(max_value)
    return (max_value)

while (True):
    try:
        print("choose the given input: mean, median, variance, deviation, min, max")
        choose_the_input = input("Enter the input: ")
        match choose_the_input:
            case "mean":
                mean() 
            case "median":
                median()
            case "variance":
                variance()
            case "deviation":
                deviation()
            case "min":
                min()
            case "max":
                max()
            case default:
                print("give the valid input")
    except ValueError: 
        print("Enter the valid input")

    cont = input("Do you want to perfom another Calculation (yes/no)!:").lower().strip()

    if cont == 'yes':
        continue
    elif cont == 'no':
        print("Thank you for using Statistics Caculator! Good Bye!")
        break

    else:
        print("Invalid Input!")
        break