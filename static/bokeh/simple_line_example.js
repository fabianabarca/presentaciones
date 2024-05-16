(function () {
    const fn = function () {
        (function (root) {
            function now() {
                return new Date();
            }

            const force = false;

            if (typeof root._bokeh_onload_callbacks === "undefined" || force === true) {
                root._bokeh_onload_callbacks = [];
                root._bokeh_is_loading = undefined;
            }


            const element = document.getElementById("e29aef14-2fdb-46c3-8424-54b42bfc651f");
            if (element == null) {
                console.warn("Bokeh: autoload.js configured with elementid 'e29aef14-2fdb-46c3-8424-54b42bfc651f' but no matching script tag was found.")
            }
            function run_callbacks() {
                try {
                    root._bokeh_onload_callbacks.forEach(function (callback) {
                        if (callback != null)
                            callback();
                    });
                } finally {
                    delete root._bokeh_onload_callbacks
                }
                console.debug("Bokeh: all callbacks have finished");
            }

            function load_libs(css_urls, js_urls, callback) {
                if (css_urls == null) css_urls = [];
                if (js_urls == null) js_urls = [];

                root._bokeh_onload_callbacks.push(callback);
                if (root._bokeh_is_loading > 0) {
                    console.debug("Bokeh: BokehJS is being loaded, scheduling callback at", now());
                    return null;
                }
                if (js_urls == null || js_urls.length === 0) {
                    run_callbacks();
                    return null;
                }
                console.debug("Bokeh: BokehJS not loaded, scheduling load and callback at", now());
                root._bokeh_is_loading = css_urls.length + js_urls.length;

                function on_load() {
                    root._bokeh_is_loading--;
                    if (root._bokeh_is_loading === 0) {
                        console.debug("Bokeh: all BokehJS libraries/stylesheets loaded");
                        run_callbacks()
                    }
                }

                function on_error(url) {
                    console.error("failed to load " + url);
                }

                for (let i = 0; i < css_urls.length; i++) {
                    const url = css_urls[i];
                    const element = document.createElement("link");
                    element.onload = on_load;
                    element.onerror = on_error.bind(null, url);
                    element.rel = "stylesheet";
                    element.type = "text/css";
                    element.href = url;
                    console.debug("Bokeh: injecting link tag for BokehJS stylesheet: ", url);
                    document.body.appendChild(element);
                }

                for (let i = 0; i < js_urls.length; i++) {
                    const url = js_urls[i];
                    const element = document.createElement('script');
                    element.onload = on_load;
                    element.onerror = on_error.bind(null, url);
                    element.async = false;
                    element.src = url;
                    console.debug("Bokeh: injecting script tag for BokehJS library: ", url);
                    document.head.appendChild(element);
                }
            };

            function inject_raw_css(css) {
                const element = document.createElement("style");
                element.appendChild(document.createTextNode(css));
                document.body.appendChild(element);
            }

            const js_urls = ["https://cdn.bokeh.org/bokeh/release/bokeh-3.3.4.min.js", "https://cdn.bokeh.org/bokeh/release/bokeh-gl-3.3.4.min.js", "https://cdn.bokeh.org/bokeh/release/bokeh-widgets-3.3.4.min.js", "https://cdn.bokeh.org/bokeh/release/bokeh-tables-3.3.4.min.js", "https://cdn.bokeh.org/bokeh/release/bokeh-mathjax-3.3.4.min.js"];
            const css_urls = [];

            const inline_js = [function (Bokeh) {
                Bokeh.set_log_level("info");
            },
            function (Bokeh) {
                (function () {
                    const fn = function () {
                        Bokeh.safely(function () {
                            (function (root) {
                                function embed_document(root) {
                                    const docs_json = '{"f741cfd0-8762-49d6-8f70-1f62fe41158d":{"version":"3.3.4","title":"Bokeh Application","roots":[{"type":"object","name":"Figure","id":"p48166","attributes":{"x_range":{"type":"object","name":"DataRange1d","id":"p48167"},"y_range":{"type":"object","name":"DataRange1d","id":"p48168"},"x_scale":{"type":"object","name":"LinearScale","id":"p48176"},"y_scale":{"type":"object","name":"LinearScale","id":"p48177"},"title":{"type":"object","name":"Title","id":"p48169","attributes":{"text":"Simple line example"}},"renderers":[{"type":"object","name":"GlyphRenderer","id":"p48205","attributes":{"data_source":{"type":"object","name":"ColumnDataSource","id":"p48199","attributes":{"selected":{"type":"object","name":"Selection","id":"p48200","attributes":{"indices":[],"line_indices":[]}},"selection_policy":{"type":"object","name":"UnionRenderers","id":"p48201"},"data":{"type":"map","entries":[["x",[1,2,3,4,5]],["y",[6,7,2,4,5]]]}}},"view":{"type":"object","name":"CDSView","id":"p48206","attributes":{"filter":{"type":"object","name":"AllIndices","id":"p48207"}}},"glyph":{"type":"object","name":"Line","id":"p48202","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"line_color":"#1f77b4","line_width":2}},"nonselection_glyph":{"type":"object","name":"Line","id":"p48203","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"line_color":"#1f77b4","line_alpha":0.1,"line_width":2}},"muted_glyph":{"type":"object","name":"Line","id":"p48204","attributes":{"x":{"type":"field","field":"x"},"y":{"type":"field","field":"y"},"line_color":"#1f77b4","line_alpha":0.2,"line_width":2}}}}],"toolbar":{"type":"object","name":"Toolbar","id":"p48175","attributes":{"tools":[{"type":"object","name":"PanTool","id":"p48188"},{"type":"object","name":"WheelZoomTool","id":"p48189","attributes":{"renderers":"auto"}},{"type":"object","name":"BoxZoomTool","id":"p48190","attributes":{"overlay":{"type":"object","name":"BoxAnnotation","id":"p48191","attributes":{"syncable":false,"level":"overlay","visible":false,"left":{"type":"number","value":"nan"},"right":{"type":"number","value":"nan"},"top":{"type":"number","value":"nan"},"bottom":{"type":"number","value":"nan"},"left_units":"canvas","right_units":"canvas","top_units":"canvas","bottom_units":"canvas","line_color":"black","line_alpha":1.0,"line_width":2,"line_dash":[4,4],"fill_color":"lightgrey","fill_alpha":0.5}}}},{"type":"object","name":"SaveTool","id":"p48196"},{"type":"object","name":"ResetTool","id":"p48197"},{"type":"object","name":"HelpTool","id":"p48198"}]}},"left":[{"type":"object","name":"LinearAxis","id":"p48183","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p48184","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p48185"},"axis_label":"y","major_label_policy":{"type":"object","name":"AllLabels","id":"p48186"}}}],"below":[{"type":"object","name":"LinearAxis","id":"p48178","attributes":{"ticker":{"type":"object","name":"BasicTicker","id":"p48179","attributes":{"mantissas":[1,2,5]}},"formatter":{"type":"object","name":"BasicTickFormatter","id":"p48180"},"axis_label":"x","major_label_policy":{"type":"object","name":"AllLabels","id":"p48181"}}}],"center":[{"type":"object","name":"Grid","id":"p48182","attributes":{"axis":{"id":"p48178"}}},{"type":"object","name":"Grid","id":"p48187","attributes":{"dimension":1,"axis":{"id":"p48183"}}},{"type":"object","name":"Legend","id":"p48208","attributes":{"items":[{"type":"object","name":"LegendItem","id":"p48209","attributes":{"label":{"type":"value","value":"Temp."},"renderers":[{"id":"p48205"}]}}]}}]}}],"defs":[{"type":"model","name":"bokeh_app_9ae0c751bae247bfb71dd92e6b031791.Params","properties":[{"name":"amp","kind":"Any","default":0.1},{"name":"freq","kind":"Any","default":0.1},{"name":"phase","kind":"Any","default":0},{"name":"offset","kind":"Any","default":-5}]},{"type":"model","name":"bokeh_app_c35fabfd0d7149de8a5322c7f372f9b5.Params","properties":[{"name":"amp","kind":"Any","default":0.1},{"name":"freq","kind":"Any","default":0.1},{"name":"phase","kind":"Any","default":0},{"name":"offset","kind":"Any","default":-5}]}]}}';
                                    const render_items = [{ "docid": "f741cfd0-8762-49d6-8f70-1f62fe41158d", "roots": { "p48166": "e29aef14-2fdb-46c3-8424-54b42bfc651f" }, "root_ids": ["p48166"] }];
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
            },
            function (Bokeh) {
            }
            ];

            function run_inline_js() {
                for (let i = 0; i < inline_js.length; i++) {
                    inline_js[i].call(root, root.Bokeh);
                }
            }

            if (root._bokeh_is_loading === 0) {
                console.debug("Bokeh: BokehJS loaded, going straight to plotting");
                run_inline_js();
            } else {
                load_libs(css_urls, js_urls, function () {
                    console.debug("Bokeh: BokehJS plotting callback run at", now());
                    run_inline_js();
                });
            }
        }(window));
    };
    if (document.readyState != "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
})();