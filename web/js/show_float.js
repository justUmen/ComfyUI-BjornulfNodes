import { app } from "../../../scripts/app.js";
import { ComfyWidgets } from "../../../scripts/widgets.js";

// Styles for the text area
const textAreaStyles = {
    readOnly: true,
    opacity: 1,
    padding: '10px',
    border: '1px solid #ccc',
    borderRadius: '5px',
    backgroundColor: '#222',
    color: 'Lime',
    fontFamily: 'Arial, sans-serif',
    fontSize: '14px',
    lineHeight: '1.4',
    resize: 'vertical',
    overflowY: 'auto',
};

// Displays input text on a node
app.registerExtension({
    name: "Bjornulf.ShowFloat",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "Bjornulf_ShowFloat") {
            function createStyledTextArea(text) {
                const widget = ComfyWidgets["STRING"](this, "text", ["STRING", { multiline: true }], app).widget;
                widget.inputEl.readOnly = true;
                const textArea = widget.inputEl;

                Object.assign(textArea.style, textAreaStyles);
                textArea.classList.add('bjornulf-show-text');
                widget.value = text;
                return widget;
            }

            function populate(text) {
                if (this.widgets) {
                    for (let i = 1; i < this.widgets.length; i++) {
                        this.widgets[i].onRemove?.();
                    }
                    this.widgets.length = 1;
                }

                const v = Array.isArray(text) ? text : [text];
                for (const list of v) {
                    if (list) {
                        createStyledTextArea.call(this, list);
                    }
                }

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