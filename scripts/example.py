def computeAverage(array):
    result = sum(array)/ len(array)
    finalResult = result.__round__(2)
    print(finalResult);

print("Averge Grade: ");  
computeAverage([87,98,85,88,81,83,82]);