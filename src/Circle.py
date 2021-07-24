from src.Basic_Figure import Figure


class Circle(Figure):
    def __init__(self, *radius):
        super().__init__()
        arg_list = []
        for i in radius:
            arg_list.append(i)
        if len(arg_list) > 1 or len(arg_list) < 1:
            raise ValueError("Use only one value")
        self.sides = arg_list
        self.is_it_string(self.sides)
