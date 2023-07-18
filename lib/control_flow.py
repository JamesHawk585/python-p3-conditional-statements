#!/usr/bin/env python3

def admin_login(username, password):
    try:
        if (username == 'admin' or username == 'ADMIN') and password == '12345':
            return 'Access granted'
        else:
             return 'Access denied'
    except: 
        return 'An Error Occured'
# Write a function admin_login() that takes two arguments, a username and a password. If the username is "admin" or "ADMIN" and the password is "12345", return "Access granted". Otherwise, return "Access denied".


def hows_the_weather(temperature):
        if temperature < 40:
            response = 'brisk'
        elif temperature >= 40 and temperature <= 65:
            response = 'a little chilly'
        elif temperature > 85:
            response = 'too dang hot'
        else: 
            response = 'perfect'
        return f"It\'s {response} out there!"


def fizzbuzz(num):
    # your code here
    pass

def calculator(operation, num1, num2):
    # your code here
    pass
