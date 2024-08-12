import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.TextToStringAndSeed",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_TextToStringAndSeed") {
            // Set seed widget to hidden input
            const seedWidget = node.widgets.find(w => w.name === "seed");
            if (seedWidget) {
                seedWidget.type = "HIDDEN";
            }
            // Set seed widget to hidden input
            const controlWidget = node.widgets.find(w => w.name === "control_after_generate");
            if (controlWidget) {
                controlWidget.type = "HIDDEN";
            }
        }
    }
});
