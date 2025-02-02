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

I've been doing competitive programming for a few years now, and during that time, I've created a decent amount of command line tools to streamline certain processes in the terminal and make life easier. This repository is a collection of the tools that I've created, which I hope can help out others! I'd be happy to take any feedback or questions!

## Summary

**CPIT** is a command-line tool designed for competitive programming, primarily tested with **Codeforces** and **C++**. It offers the following key features:

- **Automatic Compilation:** Compiles your C++ solution (`main.cpp`) into an executable (`main.exe`).
- **Test Case Parsing:** Extracts sample test cases from a Codeforces problem link.
- **Automated Testing:** Runs the compiled solution against sample test cases and compares outputs.

## Set up

First, clone this repository. You can clone this repository anywhere on your computer, as later we will set up an alias to actually run this tool that can be called from anywhere.

```
git clone https://github.com/C1XTEEN/CPIT.git
```

This tool is ran with `python3`. Make sure to install the required libraries to run it.

```
pip install -r requirements.txt
```

Ensure g++ is installed on your Windows machine for C++ compilation.

## Usage

### Checker and Testing

CPIT automates the compilation and testing process as follows:

1. **Compiles** `main.cpp` into `main.exe` using g++.
2. **Parses** the provided Codeforces problem link to generate sample test cases.
3. **Runs** the compiled solution against each test case and checks for differences.

The parsed test files will be named:
- `1.inp`, `1.out`
- `2.inp`, `2.out`
- ...and so on.

CPIT then runs `main.exe` on each `.inp` file and compares the output with the corresponding `.out` file.

### Parsing with CPIT

Run the tool from the terminal (PowerShell or Command Prompt on Windows) with the problem link as a parameter:
   ```sh
   python cpit.py [PROBLEM_LINK]
   ```

When executed, CPIT will:
- Compile `main.cpp` into `main.exe`.
- Parse the problem from the provided Codeforces link and create sample test files.
- Run `main.exe` on each sample and report any differences between your solution’s output and the expected output.

## Future Steps

I hope to continue improving CPIT and provide more features/tools to enhance convenience in competitive programming. Some future steps I have in mind are:

* Add support for other platforms for parsing, such as AtCoder
* Fix bugs where parser doesn't work if Cloudflare is in use
* Potentially more features!
