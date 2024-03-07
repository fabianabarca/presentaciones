from pyscript import document

def onready():
    loader = document.querySelector(".loader")
    loader.className = "bi bi-caret-right-fill link-success"
    
onready()