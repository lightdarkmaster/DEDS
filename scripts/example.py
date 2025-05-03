def computeAverage(array):
    result = sum(array)/ len(array)
    finalResult = result.__round__(2)
    print(finalResult);

def computeTotalScore(array):
    result = sum(array)
    print(result)
    
    
def addOne(array):
    for i in range(len(array)):
        array[i] = array[i] + 1;
        print(array);


addOne([87,98,85,88,81,83,82]);
# print("Averge Grade: ");  
# computeAverage([87,98,85,88,81,83,82]);
# average calculation
computeTotalScore([87,98,85,88,81,83,82]);