import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.RandomModelSelector",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_RandomModelSelector") {
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

            // Set seed widget to hidden input
            const seedWidget = node.widgets.find((w) => w.name === "seed");
            if (seedWidget) {
              seedWidget.type = "HIDDEN";
            }

            // Initial update
            updateModelInputs();
        }
    }
});
