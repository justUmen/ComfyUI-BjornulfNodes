import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.LoopLinesSequential",
    async nodeCreated(node) {
        if (node.comfyClass !== "Bjornulf_LoopLinesSequential") return;

        // Hide seed widget
        const seedWidget = node.widgets.find(w => w.name === "seed");
        if (seedWidget) {
            seedWidget.visible = false;
        }

        // Add line number display
        const lineNumberWidget = node.addWidget("html", "Current Line: --", null, {
            callback: () => {}, 
        });

        // Function to update line number display
        const updateLineNumber = () => {
            fetch('/get_current_line')
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    lineNumberWidget.value = `Current Line: ${data.value}`;
                }
            })
            .catch(error => {
                console.error('Error getting line number:', error);
            });
        };

        // Add increment button
        const incrementButton = node.addWidget("button", "+1", null, () => {
            fetch('/increment_lines_counter', {
                method: 'POST'
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    updateLineNumber();
                    app.ui.toast("Counter incremented", {'duration': 3000});
                } else {
                    app.ui.toast(`Failed to increment counter: ${data.error || "Unknown error"}`, {'type': 'error', 'duration': 5000});
                }
            })
            .catch((error) => {
                console.error('Error:', error);
                app.ui.toast("An error occurred while incrementing the counter.", {'type': 'error', 'duration': 5000});
            });
        });

        // Add decrement button
        const decrementButton = node.addWidget("button", "-1", null, () => {
            fetch('/decrement_lines_counter', {
                method: 'POST'
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    updateLineNumber();
                    app.ui.toast("Counter decremented", {'duration': 3000});
                } else {
                    app.ui.toast(`Failed to decrement counter: ${data.error || "Unknown error"}`, {'type': 'error', 'duration': 5000});
                }
            })
            .catch((error) => {
                console.error('Error:', error);
                app.ui.toast("An error occurred while decrementing the counter.", {'type': 'error', 'duration': 5000});
            });
        });

        // Add reset button
        const resetButton = node.addWidget("button", "Reset Counter", null, () => {
            fetch('/reset_lines_counter', {
                method: 'POST'
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    updateLineNumber();
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

        // Update line number periodically
        setInterval(updateLineNumber, 1000);

        // Override the original execute function
        const originalExecute = node.execute;
        node.execute = function() {
            const result = originalExecute.apply(this, arguments);
            if (result instanceof Promise) {
                return result.catch(error => {
                    if (error.message.includes("Counter has reached its limit")) {
                        app.ui.toast(`Execution blocked: ${error.message}`, {'type': 'error', 'duration': 5000});
                    }
                    throw error;
                });
            }
            return result;
        };
    }
});