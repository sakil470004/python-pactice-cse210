def hanoi(n, source, target, temp):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, temp, target)
        # move disk from source peg to target peg
        print("Move ",source,"-->",target)
        # move tower of size n-1 from helper to target
        hanoi(n - 1, temp, target, source)
        

hanoi(4,"A","C","B")

