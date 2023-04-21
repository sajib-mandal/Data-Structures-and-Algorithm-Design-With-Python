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
## How do you convert one number system to another number system?

Conversions: There are two thing we have to remember. Using this two points you will be able to convert any number system to any number system.
1. **Conversion from** `Decimal to baser b`.

   Q: Covert (17)10 to base 2.
   ```commandline
      2 |17
        -----
       2 | 8 -> 1
         -----
        2 | 4 -> 0
          -----
         2 | 2 -> 0
           -----
             1 -> 0
   
   (17)10 = (10001)2
   ```
   ```commandline
      (17)10 = (?)8
      
      8 | 17
        -----
         2  ->  1
   
      (17)10 = (21)8
   ```

   Keep dividing by base, take remainder, and write its opposite.
2. **Conversion from** `Base b to Decimal`.
    ```
     Convert any base 'b' to 'Decimal'.
   
      4 3 2 1 0
     (1 0 0 0 1)2 = (?)10
     Steps:
         1*2^4 + 0*2^3 + 0*2^2 + 0*2^1 + 1*2^0 = 17
     
   (10001)2 = (17)10         
    ```
   ```commandline
       (21)8 = (?)10
       = 2*8^1 + 1*8^0
       = 17
      (21)8 = (17)10
   ```
   **Example**:

   Q: How do you convert base 2 into base 8?

   A: First to convert base 2 into Decimal(10), then convert Decimal to base 8
## Continuing with operator
5. **Left shift (<<)**:

   For example:

   (10)10 = (1010)2 so what is `10 << 1`
   ```commandline
      10 << 1 = ?
      (10)10 = (1010)2
     So,
      1010 << 1 = 10100
      (10100)2 = (20)10
   ```
   So, <u>**a << 1 = 2a**</u> `(any number left shift is double the number)`
 
   <font color="red">**General Point**:</font> a << b = a*2^b

    That's means 2 << 4 is 2 << 2^4