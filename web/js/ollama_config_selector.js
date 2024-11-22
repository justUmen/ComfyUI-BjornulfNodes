import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.OllamaConfig",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_OllamaConfig") {
            // Add model_list combo widget
            const modelListWidget = node.addWidget(
                "combo",
                "select_model_here",
                "",
                (v) => {
                    // When model_list changes, update model_name
                    const modelNameWidget = node.widgets.find(w => w.name === "model_name");
                    if (modelNameWidget) {
                        modelNameWidget.value = v;
                    }
                },
                { values: [] }
            );

            // Add update button
            node.addCustomWidget({
                name: "Update model_list",
                type: "button",
                value: "Update Models",
                callback: async function() {
                    try {
                        const url = node.widgets.find(w => w.name === "ollama_url").value;
                        const response = await fetch(`${url}/api/tags`);
                        const data = await response.json();
                        
                        if (data.models) {
                            const modelNames = data.models.map(m => m.name);
                            if (modelNames.length > 0) {
                                // Update model_list widget
                                modelListWidget.options.values = modelNames;
                                modelListWidget.value = modelNames[0];
                                
                                // Update model_name widget
                                const modelNameWidget = node.widgets.find(w => w.name === "model_name");
                                if (modelNameWidget) {
                                    modelNameWidget.value = modelNames[0];
                                }
                            }
                        }
                    } catch (error) {
                        console.error('Error updating models:', error);
                    }
                }
            });
        }
    }
});