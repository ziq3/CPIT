import subprocess
import os
import shutil
import sys

def get_tests(input_ext=".inp"):
    """
    Get all test cases from the current directory.
    Test cases are files ending with input_ext (e.g. "1.inp"),
    excluding the special file ".inp" itself.
    """
    input_files = []
    p = subprocess.Popen('dir /b', shell=True, stdout=subprocess.PIPE)
    for line in p.stdout.readlines():
        file = line.decode("utf-8").strip()
        if file.endswith(input_ext) and file.lower() != input_ext:
            input_files.append(file)
    return input_files

def run_test(input_file: str, executable: str):
    """
    Copies test input (e.g. "1.inp") to ".inp", removes any old ".out" file,
    and runs the executable with forced redirection (".inp" -> ".out").
    Returns the produced output, any debug info, and expected output.
    """
    # Copy the test input file (e.g. "1.inp") to ".inp"
    shutil.copy(input_file, ".inp")
    
    # Remove previous output file if it exists
    if os.path.exists(".out"):
        os.remove(".out")
    
    # Force main.exe to read from .inp and write to .out
    cmd = f'{executable} < .inp > .out'
    proc = subprocess.Popen(cmd, shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    
    produced_lines = []
    if os.path.exists(".out"):
        with open(".out", "r", encoding="utf-8") as f:
            produced_lines = [line.strip() for line in f if line.strip()]
    
    expected_output_file = input_file.replace(".inp", ".out")
    expected_lines = []
    if os.path.exists(expected_output_file):
        with open(expected_output_file, "r", encoding="utf-8") as f:
            expected_lines = [line.strip() for line in f if line.strip()]
    
    debug_lines = [line.strip() for line in stderr.decode("utf-8").splitlines() if line.strip()]
    return produced_lines, debug_lines, expected_lines

def print_input_file(filename):
    print("Input file:", filename)

def print_results(results, debug, expected):
    print("Results:")
    for line in results:
        print(line)
    print("Debug:")
    for line in debug:
        print(line)
    print("Expected:")
    for line in expected:
        print(line)

def test_code(executable: str, input_ext=".inp"):
    tests = get_tests(input_ext)
    for test in tests:
        produced_lines, debug_lines, expected_lines = run_test(test, executable)
        print("Running on test " + test)
        if len(expected_lines) == 0:
            print("WARNING: No expected output file found")
            sys.exit(1)
        if len(produced_lines) != len(expected_lines):
            print("FAILED")
            print_input_file(test)
            print_results(produced_lines, debug_lines, expected_lines)
            sys.exit(1)
        else:
            for i in range(len(produced_lines)):
                if produced_lines[i].lower() != expected_lines[i].lower():
                    print("FAILED")
                    print_input_file(test)
                    print_results(produced_lines, debug_lines, expected_lines)
                    sys.exit(1)
            print("ACCEPTED")
            print_input_file(test)
            print_results(produced_lines, debug_lines, expected_lines)
    print("ALL SAMPLES PASSED")