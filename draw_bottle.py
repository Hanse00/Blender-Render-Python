import numpy as np

gradient = 0.1

class ParameterFunction(object):
    def __init__(self, x_function, y_function, t_min, t_max):
        self.x_function = x_function
        self.y_function = y_function
        self.t_min = t_min
        self.t_max = t_max

class TwoDimentionalPos(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "x: {}, y: {}".format(self.x, self.y)

def define_functions():
    functions = []

    functions.append(ParameterFunction("t-48", "-(3.0/80.0)*((t-48)**2)+(1.0/40.0)*(t-48)+1", 48, 52))
    functions.append(ParameterFunction("t-48", "((2*(t-48)-9)*(9*(t-48)-41))/10.0", 52, 53))
    functions.append(ParameterFunction("-(526.0/7777.0)*(t**2)+(267763570.0/280366923.0)*t+(2243152976.0/484607583.0)", "t", 0.4, 10.5))
    functions.append(ParameterFunction("(13287614475747.0/100000000000000.0)*(t**2)-(16278470704229.0/5000000000000.0)*t+(2673519351937.0/100000000000.0)", "t", 10.5, 13.5))
    functions.append(ParameterFunction("0.125*t+(85.0/16.0)", "t", 13.5, 21.5))
    functions.append(ParameterFunction("8", "t", 21.5, 32.5))
    functions.append(ParameterFunction("(11443628834973.0/5000000000000000.0)*(t**3)-(26583850931771.0/100000000000000.0)*(t**2)+(2466875588189.0/250000000000.0)*t-(1104695652178.0/10000000000.0)", "t", 32.5, 44))
    functions.append(ParameterFunction("t-44", "44", 44, 48))

    return functions

def determine_points_for_function(function, gradient):
    points = []

    for t in np.arange(function.t_min, function.t_max, gradient):
        x = eval(function.x_function)
        y = eval(function.y_function)

        points.append(TwoDimentionalPos(x, y))

    return points

def determine_points_for_functions(functions, gradient):
    points = []

    for function in functions:
        points += determine_points_for_function(function, gradient)

    return points

def main():
    functions = define_functions()

    points = determine_points_for_functions(functions, gradient)

if __name__ == "__main__":
    main()
