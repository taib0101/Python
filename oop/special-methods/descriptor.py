# Descriptor is a python object's method, which customize the access another instance's attribute through __get__, __set__, __delete__,
# that instance's attribute is also instance of another class


# class Descriptor: ------------------------------------|
#     def __get__(self, instance, value): -------------|-------------|
#         pass                                        |             |
#                                                    |             |
# class Owner: -------------------------------------|----|        |
#     instance_of_descriptor = Descriptor() <----- |    |        |
#                                                      |        |
# instance = Owner()  <-------------------------------|        |
#                                                             |
# print(instance.instance_of_descriptor) <-------------------|

class Descriptor:

    def __init__(self, number1: int = None):
        self.number1 = number1

    def __get__(self, instance, owner) -> str:
        print("From Owner's instance is : ", instance.__dict__)
        return "It called from Owner's instance"

    def __set__(self, instance, value) -> None:
        instance.__dict__['number2'] = value # is set value Owner's number2 property**
        print(f"value of {value} will set from Owner's instance\n")

    def __delete__(self, instance) -> None:
        print("Deleted")

class Owner:
    number2: int = None # **
    instance_of_descriptor = Descriptor(100)

    print("instance_of_descriptor dict : ", instance_of_descriptor.__dict__)
    print()

instance = Owner()

instance.number2 = 200
print(instance.instance_of_descriptor) # this directly hit to Descriptor's __get__ method
print()

instance.instance_of_descriptor = 300 # this directly hit to Descriptor's __set__ method
print(instance.instance_of_descriptor) # this directly hit to Descriptor's __get__ method
print()

del instance.instance_of_descriptor # this directly hit to Descriptor's __delete__ method
