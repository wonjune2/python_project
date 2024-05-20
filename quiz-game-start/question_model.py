class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

question = Question("text", False)

print(question.text)