from quest import Que


test = [
    "\n1 + 3 = ?\n\n(a) 3 \n(b) 4 \n(c) 5 \n\n",
    "\n一公尺等於幾公分 ?\n\n(a) 10 \n(b) 1000 \n(c) 100 \n\n",
    "\n香蕉是什麼顏色 ?\n(a) 黃色 \n(b) 紅色 \n(c) 粉色 \n\n"
]

questions = [
    Que(test[0],"b"),
    Que(test[1],"c"),
    Que(test[2],"a")
]

print(Que.ques)

# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(Que.ques)