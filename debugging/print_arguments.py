import sys

if len(sys.argv) <= 1:
    print("No arguments provided.")
else:
    # Print only the arguments, excluding the script name (sys.argv[0])
    for arg in sys.argv[1:]:
        print(arg)
