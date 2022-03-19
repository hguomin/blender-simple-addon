# A simple Blender add-on with debugging enabled

## How to run

1. Install Blender version 3.0  
After Blender was installed in you system, add the folder path where blender.exe located to the PATH environment variable. 

2. Get Blender's built-in Python installation path and install packages  
    Execute below command in your terminal and note down the output path:  
    ```bash
    blender --background --python-expr "import sys; print(sys.exec_prefix)"
    ```

    Install python packages in above python environment(replace {blender python path} with the path you get above):    

    ```bash  
    {blender python path}\bin\python -m ensurepip && pip install debugpy fake-bpy-module-3.0
    ```

3. Run Blender with the add-on  
    In vscode, press `CTRL+SHIFT+B` to launch Blender

4. Start debugging
    In vscode, use the `Python: Remote Attach` configuration to start debug

5. Execute the command in Blender
    In Blender, select menu `Object -> Move object by one unit`, you will see all objects in the scene will be moved by on unit in X direction.

That's it.