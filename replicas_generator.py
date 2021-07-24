MAX_LENGTH = 30


class Option:
    def __init__(self, text, link):
        self.text = text
        self.link = link

    def convert(self):
        return {
            "text": self.text,
            "link": self.link
        }


class Replica:
    def __init__(self,
                 name,
                 avatars,
                 text,
                 options):
        self.name = name
        self.avatars = avatars
        self.text = text
        self.options = options

    def __split_on_sentences(self, st):
        return st.split('. ')

    def __numerated_name(self, num):
        if not num:
            return self.name
        return f"{self.name}ad{num}"

    def split(self):
        res = []

        sentences = self.__split_on_sentences(self.text)
        i = 0
        sum_ = 0
        text = []
        c = 0
        while i < len(sentences):
            cur = sentences[i]
            l = len(cur.split())

            if not sum_ or l + sum_ <= MAX_LENGTH:
                text.append(cur)
                sum_ += l
                i += 1
            else:
                new = Replica(
                    name=self.__numerated_name(c),
                    avatars=self.avatars,
                    text='. '.join(text) +'.',
                    options=[Option("Далее", self.__numerated_name(c + 1))]
                )
                sum_ = 0
                text = []
                c += 1
                res.append(new)

        if text:
            new = Replica(
                name=self.__numerated_name(c),
                avatars=self.avatars,
                text='. '.join(text) + '.',
                options=[Option("Далее", self.__numerated_name(c + 1))]
            )
            res.append(new)

        res[-1].options = self.options
        res[-1].text = res[-1].text[:-1]
        return res

    def convert(self):
        replicas = self.split()
        res = {}

        for replica in replicas:
            cur = {"avatar": replica.avatars, "text": replica.text, "options": [x.convert() for x in replica.options]}
            res[replica.name] = cur

        return res


if __name__ == '__main__':
    avatar = [
        "static/img/helper1.png",
        "static/img/helper3.png",
        "static/img/helper4.png",
        "static/img/helper5.png"
    ]
    text = "Привет! Меня зовут Либби, я здесь, чтобы помочь тебе разобраться в своём сайте. Если у тебя будут ко мне вопросы - обращайся."
    name = "greet"

    options = [Option("У меня есть к тебе вопрос", "sections")]

    rep = Replica(name=name, avatars=avatar, text=text, options=options)
    print(rep.convert())
