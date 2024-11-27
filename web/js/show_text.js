import { app } from "../../../scripts/app.js";
import { ComfyWidgets } from "../../../scripts/widgets.js";

// Styles for the text area
const textAreaStyles = {
    readOnly: true,
    opacity: 1,
    padding: '4px',
    paddingLeft: '7px',
    border: '1px solid #ccc',
    borderRadius: '5px',
    backgroundColor: '#222',
    color: 'Lime',
    fontFamily: 'Arial, sans-serif',
    fontSize: '14px',
    lineHeight: '1.4',
    resize: 'none',
    overflowY: 'auto',
};

// Displays input text on a node
app.registerExtension({
    name: "Bjornulf.ShowText",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "Bjornulf_ShowText") {
            function populate(text) {
                if (!Array.isArray(text)) {
                    console.warn("populate expects an array, got:", text);
                    return;
                }
            
                if (this.widgets) {
                    const pos = this.widgets.findIndex((w) => w.name === "text");
                    if (pos !== -1) {
                        for (let i = pos; i < this.widgets.length; i++) {
                            this.widgets[i].onRemove?.();
                        }
                        this.widgets.length = pos;
                    }
                } else {
                    this.widgets = [];
                }
            
                text.forEach((list) => {
                    const existingWidget = this.widgets.find(w => w.name === "text" && w.value === list);
                    if (!existingWidget) {
                        const w = ComfyWidgets["STRING"](this, "text", ["STRING", { multiline: true }], app).widget;
                        w.inputEl.readOnly = true;
                        Object.assign(w.inputEl.style, textAreaStyles);
            
                        // Determine color based on type
                        let color = 'Lime'; // Default color for strings
                        const value = list.toString().trim();
            
                        if (/^-?\d+$/.test(value)) {
                            color = '#0096FF'; // Integer
                        } else if (/^-?\d*\.?\d+$/.test(value)) {
                            color = 'orange'; // Float
                        } else if (value.startsWith("If-Else ERROR: ")) {
                            color = 'red'; // If-Else ERROR lines
                        } else if (value.startsWith("tensor(")) {
                            color = '#0096FF'; // Lines starting with "tensor("
                        }
            
                        w.inputEl.style.color = color;
                        w.value = list;
                    }
                });
            
                requestAnimationFrame(() => {
                    const sz = this.computeSize();
                    if (sz[0] < this.size[0]) sz[0] = this.size[0];
                    if (sz[1] < this.size[1]) sz[1] = this.size[1];
                    this.onResize?.(sz);
                    app.graph.setDirtyCanvas(true, false);
                });
            }
            

            // When the node is executed we will be sent the input text, display this in the widget
            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function (message) {
                onExecuted?.apply(this, arguments);
                populate.call(this, message.text);
            };

            const onConfigure = nodeType.prototype.onConfigure;
            nodeType.prototype.onConfigure = function () {
                onConfigure?.apply(this, arguments);
                if (this.widgets_values?.length) {
                    populate.call(this, this.widgets_values);
                }
            };
        }
    },
});