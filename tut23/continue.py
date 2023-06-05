# using the continue keyword
for i in range(5):
    print("Starting loop "+ str(i))

    stop = input("Do you want to stop the loop (y/n): ")
    if stop == "y":
        continue

    print("Ending loop "+ str(i))

print("Program Finished")