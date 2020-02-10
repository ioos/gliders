# gliders
The front page / home page for IOOS National Glider DAC

Please do not file issues here,  all GliderDAC related issues should be filed in the [IOOS National Glider Data Assembly Center (V2)](OOS National Glider Data Assembly Center (V2)) repository.


# Installation

0. Download and install nodeJS (should come with npm)
0. Install `yarn` using your package manager. Instructions can be found [here](https://legacy.yarnpkg.com/en/docs/install/).
   
   ```
   npm install -g bower
   ```

   _You may need to run as sudo_

0. Install grunt

   ```
   npm install -g grunt-cli
   ```

0. Use `yarn` to build the project dependencies

   ```
   yarn
   ```

0. Run the project

    ```
    node bin/www
    ```

0. Accessing via localhost in browser:
  ```
    http://localhost:3000
  ```

# Docker build

The Docker build is far simpler:

```
$ docker build -t <tag> -f Dockerfile .
```

__NOTE__: ensure that `public/lib` is removed *before* building. If it exists,
`yarn` will attempt to use the existing one in the Docker build, breaking the symlink
in the container and lead to ugly CSS.

# Developing

## Deployed files:
gliders.ioos.us is the wordpress site
gliders.ioos.us/data is this repo.

Most of this project are static files. The initial pages are loaded as jade
templates.  

# Update the .env file with config variables
For testing Google Analytics and things that use env variables.
Update the .env file in your root folder similar to this:
```
GOOGLE_ANALYTICS_ID=YOUR_ENV_VAR_HERE
```
