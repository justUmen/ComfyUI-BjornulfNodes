import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "Bjornulf.ConcatVideos",
    async nodeCreated(node) {
        if (node.comfyClass === "Bjornulf_ConcatVideos") {
            // Initialize properties if not already set
            node.properties = node.properties || {};

            // Default output filename
            const defaultOutputFilename = "concatenated.mp4";

            // Ensure `output_filename` is initialized in properties
            if (!node.properties.output_filename) {
                node.properties.output_filename = defaultOutputFilename;
            }

            // Store the original serialize/configure methods
            const originalSerialize = node.serialize;
            const originalConfigure = node.configure;

            // Override serialize to save `output_filename` and inputs
            node.serialize = function() {
                const data = originalSerialize ? originalSerialize.call(this) : {};
                data.video_inputs = this.inputs
                    .filter(input => input.name.startsWith("video_path_"))
                    .map(input => ({
                        name: input.name,
                        type: input.type,
                        link: input.link || null,
                    }));
                data.properties = { ...this.properties };
                return data;
            };

            // Override configure to restore `output_filename` and inputs
            node.configure = function(data) {
                if (originalConfigure) {
                    originalConfigure.call(this, data);
                }
                if (data.video_inputs) {
                    data.video_inputs.forEach(inputData => {
                        if (!this.inputs.find(input => input.name === inputData.name)) {
                            const newInput = this.addInput(inputData.name, inputData.type);
                            newInput.link = inputData.link || null;
                        }
                    });
                }
                node.properties = { ...node.properties, ...data.properties };

                // Ensure `output_filename` is always consistent
                if (!node.properties.output_filename) {
                    node.properties.output_filename = defaultOutputFilename;
                }
                return true;
            };

            const updateInputs = () => {
                const initialWidth = node.size[0];
                const numVideosWidget = node.widgets.find(w => w.name === "number_of_videos");
                if (!numVideosWidget) return;

                const numVideos = numVideosWidget.value;

                // Store existing connections before modifying inputs
                const existingConnections = {};
                node.inputs.forEach(input => {
                    if (input.link !== null) {
                        existingConnections[input.name] = input.link;
                    }
                });

                // Clear and update inputs
                node.inputs = node.inputs.filter(input => !input.name.startsWith("video_path_"));
                for (let i = 1; i <= numVideos; i++) {
                    const inputName = `video_path_${i}`;
                    const newInput = node.addInput(inputName, "STRING");
                    if (existingConnections[inputName] !== undefined) {
                        newInput.link = existingConnections[inputName];
                    }
                }

                // Synchronize `output_filename` with properties and widget
                const outputFilenameWidget = node.widgets.find(w => w.name === "output_filename");
                if (outputFilenameWidget) {
                    outputFilenameWidget.value = node.properties.output_filename;
                }

                // Adjust size and redraw
                node.setSize(node.computeSize());
                node.size[0] = Math.max(initialWidth, 200);
                app.graph.setDirtyCanvas(true);
            };

            // Set up widget callbacks
            const numVideosWidget = node.widgets.find(w => w.name === "number_of_videos");
            if (numVideosWidget) {
                numVideosWidget.callback = updateInputs;
            }

            // Ensure `output_filename` is properly initialized on node creation
            let outputFilenameWidget = node.widgets.find(w => w.name === "output_filename");
            if (!outputFilenameWidget) {
                outputFilenameWidget = node.addWidget("string", "output_filename", node.properties.output_filename, value => {
                    node.properties.output_filename = value || defaultOutputFilename;
                });
            } else {
                // Synchronize widget value with properties
                outputFilenameWidget.value = node.properties.output_filename || defaultOutputFilename;
            }

            // Initialize inputs on node creation
            requestAnimationFrame(updateInputs);
        }
    }
});
