import { app } from "../../../scripts/app.js";

app.registerExtension({
  name: "Bjornulf.PickInput",
  async nodeCreated(node) {
    if (node.comfyClass === "Bjornulf_PickInput") {

      const updateInputButtons = (numInputs) => {
        // Remove all existing widgets
        node.widgets.length = 1;

        // Re-add the number_of_inputs widget
        // const numInputsWidget = node.addWidget("number", "Number of Inputs", "number_of_inputs", (v) => {
        //   updateInputs();
        //   app.graph.setDirtyCanvas(true);
        //   return v;
        // }, { min: 1, max: 10, step: 1, precision: 0 });

        // Add new input buttons
        for (let i = 1; i < numInputs + 1; i++) {
          node.addWidget("button", `Input ${i}`, `input_button_${i}`, () => {
            fetch(`/bjornulf_select_input_${i}`, { method: "GET" })
              .then((response) => response.text())
              .then((data) => {
                console.log(`Input ${i} response:`, data);
                // You can update the UI here if needed
              })
              .catch((error) => console.error("Error:", error));
          });
        }

        // Re-add the Stop button
        node.addWidget("button", "Stop", "Stop", () => {
          fetch("/bjornulf_stop_pick", { method: "GET" })
            .then((response) => response.text())
            .then((data) => {
              console.log("Stop response:", data);
              // You can update the UI here if needed
            })
            .catch((error) => console.error("Error:", error));
        });

        node.setSize(node.computeSize());
      };

      const updateInputs = () => {
        const numInputsWidget = node.widgets.find(
          (w) => w.name === "number_of_inputs"
        );
        if (!numInputsWidget) return;

        const numInputs = numInputsWidget.value;

        // Initialize node.inputs if it doesn't exist
        if (!node.inputs) {
          node.inputs = [];
        }

        // Filter existing text inputs
        const existingInputs = node.inputs.filter((input) =>
          input.name.startsWith("input_")
        );

        // const Everything = Symbol('Everything');
        // Determine if we need to add or remove inputs
        if (existingInputs.length < numInputs) {
          // Add new inputs if not enough existing
          for (let i = existingInputs.length + 1; i <= numInputs; i++) {
            const inputName = `input_${i}`;
            if (!node.inputs.find((input) => input.name === inputName)) {
              node.addInput(inputName, "*");
            }
          }
        } else {
          // Remove excess inputs if too many
          node.inputs = node.inputs.filter(
            (input) =>
              !input.name.startsWith("input_") ||
              parseInt(input.name.split("_")[1]) <= numInputs
          );
        }

        // Update input buttons
        updateInputButtons(numInputs);

        node.setSize(node.computeSize());
      };

      // Set seed widget to hidden input
      const seedWidget = node.widgets.find((w) => w.name === "seed");
      if (seedWidget) {
        seedWidget.type = "HIDDEN";
      }

      // Move number_of_inputs to the top initially
      const numInputsWidget = node.widgets.find(
        (w) => w.name === "number_of_inputs"
      );
      if (numInputsWidget) {
        node.widgets = [
          numInputsWidget,
          ...node.widgets.filter((w) => w !== numInputsWidget),
        ];
        numInputsWidget.callback = () => {
          updateInputs();
          app.graph.setDirtyCanvas(true);
        };
      }

      // Delay the initial update to ensure node is fully initialized
      setTimeout(updateInputs, 0);
    }
  },
});