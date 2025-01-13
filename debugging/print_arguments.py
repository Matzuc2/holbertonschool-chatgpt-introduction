import sys

if len(sys.argv) <= 1:
    print("No arguments provided.")
else:
    print("Arguments provided:")
    for arg in sys.argv[1:]:
        print(arg)