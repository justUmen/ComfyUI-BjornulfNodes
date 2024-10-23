import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.LoopIntegerSequential",
    async nodeCreated(node) {
        if (node.comfyClass !== "Bjornulf_LoopIntegerSequential") return;

        // Hide seed widget
        const seedWidget = node.widgets.find(w => w.name === "seed");
        if (seedWidget) {
            seedWidget.visible = false;
        }

        // Add get value button
        // const getValueButton = node.addWidget("button", "Get Counter Value", null, () => {
        //     fetch('/get_counter_value')
        //     .then(response => response.json())
        //     .then(data => {
        //         if (data.success) {
        //             app.ui.toast(`Current counter value: ${data.value}`, {'duration': 5000});
        //         } else {
        //             app.ui.toast(`Failed to get counter value: ${data.error || "Unknown error"}`, {'type': 'error', 'duration': 5000});
        //         }
        //     })
        //     .catch((error) => {
        //         console.error('Error:', error);
        //         app.ui.toast("An error occurred while getting the counter value.", {'type': 'error', 'duration': 5000});
        //     });
        // });

        // Add reset button
        const resetButton = node.addWidget("button", "Reset Counter", null, () => {
            fetch('/reset_counter', {
                method: 'POST'
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    app.ui.toast("Counter reset successfully!", {'duration': 5000});
                } else {
                    app.ui.toast(`Failed to reset counter: ${data.error || "Unknown error"}`, {'type': 'error', 'duration': 5000});
                }
            })
            .catch((error) => {
                console.error('Error:', error);
                app.ui.toast("An error occurred while resetting the counter.", {'type': 'error', 'duration': 5000});
            });
        });

        // Override the original execute function
        const originalExecute = node.execute;
        node.execute = function() {
            const result = originalExecute.apply(this, arguments);
            if (result instanceof Promise) {
                return result.catch(error => {
                    if (error.message.includes("Counter has reached its limit")) {
                        app.ui.toast(`Execution blocked: ${error.message}`, {'type': 'error', 'duration': 5000});
                    }
                    throw error;  // Re-throw the error to stop further execution
                });
            }
            return result;
        };
    }
});