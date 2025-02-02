import sys
import subprocess
from parser import parse_problem
from checker import test_code

def compile_main():
    compile_cmd = (
        'g++ -std=c++20 -D_GLIBCXX_DEBUG -Wall -Wextra -Wunused-variable '
        '-pedantic -Wshadow -Wformat=2 -Wfloat-equal -Wlogical-op -Wshift-overflow=2 '
        '-Wduplicated-cond -Wcast-qual -Wcast-align -Wconversion -D_GLIBCXX_DEBUG_PEDANTIC '
        '-D_GLIBCXX_ASSERTIONS -fno-sanitize-recover -Wl,--stack,268435456 main.cpp -o main.exe'
    )
    print("Compiling main.cpp...")
    result = subprocess.run(compile_cmd, shell=True)
    if result.returncode != 0:
        print("Compilation failed.")
        sys.exit(1)
    print("Compilation successful.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: cpit <link>")
        sys.exit(1)
    # First, compile main.cpp into main.exe
    compile_main()

    link = sys.argv[1]
    print("Parsing problem from link:", link)
    # Parse the problem:
    # This creates files: 1.inp, 2.inp, ... for inputs and 1.out, 2.out, ... for expected outputs
    parse_problem(link, input_ext=".inp")
    
    print("Running main.exe on parsed tests")
    # Run main.exe on each .inp file and compare its output with the corresponding .out file.
    test_code("main.exe", input_ext=".inp")