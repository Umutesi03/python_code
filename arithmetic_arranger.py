def arithmetic_arranger(problems , show_answers=False):
    if len(problems) > 5:
        return "Error : To many problems"
    
    first_operands=[]
    second_operands=[]
    lines=[]
    answers=[]

    for problem in problems :
        parts= problem.split()

        operand1 ,operator ,operand2 =parts

        if operator not in ["+" ,"-"]:
            return "Error: Operator must be '+' or '-'."
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1) >4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."  
        
        if operator == "+":
            result = str(int(operand1) + int(operand2))
        else:
            result = str(int(operand1) - int(operand2))     

        width = max(len(operand1),len(operand2)) + 2

        first_operands.append(operand1.rjust(width))
        second_operands.append(operator + " " + operand2.rjust(width-2))
        lines.append("-" * width)
        answers.append(result.rjust(width))

        arranged_first= "    ".join(first_operands)
        arranged_second= "    ".join(second_operands)
        arranged_lines = "    ".join(lines)

    if show_answers:
        arranged_answers= "    ".join(answers)
        return f"{arranged_first}\n{arranged_second}\n{arranged_lines}\n{arranged_answers}"
    else:
        return f"{arranged_first}\n{arranged_second}\n{arranged_lines}"
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')        