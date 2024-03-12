function runCode(id) {
    var pyCode = readCode(id);

    let htmlTag = `
<py-script>
${pyCode}
</py-script>
`;

    let div = document.createElement("div");
    div.innerHTML = htmlTag;
    var pyDiv = div.firstElementChild;

    var outputDiv =  document.getElementById("output-" + id);
    outputDiv.appendChild(pyDiv);

    try {
        pyDiv.evaluate();
    } catch (error) {
        console.error("Python error:");
        console.error(error);
    }

    let nextDiv = document.createElement("div");
    outputDiv.insertBefore(nextDiv, pyDiv.nextSibling);

    pyDiv = nextDiv;
}

function readCode(id) {
    var iframe = document.getElementById("iframe-" + id);
    var code = Reveal.ace[iframe.id].getValue();
    return code;
}