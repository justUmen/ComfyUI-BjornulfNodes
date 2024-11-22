import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.LoopLoraSelector",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_LoopLoraSelector") {
            node.properties = node.properties || {};

            const updateLoraInputs = () => {
                const initialWidth = node.size[0];
                const numLorasWidget = node.widgets.find(w => w.name === "number_of_loras");
                if (!numLorasWidget) return;

                const numLoras = numLorasWidget.value;
                const loraList = node.widgets.find(w => w.name === "lora_1")?.options?.values || [];
                
                // Remove excess lora widgets
                node.widgets = node.widgets.filter(w => !w.name.startsWith("lora_") || parseInt(w.name.split("_")[1]) <= numLoras);
                
                // Store current widget values in properties
                node.widgets.forEach(w => {
                    if (w.name.startsWith("lora_") || 
                        w.name.startsWith("strength_model_") || 
                        w.name.startsWith("strength_clip_")) {
                        node.properties[w.name] = w.value;
                    }
                });

                // Remove all lora-related widgets
                node.widgets = node.widgets.filter(w => 
                    !w.name.startsWith("lora_") && 
                    !w.name.startsWith("strength_model_") && 
                    !w.name.startsWith("strength_clip_")
                );
                
                // Add widgets only for the specified number of loras
                for (let i = 1; i <= numLoras; i++) {
                    const loraWidgetName = `lora_${i}`;
                    const strengthModelWidgetName = `strength_model_${i}`;
                    const strengthClipWidgetName = `strength_clip_${i}`;

                    // Add lora widget
                    const savedLoraValue = node.properties[loraWidgetName];
                    const loraWidget = node.addWidget("combo", loraWidgetName, 
                        savedLoraValue !== undefined ? savedLoraValue : loraList[0], 
                        (value) => {
                            node.properties[loraWidgetName] = value;
                        }, { 
                            values: loraList
                        }
                    );

                    // Add strength model widget
                    const savedModelValue = node.properties[strengthModelWidgetName];
                    const strengthModelWidget = node.addWidget("number", strengthModelWidgetName, 
                        savedModelValue !== undefined ? savedModelValue : 1.0, 
                        (value) => {
                            node.properties[strengthModelWidgetName] = value;
                        }, { 
                            min: -100.0, max: 100.0, step: 0.01 
                        }
                    );

                    // Add strength clip widget
                    const savedClipValue = node.properties[strengthClipWidgetName];
                    const strengthClipWidget = node.addWidget("number", strengthClipWidgetName, 
                        savedClipValue !== undefined ? savedClipValue : 1.0, 
                        (value) => {
                            node.properties[strengthClipWidgetName] = value;
                        }, { 
                            min: -100.0, max: 100.0, step: 0.01 
                        }
                    );
                }
                
                // Reorder widgets: number_of_loras first, then grouped lora widgets
                const orderedWidgets = [node.widgets.find(w => w.name === "number_of_loras")];
                for (let i = 1; i <= numLoras; i++) {
                    const loraWidgets = node.widgets.filter(w => 
                        w.name === `lora_${i}` || 
                        w.name === `strength_model_${i}` || 
                        w.name === `strength_clip_${i}`
                    );
                    orderedWidgets.push(...loraWidgets);
                }
                
                // Add any remaining widgets
                orderedWidgets.push(...node.widgets.filter(w => !orderedWidgets.includes(w)));
                node.widgets = orderedWidgets;
                
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
                
                // if (info.properties) {
                //     // Restore properties
                //     Object.assign(this.properties, info.properties);
                // }
                // const savedProperties = info.properties;
                // if (savedProperties) {
                //     Object.keys(savedProperties).forEach(key => {
                //         if (key.startsWith("lora_") || key.startsWith("strength_model_") || key.startsWith("strength_clip_")) {
                //             const widgetName = key;
                //             const widgetValue = savedProperties[key];
                //             const existingWidget = node.widgets.find(w => 
                //                 w.name === widgetName
                //             );
                //             if (existingWidget) {
                //                 existingWidget.value = widgetValue;
                //             } else {
                //                 const baseWidget = node.widgets.find(w => 
                //                     w.name === "lora_1" || 
                //                     w.name === "strength_model_1" || 
                //                     w.name === "strength_clip_1"
                //                 );
                //                 if (baseWidget) {
                //                     node.addWidget("combo", widgetName, widgetValue, () => {}, { 
                //                         values: baseWidget.options.values
                //                     });
                //                 }
                //             }
                //         }
                //     });
                // }
            // Save properties during serialization
            const originalOnSerialize = node.onSerialize;
            node.onSerialize = function(info) {
                if (originalOnSerialize) {
                    originalOnSerialize.call(this, info);
                }
                info.properties = { ...this.properties };
            };


                // Update the widgets based on the current number_of_loras value
                updateLoraInputs();
            };

            // Initial update
            updateLoraInputs();
        }
    }
});