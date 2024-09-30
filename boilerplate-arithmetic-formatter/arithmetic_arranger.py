import re


def arithmetic_arranger(problems, with_results=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  problem_lines = ["", "", "", ""] if with_results else ["", "", ""]

  for promblem in problems:
    operands = re.split(r'[+-]', promblem.replace(" ", ""))

    if "+" not in promblem and "-" not in promblem:
      return "Error: Operator must be '+' or '-'."

    operator = "+" if "+" in promblem else "-"
    for operand in operands:
      if len(operand) > 4:
        return "Error: Numbers cannot be more than four digits."
      if not operand.isdigit():
        return "Error: Numbers must only contain digits."

    max_len = max(len(operands[0]), len(operands[1]))

    problem_lines[0] += " " * 2 + " " * (
        max_len - len(operands[0])) + operands[0] + " " * 4

    problem_lines[1] += operator + " " + " " * (
        max_len - len(operands[1])) + operands[1] + " " * 4

    problem_lines[2] += "-" * (max_len + 2) + " " * 4

    if with_results:
      result_len = len(str(eval(promblem)))
      problem_lines[3] += " " + ("" if result_len > max_len else " " * (
          (max_len - result_len) + 1)) + str(eval(promblem)) + " " * 4

  arranged_problems = ""
  for line in problem_lines:
    arranged_problems += line.rstrip() + "\n"

  return arranged_problems.rstrip()
