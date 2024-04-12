import numpy as np
import pandas as pd
from code import *
import welcome


name = input("Enter name: ")
age = input("Enter age: ")

questions = pd.read_csv("D:\\C tutorials\\kbc/questions.csv")

questions = [ Question (row["'question'"], row["'option1'"], row["'option2'"], row["'option3'"], row["'option4'"], int(row['answer'])) for _, row in questions.iterrows()]
game = KBCGame (questions, name, age)
game.play()
