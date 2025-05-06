import numpy as np;
def subNumber(num1, num2):
    return num1 - num2;

def getAverage(array):
    result = sum(array) / len(array);
    finalResult = result.__round__(2);
    return finalResult;

def subtractArray(array1, array2):
    array1 = np.array(array1);
    array2 = np.array(array2);
    result = array1 - array2;
    return result;

def addArray(array1,array2):
    array1 = np.array(array1);
    array2 = np.array(array2);
    result = array1 + array2;
    
    #Prevent values from exceeding 100s
    for i in range(len(result)):
        if result[i] > 100:
            result[i] = 100;
            return result;
        else: 
            return result;


print(subtractArray([87,98,85,88,81,83,82], [1,1,1,1,1,1,1]));
print(addArray([100,98,85,88,81,83,82], [1,1,1,1,1,1,1]));
print(getAverage([87,98,85,88,81,83,82]));
print(subNumber(486, 367));