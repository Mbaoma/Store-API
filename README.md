# Store-API

## Description
This project is implemented using Flask and is a REST API for a store. 
The endpoints can be used to add items to, fetch item(s) from, edit items in, and delete items from a store.
Also names of stores can be added and retrieved from the database using the assigned endpoints.

## Installation
-   Ensure you have [Python](www.python.org) installed on your PC
  
-   Run the following command in the terminal to create a virtual environment 
```
python -m venv venv
```

-   Run the following command in the terminal to activate your virtual environment
 ``` 
 source venv/Scripts/activate
```

-   Run the following command in the terminal to install the dependencies in the requirements.txt file
``` 
pip install -r requirements.txt
```

## Test the Endpoints

-   Run ``` python app.py ``` to start the server.

-   Test the endpoints using [Postman](https://app.getpostman.com/join-team?invite_code=d692faed7a5db8bdd2b7dadfd55a34cb&ws=85327001-f59e-4ad1-be89-49d0afa6456f)

    -   Steps
  
        1.  /register
            ![image](https://user-images.githubusercontent.com/49791498/103707288-a240ed80-4fae-11eb-88c2-939d067ad610.png)

        2.  /auth
            ![image](https://user-images.githubusercontent.com/49791498/103707174-79b8f380-4fae-11eb-8bf2-7f5ad9ad30aa.png)

        3. /item/name [POST]
            ![image](https://user-images.githubusercontent.com/49791498/103707825-a588a900-4faf-11eb-9e72-28393684fd44.png)

        4. /item/name [GET]
            ![image](https://user-images.githubusercontent.com/49791498/103708116-3cedfc00-4fb0-11eb-81d3-d1bf1f2c7943.png)

        5.  /items [GET]
            ![image](https://user-images.githubusercontent.com/49791498/103708479-f2b94a80-4fb0-11eb-9bf6-a63654317590.png)
        
        6.  /item/name [PUT]
            ![image](https://user-images.githubusercontent.com/49791498/104425860-74950f00-5581-11eb-8bd7-b5a17e093055.png)
        
        7.  /item/name [DELETE]
            ![image](https://user-images.githubusercontent.com/49791498/104426181-e2d9d180-5581-11eb-9331-b7bc12e42e52.png)

        8.  /store/name [POST]
            ![image](https://user-images.githubusercontent.com/49791498/104423201-17e42500-557e-11eb-9ea5-ae83fa233769.png)

        9. /stores [GET]
            ![image](https://user-images.githubusercontent.com/49791498/104423353-46620000-557e-11eb-9df2-1e50f0747e89.png)

        10. /store/name [DELETE]
            ![image](https://user-images.githubusercontent.com/49791498/104424417-a0af9080-557f-11eb-9a48-bead079cd76b.png)
        
        11. /store/name [GET]
            ![image](https://user-images.githubusercontent.com/49791498/104425294-cc7f4600-5580-11eb-82fb-601c4d69ce67.png)
 
 This project is hosted on [heroku](https://my-shops.herokuapp.com/)
 


