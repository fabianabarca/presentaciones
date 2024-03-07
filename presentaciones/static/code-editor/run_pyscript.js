var pyDiv;

function runCode(id) {
    var pyCode = readCode(id);

    if (pyDiv) {
        pyDiv.remove();
    }

    let htmlTag = `
<py-script>
${pyCode}
</py-script>
`;

    let div = document.createElement("div");
    div.innerHTML = htmlTag;
    pyDiv = div.firstElementChild;

    var outputDiv =  document.getElementById("output-" + id);
    outputDiv.appendChild(pyDiv);

    let nextDiv = document.createElement("div");
    outputDiv.insertBefore(nextDiv, pyDiv.nextSibling);

    try {
        pyDiv.evaluate();
    } catch (error) {
        console.error("Python error:");
        console.error(error);
    }

    auxPyDiv = pyDiv;
    pyDiv = nextDiv;
}

function readCode(id) {
    var iframe = document.getElementById("iframe-" + id);
    var code = Reveal.ace[iframe.id].getValue();
    return code;
}