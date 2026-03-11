import statistics

def quicksort(numbers):

    if len(numbers)<=1:
        return numbers
    else:
        pivot = statistics.median(
            [
                numbers[0],numbers[len(numbers)//2],
                numbers[-1]
            ]
        )
        items_less,pivot,items_greater = (
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot]
        )
        return(
            quicksort(items_less)+
            pivot+
            quicksort(items_greater)
        )
          
numbers = [5,8,9,10,15,7,4,3,2,1,0]

print(quicksort(numbers))





