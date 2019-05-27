"""
Module that can test CallCentre.

It uses unittest an EX08_helper modules.
"""
import unittest
import EX08_helper


class Testing_CallCentre(unittest.TestCase):

    """
    Class to test callcentre.

    Use unittest module.
    """

    def setup(self):
        """
        CallCenter object creation using EX08_helper.get_callcentre().

        Define object from CallCenter and return it.
        Using module EX08_helper we create object and from there we use funktsioon get_callcentre().
        """
        call_centre_instance = EX08_helper.get_callcentre()
        return call_centre_instance

    def test_noun(self):
        """Test where input noun should return koer."""
        cc = self.setup()
        create = cc.create_sentence
        res1 = create('noun')
        self.assertEqual(res1, 'koer')

    def test_sentence(self):
        """Test where input sentence should return koer sööb koera."""
        cc = self.setup()
        create = cc.create_sentence
        res1 = create('sentence')
        self.assertEqual(res1, 'koer sööb koera .')

    def test_noun_loop(self):
        """Test if noun list loops back to beginning."""
        cc = self.setup()
        create = cc.create_sentence
        for i in range(7):
            res1 = create('noun')
        self.assertEqual(res1, 'porgand')

    def test_random_input(self):
        """Test if without commands input is returned."""
        cc = self.setup()
        create = cc.create_sentence
        res1 = create('Random sen')
        self.assertEqual(res1, 'Random sen')

    def test_beautifulsentence(self):
        """Test if beautifulsentence gives correct result."""
        cc = self.setup()
        create = cc.create_sentence
        res1 = create('beautifulsentence')
        self.assertEqual(res1, 'ilus koer sööb ilusat koera .')

    def test_twosentences(self):
        """Test if twosentences gives correct result."""
        cc = self.setup()
        create = cc.create_sentence
        res1 = create('twosentences')
        self.assertEqual(res1, 'koer sööb koera . porgand lööb porgandit .')

    def test_empty(self):
        """Test if empty input returns correctly."""
        cc = self.setup()
        create = cc.create_sentence
        res1 = create('')
        self.assertEqual(res1, '')

    def test_beautifulsentence_after_loop(self):
        """Test if beautifulsentence after looping gives correct result."""
        cc = self.setup()
        create = cc.create_sentence
        for i in range(8):
            res1 = create('beautifulsentence')
        self.assertEqual(res1, 'pahane madis jagab pahast madist .')

    def test_verb_noun_sentence_tadjective(self):
        """Test for input of verb, noun, sentence and targetadjective."""
        cc = self.setup()
        create = cc.create_sentence
        res1 = create('verb noun sentence targetadjective')
        self.assertEqual(res1, 'sööb koer porgand lööb koera . ilusat')

    def test_noun_randomInput_verb(self):
        """Test for random inputs inbetween commands."""
        cc = self.setup()
        create = cc.create_sentence
        res1 = create('noun Luik3d3 Järv verb !?@')
        self.assertEqual(res1, 'koer Luik3d3 Järv sööb !?@')

    def test_all_nouns(self):
        """Test for 5 nouns."""
        cc = self.setup()
        create = cc.create_sentence
        res1 = create('noun noun noun noun noun')
        self.assertEqual(res1, 'koer porgand madis kurk tomat')


if __name__ == "__main__":
    unittest.main(verbosity=5)
