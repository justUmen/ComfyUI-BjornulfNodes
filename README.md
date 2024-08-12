# 🔗 Comfyui : Bjornulf_custom_nodes v0.9 🔗

# Dependencies

- `pip install ollama` (you can also install ollama if you want :  https://ollama.com/download) - You don't need to really install it if you don't want to use my ollama node. (BUT you need to run `pip install ollama`)

# 📝 Changelog

- **v0.2**: Improve ollama node with system prompt + model selection.
- **v0.3**: Add a new node : Save image to a chosen folder.
- **v0.3**: Add comfyui Metadata / workflow to all my image-related nodes.
- **v0.4**: Support transparency option with webm format, options encoders. As well as input for audio stream. 
- **v0.5**: New node : Remove image transparency (alpha) - Fill alpha channel with solid color.
- **v0.5**: New node : Image to grayscale (black & white) - Convert an image to grayscale.
- **v0.6**: New node : Combine images (Background + Overlay) - Combine two images into a single image.
- **v0.7**: Replace Save API node with Save Bjornulf Lobechat node. (For my custom lobe-chat)
- **v0.8**: Combine images : add an option to put image top, bottom or center.
- **v0.8**: Combine texts : add option for slashes /
- **v0.8**: Add basic node to transform greenscreen in to transparency.
- **v0.9**: Add a new node : Return one random line from input.

# 📝 Nodes descriptions

## 1/2 - 👁 + ✒ Show/Write Text 
![Show Text](screenshots/write+show_text.png)

**Description:**  
Two simple nodes to write and show text.
Write node is a textarea where you can write your text.  
The show text node will only display the text. (That's why I made it a different color : green, uneditable, display only.)

## 3 - 🔗 Combine Texts
![Combine Texts](screenshots/combine_texts.png)

**Description:**  
Combine multiple text inputs into a single output. (can have separation with : comma, space, new line.)

## 4 - 🎲 Random Text
![Random Text](screenshots/random_text.png)

**Description:**  
Generate and display random text from a predefined list. Great for creating random prompts.

## 5 - ♻ Loop
![Loop](screenshots/loop.png)

**Description:**  
General-purpose loop node.

## 6 - ♻ Loop Texts
![Loop Texts](screenshots/loop_texts.png)

**Description:**  
Cycle through a list of text inputs. Great for creating dynamic text-based presentations.

## 7 - ♻ Loop Integer
![Loop Integer](screenshots/loop_integer.png)
![Loop Int + Show Text](screenshots/loop_int+show_text.png)

**Description:**  
Iterate through a range of integer values, good for `steps` in ksampler, etc...

❗ Don't forget that you can convert ksampler widgets to input by right-clicking the ksampler node :
![Widget to Input](screenshots/widget-to-input.png)

## 8 - ♻ Loop Float
![Loop Float](screenshots/loop_float.png)
![Loop Float + Show Text](screenshots/loop_float+show_text.png)

**Description:**  
Loop through a range of floating-point numbers, good for `cfg`, `denoise`, etc...

## 10 - ♻ Loop All Samplers
![Loop All Samplers](screenshots/loop_all_samplers.png)

**Description:**  
Iterate over all available samplers to apply them sequentially. Ideal for testing.

## 11 - ♻ Loop All Schedulers
![Loop All Schedulers](screenshots/loop_all_schedulers.png)

**Description:**  
Iterate over all available schedulers to apply them sequentially. Ideal for testing.

## 12 - ♻ Loop Combos
![Loop Combos](screenshots/loop_combos.png)

**Description:**  
Generate a loop from a list of my own custom combinations (scheduler+sampler), or select one combo manually.  
Good for testing.

## 13/14 - 📏 + 🖼 Resize and Save Exact name ⚠️💣
![Resize and Save Exact](screenshots/resize_save_exact.png)

**Description:**  
Resize an image to exact dimensions. The other node will save the image to the exact path.  
⚠️💣 Warning : The image will be overwritten if it already exists.

## 15 - 💾 Save Text
![Save Text](screenshots/save_text.png)

**Description:**  
Save the given text input to a file. Useful for logging and storing text data.

## 16 - 🖼💬 Save image for Bjornulf LobeChat (❗For my custom [lobe-chat](https://github.com/justUmen/Bjornulf_lobe-chat)❗)
![Save Bjornulf Lobechat](screenshots/save_bjornulf_lobechat.png)

**Description:**  
❓ I made that node for my custom lobe-chat to send+receive images from Comfyui API : [lobe-chat](https://github.com/justUmen/Bjornulf_lobe-chat)  
It will save the image in the folder `output/BJORNULF_LOBECHAT/`. 
The name will start at `api_00001.png`, then `api_00002.png`, etc...  
It will also create a link to the last generated image at the location `output/BJORNULF_API_LAST_IMAGE.png`.  
This link will be used by my custom lobe-chat to copy the image inside the lobe-chat project.  

## 17 - 🖼 Save image as `tmp_api.png` Temporary API ⚠️💣
![Save Temporary API](screenshots/save_tmp_api.png)

**Description:**  
Save image for short-term use : ./output/tmp_api.png ⚠️💣  

## 18 - 🖼📁 Save image to a chosen folder name
![Save Temporary API](screenshots/save_image_to_folder.png)

**Description:**  
Save image in a specific folder : `my_folder/00001.png`, `my_folder/00002.png`, etc...  
Also allow multiple nested folders, like for example : `animal/dog/small`.

## 19 - 🦙 Ollama
![Show Text](screenshots/ollama.png)

**Description:**  
Will generate detailed text based of what you give it.  
I recommend using `mistral-nemo` if you can run it, but it's up to you. (Might have to tweak the system prompt a bit)  
⚠️ Warning : Having an ollama node that will run for each generation might be a bit heavy on your VRAM. Think about if you really need it or not.

**Description:**  
Straight forward node to write and show text.

## 20 - 📹 Video Ping Pong
![Video Ping Pong](screenshots/video_pingpong.png)

**Description:**  
Create a ping-pong effect from a list of images (from a video) by reversing the playback direction when reaching the last frame. Good for an "infinity loop" effect.

## 21 - 📹 Images to Video
![Images to Video](screenshots/imgs2video.png)

**Description:**  
Combine a sequence of images into a video file.  
❓ I made this node because it supports transparency with webm format. (Needed for rembg)  
Temporary images are stored in the folder `ComfyUI/temp_images_imgs2video/` as well as the wav audio file.

## 22 - 🔲 Remove image Transparency (alpha)
![Remove Alpha](screenshots/remove_alpha.png)

**Description:**  
Remove transparency from an image by filling the alpha channel with a solid color. (black, white or greenscreen)  
Of course it takes in an image with transparency, like from rembg nodes.  
Necessary for some nodes that don't support transparency.  

## 23 - 🔲 Image to grayscale (black & white)
![Image to Grayscale](screenshots/grayscale.png)

**Description:**  
Convert an image to grayscale (black & white)  
Example : I sometimes use it with Ipadapter to disable color influence.  
But you can sometimes also want a black and white image... 

## 24 - 🖼+🖼 Combine images (Background + Overlay)
![Combine Images](screenshots/combine_background_overlay.png)

**Description:**  
Combine two images into a single image : a background and one (or several) transparent overlay. (allow for video frames.)  
Update 0.8 : Also have a option to put image top, bottom or center.
❗ Warning : For now, `background` is a static image. (I will allow video there later too.)  

## 25 - 🟩➜▢ Green Screen to Transparency
![Combine Images](screenshots/greeenscreen_to_transparency.png)

**Description:**  
Transform greenscreen into transparency.  
Need clean greenscreen ofc. (Can adjust threshold but very basic node.)

## 26 - 🎲 Random line from input
![Combine Images](screenshots/random_line_from_input.png)

**Description:**  
Take a random line from an input text. (When using multiple "Write Text" nodes is annoying for example, you can use that and just copy/paste a list from outside.)

