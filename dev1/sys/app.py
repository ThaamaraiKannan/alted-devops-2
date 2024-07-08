import sys
original_stdout = sys.stdout # Store original standard output
with open("output1.log", "w") as f:
    sys.stdout = f # Redirect output to the file
    print("""This will be written to the output.log file./n
          kannan
          """)
sys.stdout = original_stdout # Restore original standard output
