import unittest
from endpoints import retrieve_address, list_address,generate_address
import time
from selenium import webdriver

def verify_address(url,number_of_address) :    
    #Scrapping function used to verify that an address exist or not    
    driver = webdriver.Firefox()  
    driver.get(url)
    #used to let the page load
    time.sleep(2)
    if "There are "+number_of_address+" blockchains with result(s) to your search:" in driver.page_source:
        driver.close()
        return True
    else:
        driver.close()
        return False

class TestStringMethods(unittest.TestCase):
    '''
        Since this project is meant to be completed in three days, I won't be able to thoroughly test every aspect of it. 
        While I am aware that additional tests could be written to cover areas such as error handling and memory limitations, 
        it's important to keep in mind that testing is a whole job in itself.
        Therefore, for the purposes of this project, I focused on writing tests that cover the most critical functionality.
    '''
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
        #Let's verify that the address exist.
        '''
        I used a scraping function to test the address. Even though I know it's not the most optimized solution (a more optimized 
        solution would have been to use a library to check the address), I wanted to showcase that I know how to do simple scraping.
        That's also why the function verify_address as been created in the test/main file.
        '''
        self.assertTrue(verify_address('https://www.blockchain.com/fr/explorer/search?search='+retrieve_address(b)[2],'2'))

    '''
    Now that I have demonstrated my knowledge of using unittest, I am going to write an integration test that covers all three endpoints.
    '''
    def integration_test(self) :
        '''If we create two row in the database using the same private key it should return the same private key and public address'''
        seed1,private_key1,public_address1 = generate_address('BTC')
        seed2,private_key2,public_address2 = generate_address('BTC',private_key1)
        self.assertEqual([private_key1,public_address1], [private_key2,public_address2])

        '''Since list_address returns a list of all the elements in the database, 
        and the last two elements are exactly the same (except for the ID), we should be able to compare them.'''
        list_all_elements = list_address()
        self.assertEqual(list_all_elements[-2][1:],list_all_elements[-1][1:])
        
        '''
        Now that we have verified that the last two elements in the list of addresses are identical, 
        we can also check that they correspond by using retrieve_address and the id
        '''
        id1 = list_all_elements[-1][0]
        id2 = list_all_elements[-2][0]
        self.assertEqual(retrieve_address(id1)[1:], retrieve_address(id2)[1:])
if __name__ == '__main__':
    unittest.main()