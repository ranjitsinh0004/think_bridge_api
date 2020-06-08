## think_bridge_api
1. For the frontend `HTML,CSS,BOOTSTRAP,jquery script` have been used.
2. For the backend `Django Rest Framework` is used.
3. `Pipenv` is used as a packaging tool.
4. testcases for views,models,urls are written
5. API tesing is done with `POSTMAN`
6. Generated requirements.txt using `pipenv lock -r > requirements.txt`

### How to run the project?
1. open the terminal change the directory to project.
        `cd think_bridge_api`
        `cd Sadguru_api_prj`
2. Run the virtual environment using following command
        `pipenv shell`
3. Install the dependencies
        `pip install -r requirements.txt`
4. Run the server
        `py manage.py runserver`
5. Open the browser and observe the response on it.
        `http://127.0.0.1:8000/listapi/`
6. Click on the `+Add New` to add new products on the basis of `Beverages` or `Snacks`
7. Click on the hyperlinked products you will get the detail information of the product.
6. Created super user. To login to admin interface
        `http://127.0.0.1:8000/admin/`
        `username:admin`
        `password:admin`


### How to run testcases?
1. to run all the testcases in the `tests` folder add following command into the terminal
        `python manage.py test`

### Tracking
1. frontend functionality: 2 days
2. backend functionality: 3 days
3. Testcases/testing: 1-2 days
