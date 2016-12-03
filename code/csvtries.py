import csv     # imports the csv module
import grid as g
import car
import truck

def run(dataset, width, height, exit):

    grid = g.Grid(width, height, exit)

    # open csv file
    f = dataset

    try:
        # create reader
        reader = csv.reader(f)

        # skip first line of csv file
        next(reader)

        # iterates the rows of the file in orders
        for row in reader:
            # check whether the vehicle is a car or a truck or a redcar
            if(row[0] == "car"):
                # get string of x coordinates
                str = row[1]

                # split this string
                list = str.split(", ")

                # save values from list
                x1 = list[0]
                x2 = list[1]

                # get string of y coordinates
                str = row[2]

                # split this string
                list = str.split(", ")

                # save values from list
                y1 = list[0]
                y2 = list[1]

                newCar = car.Car(x1, x2, y1, y2, row[3], row[4])
                # add car with the values from csv file to the list of cars
                grid.all_vehicles.append(newCar)

            elif(row[0] == "truck"):
                # get string of x coordinates
                str = row[1]

                # split this string
                list = str.split(", ")

                # save values from list
                x1 = list[0]
                x2 = list[1]
                x3 = list[2]

                # get string of y coordinates
                str = row[2]

                # split this string
                list = str.split(", ")

                # save values from list
                y1 = list[0]
                y2 = list[1]
                y3 = list[2]

                newTruck = truck.Truck(x1, x2, x3, y1, y2, y3, row[3], row[4])
                # add car with the values from csv file to the list of cars
                grid.all_vehicles.append(newTruck)

            elif(row[0] == "redcar"):
                # get string of x coordinates
                str = row[1]

                # split this string
                list = str.split(", ")

                # save values from list
                x1 = list[0]
                x2 = list[1]

                # get string of y coordinates
                str = row[2]

                # split this string
                list = str.split(", ")

                # save values from list
                y1 = list[0]
                y2 = list[1]

                newCar = car.Car(x1, x2, y1, y2, row[3], row[4])
                # add car with the values from csv file to the list of cars
                grid.all_vehicles.append(newCar)

    finally:
        # close file
        f.close()
        grid.removeEmptyGrid()
        return grid
