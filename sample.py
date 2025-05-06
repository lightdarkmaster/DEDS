def subNumber(num1, num2):
    return num1 - num2;

def getAverage(array):
    result = sum(array) / len(array);
    finalResult = result.__round__(2);
    return finalResult;

print(getAverage([87,98,85,88,81,83,82]));
print(subNumber(486, 367));