import random

class Quiz(object):
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.answered = ""
        self.answer_list = []
        self.false_count = 0

    def quiz_handler(self):
        template = "*"*30 + '\n問題 : {}\n解答を入力してください\n'+ '↓'*15

        print(f'古典常識クイズを開始します。問題数は{len(self.dictionary)}問です。')
        print("難読語 -> ひらがな")
        print("文学作品 -> 作者名 or 作者不明")
        switch = input("クイズを開始しますか？ y/[N] : ")

        while switch == "y" and len(self.dictionary) != 0:
            word = random.choice(list(self.dictionary.keys()))
            print(template.format(word))
            answer = input("入力してください : ")
            if answer == "Quit":
                return "[Quit]が入力されたため、クイズを終了します。"
            elif answer == self.dictionary[word]:
                self.answered = self.dictionary.pop(word)
                self.answer_list.append(self.answered)
                print("正解です。")
                print(f'残り : {len(self.dictionary)}問!')
            elif answer != self.dictionary[word]:
                print("不正解です。")
                self.false_count += 1
                print(f'正解は[{self.dictionary[word]}]です。')
                print(f'不正解数 : {self.false_count}問です！')
        else:
            return f"問題数が0になったため、クイズを終了します。\n不正解数 : {self.false_count}"
