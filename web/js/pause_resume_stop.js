import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.PauseResume",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_PauseResume") {
            const resumeButton = node.addWidget("button", "Resume", "Resume", () => {
                fetch('/bjornulf_resume', { method: 'GET' })
                    .then(response => response.text())
                    .then(data => {
                        console.log('Resume response:', data);
                        // You can update the UI here if needed
                    })
                    .catch(error => console.error('Error:', error));
            });
            const stopButton = node.addWidget("button", "Stop", "Stop", () => {
                fetch('/bjornulf_stop', { method: 'GET' })
                    .then(response => response.text())
                    .then(data => {
                        console.log('Stop response:', data);
                        // You can update the UI here if needed
                    })
                    .catch(error => console.error('Error:', error));
            });

            // Set seed widget to hidden input
            const seedWidget = node.widgets.find((w) => w.name === "seed");
            if (seedWidget) {
              seedWidget.type = "HIDDEN";
            }
        }
    }
});