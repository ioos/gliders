# gliders
The front page / home page for IOOS National Glider DAC

Please do not file issues here,  all GliderDAC related issues should be filed in the [IOOS National Glider Data Assembly Center (V2)](OOS National Glider Data Assembly Center (V2)) repository.


# Installation

1. Download and install nodeJS (should come with npm)
2. Install bower
   
   ```
   npm install -g bower
   ```

   _You may need to run as sudo_

3. Install grunt

   ```
   npm install -g grunt-cli
   ```

4. Use node to build the project dependencies

   ```
   npm install
   ```

5. Use bower to install the UI depencies

   ```
   bower install
   ```

6. Run the project

    ```
    bin/www
    ```

# Developing

Most of this project are static files. The initial pages are loaded as jade
templates.  
