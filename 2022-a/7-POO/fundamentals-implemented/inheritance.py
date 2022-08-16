# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def who_is_this(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def who_is_this(self):
        super().swim()
        # print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.who_is_this()
peggy.swim()
peggy.run()