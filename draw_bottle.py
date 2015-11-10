class ParameterFunction(object):
    def __init__(self, x_function, y_function, t_min, t_max):
        self.x_function = x_function
        self.y_function = y_function
        self.t_min = t_min
        self.t_max = t_max

def define_functions():
    functions = []

    functions.append(ParameterFunction("-(526/7777)*(t**2)+(267763570/280366923)*t+(2243152976/484607583)", "t", 0.4, 10.5))
    functions.append(ParameterFunction("(13287614475747/100000000000000)*(t**2)-(16278470704229/5000000000000)*t+(2673519351937/100000000000)", "t", 10.5, 13.5))
    functions.append(ParameterFunction("0.125*t+(85/16)", "t", 13.5, 21.5))
    functions.append(ParameterFunction("8", "t", 21.5, 32.5))
    functions.append(ParameterFunction("(11443628834973/5000000000000000)*(t**3)-(26583850931771/100000000000000)*(t**2)+(2466875588189/250000000000)*t-(1104695652178/10000000000)", "t", 32.5, 44))
    functions.append(ParameterFunction("t-44", "44", 44, 48))
    functions.append(ParameterFunction("t-48", "-(3/80)*((t-48)**2)+(1/40)*(t-48)+1", 48, 52))
    functions.append(ParameterFunction("t-48", "((2*(t-48)-9)*(9*(t-48)-41))/10", 52, 53))

    return functions

def main():
    functions = define_functions()

    for function in functions:
        print function.x_function
        print function.y_function
        print function.t_min
        print function.t_max

if __name__ == "__main__":
    main()
