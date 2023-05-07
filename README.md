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

1. Download the [dockerhub file](https://hub.docker.com/layers/chipsi44/zeplyname/1.0/images/sha256:1f7bc927ba57a2a1469091c305e0eb55723fd1cc0bdf556bca89bdf62139d240) or build the dockerfile
2. lauch the dockerfile on the port 5000

```
docker run  -p 5000:5000 my_container_name  
```


# The database

The database used for this project is hosted on a free online service called render.com. It is a PostgreSQL database that contains a single table with columns for ID, coin, and public address.

Note that for security purposes and to avoid polluting the database, it will be taken offline once the project review is complete.

It's worth mentioning that since we don't use relations inside the database, a lightweight SQLite database file would have been sufficient. However, I wanted to demonstrate my ability to create a database on a hosted service, as well as showcase my experience using more advanced databases.

As a side note, I used pgAdmin to manage the PostgreSQL database. PgAdmin is a popular open-source administration and management tool for PostgreSQL, which provides a user-friendly interface for performing common database tasks.

# The visual

# Last note : 
Please note that this project was created as part of a company challenge, and the comments present in the code were added for the benefit of the recruiter.

To gain a better understanding of the functionalities implemented in this project, it is recommended that you review the source code. If you have any questions or concerns, please feel free to reach out to me for clarification.
