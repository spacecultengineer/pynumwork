class onevalue:
    def factorial(val):
        num_list = ['1','2','3','4','5','6','7','8','9','0','-']
        val = str(val)
        for element in range(0, len(val)):
            if not val[element] in num_list:
                raise InvalidTypeError("The value contains invalid symbols for the action")
            else:
                val = int(val)
                if val <= 0:
                    raise InvalidNumError("Command 'onevalue.factorial(val)' is not avaliable for zero and negative numbers")

                indf = val-1
                for i in range(val-1):
                    val = val * indf
                    indf -= 1
                return val



class twovalue:
    def add(val1, val2):
        num_list = ['1','2','3','4','5','6','7','8','9','0','-', '.']
        for element in range(0, len(str(val1))):
            if not str(val1)[element] in num_list:
                raise InvalidTypeError("The value " + "'" + str(val1) + "'" + " contains invalid symbols for the action")
        for element in range(0, len(str(val2))):
            if not str(val2)[element] in num_list:
                raise InvalidTypeError("The value " + "'" + str(val2) + "'" + " contains invalid symbols for the action")
        resval = val1 + val2
        return resval

    def subtract(val1, val2):
        num_list = ['1','2','3','4','5','6','7','8','9','0','-', '.']
        for element in range(0, len(str(val1))):
            if not str(val1)[element] in num_list:
                raise InvalidTypeError("The value " + "'" + str(val1) + "'" + " contains invalid symbols for the action")
        for element in range(0, len(str(val2))):
            if not str(val2)[element] in num_list:
                raise InvalidTypeError("The value " + "'" + str(val2) + "'" + " contains invalid symbols for the action")
        resval = val1 - val2
        return resval

    def multiply(val1, val2):
        num_list = ['1','2','3','4','5','6','7','8','9','0','-', '.']
        for element in range(0, len(str(val1))):
            if not str(val1)[element] in num_list:
                raise InvalidTypeError("The value " + "'" + str(val1) + "'" + " contains invalid symbols for the action")
        for element in range(0, len(str(val2))):
            if not str(val2)[element] in num_list:
                raise InvalidTypeError("The value " + "'" + str(val2) + "'" + " contains invalid symbols for the action")
        resval = val1 * val2
        return resval

    def divide(val1, val2):
        num_list = ['1','2','3','4','5','6','7','8','9','0','-', '.']
        for element in range(0, len(str(val1))):
            if not str(val1)[element] in num_list:
                raise InvalidTypeError("The value " + "'" + str(val1) + "'" + " contains invalid symbols for the action")
        for element in range(0, len(str(val2))):
            if not str(val2)[element] in num_list:
                raise InvalidTypeError("The value " + "'" + str(val2) + "'" + " contains invalid symbols for the action")
        resval = val1 / val2
        return resval



class multipleaction:
    def solvemultipleaction(equation):
        num_list = ['1','2','3','4','5','6','7','8','9','0','-', '+', '*', '/', '(', ')', ' ', '.']
        for element in range(0, len(str(equation))):
            if not str(equation)[element] in num_list:
                raise InvalidTypeError("The value " + "'" + str(equation) + "'" + " contains invalid symbols for the action")
        resval = eval(equation)
        return resval






class consolediagram:
    def createlinear(dlist):
        dn = 0
        print(dlist[dn])
        dn += 1
        for i in range(int((len(dlist) - 1) / 2)):
            print(dlist[dn] + "|  " + "█" * dlist[dn + 1])
            dn += 2



class help:
    class onevalue:
        def factorial(self):
            print("HELP:    'onevalue.factorial(int)' - searches factorial of a number")
    class twovalue:
        def add(self):
            print("HELP:    'twovalue.add(int, int)' - adds two numbers")
        def subtract(self):
            print("HELP:    'twovalue.subtract(int, int)' - subtracts two values")
        def multiply(self):
            print("HELP:    'twovalue.multiply(int, int)' -  multiplies two numbers")
        def divide(self):
            print("HELP:    'twovalue.divide(int, int)' - divides two numbers")
    class multipleaction:
        def solvemultipleaction(self):
            print("HELP:    'multipleaction.solvemultipleaction(str)' - solves quotation with multiple actions")
    class consolediagram():
        def createlinear(self):
            print("HELP:    'consolediagram.createlinear([str,str,int,str,int,...])' - creates linear console diagram")
    class miscellaneousnum:
        def roundvalue(self):
            print("HELP:    'miscellaneousnum.roundvalue(float, int)' - rounds a number")
        def modulevalue(self):
            print("HELP:    'numwork.module(int)' - finds module of a number")
        def powernum(self):
            print("HELP:    'miscellaneousnum.powervalue(float, int)' - powers a number'")


class miscellaneousnum:
    def powervalue(val, power):
        num_list = ['1','2','3','4','5','6','7','8','9','0','-', '.']
        for element in range(0, len(str(val))):
            if not str(val)[element] in num_list:
                raise InvalidTypeError("The value " + "'" + str(val) + "'" + " contains invalid symbols for the action")
        val=int(val)
        for i in range(power//2):
            val = val*val
        return val

    def roundvalue(val, rnd):
        num_list = ['1','2','3','4','5','6','7','8','9','0','-', '.']
        for element in range(0, len(str(val))):
            if not str(val)[element] in num_list:
                raise InvalidTypeError("The value " + "'" + str(val) + "'" + " contains invalid symbols for the action")
        for element in range(0, len(str(rnd))):
            if not str(rnd)[element] in num_list:
                raise InvalidTypeError("The value " + "'" + str(rnd) + "'" + " contains invalid symbols for the action")
        rndvalres = round(val, rnd)
        return rndvalres

    def modulevalue(val):
        num_list = ['1','2','3','4','5','6','7','8','9','0','-', '.']
        for element in range(0, len(str(val))):
            if not str(val)[element] in num_list:
                raise InvalidTypeError("The value " + "'" + str(val) + "'" + " contains invalid symbols for the action")
        val=int(val)
        if val < 0:
            val=str(val)
            modval = val.replace('-','')
            modval = int(modval)
            return modval
        else:
            return val




class InvalidTypeError(Exception):
    pass
class InvalidNumError(Exception):
    pass
