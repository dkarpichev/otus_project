from src.Basic_Figure import Figure


class Rectangle(Figure):
    def __init__(self, *sides):
        super().__init__()
        arg_list = []
        for i in sides:
            arg_list.append(i)
        if len(arg_list) > 2 or len(arg_list) < 2:
            raise ValueError("Enter the value for the two sides")
        self.sides = arg_list
        self.is_it_string(self.sides)
