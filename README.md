# CPIT (Competitive Programming Interface Tool)

## Table of Contents
- [Background](#background)
- [Summary](#summary)
- [Installation](#installation)
- [Usage](#usage)
  - [Checker and Testing](#checker-and-testing)
  - [Parsing with CPIT](#parsing-with-cpit)
- [Future Plans](#future-plans)

## Background

Competitive programming has been a passion of mine for several years, and during this time, I’ve developed a variety of command-line tools to simplify workflows and streamline terminal processes. This repository is a collection of these tools, and I hope they prove useful for others. Feedback and questions are always welcome!

## Summary

**CPIT** is a command-line tool tailored for competitive programming, primarily tested with **Codeforces** and **C++**. It features:

- **Automatic Compilation:** Compiles your C++ solution (`main.cpp`) into an executable (`main.exe`).
- **Test Case Parsing:** Extracts sample test cases directly from a Codeforces problem link.
- **Automated Testing:** Runs your compiled solution against the sample test cases and compares the outputs.

## Installation

1. **Download the Executable:**  
   Grab the latest CPIT executable from the releases page:  
   [Download CPIT](https://github.com/ziq3/CPIT/releases/download/1/cpit.exe)

2. **Install g++:**  
   Ensure that g++ is installed on your Windows machine, as it is required for C++ compilation.

## Usage

Make sure your solution file is named `main.cpp` and is located in the same directory as CPIT. From your terminal (PowerShell or Command Prompt), run:

```
cpit LINK_PROBLEM
```

For example:

```
cpit https://codeforces.com/contest/961/problem/E
```

### Checker and Testing

CPIT automates the compilation and testing process in the following steps:

1. **Compilation:**  
   Compiles `main.cpp` into `main.exe` using g++.

2. **Test Case Parsing:**  
   Retrieves sample test cases from the provided Codeforces problem link. The test files are generated with the following naming convention:
   - `1.inp` and `1.out`
   - `2.inp` and `2.out`
   - ... and so on.

3. **Automated Testing:**  
   Executes `main.exe` on each `.inp` file and compares the output with its corresponding `.out` file to identify any discrepancies.

### Parsing with CPIT

Alternatively, you can invoke the tool via Python (if needed) using:

```
python cpit.py [PROBLEM_LINK]
```

When executed, CPIT will:
- Compile `main.cpp` into `main.exe`.
- Parse the problem from the provided Codeforces link and create sample test files.
- Run `main.exe` on each test case and report any output differences compared to the expected results.

## Future Plans

I am continually working to enhance CPIT. Upcoming improvements include:

- **Platform Support:** Adding parsing support for additional competitive programming platforms (e.g., AtCoder).
- **Improved Reliability:** Resolving issues with the parser, especially when Cloudflare protection is active.
- **New Features:** Introducing more functionalities to further streamline competitive programming workflows.

Feel free to contribute, report issues, or suggest enhancements. Enjoy coding!
