#!/usr/bin/env python
# -*- coding: utf-8 -*-
import webbrowser


class CuriousObject:
    def __init__(self):
        self.knowledge = {}

    def ask(self, question):
        if question in self.knowledge:
            return self.knowledge[question]
        else:
            return "I don't know the answer to this question. I can learn more!"

    def learn(self, question, answer):
        self.knowledge[question] = answer
        self.save_to_file(question, answer)
        print("I learned a new answer!")

    def save_to_file(self, question, answer):
        with open("knowledge.txt", "a") as file:
            file.write(f"{question}:{answer}\n")

# Create a curious object named "gants"
jants = CuriousObject()

# Load the saved knowledge from the file into memory
with open("knowledge.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        question, answer = line.strip().split(":")
        jants.learn(question, answer)

# Test and learn Gantz inquiry
while True:
    question = input("ask gants: ")
    if question == "stop":
        break
    answer = jants.ask(question)
    print(answer)
    if answer == "I don't know the answer to this question. I can learn more!":
        new_answer = input("what is the answer؟ ")
        jants.learn(question, new_answer)