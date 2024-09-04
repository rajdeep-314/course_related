# Course related programs

This repository is for programs related to or inspired by my courses at IIT Palakkad. Currently, the programs are primarily for my third semester's courses.


## List 

*<< A list of program ideas >>*


**[Discrete mathematics]**

- WFPF checker: Checks if a given expression is a *well-formed propositional formula* (also known as a *well-formed propositional expression*)
- Quantified predicate expression evaluator: Evaluates a simplistic *predicate expression* (also known as a *first-order logic expression*) of the form `[quantifier(s)] [predicate expression]`. Using Python's builtin `any` and `and` functions combined with generator expressions might turn this to a single line Python expression.
- WFPF evaluator: A program to evaluate a given WFPF (after validating it). A possible (but boring) approach is to textually substitute each operator by the corresponding Python boolean operator. A more fundamental approach would be to implement operator precedence yourself (with an option to have a custom precedence), use a parse tree, among other related ideas.
- Automated theorem prover: **Very** ambitious but maybe something like a very basic version of [coq](https://en.wikipedia.org/wiki/Coq_(software)), with a language to express first-order-logic-esque statements, etc.

**[Foundations of Computing Systems]**

- Boolean function to straight line: A program that takes a boolean function as input (as a truth table, maybe) and returns it's straight-line equivalent
- Implement boolean functions using bash, maybe
    - Implement a basic NAND gate, use it for developing further useful combinational circuits
    - Maybe simulate sequential circuits too, somehow
- An assembler for HACK in Python (sort of as a precursor to the next point)
	- Acts on a `.asm` file, maybe passed as a command line argument
	- Converts it to a file with each line representing a binary instruction. Saves the file with the extension `.hack` (meant to be executed in the CPU Emulator)
	- Perform some basic optimization, making the number of passes low, etc. This sounds very "explorable"
- A two-pass assembler in OCaml

**[Linked to no particular course]**

- Random number generator:
    - A uniform random distribution generator for a circle, triangle and maybe for regular polygons, in general
    - A probability distribution based RNG (linear, quadratic, discrete values, maybe a custom function, etc), implemented using a regular RNG (like Python's `random.random()`)
    - Maybe use gnuplot to test the above-mentioned programs

