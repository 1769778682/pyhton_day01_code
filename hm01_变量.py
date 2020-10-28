"""
文件命名规则: 组成内容可包含字母/数字/下划线, 不能以数字开头, 不要使用使用中文
"""
# 保存一个名字
# 变量名 = 数值
# name = '小明'
# NAME = '小红'
# # 姓名 = '小刚'  # 变量名不能用中文
# my_name = '合理'

# 查看 Python 关键字
# 1.导包
import keyword
# 2.调用方法
print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
'return', 'try', 'while', 'with', 'yield']
"""