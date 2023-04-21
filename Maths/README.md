# Math for DSA
## Bitwise Operators:
1. **AND**: 

    | a | b | a & b |
    |---|---|-------|
    | 0 | 0 | 0     |
    | 0 | 1 | 0     |
    | 1 | 0 | 0     |
    | 1 | 1 | 1     |
   * **Observation**:
   
     When you `& 1` with any number, digit remain the same.
     ```
        1 1 0 0 1 0 1 0 0
       &1 1 1 1 1 1 1 1 1
       -------------------
        1 1 0 0 1 0 1 0 0
     ```
2. **OR**:

    | a | b | a or b |
    |---|---|--------|
    | 0 | 0 | 0      |
    | 0 | 1 | 1      |
    | 1 | 0 | 1      |
    | 1 | 1 | 1      |
3. **XOR(^)**: (if and only if) also called `exclusive OR`. If you have two number only one should be TRUE.

    | a | b | a ^ b |
    |---|---|-------|
    | 0 | 0 | 0     |
    | 0 | 1 | 1     |
    | 1 | 0 | 1     |
    | 1 | 1 | 0     |
   * **Observation**:
   
     If XOR any number with `1`, then it give `complement of the number (complement means oposite 0->1, 1->0)`.
     
     a^1 = ~a
   
     a^0 = a
   
     a^a = 0 (32 ^ 32 = 0)
4. **Complement (~)**:
   ```
    a =  1 0 1 1 0

   ~a = 0 1 0 0 1
   ```
## Conversion of (Number Systems) or Conversion With Various Basics:
Two ways we can convert any number with any other number.
1. **Decimal**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 `(Base: 10) like (357)10, (10)10`
2. **Binary**: 0 & 1 `(Base: 2) like (10)10 = (1010)2, (7)10 = (111)2`
3. **Octal**: 0, 1, 2, 3, 4, 5, 6, 7 `(Base: 8)`
   ```commandline
   Decimal: 0, 1, 2, 3, 4, 5, 6, 7, 8,  9,  10, 11, 12, 13, 14, 15, ...
   Octal:   0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20, ...
   
   '8' in Decimal '10' is Octal: (8)10 = (10)8
   '9' in Decimal '11' is Octal: (9)10 = (11)8
   ```
4. **Hexadecimal**: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F `(Base: 16)`
   ```commandline
   Decimal:     0, 1, 2, 3, 4, 5, 6, 7, 8,  9,  10, 11, 12, 13, 14, 15, ...
   Octal:       0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20, ...
   Hexadecimal: 0, 1, 2, 3, 4, 5, 6, 7, 8,  9,  A,  B,  C,  D,  E,  F 
   
   (10)10 = (A)16
   (12)10 = (C)16
   ```
**How do you convert one number system to another number system?**

Conversion: