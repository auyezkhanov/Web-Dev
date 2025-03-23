def countingValleys(n, path):
    sea_level = 0
    valleys = 0
    altitude = 0

    for step in path:
        if step == 'U':
            altitude += 1
        else:
            altitude -= 1

        # A valley is completed when we come back to sea level from below
        if altitude == 0 and step == 'U':
            valleys += 1

    return valleys

print(countingValleys(12, "DDUUDDUDUUUD"))  
print(countingValleys(10, "UDUUUDUDDD"))    
print(countingValleys(8, "DDUUUUDD"))      
