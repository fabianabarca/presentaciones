import random
from pyscript import document


def age2number(event):
    input_age = document.querySelector("#age")
    age = input_age.value
    random.seed(age)
    output_number = document.querySelector("#number")
    output_number.innerText = random.randint(0, 101)