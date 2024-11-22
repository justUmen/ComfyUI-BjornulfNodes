import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.LoopModelSelector",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_LoopModelSelector") {
            node.properties = node.properties || {};

            const updateModelInputs = () => {
                const initialWidth = node.size[0];
                const numModelsWidget = node.widgets.find(w => w.name === "number_of_models");
                if (!numModelsWidget) return;

                const numModels = numModelsWidget.value;
                const checkpointsList = node.widgets.find(w => w.name === "model_1")?.options?.values || [];

                // Remove excess model widgets
                node.widgets = node.widgets.filter(w => 
                    !w.name.startsWith("model_") || parseInt(w.name.split("_")[1]) <= numModels
                );

                // Store current widget values in properties
                node.widgets.forEach(w => {
                    if (w.name.startsWith("model_")) {
                        node.properties[w.name] = w.value;
                    }
                });

                // Remove all model-related widgets
                node.widgets = node.widgets.filter(w => 
                    !w.name.startsWith("model_")
                );

                // Add new model widgets
                for (let i = 1; i <= numModels; i++) {
                    const widgetName = `model_${i}`;
                    const savedValue = node.properties[widgetName];
                    const defaultIndex = Math.min(i - 1, checkpointsList.length - 1);
                    const defaultValue = savedValue !== undefined ? savedValue : checkpointsList[defaultIndex];

                    const modelWidget = node.addWidget("combo", widgetName, defaultValue, (value) => {
                        node.properties[widgetName] = value;
                    }, { 
                        values: checkpointsList
                    });
                }

                // Reorder widgets: number_of_models first, then the model widgets
                const orderedWidgets = [node.widgets.find(w => w.name === "number_of_models")];
                for (let i = 1; i <= numModels; i++) {
                    const modelWidgets = node.widgets.filter(w => w.name === `model_${i}`);
                    orderedWidgets.push(...modelWidgets);
                }

                // Add any remaining widgets
                orderedWidgets.push(...node.widgets.filter(w => !orderedWidgets.includes(w)));
                node.widgets = orderedWidgets;

                // Adjust node size
                node.setSize(node.computeSize());
                node.size[0] = initialWidth; // Keep width fixed
            };

            // Set up number_of_models widget callback
            const numModelsWidget = node.widgets.find(w => w.name === "number_of_models");
            if (numModelsWidget) {
                numModelsWidget.callback = () => {
                    updateModelInputs();
                    app.graph.setDirtyCanvas(true);
                };
            }

            // Handle deserialization
            const originalOnConfigure = node.onConfigure;
            node.onConfigure = function(info) {
                if (originalOnConfigure) {
                    originalOnConfigure.call(this, info);
                }

                // Restore model widgets based on saved properties
                // const savedProperties = info.properties;
                // if (savedProperties) {
                //     Object.keys(savedProperties).forEach(key => {
                //         if (key.startsWith("model_")) {
                //             const widgetName = key;
                //             const widgetValue = savedProperties[key];
                //             const existingWidget = node.widgets.find(w => w.name === widgetName);

                //             if (existingWidget) {
                //                 existingWidget.value = widgetValue;
                //             } else {
                //                 const checkpointsList = node.widgets.find(w => w.name === "model_1")?.options?.values || [];
                //                 const defaultIndex = Math.min(parseInt(widgetName.split("_")[1]) - 1, checkpointsList.length - 1);
                //                 node.addWidget("combo", widgetName, widgetValue || checkpointsList[defaultIndex], () => {}, {
                //                     values: checkpointsList
                //                 });
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

                // Update model inputs after restoring saved state
                updateModelInputs();
            };

            // Serialize method to save properties
            const originalSerialize = node.serialize;
            node.serialize = function() {
                const data = originalSerialize ? originalSerialize.call(this) : {};
                data.properties = { ...this.properties };
                return data;
            };

            // Initial update
            updateModelInputs();
        }
    }
});
