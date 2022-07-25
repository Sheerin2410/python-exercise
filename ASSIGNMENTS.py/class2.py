{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sid\n"
     ]
    }
   ],
   "source": [
    "# accept name from user\n",
    "\n",
    "name = input('Enter your name:')\n",
    "print(name)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n"
     ]
    }
   ],
   "source": [
    "num1 = int(input('Enter number 1:'))\n",
    "num2  = int(input('Enter number 2:'))\n",
    "\n",
    "ans =num1 + num2\n",
    "\n",
    "print(ans)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "number =int(input('enter a number:'))\n",
    "ans = number * number * number\n",
    "\n",
    "print(ans)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "36\n"
     ]
    }
   ],
   "source": [
    "year = int(input('enter years:'))\n",
    "ans = year * 12\n",
    "\n",
    "print(ans)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.5\n"
     ]
    }
   ],
   "source": [
    "month = int(input('enter months:'))\n",
    "\n",
    "year = month / 12\n",
    "\n",
    "print(year)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "oprator : if we want to perform any optrations at time we are using  some specific symbols\n",
    "\n",
    "a + b \n",
    "\n",
    "here,  +  is an oprator\n",
    "\n",
    "a and b  both are operands\n",
    "\n",
    "(a + b )  expression"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "\n",
    "types of  oprators:\n",
    "\n",
    "\n",
    "1) airthmatic oprators\n",
    "\n",
    "+  -  *  /  %  //  **\n",
    "\n",
    "\n",
    "2)  assignment oprators\n",
    "\n",
    "\n",
    "=\n",
    "\n",
    "3)  conditional oprators or tenary oprators\n",
    "\n",
    "?:\n",
    "\n",
    "\n",
    "exp1 ?  exp2  :exp3\n",
    "\n",
    "4) membership oprators:\n",
    "\n",
    "\n",
    "in not in\n",
    "\n",
    "\n",
    "5) logical oprators:\n",
    "\n",
    "and \n",
    "\n",
    "not\n",
    "\n",
    "or\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "control statements\n",
    "\n",
    "\n",
    "there are 3 types of controls statement\n",
    "\n",
    "1)  conditional\n",
    "\n",
    "2) looping\n",
    "\n",
    "3) jumping\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "1) conditional statement:\n",
    "\n",
    "        if statement\n",
    "        if ...else statement\n",
    "        elif statement\n",
    "        nested if statement\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "syntax: \n",
    "\n",
    "\n",
    "        if condition:\n",
    "                statment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "positive number\n"
     ]
    }
   ],
   "source": [
    "number =int(input('Enter a number:'))\n",
    "\n",
    "if number > 0:\n",
    "    print('positive number')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you are eligible for vote\n"
     ]
    }
   ],
   "source": [
    "# accept age fro m use and chack he is eligible for vote or not\n",
    "\n",
    "age = int(input('enter your age:'))\n",
    "\n",
    "if age > 18:\n",
    "    print('you are eligible for vote')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "odd number\n"
     ]
    }
   ],
   "source": [
    "number =int(input('enter your number:'))\n",
    "\n",
    "if number % 2 == 0:\n",
    "    print('this number is Even')\n",
    "else:\n",
    "    print('odd number')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "task1 = accept days from user and convert it into number of months\n",
    "\n",
    "\n",
    "task2 = accept number of hours and convert into minutes\n",
    "\n",
    "task3 = find simple intrest \n",
    "\n",
    "formula = si = pnr / 100\n",
    "\n",
    "p = principal amount\n",
    "n = terms\n",
    "\n",
    "r = rate of intrewst\n",
    "\n",
    "\n",
    "task4 = accept minutes and convert it into seconds and hours \n",
    "\n",
    "\n",
    "task4 : accept marks and chack student is fail or pass\n",
    "\n",
    "task6 = find enterd number is positive or nagetive\n",
    "\n",
    "task7 = find area of circle\n",
    "\n",
    "    formula:\n",
    "\n",
    "    are of circle : pi * r * r\n",
    "\n",
    "\n",
    "    Hint :  varriables , input , if...else condition\n",
    "    \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.6 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "b8eeea7db13471468ad276e1aa6abbd3f9f4200994ed792cdeec60c0462f2e2a"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
------------------------
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "conditional statement: \n",
    "\n",
    "1) if ....statement\n",
    "2) if ....else condition\n",
    "3)  elif statement:     for multiple condition\n",
    "\n",
    "\n",
    "syntax:\n",
    "\n",
    "if condition:\n",
    "            statement\n",
    "elif condition:\n",
    "            statement\n",
    "elif condition:\n",
    "            statement\n",
    "else:\n",
    "            statement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "num = 10\n"
     ]
    }
   ],
   "source": [
    "# elif statement\n",
    "\n",
    "\n",
    "num = int(input('Enter your number:'))\n",
    "\n",
    "if num== 10:\n",
    "    print('num = 10')\n",
    "elif num == 20:\n",
    "    print('num = 20')\n",
    "elif num == 30:\n",
    "    print('num = 30')\n",
    "else:\n",
    "    print('invalid number')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "print is below 10 or number is above 100\n"
     ]
    }
   ],
   "source": [
    "num = int(input('Enter your number'))\n",
    "\n",
    "if num >= 10 and num <= 50:\n",
    "    print('number is between 10 - 50')\n",
    "elif num >= 51 and num <= 100:\n",
    "    print('number is between 51 - 100')\n",
    "else:\n",
    "    print('print is below 10 or number is above 100')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you are pass with D grade\n"
     ]
    }
   ],
   "source": [
    "mark = int(input('Enter your mark:'))\n",
    "\n",
    "if mark >= 70:\n",
    "    print('you are in pass with A grade')\n",
    "elif mark >= 60 and mark < 70:\n",
    "    print('you are pass with B grade')\n",
    "elif mark >= 50 and mark < 60:\n",
    "    print('you are pass with C grade')\n",
    "elif mark >= 40 and mark < 50:\n",
    "     print('you are pass with D grade')\n",
    "else:\n",
    "    print('you are fail')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "nested if statement:\n",
    "\n",
    "if inside the if statement\n",
    "\n",
    "\n",
    "syntax:\n",
    "\n",
    "if condition:\n",
    "        statement\n",
    "if condition:\n",
    "        if condition:\n",
    "        if condition:\n",
    "                statement\n",
    "        else:\n",
    "                statement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "invalid password\n"
     ]
    }
   ],
   "source": [
    "email ='vyas1604@gmail.com'\n",
    "password =123456\n",
    "\n",
    "s_email = input('enter email:')\n",
    "s_password = input('enter your password:')\n",
    "\n",
    "if s_email == email:\n",
    "    if s_password == password:\n",
    "        print('WELCOME TO PYTHON')\n",
    "    else:\n",
    "        print('invalid password')\n",
    "else:\n",
    "    print('invalid email')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "invalid input\n"
     ]
    }
   ],
   "source": [
    "\n",
    "mark = int(input('Enter your mark:'))\n",
    "\n",
    "if mark >= 0 and mark<= 100:\n",
    "    if mark >= 70:\n",
    "        print('you are in pass with A grade')\n",
    "    elif mark >= 60 and mark < 70:\n",
    "        print('you are pass with B grade')\n",
    "    elif mark >= 50 and mark < 60:\n",
    "        print('you are pass with C grade')\n",
    "    elif mark >= 40 and mark < 50:\n",
    "        print('you are pass with D grade')\n",
    "    else:\n",
    "        print('you are fail')\n",
    "else:\n",
    "    print('invalid input')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.6 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "b8eeea7db13471468ad276e1aa6abbd3f9f4200994ed792cdeec60c0462f2e2a"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
