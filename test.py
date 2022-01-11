import app
import unittest
from datetime import date
from project import Project
from constant import *


class Tests(unittest.TestCase):
    def test_set_1(self):
        project_set = [
            Project(date(2015, 9, 1), date(2015, 9, 3), LOW_COST_CITY_TYPE)
        ]

        reimbursement = app.calc_reimbursement(project_set=project_set)
        self.assertEqual(reimbursement, 165)

    def test_set_2(self):
        project_set = [
            Project(date(2015, 9, 1), date(2015, 9, 1), LOW_COST_CITY_TYPE),
            Project(date(2015, 9, 2), date(2015, 9, 6), HIGH_COST_CITY_TYPE),
            Project(date(2015, 9, 6), date(2015, 9, 8), LOW_COST_CITY_TYPE)
        ]

        reimbursement = app.calc_reimbursement(project_set=project_set)
        self.assertEqual(reimbursement, 590)

    def test_set_3(self):
        project_set = [
            Project(date(2015, 9, 1), date(2015, 9, 3), LOW_COST_CITY_TYPE),
            Project(date(2015, 9, 5), date(2015, 9, 7), HIGH_COST_CITY_TYPE),
            Project(date(2015, 9, 8), date(2015, 9, 8), HIGH_COST_CITY_TYPE)
        ]

        reimbursement = app.calc_reimbursement(project_set=project_set)
        self.assertEqual(reimbursement, 445)

    def test_set_4(self):
        project_set = [
            Project(date(2015, 9, 1), date(2015, 9, 1), LOW_COST_CITY_TYPE),
            Project(date(2015, 9, 1), date(2015, 9, 1), LOW_COST_CITY_TYPE),
            Project(date(2015, 9, 2), date(2015, 9, 2), HIGH_COST_CITY_TYPE),
            Project(date(2015, 9, 2), date(2015, 9, 3), HIGH_COST_CITY_TYPE)
        ]

        reimbursement = app.calc_reimbursement(project_set=project_set)
        self.assertEqual(reimbursement, 185)

if __name__ == '__main__':
    unittest.main()
