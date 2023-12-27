class Car:
    def __init__(self, make, model):
        # Private attribute
        self._make = make
        # Private attribute
        self._model = model
        # Protected attribute
        self._mileage = 0

    # Public method
    def drive(self, miles):
        print(f"Driving {miles} miles.")
        self._mileage += miles

    # Public method
    def display_info(self):
        print(f"{self._make} {self._model}, Mileage: {self._mileage} miles")


# Example usage
if __name__ == "__main__":
    my_car = Car("Honda", "Civic")

    # Accessing public method
    my_car.drive(100)
    my_car.display_info()

    # Trying to access private attribute directly (not recommended)
    # This will work, but it's against the encapsulation principle
    print(my_car._make)
