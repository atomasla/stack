## Github Actions

### Issue #11 Build and push the image to the Docker hub using Github Actions (ci.yaml)
Imagine for a moment that you are forced to build manually the docker image whenever you make a little change to your application code.  
Would it be tedious right?  
Now imagine you also have to test and push your changes to a registry manually so that your deployments can pull the latest version from this registry.  
Every single time your code changes... You would probably quit software development, right? I would do the same. 

I'm glad there exist a lot of tools that automate the continuous integration process. Github Actions is one of them.  
In this case, we focus on the continuous integration pipeline but there is a lot more, such as continuous deployment(we will use later), sending emails, monitoring, changing file content, testing... and they are all pre-built in the Marketplace, we just have to copy the ones we want to use and paste them inside the .github/workflows directory.

We can split the yaml into 2 parts: the triggers, and the jobs.  

The triggers, as its name suggests, will trigger the jobs whenever a Github event occurs. There is a lot of events but the most common are push and pull request.  
Note that you will need to specify the name of the branch in which this event will take place. 

The jobs are nothing but actions you want to take when the event occurs. The yaml may contain one or more jobs that will run in parallel inside the Github servers. In our file, there is only one job, but it contains 3 different steps, these will run sequentially.

The first step checkouts the repo, It will set the Github environment working directory to our repo root directory.

The second one logs in against the Docker registry. It needs the DOCKERHUB_USERNAME and DOCKERHUB_TOKEN secrets, which we have previously uploaded to the repo settings.

Once we are logged we can build and push the image. This is done in the last step.  
Remember that the build context and the Dockerfile are not located in the same directory. So we must pass the context and file parameters to the action as if we were doing it on our local machine.

In summary, we have created a workflow that whenever a push happens in the master branch(includes the pull request merges) will automatically build and push the image to the atomasla/stack docker registry. In the DevOps world, this is what we call continuous integration.
