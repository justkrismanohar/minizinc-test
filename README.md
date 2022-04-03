# Deploying Minizinc on Heroku

1. Go to heroku dashboard and create an applicaton. Let say you named it your-minizinc-app
2. Login with the Heroku CLI <code>heroku login</code>
3. At the CLI set the app to run as a container <code>heroku stack:set container -a your-minizinc-app</code>
4. Go the heroku dashboard for your app, go to settings verify the stack is set to container
5. Configure the <code>Dockerfile</code> to software for the applicaiton. The sample <code>Dockerfile</code> builds from the minizinc/minizinc:latest-alpine. This image has minzinc installed on the alpine. Starting from there, python and the base application are installed.
6. Confgiure the <code>heroku.yml</code> file. The sample <code>heroku.yml</code> builds web process based on the <code>Dockerfile</code>. Ensure <code>run</code> in <code>heroku.yml</code> is configured to start your application. 
7. Push repository to GitHub.
8. On the heroku dashboard for your app, go to the deploy tab, under deployment method choose GitHub. You may need to grant heroku permissions. 
9. Search for the repository with the  <code>Dockerfile</code> and <code>heroku.yml</code> files to deploy. 
10. Once the repository is found, click connect.
11. At this point you can configure what brach you would like deploy, set auto-deployment options etc. Then click deploy branch.
12. If there are any errors it will show up in the deployment logs.




### References

1. https://devcenter.heroku.com/articles/build-docker-images-heroku-yml#run-defining-the-processes-to-run
2. https://hub.docker.com/r/minizinc/minizinc
