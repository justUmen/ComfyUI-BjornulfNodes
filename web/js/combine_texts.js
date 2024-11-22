import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.CombineTexts",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_CombineTexts") {
            const updateInputs = () => {
                const initialWidth = node.size[0];
                const numInputsWidget = node.widgets.find(w => w.name === "number_of_inputs");
                if (!numInputsWidget) return;

                const numInputs = numInputsWidget.value;
                
                // Initialize node.inputs if it doesn't exist
                if (!node.inputs) {
                    node.inputs = [];
                }
                
                // Filter existing text inputs
                const existingInputs = node.inputs.filter(input => input.name.startsWith('text_'));
                
                // Determine if we need to add or remove inputs
                if (existingInputs.length < numInputs) {
                    // Add new text inputs if not enough existing
                    for (let i = existingInputs.length + 1; i <= numInputs; i++) {
                        const inputName = `text_${i}`;
                        if (!node.inputs.find(input => input.name === inputName)) {
                            node.addInput(inputName, "STRING");
                        }
                    }
                } else {
                    // Remove excess text inputs if too many
                    node.inputs = node.inputs.filter(input => !input.name.startsWith('text_') || parseInt(input.name.split('_')[1]) <= numInputs);
                }
                
                node.setSize(node.computeSize());
                node.size[0] = initialWidth; // Keep width fixed
            };

            // Move number_of_inputs to the top initially
            const numInputsWidget = node.widgets.find(w => w.name === "number_of_inputs");
            if (numInputsWidget) {
                node.widgets = [numInputsWidget, ...node.widgets.filter(w => w !== numInputsWidget)];
                numInputsWidget.callback = () => {
                    updateInputs();
                    app.graph.setDirtyCanvas(true);
                };
            }

            // Delay the initial update to ensure node is fully initialized
            setTimeout(updateInputs, 0);
        }
    }
});
