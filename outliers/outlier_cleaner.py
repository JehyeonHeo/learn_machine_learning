#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    
    ### your code goes here
    errors = []
    for i in range(len(predictions)):
        error = predictions[i] - net_worths[i]
        errors.append(error)
        
    abs_errors = [abs(error) for error in errors]
    tuples = []
    for i in range(len(abs_errors)):
        tuples.append((ages[i][0], net_worths[i][0], abs_errors[i][0]))

    tuples = sorted(tuples, key = lambda tuples : tuples[2])

    for j in range(int(len(tuples) * 0.9)):
        cleaned_data.append(tuples[j])

    for data in cleaned_data:
        print data
    
    return cleaned_data

