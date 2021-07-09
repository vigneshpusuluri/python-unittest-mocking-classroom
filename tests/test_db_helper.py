from src.db_helper import DbHelper
from unittest import TestCase
from unittest import mock

class testDbHelper(TestCase):

    def setUp(self):
        self.test = DbHelper()
        

    def test_without_mock(self):
        actualresult = self.test.get_maximum_salary()
        expecteresult = 499999
        self.assertEqual(actualresult,expecteresult)

    @mock.patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self , Mocking_db_helper):
        test_db=Mocking_db_helper()

        test_db.get_maximum_salary.return_value = 499999
        max=self.test.get_maximum_salary()
        
        test_db.get_minimum_salary.return_value = 10001
        min=self.test.get_minimum_salary()
        
        self.assertGreater(max,min)
