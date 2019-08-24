# pyramid-docker
Sample web application development environment with docker-compose, pipenv and pyramid

# Bootstraping docker pipenv pyramid system

Resources:
- https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tour.html
- https://docs.pipenv.org/en/latest/install/
- https://hub.docker.com/r/kennethreitz/pipenv/dockerfile


1. Start with simple `docker-compose.yml` file:
   ```
   version: '3'
   services:

     webapp:
       image: kennethreitz/pipenv
       volumes:
         - .:/app
         - ./.local:/root/.local
       command: tail -f /dev/null
   ```
   We mount our code folder to /app and `./.local` to store the virtualenv of our app


2. Get the container up:
```
$ docker-compose up
```

3. From another shell, get into the container:
```
$ docker-compose exec webapp bash
```

4. Setup an env and install pyramid
```
# pipenv --three
# pipenv install pyramid
```

5. Check the environment:
```
(app)# pipenv shell
(app)# pip freeze
```

6. Follow https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tour.html#hello-world

7. Update the docker-compose.yml file with the exposed port and application runner:
```
version: '3'
services:

  webapp:
    image: kennethreitz/pipenv
    volumes:
      - .:/app
      - ./.local:/root/.local
    ports:
      - 6543:6543
    command: pipenv run python ./app.py
```
   With this setup you still need to restart the docker-compose when you changed the code.

8. For installing new packages, you can use from the bash command line:
```
$ docker-compose exec webapp pipenv install pyramid_jinja2
```
