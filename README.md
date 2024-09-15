# Pixtral_Recipies
Pixtral Notebooks and Notes

Note: Currently the pixtral model takes 24GB of memory and there is no quantized version available that be be used
to serve using vLLM, hence we will revisit this at a later time

# In order to test this project, we can do that following

```
    (pixtralai-ARkyVg7q-py3.10) (base) cerebrum@cerebrum:~/Projects/Pixtral_Recipies$ poetry env info

    Virtualenv
    Python:         3.10.12
    Implementation: CPython
    Path:           /home/cerebrum/.cache/pypoetry/virtualenvs/pixtralai-ARkyVg7q-py3.10
    Valid:          True

    System
    Platform: linux
    OS:       posix
    Python:   /usr
```

    1. Add the abobe Path as the Python Interpreter
    2. python3 -m pytest --capture=no
