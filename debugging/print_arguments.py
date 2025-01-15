import sys

if len(sys.argv) <= 1:
    print("No arguments provided.")
else:
    for arg in sys.argv[1:]:
        print(arg)
