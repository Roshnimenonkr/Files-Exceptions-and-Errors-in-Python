f=open("output.txt","w")
a=input("Enter text to write to the file:")
writing=f.write(a+"\n")
print("Data Successfully written to the file")
f.close()

f=open("output.txt","a")
b=input("Enter additional text to append:")
appending=f.write(b+"\n");
print("Data successfully appended")
f.close()

f=open("output.txt","r")
print("Final content of output.txt:")
for x in f:
    print(x)
f.close()


