import logging

import logging

# 1 Create your custom logger
parent = logging.getLogger("app")
parent.setLevel(logging.DEBUG)
parent.propagate = False  # stop bubbling to root

# 2 Create a handler
filehandler = logging.FileHandler("toto", encoding="utf-8")
consolehandler = logging.StreamHandler()
formatter = logging.Formatter("{asctime} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M")
filehandler.setFormatter(formatter)

# 3 Attach handler to logger
parent.addHandler(filehandler)
parent.addHandler(consolehandler)

print(parent.handlers)

parent.warning("Watch out!")    