from add_subtract import add, subtract
from multiply_divide import multiply, divide

print("欢迎使用加减计算器！")

expression = input("请输入一个表达式 (例如: 10 * 5): ")

parts = expression.split()

num1 = float(parts[0])
operator = parts[1]
num2 = float(parts[2])

result = None

# 整合了所有运算
if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = subtract(num1, num2)
elif operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    result = divide(num1, num2)
else:
    print(f"错误：不支持的运算符 '{operator}'")

if result is not None:
    print(f"计算结果是: {result}")