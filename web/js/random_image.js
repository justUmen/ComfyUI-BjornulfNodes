import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.RandomImage",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_RandomImage") {
            const updateInputs = () => {
                const numInputsWidget = node.widgets.find(w => w.name === "number_of_images");
                if (!numInputsWidget) return;

                const numInputs = numInputsWidget.value;

                // Initialize node.inputs if it doesn't exist
                if (!node.inputs) {
                    node.inputs = [];
                }

                // Filter existing image inputs
                const existingInputs = node.inputs.filter(input => input.name.startsWith('image_'));

                // Determine if we need to add or remove inputs
                if (existingInputs.length < numInputs) {
                    // Add new image inputs if not enough existing
                    for (let i = existingInputs.length + 1; i <= numInputs; i++) {
                        const inputName = `image_${i}`;
                        if (!node.inputs.find(input => input.name === inputName)) {
                            node.addInput(inputName, "IMAGE");
                        }
                    }
                } else {
                    // Remove excess image inputs if too many
                    node.inputs = node.inputs.filter(input => !input.name.startsWith('image_') || parseInt(input.name.split('_')[1]) <= numInputs);
                }

                node.setSize(node.computeSize());
            };

            // Set seed widget to hidden input
            const seedWidget = node.widgets.find(w => w.name === "seed");
            if (seedWidget) {
                seedWidget.type = "HIDDEN";
            }

            // Move number_of_images to the top initially
            const numInputsWidget = node.widgets.find(w => w.name === "number_of_images");
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
