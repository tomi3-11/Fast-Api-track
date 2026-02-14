# Hello World API
Here is a simple api that has one endpoint and returns a simple `hello from fastapi` message.

## Features
- A simple index route
- A docker container
- Shell scripts for automation

## How to use the scripts and run the application
All the commands are in the shell script u can just run the following or open the file and run the commnds individually

1. You need to make the script executable first.
    1. Check if executable
    ```sh
    ls -la
    ```
        1. Output (Not executable)
        ```sh
        -rw-r--r-- 1 hakan hakan  198 Jan 24 22:19 build_and_run.sh
        ```
        2. Output (Executable)
        ```sh
        -rwxr-xr-x 1 hakan hakan  198 Jan 24 22:21 build_and_run.sh
        ```
    2. If not then do this
    ```sh
    chmod +x build_and_run.sh
    ```
2. Now run the script
```sh
# Replace the image-name and container-name with the actual names

./build_and_run.sh "<image-name>" "<container-name>"
```

3. Go to your browser at:
```sh
# Just plain Json in the browser
http://127.0.0.1:8000

# using swagger UI
http://127.0.0.1:8000/docs

# Redoc
http://127.0.0.1:8000/redoc
```

More can be got from the project files
