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

The solution uses the built-in **List** data structure. It's important to verify that the implemetation of the methods *get item*, *append*, *pop* (when a index is not specified), as the emptiness verification (since it's a particular case of *get length* method with a comparison) run all in O(1), according to [this article](https://wiki.python.org/moin/TimeComplexity).

### VoxusStack Class

The VoxusStack uses two stacks (*mainStack* and *minStack*) to solve the problem. The former is used as an ordinary LIFO stack, i.e., every value stacked to a VoxusStack instance is appended to it as the last element, and the *pop* operation removes and returns this last element. The latter, is also a LIFO structure, but stores just the min values, and is responsible for allowing the *min* operation to run in O(1).

#### Properties:

+ **mainStack**: stacks all the values pushed to a VoxusStack instance.
+ **minStack**: stacks the values pushed to a VoxusStack instance that are equal or less than the last value stacked in minStack.

#### Methods:

+ **push(val)**: Adds val to the end of the mainStack. If val is equal or less than the last value stacked in minStack (or if minStack is empty), then it is also stacked in minStack.
+ **pop()**: Pops (removes and returns) the last element of mainStack. If it's equal to the last value stacked in minStack, this last element from minStack is also removed.
+ **min()**: Returns the smallest item in the stack, i.e., the last element of minStack (it's not removed).

## Proofs

### Push method runs in O(1)

The push method calls the method append of a list, i.e., as stated previously, an O(1) method. It's followed by a verification of the emptiness of the list and a comparison operation, both O(1). If the result of the operation is true, another list append is made, therefore, another O(1) operation. In the worst case, just O(1) operations are executed, so the method is O(1).

### Pop method runs in O(1)

Since the pop operation of a list, as a get element operation from this list and a comparison operation, are all O(1) operations, and just this operations are executed without loops, the pop method of the VoxusStack runs in O(1).

### Min method runs in O(1)

The min method just does an emptiness verification and gets an item in a list, therefore it's an O(1) method.