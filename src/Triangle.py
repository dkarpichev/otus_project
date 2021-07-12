from src.Basic_Figure import Figure


class Triangle(Figure):
    def __init__(self, *args):
        super().__init__()
        arg_list = []
        for i in args:
            arg_list.append(i)
        if len(arg_list) > 3 or len(arg_list) < 3:
            self.__class__ = None
        self.sides = arg_list
        self.is_it_string(self.sides)
