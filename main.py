# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Device:
    electrical = True

    def connect_device(self):
        print("connected")


class Mouse(Device):
    function = "HID"
    color = "black"
    shape = "oval"
# instance attribute

    def __init__(self, c, s):
        self.color = c
        self.shape = s

    def connect_device(self):
        print("Plugged")

m = Mouse("blue", "rectrangular")
m2 = Mouse("magenta", "round")

print(m.color)
print(m2.shape)

m.color = "red"
print(m.color)

print(m2.electrical)

m.connect_device()




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
