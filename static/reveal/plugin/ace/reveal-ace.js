var version = "1.32.7";
var mode = "python";
var theme = "monokai";

function writeHTML(currentDocument, version, mode, theme, code) {
	var html = 
`
<!DOCTYPE html>
<html>
<head>
	<script src='https://cdnjs.cloudflare.com/ajax/libs/ace/${version}/ace.js' type='text/javascript' charset='utf-8'></script>
	<script src='https://cdnjs.cloudflare.com/ajax/libs/ace/${version}/mode-${mode}.js' type='text/javascript' charset='utf-8'></script>
	<script src='https://cdnjs.cloudflare.com/ajax/libs/ace/${version}/theme-${theme}.js' type='text/javascript' charset='utf-8'></script>
	<script src='https://cdnjs.cloudflare.com/ajax/libs/ace/${version}/ext-themelist.js' type='text/javascript' charset='utf-8'></script>
	<script src='https://cdnjs.cloudflare.com/ajax/libs/ace/${version}/ext-error_marker.js' type='text/javascript' charset='utf-8'></script>
</head>
<body>
	<div id='editor' style='position:absolute; left:0; top:0; bottom:0; right:0;'>${code}</div>
</body>
</html>
`;
	currentDocument.write(html);
	return currentDocument;
}

var RevealAce = window.RevealAce || (function() {
	if(!Reveal.ace) Reveal.ace = {};

	function extend(o) {
		for(var i = 1; i < arguments.length; i++)
			for(var key in arguments[i])
				o[key] = arguments[i][key];
		return o;
	};

	function buildEditor(iframe) {
		var iframeWindow = iframe.contentWindow, currentDocument = iframeWindow.document;
		currentDocument = writeHTML(currentDocument, version, mode, theme, iframe.innerHTML)
			
		iframe.onload = function() {
			var editor = iframeWindow.ace.edit(currentDocument.getElementById('editor'));
						
			var fetched_mode = iframeWindow.ace.require("ace/mode/" + mode).Mode;
			editor.session.setMode(new fetched_mode());

			editor.session.setOptions({
				wrapMethod: "code",
			});

			editor.setOptions({
				customScrollbar: true,
				highlightActiveLine: true,
				wrapBehavioursEnabled: true,
				highlightGutterLine: true,
				autoScrollEditorIntoView: true,
				animatedScroll: true,
				copyWithEmptySelection: true,			
				fontSize: "12pt",
				theme: "ace/theme/" + theme
			});

			// Events
			if(iframe.dataset.oninit)
				(new Function("editor", iframe.dataset.oninit)).call(editor, editor);
			
			if(options.onchange)
				editor.getSession().on('change', options.onchange);

			if(iframe.dataset.onchange) {
				var onchange = new Function("value", "editor", iframe.dataset.onchange);

				editor.getSession().on('change', function() {
					var value = editor.getValue();
					return onchange.call(editor, value, editor);
				});
			}

			if(iframe.id) {
				Reveal.ace[iframe.id] = editor;
			}
		};

		currentDocument.close();
	}

	var module = {};
	var config = Reveal.getConfig();
	var options = extend({
		className: "ace",
		autoFocus: false,
		onchange: null,
		oninit: null
	}, config.ace || {});

	var aceTags = document.getElementsByClassName(options.className);

	for(var i = 0; i < aceTags.length; i++) {
		if(!aceTags[i].contentWindow) {
			console.warn("Ace editors must be embedded in an iframe.");
			continue;
		}

		buildEditor(aceTags[i]);
	}

	return module;
})();