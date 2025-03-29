try:
    f = open("sample.txt", "r")
    print("Reading file content:")
    x = 1
    for i in f:
        print("Line ", x, ":", i)
        x += 1
except FileNotFoundError:
    print("Error:The file 'sample.txt' was not found")

