# Python - Everything is object

![alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/252/r_208403_QPSN8.jpg)

In this project, I studied object instantiation in Python, delving into variable aliasing and object identifiers, types, and mutability. The project involved a series of quiz-like questions the answers to which I provided in single-line `.txt` files.

![alt text](https://media.giphy.com/media/wAjfQ9MLUfFjq/giphy.gif)

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files.

## Tasks :page_with_curl:

* **0. Who am I?**
  * [0-answer.txt](./0-answer.txt): What function would you use to print the type of an object?


* **1. Where are you?**
  * [1-answer.txt](./1-answer.txt): How do you get a variable's identifier (which is the memory address in the CPython implementation)?

* **2. Right count**
  * [2-answer.txt](./2-answer.txt): In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = 100
```

* **3. Right count =**
  * [3-answer.txt](./3-answer.txt): In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = 89
```

* **4. Right count =**
  * [4-answer.txt](./4-answer.txt): In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = a
```

* **5. Right count =+**
  * [5-answer.txt](./5-answer.txt): In the following code, do `a` and `b` point to the same object?
```
>>> a = 89
>>> b = a + 1
```

* **6. Is equal**
  * [6-answer.txt](./6-answer.txt): What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

* **7. Is the same**
  * [7-answer.txt](./7-answer.txt): What do these 3 lines print?
```
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

* **8. Is really equal**
  * [8-answer.txt](./1-answer.txt): What do these 3 lines print?
```
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

