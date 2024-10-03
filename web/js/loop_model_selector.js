import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.LoopModelSelector",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_LoopModelSelector") {
            const updateModelInputs = () => {
                const numModelsWidget = node.widgets.find(w => w.name === "number_of_models");
                if (!numModelsWidget) return;

                const numModels = numModelsWidget.value;
                const checkpointsList = node.widgets.find(w => w.name === "model_1").options.values;
                
                // Remove excess model widgets
                node.widgets = node.widgets.filter(w => !w.name.startsWith("model_") || parseInt(w.name.split("_")[1]) <= numModels);
                
                // Add new model widgets if needed
                for (let i = 1; i <= numModels; i++) {
                    const widgetName = `model_${i}`;
                    if (!node.widgets.find(w => w.name === widgetName)) {
                        const defaultIndex = Math.min(i - 1, checkpointsList.length - 1);
                        node.addWidget("combo", widgetName, checkpointsList[defaultIndex], () => {}, { 
                            values: checkpointsList
                        });
                    }
                }
                
                // Reorder widgets
                node.widgets.sort((a, b) => {
                    if (a.name === "number_of_models") return -1;
                    if (b.name === "number_of_models") return 1;
                    if (a.name === "seed") return 1;
                    if (b.name === "seed") return -1;
                    if (a.name.startsWith("model_") && b.name.startsWith("model_")) {
                        return parseInt(a.name.split("_")[1]) - parseInt(b.name.split("_")[1]);
                    }
                    return a.name.localeCompare(b.name);
                });
                
                node.setSize(node.computeSize());
            };

            // Set up number_of_models widget
            const numModelsWidget = node.widgets.find(w => w.name === "number_of_models");
            if (numModelsWidget) {
                numModelsWidget.callback = () => {
                    updateModelInputs();
                    app.graph.setDirtyCanvas(true);
                };
            }

            // Set seed widget to integer input
            const seedWidget = node.widgets.find((w) => w.name === "seed");
            if (seedWidget) {
                seedWidget.type = "HIDDEN"; // Hide seed widget after restoring saved state
            }

            // Handle deserialization
            const originalOnConfigure = node.onConfigure;
            node.onConfigure = function(info) {
                if (originalOnConfigure) {
                    originalOnConfigure.call(this, info);
                }
                
                // Restore model widgets based on saved properties
                const savedProperties = info.properties;
                if (savedProperties) {
                    Object.keys(savedProperties).forEach(key => {
                        if (key.startsWith("model_")) {
                            const widgetName = key;
                            const widgetValue = savedProperties[key];
                            const existingWidget = node.widgets.find(w => w.name === widgetName);
                            if (existingWidget) {
                                existingWidget.value = widgetValue;
                            } else {
                                node.addWidget("combo", widgetName, widgetValue, () => {}, { 
                                    values: node.widgets.find(w => w.name === "model_1").options.values
                                });
                            }
                        }
                    });
                }
                
                // Ensure seed is a valid integer
                const seedWidget = node.widgets.find(w => w.name === "seed");
                if (seedWidget && isNaN(parseInt(seedWidget.value))) {
                    seedWidget.value = 0; // Set a default value if invalid
                }
                
                // Update model inputs after restoring saved state
                updateModelInputs();
            };

            // Initial update
            updateModelInputs();
        }
    }
});
