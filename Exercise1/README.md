# Exercise 1

## The challenge
```
Filas

Implemente uma classe de pilha de inteiros que possui os métodos
push​, pop​ e min​, onde min​ retorna o menor inteiro na pilha e todos​ os
métodos são executados em O(1)

Submissão:
● Link com acesso para código no repositório git ou equivalente
● Arquivo no repositório explicando em palavras como a estrutura
funciona e porque todos os métodos executados rodam em O(1)
```

## The code

### Overview

The code is written in [Python](https://www.python.org/) and it's fully compatile with its latest version (3.6.2). It uses the third-party library [pytest](https://docs.pytest.org/en/latest/) (version 3.2.3) to run automated tests.

This project is composed of just two python files, [voxus_stack.py](voxus_stack.py), containing the implementation of the stack class that solves the challenge, and [test_voxus_stack.py](test_voxus_stack.py), used for testing purposes.

The solution uses the built-in Python **List** data structure. It's important to note that the implemetation of the methods *get item*, *append* and *pop* (when a index is not specified) run both in O(1), according to [this article](https://wiki.python.org/moin/TimeComplexity).

### VoxusStack Class

#### Properties

##### mainStack

##### minStack

#### Methods

##### push()

##### pop()

##### min()

## Proofs

### push method runs in O(1)

### pop method runs in O(1)

### min method runs in O(1)