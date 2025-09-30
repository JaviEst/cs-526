def doIt(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return doIt(n-1) + doIt(n-2) - doIt(n-3) 

if __name__ == "__main__":
    print("Output of doIt(1) function:")
    print(doIt(1))
    print("Output of doIt(3) function:")
    print(doIt(3))
    print("Output of doIt(6) function:")
    print(doIt(6))