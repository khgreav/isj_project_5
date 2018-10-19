#!/usr/bin/env python3
class Polynomial(object):
    """Class for polynomials handling."""

    def __init__(self,*argv,**kwargs):
        """This method parses arguments and initiates variables."""
        self.coefs = []
        
        if len(argv) == 1 and type(argv[0]) == list: # list of values
            self.coefs = argv[0]
        elif len(argv) == 1 and type(argv[0]) == int:
            self.coefs.append(argv[0])
            print(self.coefs)
        elif len(argv) > 1: # set of values
            for i in argv:
                if type(i) != int:
                    print("Invalid argument type.")
                    exit()
                self.coefs.append(i)
        elif len(argv) == 0 and len(kwargs) > 0: # x=y format
            dictcoefs = {key: value for key, value in sorted(kwargs.items())} # sort dictionary
            highest = list(dictcoefs.keys())[-1][1:] # take the highest key
            for j in range(int(highest)+1):
                if not "x"+str(j) in dictcoefs.keys(): # if key does not exist add it
                    dictcoefs.update({"x"+str(j):0})
            dictcoefs = {key: value for key, value in sorted(dictcoefs.items())} # sort one last time
            self.coefs = list(dictcoefs.values())
                  
    def __repr__(self):
        """Method calls function that converts polynomial to string."""
        return self.toString(self.coefs)

    def toString(self,coefs):
        """This method converts polynomial object into string."""
        outputstr = ""
        init = 1
        counter = len(coefs) - 1
        
        for coef in coefs[::-1]:
            if init == 1: # first number, dont want to print a + or - sign
                if coef < 0:
                    outputstr += "- "
                elif coef == 0:
                    if len(self.coefs) == 1:
                        outputstr += "0"
                        break
                    counter -= 1
                    continue # skip zero
                else:
                    outputstr += ""
                init = 0 # first number processed
            else:
                if coef == 0:
                    counter -= 1
                    continue
                elif coef < 0:
                    outputstr += " - " # negative numbers
                else:
                    outputstr += " + " # positive numbers
                    
            if counter == 0: # power of 0
                if coef != 0:
                    outputstr += str(abs(coef)) # use absolute value since i'm adding + and - separately
            elif counter == 1:
                if coef == 1:
                    outputstr += "x"
                elif coef == -1:
                    outputstr += "x"
                else:
                    outputstr += str(abs(coef))+"x"
            else:
                if coef == 1:
                    outputstr += "x^"+str(counter)
                elif coef == -1:
                    outputstr += "x^"+str(counter)
                else:
                    outputstr += str(abs(coef))+"x^"+str(counter)                             
            counter -= 1
            
        return outputstr

    def __eq__(self,other):
        """This method checks if two polynomials are equal."""
        return self.toString(self.coefs) == str(other)

    def __add__(self,other):
        """This method adds up 2 polynomials."""
        sumcoefs = []
        counter = 0
        extend = 0
        
        if len(self.coefs) == len(other.coefs): # no need to extend lists
            llist = self.coefs
            slist = other.coefs
        elif len(self.coefs) < len(other.coefs): # self shorther than other, extend
            llist = other.coefs
            slist = self.coefs
            extend = 1
        else:
            llist = self.coefs # self longer than other, extend
            slist = other.coefs
            extend =1

        if extend == 1: # extending lists to the same lenght
            for i in range(len(llist) - len(slist)):
                slist.append(0)

        for coef in llist: # add them numbers up
            sumcoefs.append(coef + slist[counter])
            counter += 1
            
        return self.toString(sumcoefs)

    def derivative(self):
        """Returns a new derivated polynomial object"""
        derivcoefs = []
        if len(self.coefs) == 1: # derivative of a constant is 0
            derivcoefs.append(0)
            return Polynomial(derivcoefs)
        else:
            counter = 0
            for coef in self.coefs:
                derivcoefs.append(coef * counter) # value times counter (exponent)
                counter += 1
            deriv = Polynomial(derivcoefs[1:]) # returning new polynomial to preserve the old object
        return deriv

    def at_value(self,*argv):
        """Method calculates the output value based on the input value."""
        counter = len(self.coefs)-1
        result = 0
        if len(argv) == 0: 
            return result
        elif len(argv) == 1:
            for coef in self.coefs[::-1]:
                result += coef * argv[0] ** counter # value * constant to the power of exponent
                counter -= 1
            return result
        elif len(argv) == 2: # 2 values for at_value
            result1 = 0
            for coef in self.coefs[::-1]:
                result1 += coef * argv[0] ** counter # value * constant to the power of exponent
                result += coef * argv[1] ** counter # value * constant to the power of exponent
                counter -= 1
            return result - result1
        else: # cheeky way to end
            print("More than 2 arguments are not supported by the at_value function")
            exit(-1)
