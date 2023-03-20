# orhelper
orhelper is a module which aims to facilitate interacting and scripting with OpenRocket from Python.

## Prerequisites
- OpenRocket 15.03
- Java JDK 1.8
     - [Open JDK 1.8](https://github.com/ojdkbuild/ojdkbuild)
     - [Oracle JDK 8](https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html) (requires signup)
     - Ubuntu: `sudo apt-get install openjdk-8-jre`
- Python >=3.6

## Setup JDK

### Linux
For most people jpype will be able to automatically find the JDK. However, if it fails or you want to be sure you are using the correct version, add the JDK path to a JAVA_HOME environment variable:
- Find installation directory (e.g. `/usr/lib/jvm/[YOUR JDK 1.8 FOLDER HERE]`)
- Open the `~/.bashrc` file with your favorite text editor (will likely need sudo privileges)
- Add the following line to the `~/.bashrc` file:
    ```
    export JAVA_HOME="/usr/lib/jvm/[YOUR JDK 1.8 FOLDER HERE]"
    ```
- Restart your terminal or run the following for the changes to take effect:
    ```
    source ~/.bashrc
    ```

### Windows

- Set Windows environment variables to the following:
    - Oracle
        ```
        JAVA_HOME = C:\Program Files\Java\[YOUR JDK 1.8 FOLDER HERE]
        ```
    - OpenJDK
        ```
        JAVA_HOME = C:\Program Files\ojdkbuild\[YOUR JDK 1.8 FOLDER HERE]
        ```

## Installing

- Install orhelper from pip
    ```
    pip install orhelper
    ```

- [Download](https://github.com/openrocket/openrocket/releases/download/release-15.03/OpenRocket-15.03.jar) the OpenRocket .jar file (if you don't already have it)
    - Linux  
        ```
        wget https://github.com/openrocket/openrocket/releases/download/release-15.03/OpenRocket-15.03.jar
        ```

- Set environment variable `CLASSPATH` path to OpenRocket .jar file. (Only required if it's not already at `.\OpenRocket-15.03.jar`)
    ```
    CLASSPATH=\some\path\to\OpenRocket-15.03.jar
    ```
  --- WLOO ROCKETRY: An OpenRocket is already provided in this repo, set your CLASSPATH to that one. ---
  --- If it is your first time running you may need to first do 
  ```
  $ java -jar OpenRocket.jar
  ```
  and load the engine RSE (Kismet) and save the rocket along with the engine to your desired ork file. ---
- See `examples/` for usage examples
- See [the OpenRocket wiki](https://github.com/openrocket/openrocket/wiki/Scripting-with-Python-and-JPype) for more info on usage and the examples 

  --- FORMAT :
  ```
  time, altitude, total accel, total vel, stability, air pressure
  ```
  ---

 ## Usage (for WLOO ROCKETRY):
 ```
 $ bash ./examples/mc_script.sh <num runs>
 ```
 
 - Please change the configurations in `examples/monte_carlo.py` as needed.

## Credits
- Richard Graham for the original script: [Source](https://sourceforge.net/p/openrocket/mailman/openrocket-devel/thread/4F17AA0C.1040002@rdg.cc/)
- @not7cd for some initial organization and clean-up: [Source](https://github.com/not7cd/orhelper)
- And of course everyone who has contributed to OpenRocket over the years.
