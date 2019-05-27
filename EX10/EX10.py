"""
Module that can create sentence with create_sentence function.

autor: Jaanus
"""


class CallCentre():

    """
    Class that uses function create_sentence to make sentences.

    Has commands that get replaced with given words.
    """

    def __init__(self):
        """Contain indexes matched with parts of the sentence in the generator."""
        self.noun = CallCentre.generator(0)
        self.target = CallCentre.generator(2)
        self.verb = CallCentre.generator(1)
        self.adjective = CallCentre.generator(3)
        self.targetadj = CallCentre.generator(4)

    def generator(index):
        """Cycle through words."""
        # lists = [[nouns], [verbs], [targets], [adjectives], [target adjectives]]
        lists = [['koer', 'porgand', 'madis', 'kurk', 'tomat'], ['sööb', 'lööb', 'jagab', 'tahab', 'ei taha'], ['koera', 'porgandit', 'madist', 'kurki', 'tomatit'], ['ilus', 'kole', 'pahane', 'magus', 'sinu'], ['ilusat', 'koledat', 'pahast', 'magusat', 'sinu']]
        while True:
            for word in lists[index]:
                yield word

    def create_sentence(self, text):
        """Function that using given string replaces commands with words."""
        text = text.replace('beautifulsentence', 'adjective noun verb targetadjective target .')
        text = text.replace('twosentences', 'sentence sentence')
        text = text.replace('sentence', 'noun verb target .')
        text = text.split(' ')
        instructions = ('noun', 'verb', 'target', 'adjective', 'targetadjective')
        command = [self.noun, self.verb, self.target, self.adjective, self.targetadj]
        new_text = [word if word not in instructions else next(command[instructions.index(word)]) for word in text]
        return ' '.join(new_text)

if __name__ == "__main__":
    n = CallCentre()
    print(n.create_sentence('noun noun ! sentence beautifulsentence @ twosentences'))
    n = CallCentre()
    print(n.create_sentence('noun noun noun noun noun noun noun noun'))
