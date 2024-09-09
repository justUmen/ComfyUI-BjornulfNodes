import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.CombineTextsByLines",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_CombineTextsByLines") {
            const updateInputsAndOutputs = () => {
                const numInputsWidget = node.widgets.find(w => w.name === "number_of_inputs");
                const numLinesWidget = node.widgets.find(w => w.name === "number_of_lines");
                if (!numInputsWidget || !numLinesWidget) return;

                const numInputs = numInputsWidget.value;
                const numLines = numLinesWidget.value;
                
                // Update inputs
                if (!node.inputs) {
                    node.inputs = [];
                }
                
                // Remove excess inputs
                node.inputs = node.inputs.filter(input => !input.name.startsWith('text_') || parseInt(input.name.split('_')[1]) <= numInputs);
                
                // Add new inputs if needed
                for (let i = node.inputs.length; i < numInputs; i++) {
                    const inputName = `text_${i + 1}`;
                    if (!node.inputs.find(input => input.name === inputName)) {
                        node.addInput(inputName, "STRING");
                    }
                }
                
                // Update outputs
                if (!node.outputs) {
                    node.outputs = [];
                }
                
                // Remove excess outputs
                while (node.outputs.length > numLines) {
                    node.removeOutput(node.outputs.length - 1);
                }
                
                // Add new outputs if needed
                while (node.outputs.length < numLines) {
                    node.addOutput(`Line ${node.outputs.length + 1}`, "STRING", { array: true });
                }

                // Update output labels and types
                node.outputs.forEach((output, index) => {
                    output.name = `line_${index + 1}`;
                    output.label = `Line ${index + 1}`;
                    output.type = "STRING";
                    output.array = true;
                });
                
                node.setSize(node.computeSize());
            };

            // Move control widgets to the top and remove any text area widgets
            node.widgets = node.widgets.filter(w => w.name === "number_of_inputs" || w.name === "number_of_lines");

            // Set up callbacks
            node.widgets.forEach(w => {
                w.callback = () => {
                    updateInputsAndOutputs();
                    app.graph.setDirtyCanvas(true);
                };
            });

            // Initial update
            setTimeout(updateInputsAndOutputs, 0);
        }
    }
});