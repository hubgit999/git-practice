def simple_calculator():
    """
    一个简单的加减法计算器。
    它会提示用户输入两个数字和一个操作符 (+ 或 -)，然后输出结果。
    """
    print("--- 简单加减法计算器 ---")

    try:
        # 提示用户输入第一个数字
        num1 = float(input("请输入第一个数字: "))

        # 提示用户输入操作符
        operator = input("请输入操作符 ('+' 或 '-'): ")

        # 提示用户输入第二个数字
        num2 = float(input("请输入第二个数字: "))

    except ValueError:
        # 捕获非数字输入错误
        print("错误：请输入有效的数字。")
        return  # 退出函数

    # 进行计算
    if operator == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif operator == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    else:
        # 处理无效的操作符输入
        print("错误：操作符无效。请使用 '+' 或 '-'。")


# 运行计算器函数
simple_calculator()