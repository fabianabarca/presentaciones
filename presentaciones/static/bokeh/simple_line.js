(function () {
    const fn = function () {
        Bokeh.safely(function () {
            (function (root) {
                function embed_document(root) {
                    const docs_json = '{"ab7be9d1-cca5-46bf-b217-712e397bde70":{"version":"3.3.4","title":"Bokeh Application","roots":[{"type":"object","name":"Figure","id":"p1001","attributes":{"height":400,"sizing_mode":"stretch_width","x_range":{"type":"object","name":"DataRange1d","id":"p1002"},"y_range":{"type":"object","name":"DataRange1d","id":"p1003"},"x_scale":{"type":"object","name":"LinearScale","id":"p1011"},"y_scale":{"type":"object","name":"LinearScale","id":"p1012"},"title":{"type":"object","name":"Title","id":"p1004","attributes":{"text":"Ejemplo de una gr\u00e1fica simple de Bokeh"}},"renderers":[{"type":"object","name":"GlyphRenderer","id":"p1040","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p1034","attributes":{"selected":{"type":"object","name":"Selection","id":"p1035","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p1036"},"data":{"type":"map","entries":[["x",[1,2,3,4,5]],["y",[6,7,2,4,5]]]}}},"view":{"type":"object","name":"CDSView","id":"p1041","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p1042"}}},"glyph":{"type":"object","name":"Line","id":"p1037","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"line_color":"#1f77b4","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p1038","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"line_color":"#1f77b4","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p1039","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"line_color":"#1f77b4","line_alpha":0.2,"line_width":2}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p1010","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p1023"},{"type":"object","name":"WheelZoomTool","id":"p1024","attributes":{"renderers":"auto"}},{"type":"object","name":"BoxZoomTool","id":"p1025","attributes":{"overlay":{"type":"object","name":"BoxAnnotation","id":"p1026","attributes":{"syncable":false,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5}}}},{"type":"object","name":"SaveTool","id":"p1031"},{"type":"object","name":"ResetTool","id":"p1032"},{"type":"object","name":"HelpTool","id":"p1033"}]}},"left":[{"type":"object","name":"LinearAxis","id":"p1018","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1019","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1020"},"axis_label":"Valor de y","major_label_policy":{"type":"object","name":"AllLabels","id":"p1021"}}}],"below":[{"type":"object","name":"LinearAxis","id":"p1013","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p1014","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p1015"},"axis_label":"Valor de x","major_label_policy":{"type":"object","name":"AllLabels","id":"p1016"}}}],"center":[{"type":"object","name":"Grid","id":"p1017","attributes":{"axis":{"id":"p1013"}}},{"type":"object","name":"Grid","id":"p1022","attributes":{"dimension":1,"axis":{"id":"p1018"}}},{"type":"object","name":"Legend","id":"p1043","attributes":{"items":[{"type":"object","name":"LegendItem","id":"p1044","attributes":{"label":{"type":"value","value":"Temp."},"renderers":[{"id":"p1040"}]}}]}}]}}]}}';
                    const render_items = [{ "docid": "ab7be9d1-cca5-46bf-b217-712e397bde70", "roots": { "p1001": "b085a7a4-44c5-4bc4-bbb0-a2c5b3dc7f5c" }, "root_ids": ["p1001"] }];
                    root.Bokeh.embed.embed_items(docs_json, render_items);
                }
                if (root.Bokeh !== undefined) {
                    embed_document(root);
                } else {
                    let attempts = 0;
                    const timer = setInterval(function (root) {
                        if (root.Bokeh !== undefined) {
                            clearInterval(timer);
                            embed_document(root);
                        } else {
                            attempts++;
                            if (attempts > 100) {
                                clearInterval(timer);
                                console.log("Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing");
                            }
                        }
                    }, 10, root)
                }
            })(window);
        });
    };
    if (document.readyState != "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
})();