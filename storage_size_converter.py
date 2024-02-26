"""
This module can be used for converting storage size in different units, like bits, gigabits etc.
It was finished on 2023-09-09a.m. with my 3-hour dedication.
And it was really a tough but worthwhile process to structure and idea and debug.
Thanks for IB can give me motivation to innovate and think more meaningful and practical through CAS.
"""

__author__ = "Jinhao Li"

import re


def main(*args, **kwargs):
    mode = int(str(input("1) One => one;"
                         "\n2) One => All other units"
                         "\nSelect Mode: ")))
    ask_input: str = ''
    while not re.search(r'\d+\s+\w+', ask_input):
        ask_input = str(input(
            f"Pls input the value and unit(i.e. {tuple(conv.keys())}) (e.g. 5 tera, no s needed): "))
    input_value, input_unit = ask_input.split()
    input_value = float(input_value)
    if mode == 1:
        mode_one(input_value, input_unit)
    elif mode == 2:
        mode_two(input_value, input_unit)
    else:
        raise KeyError
    print("Done")


def convert(input_value, input_u, output_u, *args, **kwargs) -> tuple:
    exact_byte = conv[input_u]["exact size"] * input_value
    approx_byte = conv[input_u]["approx size"] * input_value
    exact_output = exact_byte / conv[output_u]["exact size"]
    approx_output = approx_byte / conv[output_u]["approx size"]
    return exact_output, approx_output


def mode_one(input_value, input_unit, *args, **kwargs):
    output_unit = str(input(f"Input the output unit {tuple(conv.keys())}: ")).lower()
    exact_output, approx_output = convert(input_value, input_unit, output_unit)
    print(
        f""" {input_value} {conv[input_unit]['abbr']} => exact {exact_output:,} {conv[output_unit]['abbr']} Or, => approx {int(approx_output):,} {conv[output_unit]['abbr']} """)


def mode_two(input_value, input_unit, *args, **kwargs):
    global items_ls
    res_dict = dict()
    res_u_ls = list(conv.keys())
    res_u_ls.remove(input_unit)
    for res_u in res_u_ls:
        exact_output, approx_output = convert(input_value, input_unit, res_u)
        res_dict[conv[res_u]["abbr"]] = [exact_output, approx_output]
        items_ls = list(res_dict.items())
    print(
        f""" {input_value} {conv[input_unit]["abbr"]} is equivalent to(index exact/approx unit):  
----------------------------------------------------------------------------------- """)
    for index in range(len(res_dict)):
        unit, result_tuple = items_ls[index]
        print(f"=> {index + 1}) {result_tuple[0]:,} {unit} | {result_tuple[1]:,} {unit}")

    # Conversion rule


conv = {"bit": {"abbr": "b", "exact size": 1, "approx size": 1},
        "byte": {"abbr": "B", "exact size": 8, "approx size": 8},
        "kilo": {"abbr": "Kb", "exact size": 1024, "approx size": 1000},
        "mega": {"abbr": "Mb", "exact size": 1024 ** 2, "approx size": 1000 ** 2},
        "giga": {"abbr": "Gb", "exact size": 1024 ** 3, "approx size": 1000 ** 3},
        "tera": {"abbr": "Tb", "exact size": 1024 ** 4, "approx size": 1000 ** 4}, }
if __name__ == "__main__":
    main()
