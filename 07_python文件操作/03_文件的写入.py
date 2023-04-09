"""
演示文件的写入操作
"""
# 打开文件，不存在的文件, r, w, a
f = open("../data/test.txt", "w", encoding="UTF-8")
# write写入
f.write("Hello!!!")  # 内容写入到内存中
# flush刷新
# f.flush()  # 将内存中积攒的内容，写入到硬盘的文件中
# # close关闭
f.close()  # close方法，内置了flush的功能的
