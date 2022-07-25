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

To retrieve the current weather in Rome I've searched into a bunch of free APIs.  
OpenWeather offers a free tier subscription which has a maximum of 1.000 calls per day.  
It looked good to me so I signed myself up.  

An API key is required as a parameter on every API call.  
Since I wouldn't be happy if someone gets my personal key and exceed the limit on my name I've considered it as sensible data.
That being said the way I hide the key on my code is by leveraging the os.environment.get() method, which gets the environment variable at the execution time.  
At the time of writing this README file, the key has been exported to my local ubuntu environment but this key will be required wherever this module runs.  
So I will treat this as my first prerequisite.

The rest of the code is very intuitive. The requests module offers a simple get method that returns a response object, once parsed into a json, It hasn't been that difficult to get the temperature and the description by indexing it.
