## Steps to follow to run the solution:

1) If you don't have Github PAT token, [create](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) a new one , make sure token should have enough permission to read public gists.
2) Open terminal and run below command to export PAT token.

    `export GH_TOKEN=<YOUR-GH-TOKEN>`
3) Clone the repo and build docker image, make sure docker is installed on tour machine

    `docker build -t my-app .`
4) Run container on local machine, make sure port 8080 is free.

    `docker run  -d --env GH_TOKEN -p 8080:8080 my-app`
5) Once container is up and running, api is ready to serve on `/users/<USER>` path.

    `curl localhost:8080/users/<USER>/`

 you should be able to see list of all public gists for the USER.
 ```
 [
   {
    "html_url": <html url of the gist>,
    "url": <url of gist>
  },
   {
    "html_url": <html url of the gist>,
    "url": <url of gist>
  },
  .
  .
  .
 ]
 ```


### Unit testing:
- Follow steps 1 to 3 as mentioned above.
- Run below command to run unit test, make sure port 8080 is free.

  `docker run --env GH_TOKEN -p 8080:8080 my-app test_app.py`
