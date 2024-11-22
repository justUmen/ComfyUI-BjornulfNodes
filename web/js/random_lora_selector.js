import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.RandomLoraSelector",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_RandomLoraSelector") {
            node.properties = node.properties || {};
            const updateLoraInputs = () => {
                const initialWidth = node.size[0];
                const numLorasWidget = node.widgets.find(w => w.name === "number_of_loras");
                if (!numLorasWidget) return;

                const numLoras = numLorasWidget.value;
                const loraList = node.widgets.find(w => w.name === "lora_1")?.options?.values || [];

                // Save existing properties before clearing widgets
                node.widgets.forEach(w => {
                    if (w.name.startsWith("lora_") || ["strength_model", "strength_clip", "seed", "control_after_generate"].includes(w.name)) {
                        node.properties[w.name] = w.value;
                    }
                });

                // Remove all LORA widgets
                node.widgets = node.widgets.filter(w => !w.name.startsWith("lora_"));

                // Ensure shared strength widgets exist (top section)
                const ensureWidget = (name, type, defaultValue, config) => {
                    let widget = node.widgets.find(w => w.name === name);
                    if (!widget) {
                        const savedValue = node.properties[name];
                        widget = node.addWidget(type, name,
                            savedValue !== undefined ? savedValue : defaultValue,
                            value => { node.properties[name] = value; },
                            config
                        );
                    } else {
                        widget.value = node.properties[name] || widget.value;
                    }
                };

                ensureWidget("number_of_loras", "number", 3, { min: 1, max: 20, step: 1 });
                ensureWidget("strength_model", "number", 1.0, { min: -100.0, max: 100.0, step: 0.01 });
                ensureWidget("strength_clip", "number", 1.0, { min: -100.0, max: 100.0, step: 0.01 });
                ensureWidget("seed", "number", 0, { step: 1 });
                ensureWidget("control_after_generate", "checkbox", false, {});

                // Add LORA widgets (bottom section)
                for (let i = 1; i <= numLoras; i++) {
                    const loraWidgetName = `lora_${i}`;
                    const savedLoraValue = node.properties[loraWidgetName];
                    node.addWidget("combo", loraWidgetName,
                        savedLoraValue !== undefined ? savedLoraValue : loraList[0],
                        value => { node.properties[loraWidgetName] = value; },
                        { values: loraList }
                    );
                }

                // Reorder widgets: shared widgets first, followed by LORA widgets
                const sharedWidgetNames = ["number_of_loras", "strength_model", "strength_clip", "seed", "control_after_generate"];
                const sharedWidgets = sharedWidgetNames.map(name => node.widgets.find(w => w.name === name));
                const loraWidgets = node.widgets.filter(w => w.name.startsWith("lora_"));
                const remainingWidgets = node.widgets.filter(w => !sharedWidgets.includes(w) && !loraWidgets.includes(w));

                node.widgets = [...sharedWidgets, ...remainingWidgets, ...loraWidgets];
                node.setSize(node.computeSize());
                node.size[0] = initialWidth; // Keep width fixed
            };

            // Set up number_of_loras widget callback
            const numLorasWidget = node.widgets.find(w => w.name === "number_of_loras");
            if (numLorasWidget) {
                numLorasWidget.callback = () => {
                    updateLoraInputs();
                    app.graph.setDirtyCanvas(true);
                };
            }

            // Handle deserialization
            const originalOnConfigure = node.onConfigure;
            node.onConfigure = function(info) {
                if (originalOnConfigure) {
                    originalOnConfigure.call(this, info);
                }

                // Restore saved properties
                if (info.properties) {
                    Object.assign(this.properties, info.properties);
                }

                // Update the widgets based on the current number_of_loras value
                updateLoraInputs();
            };

            // Save properties during serialization
            const originalOnSerialize = node.onSerialize;
            node.onSerialize = function(info) {
                if (originalOnSerialize) {
                    originalOnSerialize.call(this, info);
                }
                info.properties = { ...this.properties };
            };

            // Initial update
            updateLoraInputs();
        }
    }
});
