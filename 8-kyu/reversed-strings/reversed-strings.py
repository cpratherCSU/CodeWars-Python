def solution(string):
    rString = ""
    for x in range((len(string)) - 1, -1, -1):
        rString += string[x]
    print(f"{rString}")
    return rString
    
def main():
    myString = "world"
    return solution(myString)
​
if __name__ == "__main__":
    import sys
    sys.exit(main())