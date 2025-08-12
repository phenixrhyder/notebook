# app.py

import gradio as gr

# --- 1. DEFINE YOUR CORE FUNCTION ---
# This is where your main logic will go.
# Replace this example function with your own function that processes assets.
# For example, it might take a file path as input and return a modified file path.
def process_asset(input_text):
  """
  This is a placeholder function.
  You will replace this with your Blender script logic.
  """
  # For now, it just adds "processed:" to the input text.
  output_text = f"Processed: {input_text}"
  print(f"Input: {input_text}, Output: {output_text}") # for debugging in the logs
  return output_text


# --- 2. CREATE THE GRADIO INTERFACE ---
# This creates the web UI that users will interact with.
# You can have inputs like file uploads, sliders, text boxes, etc.
# You can have outputs like images, 3D models, text, or files.
with gr.Blocks() as demo:
  gr.Markdown("# My Asset Warp Tool") # Title for your app
  gr.Markdown("Upload your asset or enter text to process it with my Blender tool.") # Description

  # Define the input component (e.g., a textbox)
  input_component = gr.Textbox(label="Asset Name")

  # Define the output component
  output_component = gr.Textbox(label="Processing Result")

  # Define the button that will trigger the function
  process_button = gr.Button("Process Asset")

  # Link the button to your function
  # When the button is clicked, it will run the `process_asset` function,
  # taking the value from `input_component` and putting the result in `output_component`.
  process_button.click(
      fn=process_asset,
      inputs=input_component,
      outputs=output_component
  )


# --- 3. LAUNCH THE APP ---
# This command starts the web server.
if __name__ == "__main__":
  demo.launch()
