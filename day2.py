{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Assignment day 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#1\n",
    "n=eval(input(\"enter a number\"))\n",
    "i=1\n",
    "sum=0\n",
    "while i<=n:\n",
    "    sum=sum+i\n",
    "    i=i+1\n",
    "    print(\"sum of \",i,\" numbers is \",sum)\n",
    "   \n",
    "\n",
    "    "
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
      "enter a number17\n",
      "it is a prime number\n"
     ]
    }
   ],
   "source": [
    "#2\n",
    "count=0\n",
    "i=1\n",
    "n=eval(input(\"enter a number\"))\n",
    "for i in range(1,n+1):\n",
    "    if (n%i)==0:\n",
    "        count = count+1\n",
    "if count==2:\n",
    "    print(\"it is a prime number\")\n",
    "else:\n",
    "    print(\"it is not a prime number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
