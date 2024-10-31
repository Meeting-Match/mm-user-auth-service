# mm-user-auth-service
Implements a microservice for managing user authentication, registration, and profile data for the Meeting Match application.

### What does this do?
- The auth is now using Django REST Framework. This will do a lot of nice backend API stuff for us like serialize our models. I think we should probably end up doing this for the rest of the microservices.
- It is also using Simple JWT Authentication for Django REST Framework.
- The interface works like this:
	- It is called by the frontend.
	- The two URLs you have are `register` and `token`.
	- `register` takes a username, email, and password, and creates a user based off of these.
	- `token` takes a username and password, and if these are valid, it will return a JWT token. This token is stored by the frontend, which includes it in headers when making calls to the other microservices. The other microservices will decrypt this token and confirm it represents a valid user. It will also contain some information about the user like permissions. 
		- The auth microservice is currently quite minimal so we may have to add permissions later.
