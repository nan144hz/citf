# CITF: Compile It in Files

**CITF** is a prototype of a "compiler" that uses only files for compiling *.citf* files. I don't recommend using CITF now, because it is on non-released versions.

<br>

## How the compiler will work?

**CITF** has it own prompt, with basic commands. On this prompt, you can compile files with the command below

```citf -c <filename>```

With this command, the prompt will call the compiler, and the compiler will compile the provided file. To compile a *.citf*, CITF copy it own compiler files to paste on the directory where the provided file is. The folder containing the compiler files is called **cenv** (like a venv, but an environment for CITF), and inside there, the compiler creates a folder called build, where are the files to compile and then execute the code.

<br>

## What are the files inside the **build** folder and what are they for?

Let me explain with a tree

```
- code.citf (where is your code)
- cenv (citf environment folder)
  | - build (build folder)
    | -> .TOKENS (where are all the tokens)
    | -> .VARIABLES (where are all the variables)
    | -> .CONSTANTS (where are all the constants)
    | -> compiled.py (compiled code to execute)
```