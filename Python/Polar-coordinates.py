import cmath
import re

def convertToPolar(realPart, imaginaryPart):
    print(abs(complex(realPart, imaginaryPart)))
    print(cmath.phase(complex(realPart, imaginaryPart)))
    


if __name__ == '__main__':
    
    complexNumber = list(map(int,re.findall(r'-?\d+',input())))

    convertToPolar(complexNumber[0], complexNumber[1])

