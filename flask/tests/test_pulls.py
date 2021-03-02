from unittest import TestCase
from handlers import pulls
import json


class TestPulls(TestCase):

    def setUp(self):
        """Init"""

    def test_pulls(self):

        with open('./2.json', 'r') as myfile:
            data = myfile.read()
            # parse file
        input_json = json.loads(data)
        t_open = [{
            'num': 1,
            'title': "Homework144: John Dow",
            'link': "https://github.com/alenaPy/devops_lab/pull/1"
        }]
        t_closed = [{
            'num': 2,
            'title': "Homework111: Krevedko",
            'link': "https://github.com/alenaPy/devops_lab/pull/2"
        }]
        t_accepted = [{
            'num': 3,
            'title': "Homework222: AAA BBB",
            'link': "https://github.com/alenaPy/devops_lab/pull/3"
        }]
        t_nw = [{
            'num': 4,
            'title': "Homework5: CCC DDD",
            'link': "https://github.com/alenaPy/devops_lab/pull/4"
        }]
        self.assertEqual(pulls.get_pulls('open', input_json), t_open)
        self.assertEqual(pulls.get_pulls('closed', input_json), t_closed)
        self.assertEqual(pulls.get_pulls('accepted', input_json), t_accepted)
        self.assertEqual(pulls.get_pulls('needs work', input_json), t_nw)

    def tearDown(self):
        """Finish"""
