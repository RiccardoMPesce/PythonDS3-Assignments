# PythonDS3 Assignments
Homeworks from [Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/runestone/books/published/pythonds3/index.html) book.

### Chapter 1
1. Implement the simple methods `get_num` and `get_den` that will return the numerator and denominator of a fraction. ([Solution](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap1/ch-1-ex-1.py))
2. In many ways it would be better if all fractions were maintained in lowest terms right from the start. Modify the constructor for the `Fraction` class so that `GCD` is used to reduce fractions immediately. Notice that this means the `__add__` function no longer needs to reduce. Make the necessary modifications. ([Solution](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap1/ch-1-ex-2.py))
3. Implement the remaining simple arithmetic operators (`__sub__`, `__mul__`, and `__truediv__`). ([Solution](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap1/ch-1-ex-3.py))
4. Implement the remaining relational operators (`__gt__`, `__ge__`, `__lt__`, `__le__`, and `__ne__`). ([Solution](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap1/ch-1-ex-4.py))
5. Modify the constructor for the fraction class so that it checks to make sure that the numerator and denominator are both integers. If either is not an integer, the constructor should raise an exception. ([Solution](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap1/ch-1-ex-5.py))
6. In the definition of fractions we assumed that negative fractions have a negative numerator and a positive denominator. Using a negative denominator would cause some of the relational operators to give incorrect results. In general, this is an unnecessary constraint. Modify the constructor to allow the user to pass a negative denominator so that all of the operators continue to work properly. ([Solution](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap1/ch-1-ex-6.py))
7. Research the `__radd__` method. How does it differ from `__add__`? When is it used? Implement `__radd__`. ([Solution](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap1/ch-1-ex-7.py))
8. Repeat the last question but this time consider the `__iadd__` method. ([Solution](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap1/ch-1-ex-8.py))
9. Research the `__repr__` method. How does it differ from `__str__`? When is it used? Implement `__repr__`. ([Solution](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap1/ch-1-ex-9.py))
10. Research other types of gates that exist (such as NAND, NOR, and XOR). Add them to the circuit hierarchy. How much additional coding did you need to do? ([Solution](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap1/ch-1-ex-10.py))
11. The most simple arithmetic circuit is known as the half adder. Research the simple half-adder circuit. Implement this circuit. ([Solution](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap1/ch-1-ex-11.py))
12. Now extend that circuit and implement an 8-bit full adder. ([Solution](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap1/ch-1-ex-12.py))

### Chapter 4
* [Decimal to Generic Base Converter](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap4/decimal_to_base.py)

### Chapter 5
* [Water Jugs Problem](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap5/water_jugs.py)
* [Reverse List (with Recursion)](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap5/reverse_list.py)
* [Knapsack Problem (using Dynamic Programming)](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap5/knapsack.py)
* [Minimum Subset summing to S (using Dynamic Programming)](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap5/coin_change.py)
* [Minimum Edit Distance (using Dynamic Programming)](https://github.com/RiccardoMPesce/PythonDS3-Selected-Assignments/blob/main/chap5/min_edit_distance.py)
