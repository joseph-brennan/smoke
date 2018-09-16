## To run tests from the command prompt:

##	1. For all three subsets of tests (editor/backend/smokr)
		*from the /smoke/ directory	
	 	*$ docker-compose -f docker-compose.test.yml up

##	2. From editor
		*from the /smoke/ directory
		*$ docker-compose -f docker-compose.yml up
		*from a web browser, visit localhost:8080 and go to the editor tab

##	3. From backend
		*from the smoke/smoke-backend directory
		*$ .travis/test.sh

##	4. From smokr
		*from the smoke/smokr directory
		*$ .travis/test.sh
