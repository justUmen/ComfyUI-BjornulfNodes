import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.CivitAIModelSelector",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_CivitAIModelSelector") {
            // Find all upload widgets
            const uploadWidgets = node.widgets.filter(w => w.type === "file");
            
            uploadWidgets.forEach(widget => {
                // Store the original draw function
                const originalDraw = widget.draw;
                
                // Override the draw function
                widget.draw = function(ctx, node, width, pos, height) {
                    const result = originalDraw.call(this, ctx, node, width, pos, height);
                    
                    // Hide all file inputs for this widget
                    const fileInputs = document.querySelectorAll(`input[type="file"][data-widget="${this.name}"]`);
                    fileInputs.forEach(input => {
                        input.style.display = 'none';
                    });
                    
                    return result;
                };
            });
        }
    }
});