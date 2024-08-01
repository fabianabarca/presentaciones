from pyscript import document

def onready():
    loaders = document.querySelectorAll(".loader")
    for loader in loaders:
        loader.className = "bi bi-caret-right-fill link-primary"

onready()