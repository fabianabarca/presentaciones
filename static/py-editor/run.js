function runCode(id) {
    var pyCode = readCode(id);

    let htmlTag = `
<script type="py" target="output-${id}" config='{"packages":["numpy", "scipy", "matplotlib", "pandas"]}'>
from pyscript import display

${pyCode}
</script>
`;

    let div = document.createElement("div");
    div.innerHTML = htmlTag;
    var pyDiv = div.firstElementChild;

    var outputDiv = document.getElementById("output-" + id);
    outputDiv.appendChild(pyDiv);
    outputDiv.classList.add("output-container");

    let nextDiv = document.createElement("div");
    outputDiv.insertBefore(nextDiv, pyDiv.nextSibling);

    pyDiv = nextDiv;
}

function readCode(id) {
    var iframe = document.getElementById("iframe-" + id);
    var code = Reveal.ace[iframe.id].getValue();
    return code;
}

