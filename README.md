# Course related programs

This repository is for programs related to or inspired by my courses at IIT Palakkad. Currently, the programs are primarily for my third semester's courses.


## List 

*<< A list of program ideas >>*


**[Discrete mathematics]**

- WFPF checker: Checks if a given expression is a *well-formed propositional formula* (also known as a *well-formed propositional expression*)
- Quantified predicate expression evaluator: Evaluates a simplistic *predicate expression* (also known as a *first-order logic expression*) of the form `[quantifier(s)] [predicate expression]`. Using Python's builtin `any` and `and` functions combined with generator expressions might turn this to a single line Python expression.
- WFPF evaluator: A program to evaluate a given WFPF (after validating it). A possible (but boring) approach is to textually substitute each operator by the corresponding Python boolean operator. A more fundamental approach would be to implement operator precedence yourself (with an option to have a custom precedence), use a parse tree, among other related ideas.

**[Foundations of Computing Systems]**

- Boolean function to straight line: A program that takes a boolean function as input (as a truth table, maybe) and returns it's straight-line equivalent

**[Linked to no particular course]**

- Random number generator:
    - A uniform random distribution generator for a circle, triangle and maybe for regular polygons, in general
    - A probability distribution based RNG (linear, quadratic, discrete values, maybe a custom function, etc), implemented using a regular RNG (like Python's `random.random()`)
    - Maybe use gnuplot to test the above-mentioned programs

