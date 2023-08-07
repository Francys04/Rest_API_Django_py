
## Rest-API-Django-Frame
- This project is a Django-based RESTful API for managing advocates and companies. It provides endpoints for performing CRUD operations on advocates and companies, with JWT token-based authentication.

### Table of Contents
- Overview
- Features
- Advocates
- Companies
- Installation
- Usage
- API Endpoints
- Authentication
- Contributing
- License
- Serializer
#### Overview
- Project Name is a powerful Django project that leverages the Django REST framework to create an API for managing advocates and companies. It provides a user-friendly way to interact with the database using CRUD operations, while also ensuring data security through JWT token-based authentication.

#### Features
1. Advocates
- List all advocates with the ability to search by name or bio.
- Create a new advocate.
- View advocate details.
- Update advocate information.
- Delete advocates.
2. Companies
- List all companies.
- View company details, including the count of associated advocates.
- Create a new company.
### Installation
- Clone the repository:
git clone  https://github.com/Francys04/Rest_API_Django_py
- cd your-project
- Create and activate a virtual environment: 
source venv/bin/activate  # On Windows: venv\Scripts\activate
- Install project dependencies:
`pip install -r requirements.txt`
- Run database migrations:
`python manage.py migrate`
- Usage
Start the development server:

`python manage.py runserver`
- Access the API endpoints at http://127.0.0.1:8000/.

### API Endpoints
1. GET /advocates: List all advocates. Supports searching by name or bio using the query parameter.

2. POST /advocates: Create a new advocate.

3. GET /advocates/:username: View advocate details.

4. PUT /advocates/:username: Update advocate information.

5. DELETE /advocates/:username: Delete an advocate.

6. GET /companies: List all companies.

7. GET /companies/:id: View company details, including the count of associated advocates.

8. POST /companies: Create a new company.

### Authentication
To access endpoints that require authentication, you need to obtain a JWT (JSON Web Token). Follow these steps:

1. Use the /token endpoint to obtain a JWT token by providing your valid credentials (username and password) in the request body.
`curl -X POST http://127.0.0.1:8000/token/ -d "username=yourusername&password=yourpassword"`
- The response will include an access token and a refresh token. Use the access token in the Authorization header of your API requests:
`curl -H "Authorization: Bearer your-access-token" http://127.0.0.1:8000/advocates/`
- If the access token expires, use the refresh token to obtain a new one using the /token/refresh endpoint.

`curl -X POST http://127.0.0.1:8000/token/refresh/ -d "refresh=your-refresh-token"`
2. Examples
- List all advocates:

`curl http://127.0.0.1:8000/advocates/`
- Create a new advocate:

`curl -X POST http://127.0.0.1:8000/advocates/ -d "username=alex&bio=Experienced advocate"`
- Retrieve details of an advocate:

`curl http://127.0.0.1:8000/advocates/alex/`
Update advocate information:

`curl -X PUT http://127.0.0.1:8000/advocates/alex/ -d "username=alexander&bio=Experienced advocate, specialized in criminal law"`
- Delete an advocate:

`curl -X DELETE http://127.0.0.1:8000/advocates/alex/`
- List all companies:

`curl http://127.0.0.1:8000/companies/`
- Retrieve details of a company:

`curl http://127.0.0.1:8000/companies/1/`
- Create a new company:

`curl -X POST http://127.0.0.1:8000/companies/ -d "name=LawFirm"`
#### !!! Remember to replace yourusername and yourpassword with your actual credentials when making requests!!!

#### AdvocateSerializer
- The AdvocateSerializer is responsible for converting Advocate model instances into JSON representations and vice versa. It specifies how the Advocate model fields should be serialized and deserialized.
```
class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()  # Nested serializer to include Company details

    class Meta:
        model = Advocate
        fields = ['username', 'bio', 'company']
```
- ModelSerializer: Inheriting from ModelSerializer automatically generates serializer fields based on the specified model's fields. It saves you from explicitly defining each field.

- company = CompanySerializer(): Here, you're including a nested serializer for the company field, which is a ForeignKey relationship to the Company model. This means that when an Advocate is serialized, the associated Company details will also be included in the serialized output.

- fields = ['username', 'bio', 'company']: Specifies which fields from the Advocate model should be included in the serialized output.

- CompanySerializer
The CompanySerializer follows a similar structure to the AdvocateSerializer and handles the serialization and deserialization of Company model instances.

```
class CompanySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
```
- ModelSerializer: Similar to AdvocateSerializer, this indicates that you want to use the ModelSerializer behavior for serializing and deserializing the Company model.

- employee_count = SerializerMethodField(read_only=True): This field is a custom field that doesn't directly correspond to a model field. It uses SerializerMethodField to include derived or calculated data in the serialized output. In this case, get_employee_count method calculates the count of employees associated with the company.

- fields = '__all__': This specifies that you want to include all fields from the Company model in the serialized output.

- Serializers are an essential part of building RESTful APIs with Django Rest Framework. They allow you to define the structure of your API responses and handle data validation during request parsing. By using serializers, you can ensure that data is presented consistently and efficiently between the frontend and backend of your application.