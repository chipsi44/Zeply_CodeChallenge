import unittest
from endpoints import retrieve_address, list_address

from selenium import webdriver

url = 'https://www.blockchain.com/explorer/search?search=1DWYh3rB35tyK5fWqbZz8crQwbfdDBq8Pv'

driver = webdriver.Firefox()  # replace with appropriate webdriver for your browser
driver.get(url)
if "There are 2 blockchains with result(s) to your search:" in driver.page_source:
    print('The text "Oups! couldn\'t find  what you\'re looking for" was found.')
else:
    print('The text "Oups! couldn\'t find  what you\'re looking for" was not found.')

driver.close()



class TestStringMethods(unittest.TestCase):
    
    def test_retrieve_address(self):
        '''
        In this case, the test is based on the rows with id 7 and 11 in the database.
        However, if those id are not present, you can change them to other valid id. 
        Additionally, there are only two currencies in the test, so if you add more currencies, you should also update the `coin_list`.
        '''
        a = '7'
        b = '11'
        #Let's verify that we can get our three elements (ID,Coin,Address)
        self.assertEqual(len(retrieve_address(a)), 3)
        self.assertEqual(len(retrieve_address(b)), 3)
        print('Three elements test passed')
        #in this test we ensure that we get the id we asked for !
        self.assertEqual(str(retrieve_address(a)[0]), a)
        self.assertEqual(str(retrieve_address(b)[0]), b)
        print("Id test passed")
        #Let's verify that the coin is in our coin list ! 
        coin_list = ["BTC","ETH"]
        self.assertTrue(retrieve_address(a)[1] in coin_list )
        self.assertTrue(retrieve_address(b)[1] in coin_list )
        print("coin test passed")
        

    def test_list_address(self):
        self.assertEqual('FOO','FOO')
        

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
