<div id="top"></div>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/atomasla/stack">
    <img src="../images/stack-logo.jpeg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">s t a c k</h3>
</div>



<!-- ABOUT THE PROJECT -->
## Python

### Issue #5 Get the current weather in Rome
To retrieve the current weather in Rome I've searched into a bunch of free APIs.  
OpenWeather offers a free tier subscription which has a maximum of 1.000 calls per day.  
It looked good to me so I signed myself up.  

An API key is required as a parameter on every API call.  
Since I wouldn't be happy if someone gets my personal key and exceed the limit on my name I've considered it as sensitive data.
That being said the way I hide the key on my code is by leveraging the os.environment.get() method, which gets the environment variable at the execution time.  
At the time of writing this README file, the key has been exported to my local ubuntu environment but this key will be required wherever this module runs.  
So I will treat this as my first prerequisite.

I think the rest of the code is very intuitive. The requests module offers a get method that returns a response object that I have parsed into a json.  
I obtain the temperature and a short description by indexing this json and then the method ends returning a string with both data concatenated.


### Issue #7 Deploy an API to serve the current weather in Rome
The main goal of this issue is to create a REST API to serve the current weather in Rome.
You might think that I'm reinventing the wheel by offering the same API data that I get from a public one.
Well, you are right but please remember that this is not relevant. We focus on the stack.
Maybe in the close future some fancy features like adding other cities will be added to the service... or a fancy quote in the native language of the queried city... Anyways, this is not important right now.

Since I've chosen python to get this data from a public API, I think it is a good idea to find a python library to set the API service.  
FastAPI has been the chosen one. It has been kind of fast deployment as the name suggests. However, I would like to focus on the main issues I found while developing this new python module called main.py


The first topic: asynchrony.
As I mentioned before, I get the data from an external/public/free REST API, and that requires a request/response between my local machine and the service.

If I want to show off this data on the API service and I don't use any asynchronous clauses the only thing that it will be shown is a "500 Internal Server Error". This happens because we are trying to publish some data we don't yet have. So, we must wait for the public API call ends, and we will be able to serve the data we want from this first call.
The only way I can do this in the asynchronous way is by using async/await clauses. An async clause is added to the get_weather function, and an await is needed whenever this function is called. In this particular case, inside the body of our API rome_weather method.

The other topic is about the weather_api_token environment variable. Once solved the problem above the first executions returned an "Invalid API key" response. That is because FastAPI uses uvicorn server under the hood to serve the API in your local machine. But it has its own environment, so whenever you want to start the service up you must pass the API key. 

The deployment of the service will be:
```
WEATHER_API_KEY="b7dd7a710ec496df969b47a6f9481e5a" uvicorn main:app
```
Instead of 
```
uvicorn main:app
```
By default, the service listens requests on the port 8000, so according to my main.py the actual request will run on http://localhost:8000/rome

Last but not least notice that we are using the FastAPI and uvicorn external libraries, so a previous installation will be required.
I think there are a few ways to do that but in my opinion the pip package manager is the easiest one.
So the execution of these 2 following commands was needed
```
pip install fastapi
pip install uvicorn[standard]
```
A reboot was needed in my local machine. However, the important thing here is we must keep in mind these 2 libraries will probably be part of our future requirements.txt. A text file that will contain all the required external libraries. 
