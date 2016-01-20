# gliders
The front page / home page for IOOS National Glider DAC

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

6. Setup a python virtualenv for this project

   ```
   mkvirtualenv gliders
   ```

7. Install the python dependencies

   ```
   pip install -r requirements/standalone.txt
   ```

8. If you're actively developing and debugging the project install the dev tools

   ```
   pip install -r requirements/dev.txt
   ```

9. Compile the javascript files

   ```
   grunt
   ```

10. Run the project

    ```
    python app.py
    ```

# Developing

Most of this project is static files. The initial pages are loaded as a jinja
template so flask can do dependency injection and asset management.  

Pages link to CSS and Javascript files through the "Assets.json" file which
tells grunt where assets are located and how to compile them.
