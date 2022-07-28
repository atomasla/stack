## Docker

### Issue #9 Dockerize the app
In this project, we will use Docker to build an image with all the components of our application.  
Docker is well known for its hub, which provides a lot of images we can pull and use as a base to build our own ones.

So far we have our app on 2 python modules, rome_weather.py & main.py, so we will need python installed on our image.  
We could have started from an OS image like ubuntu or centOS and installed python inside, but since python has an official image that obviously has python installed why don't use this one?  
Indeed, It is a good practice, it reduces the image size. In Docker, the more specific the better.

As you may have noticed our Dockerfile is located inside the /docker directory, and not in the root directory where it is usually.  
Well, that is because I want to maintain a directory per technology structure. I think it is useful because I want to write all these comments regarding each technology, for that I can just create a README.md for each directory.
So, how can we copy the python files (which are located in /python) inside the image (which is located in /docker)?  
The current working directory is called the build context, by default the Dockerfile is assumed to be here, but you can specify a different location with the option -f in the docker build command, and pass one directory (in this case /python) as the build context parameter.

So whenever we want to build the app image, once located in the root directory, we will run:
```
docker build -t stack -f docker/Dockerfile python
```
Instead of:
```
docker build -t stack .
```
Regarding the Dockerfile, I wanted to keep it as simple as possible.  
First, we set by convention the working directory in /usr/src/app, here we copy the requirements.txt which contains all the necessary python libraries.  
Lastly, we copy the build context (.) inside the image working directory (.) so that we have all the python modules copied within the image and located in /usr/src/app/python.