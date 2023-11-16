# r = 讀取
# w = 覆寫
# a = 在原先的資料後寫

# file = open("123.txt" , mode="r")
# file = open("123.txt" , mode="w")
# file = open("123.txt" , mode="a" , encoding="utf-8")
# file.write("\n 你好")
# # print(file.readlines())
# file.close()

with open("123.txt" , mode="a" , encoding="utf-8") as file:
    file.write("\n 哈哈")
