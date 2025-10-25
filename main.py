# main.py

# 导入你负责的乘除法函数
from multiply_divide import multiply, divide

# 为你的同学预留导入位置，他们实现功能后可以取消这行注释
# from add_subtract import add, subtract

print("欢迎使用简易计算器！")

#获取用户表达式
expression = input("请输入一个表达式 (中间请加空格,例如: 10 * 5): ")


# "10 * 5" -> ["10", "*", "5"]
parts = expression.split()

num1 = float(parts[0])
operator = parts[1]
num2 = float(parts[2])

result = None

# 根据运算符，调用相应的函数
if operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    result = divide(num1, num2)

else:
    print(f"错误：不支持的运算符 '{operator}'")

# 打印结果
if result is not None:
    print(f"计算结果是: {result}")