# **Zeply_CodeChallenge**

# Description : 

### **Context** : This project was created as part of a challenge for a company named Zeply.The purpose of this code challenge is to assess my technical skills, namely, code structure, code quality, naming conventions, knowledge of commonly used frameworks, and overall problem-solving skills. 

<br>

In this Python challenge we want you to implement a simple REST API for
generating valid cryptocurrency addresses and displaying them. 
Specifically, your API should provide three endpoints, as follows:
1. **Generate Address**  : The core functionality of the API is to take a cryptocurrency as input and return a valid
address for that currency as output. 
2. **List Addresses** : The List endpoint takes no input and returns a list of all the
addresses generated so far.
3. **Retrieve Addresses** : The Retrieve endpoint takes an ID, and returns the corresponding
address as stored in the database.

<br>

#  How to use :

1. Download or fork the project
2. Use pip install -r requirements.txt 
3. You can import the three endpoints from YourProjectFile.endpoints 

```
from YourProjectFile.endpoints import retrieve_address, list_address,generate_address
```
**example** :
```
from endpoints import retrieve_address, list_address,generate_address
class TestStringMethods(unittest.TestCase):
    def integration_test(self) :
            '''If we create two row in the database using the same private key it should return the same private key and public         
             address'''
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
```