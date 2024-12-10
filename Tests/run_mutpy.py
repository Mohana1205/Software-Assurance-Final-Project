import subprocess

# Run mutpy using the correct entry point 'mutpy.cli'
try:
    result = subprocess.run(
        ['python', '-m', 'mutpy.cli', 'run', '-d', 'bank.py', '-t', 'tests/test_bank.py'],
        capture_output=True, text=True, check=True
    )
    
    # Print the standard output of the mutation test
    print("Mutation Testing Results:")
    print(result.stdout)

except subprocess.CalledProcessError as e:
    # Print the error message if the command fails
    print("Error occurred:")
    print("STDOUT:", e.stdout)
    print("STDERR:", e.stderr)
