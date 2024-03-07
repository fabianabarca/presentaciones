var pyDiv;

function runCode(id) {
    var pyOutput =  document.getElementById("output-" + id);
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
    pyOutput.appendChild(pyDiv);

    try {
        pyDiv.evaluate();
    } catch (error) {
        console.error("Python error:");
        console.error(error);
    }
}

function readCode(id) {
    var iframe = document.getElementById("iframe-" + id);
    var code = Reveal.ace[iframe.id].getValue();
    return code;
}