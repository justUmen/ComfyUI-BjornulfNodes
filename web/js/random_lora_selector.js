import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.RandomLoraSelector",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_RandomLoraSelector") {
            const updateLoraInputs = () => {
                const numLorasWidget = node.widgets.find(w => w.name === "number_of_loras");
                if (!numLorasWidget) return;

                const numLoras = numLorasWidget.value;
                const loraList = node.widgets.find(w => w.name === "lora_1").options.values;
                
                // Remove excess lora widgets
                node.widgets = node.widgets.filter(w => !w.name.startsWith("lora_") || parseInt(w.name.split("_")[1]) <= numLoras);
                
                // Add new lora widgets if needed
                for (let i = 1; i <= numLoras; i++) {
                    const widgetName = `lora_${i}`;
                    if (!node.widgets.find(w => w.name === widgetName)) {
                        const defaultIndex = Math.min(i - 1, loraList.length - 1);
                        node.addWidget("combo", widgetName, loraList[defaultIndex], () => {}, { 
                            values: loraList
                        });
                    }
                }
                
                // Reorder widgets
                node.widgets.sort((a, b) => {
                    if (a.name === "number_of_loras") return -1;
                    if (b.name === "number_of_loras") return 1;
                    if (a.name === "seed") return 1;
                    if (b.name === "seed") return -1;
                    if (a.name.startsWith("lora_") && b.name.startsWith("lora_")) {
                        return parseInt(a.name.split("_")[1]) - parseInt(b.name.split("_")[1]);
                    }
                    return a.name.localeCompare(b.name);
                });
                
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
                
                // Restore lora widgets based on saved properties
                const savedProperties = info.properties;
                if (savedProperties) {
                    Object.keys(savedProperties).forEach(key => {
                        if (key.startsWith("lora_")) {
                            const widgetName = key;
                            const widgetValue = savedProperties[key];
                            const existingWidget = node.widgets.find(w => w.name === widgetName);
                            if (existingWidget) {
                                existingWidget.value = widgetValue;
                            } else {
                                node.addWidget("combo", widgetName, widgetValue, () => {}, { 
                                    values: node.widgets.find(w => w.name === "lora_1").options.values
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
                
                // Update lora inputs after restoring saved state
                updateLoraInputs();
            };

            // Initial update
            updateLoraInputs();
        }
    }
});