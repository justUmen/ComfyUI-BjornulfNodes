import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.LoopLoraSelector",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_LoopLoraSelector") {
            const updateLoraInputs = () => {
                const numLorasWidget = node.widgets.find(w => w.name === "number_of_loras");
                if (!numLorasWidget) return;

                const numLoras = numLorasWidget.value;
                const loraList = node.widgets.find(w => w.name === "lora_1").options.values;
                
                // Remove excess lora widgets and their corresponding strength widgets
                node.widgets = node.widgets.filter(w => 
                    !w.name.startsWith("lora_") && 
                    !w.name.startsWith("strength_model_") && 
                    !w.name.startsWith("strength_clip_") || 
                    parseInt(w.name.split("_").pop()) <= numLoras
                );
                
                // Add new lora widgets and their corresponding strength widgets if needed
                for (let i = 1; i <= numLoras; i++) {
                    const loraWidgetName = `lora_${i}`;
                    const strengthModelWidgetName = `strength_model_${i}`;
                    const strengthClipWidgetName = `strength_clip_${i}`;

                    if (!node.widgets.find(w => w.name === loraWidgetName)) {
                        const defaultIndex = Math.min(i - 1, loraList.length - 1);
                        node.addWidget("combo", loraWidgetName, loraList[defaultIndex], () => {}, { 
                            values: loraList
                        });
                    }

                    if (!node.widgets.find(w => w.name === strengthModelWidgetName)) {
                        node.addWidget("number", strengthModelWidgetName, 1.0, () => {}, { 
                            min: -100.0, max: 100.0, step: 0.01 
                        });
                    }

                    if (!node.widgets.find(w => w.name === strengthClipWidgetName)) {
                        node.addWidget("number", strengthClipWidgetName, 1.0, () => {}, { 
                            min: -100.0, max: 100.0, step: 0.01 
                        });
                    }
                }
                
                // Reorder widgets
                const orderedWidgets = [node.widgets.find(w => w.name === "number_of_loras")];
                for (let i = 1; i <= numLoras; i++) {
                    orderedWidgets.push(
                        node.widgets.find(w => w.name === `lora_${i}`),
                        node.widgets.find(w => w.name === `strength_model_${i}`),
                        node.widgets.find(w => w.name === `strength_clip_${i}`)
                    );
                }
                orderedWidgets.push(...node.widgets.filter(w => !orderedWidgets.includes(w)));
                node.widgets = orderedWidgets.filter(w => w !== undefined);
                
                node.setSize(node.computeSize());
            };

            // Set up number_of_loras widget
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
                
                // Restore lora widgets and strength widgets based on saved properties
                const savedProperties = info.properties;
                if (savedProperties) {
                    Object.keys(savedProperties).forEach(key => {
                        if (key.startsWith("lora_") || key.startsWith("strength_model_") || key.startsWith("strength_clip_")) {
                            const widgetName = key;
                            const widgetValue = savedProperties[key];
                            const existingWidget = node.widgets.find(w => w.name === widgetName);
                            if (existingWidget) {
                                existingWidget.value = widgetValue;
                            } else {
                                if (key.startsWith("lora_")) {
                                    node.addWidget("combo", widgetName, widgetValue, () => {}, { 
                                        values: node.widgets.find(w => w.name === "lora_1").options.values
                                    });
                                } else {
                                    node.addWidget("number", widgetName, widgetValue, () => {}, { 
                                        min: -100.0, max: 100.0, step: 0.01 
                                    });
                                }
                            }
                        }
                    });
                }
                
                // Update lora inputs after restoring saved state
                updateLoraInputs();
            };

            // Initial update
            updateLoraInputs();
        }
    }
});