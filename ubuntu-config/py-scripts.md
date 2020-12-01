# Python "Scripts" tutorial

In order to launch your python scripts (created with the argument parser of your choice) you have to define a directories wherever on your system which i'll call "bin". For Example on your root dir:

```
cd
mkdir bin
```
on your script insert the header (top of the file)

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
```
or `python3`. Move your script to the `bin` directory and make it executable with

```
chmod +x script.py
```

Add the bin directory to `PATH` variable in `.bashrc`

```
export PATH=$PATH:/home/path/to/bin
```

and source it with

```
source .bashrc
```

and you should be good to go
