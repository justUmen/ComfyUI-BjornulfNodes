# 🔗 Comfyui : Bjornulf_custom_nodes v0.48 🔗

A list of 55 custom nodes for Comfyui : Display, manipulate, and edit text, images, videos, and more.  
You can manage looping operations, generate randomized content, trigger logical conditions, pause and manually control your workflows and even work with external AI tools, like Ollama or Text To Speech.  

# Coffee : ☕☕☕☕☕ 5/5

❤️❤️❤️ <https://ko-fi.com/bjornulf> ❤️❤️❤️

# ☘ This project is part of my AI trio. ☘

1 - 📝 Text/Chat AI generation : [Bjornulf Lobe Chat Fork](https://github.com/justUmen/Bjornulf_lobe-chat)  
2 - 🔊 Speech AI generation : [Bjornulf Text To Speech](https://github.com/justUmen/Bjornulf_XTTS)  
<u>**3 - 🎨 Image AI generation :** [Bjornulf Comfyui custom nodes](https://github.com/justUmen/ComfyUI-BjornulfNodes) (you are here)</u>  

# 📋 Nodes menu by category

## 👁 Display and Show 👁
`1.` [👁 Show (Text, Int, Float)](#1----show-text-int-float)  
`49.` [📹👁 Video Preview](#49----video-preview)  

## ✒ Text ✒
`2.` [✒ Write Text](#2----write-text)  
`3.` [✒🗔 Advanced Write Text (+ 🎲 random selection and 🅰️ variables)](#3----advanced-write-text---random-selection-and-🅰%EF%B8%8F-variables)  
`4.` [🔗 Combine Texts](#4----combine-texts)  
`15.` [💾 Save Text](#15----save-text)  
`26.` [🎲 Random line from input](#26----random-line-from-input)  
`28.` [🔢🎲 Text with random Seed](#28----text-with-random-seed)  
`32.` [🧑📝 Character Description Generator](#32----character-description-generator)  
`48.` [🔀🎲 Text scrambler (🧑 Character)](#48----text-scrambler--character)  

## ♻ Loop ♻
`6.` [♻ Loop](#6----loop)  
`7.` [♻ Loop Texts](#7----loop-texts)  
`8.` [♻ Loop Integer](#8----loop-integer)  
`9.` [♻ Loop Float](#9----loop-float)  
`10.` [♻ Loop All Samplers](#10----loop-all-samplers)  
`11.` [♻ Loop All Schedulers](#11----loop-all-schedulers)  
`12.` [♻ Loop Combos](#12----loop-combos)  
`27.` [♻ Loop (All Lines from input)](#27----loop-all-lines-from-input)  
`33.` [♻ Loop (All Lines from input 🔗 combine by lines)](#33----loop-all-lines-from-input--combine-by-lines)  
`38.` [♻🖼 Loop (Images)](#38----loop-images)  
`39.` [♻ Loop (✒🗔 Advanced Write Text + 🅰️ variables)](#39----loop--advanced-write-text)  
`42.` [♻ Loop (Model+Clip+Vae) - aka Checkpoint / Model](#42----loop-modelclipvae---aka-checkpoint--model)  
`53.` [♻ Loop Load checkpoint (Model Selector)](#53----loop-load-checkpoint-model-selector)  
`54.` [♻ Loop Lora Selector](#54)  

## 🎲 Randomization 🎲
`3.` [✒🗔 Advanced Write Text (+ 🎲 random selection and 🅰️ variables)](#3----advanced-write-text---random-selection-and-🅰%EF%B8%8F-variables)  
`5.` [🎲 Random (Texts)](#5----random-texts)  
`26.` [🎲 Random line from input](#26----random-line-from-input)  
`28.` [🔢🎲 Text with random Seed](#28----text-with-random-seed)  
`37.` [🎲🖼 Random Image](#37----random-image)  
`40.` [🎲 Random (Model+Clip+Vae) - aka Checkpoint / Model](#40----random-modelclipvae---aka-checkpoint--model)  
`41.` [🎲 Random Load checkpoint (Model Selector)](#41----random-load-checkpoint-model-selector)  
`48.` [🔀🎲 Text scrambler (🧑 Character)](#48----text-scrambler--character)  
`55.` [🎲 Random Lora Selector](#55)  

## 🖼💾 Image Save 💾🖼
`16.` [💾🖼💬 Save image for Bjornulf LobeChat](#16----save-image-for-bjornulf-lobechat-for-my-custom-lobe-chat)  
`17.` [💾🖼 Save image as `tmp_api.png` Temporary API](#17----save-image-as-tmp_apipng-temporary-api-%EF%B8%8F)  
`18.` [💾🖼📁 Save image to a chosen folder name](#18----save-image-to-a-chosen-folder-name)  
`14.` [💾🖼 Save Exact name](#1314------resize-and-save-exact-name-%EF%B8%8F)  

## 🖼📥 Image Load 📥🖼
`29.` [📥🖼 Load Image with Transparency ▢](#29----load-image-with-transparency-)  
`43.` [📥🖼📂 Load Images from output folder](#43----load-images-from-output-folder)  

## 🖼 Image - others 🖼
`13.` [📏 Resize Image](#1314------resize-and-save-exact-name-%EF%B8%8F)  
`22.` [🔲 Remove image Transparency (alpha)](#22----remove-image-transparency-alpha)  
`23.` [🔲 Image to grayscale (black & white)](#23----image-to-grayscale-black--white)  
`24.` [🖼+🖼 Stack two images (Background + Overlay)](#24----stack-two-images-background--overlay)  
`25.` [🟩➜▢ Green Screen to Transparency](#25----green-screen-to-transparency)  
`29.` [⬇️🖼 Load Image with Transparency ▢](#29----load-image-with-transparency-)  
`30.` [🖼✂ Cut image with a mask](#30----cut-image-with-a-mask)  
`37.` [🎲🖼 Random Image](#37----random-image)  
`38.` [♻🖼 Loop (Images)](#38----loop-images)  
`43.` [⬇️📂🖼 Load Images from output folder](#43----load-images-from-output-folder)  
`44.` [🖼👈 Select an Image, Pick](#44----select-an-image-pick)  
`46.` [🖼🔍 Image Details](#46----image-details)  
`47.` [🖼 Combine Images](#47----combine-images)  

## 🚀 Load checkpoints 🚀
`40.` [🎲 Random (Model+Clip+Vae) - aka Checkpoint / Model](#40----random-modelclipvae---aka-checkpoint--model)  
`41.` [🎲 Random Load checkpoint (Model Selector)](#41----random-load-checkpoint-model-selector)  
`42.` [♻ Loop (Model+Clip+Vae) - aka Checkpoint / Model](#42----loop-modelclipvae---aka-checkpoint--model)  
`53.` [♻ Loop Load checkpoint (Model Selector)](#53----loop-load-checkpoint-model-selector)

## 🚀 Load loras 🚀

## 📹 Video 📹
`20.` [📹 Video Ping Pong](#20----video-ping-pong)  
`21.` [📹 Images to Video (FFmpeg)](#21----images-to-video)  
`49.` [📹👁 Video Preview](#49----video-preview)  
`50.` [🖼➜📹 Images to Video path (tmp video)](#50----images-to-video-path-tmp-video)  
`51.` [📹➜🖼 Video Path to Images](#51----video-path-to-images)  
`52.` [🔊📹 Audio Video Sync](#52----audio-video-sync)  

## 🤖 AI 🤖
`19.` [🦙 Ollama](#19----ollama)  
`31.` [🔊 TTS - Text to Speech](#31----tts---text-to-speech-100-local-any-voice-you-want-any-language)  

## 🔊 Audio 🔊
`31.` [🔊 TTS - Text to Speech](#31----tts---text-to-speech-100-local-any-voice-you-want-any-language)  
`52.` [🔊📹 Audio Video Sync](#52----audio-video-sync)  

## 💻 System 💻
`34.` [🧹 Free VRAM hack](#34----free-vram-hack)  

## 🧍 Manual user Control 🧍
`35.` [⏸️ Paused. Resume or Stop, Pick 👇](#35---%EF%B8%8F-paused-resume-or-stop-)  
`36.` [⏸️ Paused. Select input, Pick 👇](#36---%EF%B8%8F-paused-select-input-pick-one)  

## 🧠 Logic / Conditional Operations 🧠
`45.` [🔀 If-Else (input / compare_with)](#45----if-else-input--compare_with)  

# ☁ Usage in cloud : 

Comfyui is great for local usage, but I sometimes need more power than what I have...  
I have a computer with a 4070 super with 12GB and flux fp8 simple wokflow take about ~40 seconds. With a 4090 in the cloud I can run flux fp16 in ~12 seconds. (There are of course also some workflow that I can't even run locally.)  

My referal link for Runpod : <https://runpod.io?ref=tkowk7g5> (If you use that i will have a commission, at no extra cost for you.)  
If you want to use my nodes and comfyui in the cloud (and can install more stuff), I'm managing an optimized ready-to-use template on runpod : <https://runpod.io/console/deploy?template=r32dtr35u1&ref=tkowk7g5>  
Template name : `bjornulf-comfyui-allin-workspace`, can be operational in ~3 minutes. (Depending on your pod, setup and download of extra models or whatever not included.)  
You need to create and select a network volume before using that, size is up to you, i have 50Gb Storage because i use cloud only for Flux or lora training on a 4090. (~0.7$/hour)  
⚠️ When pod is ready, you need to open a terminal in browser (After clicking on `connect` from your pod) and use this to launch ComfyUI manually : `cd /workspace/ComfyUI && python main.py --listen 0.0.0.0 --port 3000` (Much better to control it with a terminal, check logs, etc...)  
After that you can just click on the `Connect to port 3000` button.  
As file manager, you can use the included `JupyterLab` on port 8888.  
If you have any issues with it, please let me know.  
It will manage everything in Runpod network storage (`/workspace/ComfyUI`), so you can stop and start the cloud GPU without losing anything, change GPU or whatever.  
Zone : I recommend `EU-RO-1`, but up to you.  
Top-up your Runpod account with minimum 10$ to start.  
⚠️ Warning, you will pay by the minute, so not recommended for testing or learning comfyui. Do that locally !!!  
Run cloud GPU only when you already have your workflow ready to run.  
Advice : take a cheap GPU for testing, downloading models or settings things up.  
To download checkpoint or anything else, you need to use the terminal.  
For downloading from Huggingface (get token here <https://huggingface.co/settings/tokens>).  
Here is example for everything you need for flux dev :  
```
huggingface-cli login --token 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
huggingface-cli download black-forest-labs/FLUX.1-dev flux1-dev.safetensors --local-dir /workspace/ComfyUI/models/unet
huggingface-cli download comfyanonymous/flux_text_encoders clip_l.safetensors --local-dir /workspace/ComfyUI/models/clip
huggingface-cli download comfyanonymous/flux_text_encoders t5xxl_fp16.safetensors --local-dir /workspace/ComfyUI/models/clip
huggingface-cli download black-forest-labs/FLUX.1-dev ae.safetensors --local-dir /workspace/ComfyUI/models/vae
```
To use Flux you can just drag and drop in your browser comfyui interface the .json from my github repo : `workflows/FLUX_dev_troll.json`, direct link : <https://github.com/justUmen/ComfyUI-BjornulfNodes/blob/main/workflows/FLUX_dev_troll.json>.  

For downloading from civitai (get token here <https://civitai.com/user/account>), just copy/paste the link of checkpoint you want to download and use something like that, with your token in URL :  
```
CIVITAI="8b275fada679ba5812b3da2bf35016f6"
wget --content-disposition -P /workspace/ComfyUI/models/checkpoints "https://civitai.com/api/download/models/272376?type=Model&format=SafeTensor&size=pruned&fp=fp16&token=$CIVITAI"
```
If you have any issues with this template from Runpod, please let me know, I'm here to help. 😊   

# 🏗 Dependencies (nothing to do for runpod ☁)

## 🪟🐍 Windows : Install dependencies on windows with embedded python (portable version)

First you need to find this python_embedded `python.exe`, then you can right click or shift + right click inside the folder in your file manager to open a terminal there.  

This is where I have it, with the command you need :  
`H:\ComfyUI_windows_portable\python_embeded> .\python.exe -m pip install pydub ollama`  

When you have to install something you can retake the same code and install the dependency you want :  
`.\python.exe -m pip install whateveryouwant`  

You can then run comfyui.  

## 🐧🐍 Linux : Install dependencies (without venv, not recommended)

- `pip install ollama` (you can also install ollama if you want :  https://ollama.com/download) - You don't need to really install it if you don't want to use my ollama node. (BUT you need to run `pip install ollama`)
- `pip install pydub` (for TTS node)

## 🐧🐍 Linux : Install dependencies with python virtual environment (venv)

If you want to use a python virtual environment only for comfyUI, which I recommended, you can do that for example (also pre-install pip) :  

```
sudo apt-get install python3-venv python3-pip
python3 -m venv /the/path/you/want/venv/bjornulf_comfyui
```

Once you have your environment in this new folder, you can activate it with and install dependencies inside :  

```
source /the/path/you/want/venv/bjornulf_comfyui/bin/activate
pip install ollama pydub
```

Then you can start comfyui with this environment (notice that you need to re-activate it each time you want to launch comfyui) :  

```
cd /where/you/installed/ComfyUI && python main.py
```

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
- **v0.10**: Add a new node : Loop (All Lines from input) - Iterate over all lines from an input text.
- **v0.11**: Add a new node : Text with random Seed - Generate a random seed, along with text.
- **v0.12**: Combine images : Add option to move vertically and horizontally. (from -50% to 150%)
- **v0.13**: Add a new node: Load image with transparency (alpha) - Load an image with transparency.
- **v0.14**: Add a new node: Cut image from a mask
- **v0.15**: Add two new nodes: TTS - Text to Speech and Character Description Generator
- **v0.16**: Big changes on Character Description Generator
- **v0.17**: New loop node, combine by lines.
- **v0.18**: New loop node, Free VRAM hack
- **v0.19**: Changes for save to folder node : ignore missing images filenames, will use the highest number found + 1.
- **v0.20**: Changes for lobechat save image : include the code of free VRAM hack + ignore missing images filenames
- **v0.21**: Add a new write text node that also display the text in the comfyui console (good for debugging)
- **v0.22**: Allow write text node to use random selection like this {hood|helmet} will randomly choose between hood or helmet.
- **v0.23**: Add a new node: Pause, resume or stop workflow.
- **v0.24**: Add a new node: Pause, select input, pick one.
- **v0.25**: Two new nodes: Loop Images and Random image.
- **v0.26**: New node : Loop write Text. Also increase nb of inputs allowed for most nodes. (+ update some breaking changes)
- **v0.27**: Two new nodes : Loop (Model+Clip+Vae) and Random (Model+Clip+Vae) - aka Checkpoint / Model
- **v0.28**: Fix random texts and add a lot of screenshots examples for several nodes.
- **v0.29**: Fix floating points issues with loop float node.
- **v0.30**: Update the basic Loop node with optional input.
- **v0.31**: ❗Sorry, Breaking changes for Write/Show text nodes, cleaner system : 1 simple write text and the other is 1 advanced with console and special syntax. Also Show can now manage INT, FLOAT, TEXT.
- **v0.32**: Quick rename to avoid breaking loop_text node.
- **v0.33**: Control random on paused nodes, fix pydub sound bug permissions on Windows.
- **v0.34**: Two new nodes : Load Images from output folder and Select an Image, Pick.
- **v0.35**: Great improvements of the TTS node 31. It will also save the audio file in the "ComfyUI/Bjornulf_TTS/" folder. - Not tested on windows yet -
- **v0.36**: Fix random model.
- **v0.37**: New node : Random Load checkpoint (Model Selector). Alternative to the random checkpoint node. (Not preloading all checkpoints in memory, slower to switch between checkpoints, but more outputs to decide where to store your results.)
- **v0.38**: New node : If-Else logic. (input == compare_with), examples with different latent space size. +fix some deserialization issues.
- **v0.39**: Add variables management to Advanced Write Text node.
- **v0.40**: Add variables management to Loop Advanced Write Text node. Add menu for all nodes to the README.
- **v0.41**: Two new nodes : image details and combine images. Also ❗ Big changes to the If-Else node. (+many minor changes)
- **v0.42**: Better README with category nodes, changes some node titles
- **v0.43**: Add control_after_generate to Ollama and allow to keep in VRAM for 1 minute if needed. (For chaining quick generations.) Add fallback to 0.0.0.0
- **v0.44**: Allow ollama to have a cusom url in the file `ollama_ip.txt` in the comfyui custom nodes folder. Minor changes, add details/updates to README.
- **v0.45**: Add a new node : Text scrambler (Character), change text randomly using the file `scrambler/scrambler_character.json` in the comfyui custom nodes folder.
- **v0.46**: ❗ A lot of changes to Video nodes. Save to video is now using FLOAT for fps, not INT. (A lot of other custom nodes do that as well...) Add node to preview video, add node to convert a video path to a list of images. add node to convert a list of images to a temporary video + video_path. add node to synchronize duration of audio with video. (useful for MuseTalk) change TTS node with many new outputs ("audio_path", "full_path", "duration") to reuse with other nodes like MuseTalk, also TTS rename input to "connect_to_workflow", to avoid mistakes sending text to it.
- **v0.47**: New node : Loop Load checkpoint (Model Selector).
- **v0.48**: Two new nodes for loras : Random Lora Selector and Loop Lora Selector.

# 📝 Nodes descriptions

## 1 - 👁 Show (Text, Int, Float)

![Show Text](screenshots/show.png)

**Description:**  
The show node will only display text, or a list of several texts. (read only node)  
3 types are managed : Green is for STRING type, Orange is for FLOAT type and blue is for INT type. I put colors so I/you don't try to edit them. 🤣  

## 2 - ✒ Write Text

![write Text](screenshots/write.png)

**Description:**  
Simple node to write text.  

## 3 - ✒🗔 Advanced Write Text (+ 🎲 random selection and 🅰️ variables)

![write Text Advanced](screenshots/write_advanced.png)

**Description:**  
Advanced Write Text node allows for special syntax to accept random variants, like `{hood|helmet}` will randomly choose between hood or helmet.  
You also have `seed` and `control_after_generate` to manage the randomness.  
It is also displaying the text in the comfyui console. (Useful for debugging)  
Example of console logs :  
```
Raw text: photo of a {green|blue|red|orange|yellow} {cat|rat|house}
Picked text: photo of a green house
```

You can also create and reuse variables with this syntax : `<name>`.
Usage example : 

![variables](screenshots/variables.png)

## 4 - 🔗 Combine Texts
![Combine Texts](screenshots/combine_texts.png)

**Description:**  
Combine multiple text inputs into a single output. (can have separation with : comma, space, new line or nothing.)

## 5 - 🎲 Random (Texts)
![Random Text](screenshots/random_text.png)

**Description:**  
Generate and display random text from a predefined list. Great for creating random prompts.  
You also have `control_after_generate` to manage the randomness.  

## 6 - ♻ Loop
![Loop](screenshots/loop.png)

**Description:**  
General-purpose loop node, you can connect that in between anything.  
It has an optional input, if no input is given, it will loop over the value of the STRING "if_no_input" (take you can edit).  
❗ Careful this node accept everything as input and output, so you can use it with texts, integers, images, mask, segs etc... but be consistent with your inputs/outputs.  
Do not use this Loop if you can do otherwise.  

This is an example together with my node 28, to force a different seed for each iteration :   
![Loop](screenshots/loop4.png)

## 7 - ♻ Loop Texts
![Loop Texts](screenshots/loop_texts.png)

**Description:**  
Cycle through a list of text inputs.  

Here is an example of usage with combine texts and flux :  
![Loop Texts example](screenshots/loop_text_example.png)

## 8 - ♻ Loop Integer
![Loop Integer](screenshots/loop_integer.png)
![Loop Int + Show Text](screenshots/loop_int+show_text.png)

**Description:**  
Iterate through a range of integer values, good for `steps` in ksampler, etc...

❗ Don't forget that you can convert ksampler widgets to input by right-clicking the ksampler node :  
![Widget to Input](screenshots/widget-to-input.png)

Here is an example of usage with ksampler (Notice that with "steps" this node isn't optimized, but good enough for quick testing.) :  
![Widget to Input](screenshots/example_loop_integer.png)

## 9 - ♻ Loop Float
![Loop Float + Show Text](screenshots/loop_float+show_text.png)
![Loop Float](screenshots/loop_float.png)

**Description:**  
Loop through a range of floating-point numbers, good for `cfg`, `denoise`, etc...  

Here is an example with controlnet, trying to make a red cat based on a blue rabbit :  
![Loop All Samplers](screenshots/loop_float_example.png)

## 10 - ♻ Loop All Samplers
![Loop All Samplers](screenshots/loop_all_samplers.png)

**Description:**  
Iterate over all available samplers to apply them sequentially. Ideal for testing.  

Here is an example of looping over all the samplers with the normal scheduler :  
![Loop All Samplers](screenshots/example_loop_all_samplers.png)

## 11 - ♻ Loop All Schedulers
![Loop All Schedulers](screenshots/loop_all_schedulers.png)

**Description:**  
Iterate over all available schedulers to apply them sequentially. Ideal for testing. (same idea as sampler above, but for schedulers)  

## 12 - ♻ Loop Combos
![Loop Combos](screenshots/loop_combos.png)

**Description:**  
Generate a loop from a list of my own custom combinations (scheduler+sampler), or select one combo manually.  
Good for testing.

Example of usage to see the differences between different combinations :    
![example combos](screenshots/example_combos.png)

## 13/14 - 📏 + 🖼 Resize and Save Exact name ⚠️💣
![Resize and Save Exact](screenshots/resize_save_exact.png)

**Description:**  
Resize an image to exact dimensions. The other node will save the image to the exact path.  
⚠️💣 Warning : The image will be overwritten if it already exists.

## 15 - 💾 Save Text
![Save Text](screenshots/save_text.png)

**Description:**  
Save the given text input to a file. Useful for logging and storing text data.

## 16 - 💾🖼💬 Save image for Bjornulf LobeChat (❗For my custom [lobe-chat](https://github.com/justUmen/Bjornulf_lobe-chat)❗)
![Save Bjornulf Lobechat](screenshots/save_bjornulf_lobechat.png)

**Description:**  
❓ I made that node for my custom lobe-chat to send+receive images from Comfyui API : [lobe-chat](https://github.com/justUmen/Bjornulf_lobe-chat)  
It will save the image in the folder `output/BJORNULF_LOBECHAT/`. 
The name will start at `api_00001.png`, then `api_00002.png`, etc...  
It will also create a link to the last generated image at the location `output/BJORNULF_API_LAST_IMAGE.png`.  
This link will be used by my custom lobe-chat to copy the image inside the lobe-chat project.  

## 17 - 💾🖼 Save image as `tmp_api.png` Temporary API ⚠️💣
![Save Temporary API](screenshots/save_tmp_api.png)

**Description:**  
Save image for short-term use : ./output/tmp_api.png ⚠️💣  

## 18 - 💾🖼📁 Save image to a chosen folder name
![Save Temporary API](screenshots/save_image_to_folder.png)

**Description:**  
Save image in a specific folder : `my_folder/00001.png`, `my_folder/00002.png`, etc...  
Also allow multiple nested folders, like for example : `animal/dog/small`.

## 19 - 🦙 Ollama
![Ollama](screenshots/ollama_1.png)

**Description:**  
Will generate detailed text based of what you give it.  
I recommend using `mistral-nemo` if you can run it, but it's up to you. (Might have to tweak the system prompt a bit)  

You also have `control_after_generate` to force the node to rerun for every workflow run. (Even if there is no modification of the node or its inputs.)  

You have the option to keep in in you VRAM for a minute with `keep_1min_in_vram`. (If you plan having to generate many times with the same prompt)  
Each run will be significantly faster, but not free your VRAM for something else.  

![Ollama](screenshots/ollama_2.png) 

⚠️ Warning : Using `keep_1min_in_vram` might be a bit heavy on your VRAM. Think about if you really need it or not. Most of the time, when using `keep_1min_in_vram`, you don't want to have also a generation of image or anything else in the same time.  

⚠️ You can create a file called `ollama_ip.txt` in my comfyui custom node folder if you have a special IP for your ollama server, mine is : `http://192.168.1.37:11434`  

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

## 24 - 🖼+🖼 Stack two images (Background + Overlay)
![Superpose Images](screenshots/combine_background_overlay.png)

**Description:**  
Stack two images into a single image : a background and one (or several) transparent overlay. (allow to have a video there, just send all the frames and recombine them after.)  
Update 0.11 : Add option to move vertically and horizontally. (from -50% to 150%)  
❗ Warning : For now, `background` is a static image. (I will allow video there later too.)  
⚠️ Warning : If you want to directly load the image with transparency, use my node `🖼 Load Image with Transparency ▢` instead of the `Load Image` node.  

## 25 - 🟩➜▢ Green Screen to Transparency
![Greenscreen to Transparency](screenshots/greeenscreen_to_transparency.png)

**Description:**  
Transform greenscreen into transparency.  
Need clean greenscreen ofc. (Can adjust threshold but very basic node.)

## 26 - 🎲 Random line from input
![Random line from input](screenshots/random_line_from_input.png)

**Description:**  
Take a random line from an input text. (When using multiple "Write Text" nodes is annoying for example, you can use that and just copy/paste a list from outside.)  
You can change fixed/randomize for `control_after_generate` to have a different text each time you run the workflow. (or not)  

## 27 - ♻ Loop (All Lines from input)
![Loop input](screenshots/loop_all_lines.png)

**Description:**  
Iterate over all lines from an input text. (Good for testing multiple lines of text.)

## 28 - 🔢 Text with random Seed

**Description:**  

❗ This node is used to force to generate a random seed, along with text.  
But what does that mean ???  
When you use a loop (♻), the loop will use the same seed for each iteration. (That is the point, it will keep the same seed to compare results.)  
Even with `randomize` for `control_after_generate`, it is still using the same seed for every loop, it will change it only when the workflow is done.  
Simple example without using random seed node : (Both images have different prompt, but same seed)  

![Text with random Seed 1](screenshots/random_seed_1.png)

So if you want to force using another seed for each iteration, you can use this node in the middle.
For example, if you want to generate a different image every time. (aka : You use loop nodes not to compare or test results but to generate multiple images.)  
Use it like that for example : (Both images have different prompt AND different seed)  

![Text with random Seed 2](screenshots/random_seed_2.png)

Here is an example of the similarities that you want to avoid with FLUX with different prompt (hood/helmet) but same seed :

![Text with random Seed 3](screenshots/random_seed_3_flux.png)

Here is an example of the similarities that you want to avoid with SDXL with different prompt (blue/red) but same seed :

![Text with random Seed 4](screenshots/random_seed_4_sdxl.png)

FLUX : Here is an example of 4 images without Random Seed node on the left, and on the right 4 images with Random Seed node :

![Text with random Seed 5](screenshots/result_random_seed.png)

## 29 - 🖼 Load Image with Transparency ▢
![Load image Alpha](screenshots/load_image_alpha.png)

**Description:**  
Load an image with transparency.  
The default `Load Image` node will not load the transparency.  

## 30 - 🖼✂ Cut image with a mask
![Cut image](screenshots/image_mask_cut.png)

**Description:**  
Cut an image from a mask.  

## 31 - 🔊 TTS - Text to Speech (100% local, any voice you want, any language)
![TTS](screenshots/tts.png)

**Description:**  
[Listen to the audio example](https://github.com/user-attachments/assets/5a4a67ff-cf70-4092-8f3b-1ccc8023d8c6)

❗ Node never tested on windows, only on linux for now. ❗  

Use my TTS server to generate speech from text, based on XTTS v2.  
❗ Of course to use this comfyui node (frontend) you need to use my TTS server (backend) : <https://github.com/justUmen/Bjornulf_XTTS>  
I made this backend for <https://github.com/justUmen/Bjornulf_lobe-chat>, but you can use it with comfyui too with this node.  
After having `Bjornulf_XTTS` installed, you NEED to create a link in my Comfyui custom node folder called `speakers` : `ComfyUI/custom_nodes/Bjornulf_custom_nodes/speakers`  
That link must be a link to the folder where you installed/stored the voice samples you use for my TTS, like `default.wav`.  
If my TTS server is running on port 8020 (You can test in browser with the link <http://localhost:8020/tts_stream?language=en&speaker_wav=default&text=Hello>) and voice samples are good, you can use this node to generate speech from text.  

**Details**  
This node should always be connected to a core node : `Preview audio`.  

My node will generate and save the audio files in the `ComfyUI/Bjornulf_TTS/` folder, followed by the language selected, the name of the voice sample, and the text.  
Example of audio file from the screenshot above : `ComfyUI/Bjornulf_TTS/Chinese/default.wav/你吃了吗.wav`  
You can notice that you don't NEED to select a chinese voice to speak chinese. Yes it will work, you can record yourself and make yourself speak whatever language you want.  
Also, when you select a voice with this format `fr/fake_Bjornulf.wav`, it will create an extra folder `fr` of course. : `ComfyUI/Bjornulf_TTS/English/fr/fake_Bjornulf.wav/hello_im_me.wav`. Easy to see that you are using a french voice sample for an english recording.  

`control_after_generate` as usual, it is used to force the node to rerun for every workflow run. (Even if there is no modification of the node or its inputs.)  
`overwrite` is used to overwrite the audio file if it already exists. (For example if you don't like the generation, just set overwrite to True and run the workflow again, until you have a good result. After you can set it to back to False. (Paraphrasing : without overwrite set to True, It won't generate the audio file again if it already exists in the `Bjornulf_TTS` folder.)  
`autoplay` is used to play the audio file inside the node when it is executed. (Manual replay or save is done in the `preview audio` node.)  

So... note that if you know you have an audio file ready to play, you can still use my node but you do NOT need my TTS server to be running.
My node will just play the audio file if it can find it, won't try to connect th backend TTS server.  
Let's say you already use this node to create an audio file saying `workflow is done` with the Attenborough voice  :  

![TTS](screenshots/tts_end.png)  

As long as you keep exactly the same settings, it will not use my server to play the audio file! You can safely turn the TTS server off, so it won't use your precious VRAM Duh. (TTS server should be using ~3GB of VRAM.)  

Also `connect_to_workflow` is optional, it means that you can make a workflow with ONLY my TTS node to pre-generate the audio files with the sentences you want to use later, example :  
![TTS](screenshots/tts_preload.png)  

If you want to run my TTS nodes along side image generation, i recommend you to use my PAUSE node so you can manually stop the TTS server after my TTS node. When the VRAM is freed, you can the click on the RESUME button to continue the workflow.  
If you can afford to run both at the same time, good for you, but Locally I can't run my TTS server and FLUX at the same time, so I use this trick. :  

![TTS](screenshots/tts_preload_2.png)  


### 32 - 🧑📝 Character Description Generator
![characters](screenshots/characters.png)
![characters](screenshots/characters2.png)

**Description:**  
Generate a character description based on a json file in the folder `characters` : `ComfyUI/custom_nodes/Bjornulf_custom_nodes/characters`  
Make your own json file with your own characters, and use this node to generate a description.  
❗ For now it's very basic node, a lot of things are going to be added and changed !!!  
Some details are unusable for some checkpoints, very much a work in progress, the json structure isn't set in stone either.  
Some characters are included.  

### 33 - ♻ Loop (All Lines from input 🔗 combine by lines)

![loop combined](screenshots/loop_combined.png)

**Description:**  
Sometimes you want to loop over several inputs but you also want to separate different lines of your output.  
So with this node, you can have the number of inputs and outputs you want. See example for usage.  

### 34 - 🧹 Free VRAM hack
![free vram](screenshots/free_vram_hack1.png)
![free vram](screenshots/free_vram_hack2.png)

**Description:**  
So this is my attempt at freeing up VRAM after usage, I will try to improve that.  
For me, on launch ComfyUI is using 180MB of VRAM, after my clean up VRAM node it can go back down to 376MB.  
I don't think there is a clean way to do that, so I'm using a hacky way.  
So, not perfect but better than being stuck at 6GB of VRAM used if I know I won't be using it again...  
Just connect this node with your workflow, it takes an image as input and return the same image without any changes.  
❗ Comfyui is using cache to run faster (like not reloading checkpoints), so only use this free VRAM node when you need it.  
❗ For this node to work properly, you need to enable the dev/api mode in ComfyUI. (You can do that in the settings)  

### 35 - ⏸️ Paused. Resume or Stop ?

![pause resume stop](screenshots/pause1.png)
![pause resume stop](screenshots/pause2.png)
![pause resume stop](screenshots/pause3.png)

**Description:**  
Automatically pause the workflow, and rings a bell when it does. (play the audio `bell.m4a` file provided)  
You can then manually resume or stop the workflow by clicking on the node's buttons.  
I do that let's say for example if I have a very long upscaling process, I can check if the input is good before continuing. Sometimes I might stop the workflow and restart it with another seed.  
You can connect any type of node to the pause node, above is an example with text, but you can send an IMAGE or whatever else, in the node `input = output`. (Of course you need to send the output to something that has the correct format...)  

### 36 - ⏸️🔍 Paused. Select input, Pick one

![pick input](screenshots/pick.png)

**Description:**  
Automatically pause the workflow, and rings a bell when it does. (play the audio `bell.m4a` file provided)  
You can then manually select the input you want to use, and resume the workflow with it.  
You can connect this node to anything you want, above is an example with IMAGE. But you can pick whatever you want, in the node `input = output`.  

### 37 - 🎲🖼 Random Image

![random image](screenshots/random_image.png)

**Description:**  
Just take a random image from a list of images.  

### 38 - ♻🖼 Loop (Images)

![loop images](screenshots/loop_images.png)

**Description:**  
Loop over a list of images.  
Usage example : You have a list of images, and you want to apply the same process to all of them.  
Above is an example of the loop images node sending them to an Ipadapter workflow. (Same seed of course.)  

### 39 - ♻ Loop (✒🗔 Advanced Write Text)

![loop write text](screenshots/loop_write_text.png)

**Description:**  
If you need a quick loop but you don't want something too complex with a loop node, you can use this combined write text + loop.  
It will take the same special syntax as the Advanced write text node `{blue|red}`, but it will loop over ALL the possibilities instead of taking one at random.  
0.40 : You can also use variables `<name>` in the loop.  

### 40 - 🎲 Random (Model+Clip+Vae) - aka Checkpoint / Model

![random checkpoint](screenshots/random_checkpoint.png)

**Description:**  
Just simply take a trio at random from a load checkpoint node.  
Notice that it is using the core Load checkpoint node. It means that all checkpoint will be preloaded in memory.  

Details :  
- It will take more VRAM, but it will be faster to switch between checkpoints.  
- It can't give you the currently loaded checkpoint name's.  

Check node number 41 before deciding which one to use.  

### 41 - 🎲 Random Load checkpoint (Model Selector)

![pick input](screenshots/random_load_checkpoint.png)

**Description:**  
This is another way to select a load checkpoint node randomly.  
It will not preload all the checkpoints in memory, so it will be slower to switch between checkpoints.  
But you can use more outputs to decide where to store your results. (`model_folder` is returning the last folder name of the checkpoint.)  
I always store my checkpoints in a folder with the type of the model like `SD1.5`, `SDXL`, etc... So it's a good way for me to recover that information quickly.  

Details :  
- Note that compared to node 40, you can't have separate configuration depending of the selected checkpoint. (For example `CLIP Set Last Layer` node set at -2 for a specific model, or a separate vae or clip.) Aka : All models are going to share the exact same workflow.  

Check node number 40 before deciding which one to use.  
Node 53 is the loop version of this node.  

### 42 - ♻ Loop (Model+Clip+Vae) - aka Checkpoint / Model

![pick input](screenshots/loop_checkpoint.png)

**Description:**  
Loop over all the trios from several checkpoint node.  

### 43 - 📥🖼📂 Load Images from output folder

![pick input](screenshots/load_images_folder.png)

**Description:**  
Quickly select all images from a folder inside the output folder. (Not recursively.)  
So... As you can see from the screenshot the images are split based on their resolution.  
It's also not possible to edit dynamically the number of outputs, so I just picked a number : 4.  
The node will separate the images based on their resolution, so with this node you can have 4 different resolutions per folder. (If you have more than that, maybe you should have another folder...)  
To avoid error or crash if you have less than 4 resolutions in a folder, the node will just output white tensors. (white square image.)  
So this node is a little hacky for now, but i can select my different characters in less than a second.  
If you want to know how i personnaly save my images for a specific character, here is part of my workflow (Notice that i personnaly use / for folders because I'm on linux) :  
![pick input](screenshots/character_save.png)  
In this example I put "character/" as a string and then combine with "nothing". But it's the same if you do "character" and then combine with "/". (I just like having a / at the end of my folder's name...)  

If you are satisfied with this logic, you can then select all these nodes, right click and `Convert to Group Node`, you can then have your own customized "save character node" :  
![pick input](screenshots/bjornulf_save_character_group.png)

Here is another example of the same thing but excluding the save folder node :  
![pick input](screenshots/bjornulf_save_character_group2.png)

⚠️ If you really want to regroup all the images in one flow, you can use my node 47 `Combine images` to put them all together.  

### 44 - 🖼👈 Select an Image, Pick

![pick input](screenshots/select_image.png)

**Description:**  
Select an image from a list of images.  
Useful in combination with my Load images from folder and preview image nodes.  

You can also of course make a group node, like this one, which is the same as the screenshot above :  
![pick input](screenshots/select_image_group.png)

### 45 - 🔀 If-Else (input / compare_with)

![if else](screenshots/if_0.png)


**Description:**  
If the `input` given is equal to the `compare_with` given in the widget, it will forward `send_if_true`, otherwise it will forward `send_if_false`. (If no `send_if_false` it will return `None`.)  
You can forward anything, below is an example of forwarding a different size of latent space depending if it's SDXL or not.  

![if else](screenshots/if_0_1.png)

Here is an example of the node with all outputs displayed with Show text nodes :  

![if else](screenshots/if_1.png)

`send_if_false` is optional, if not connected, it will be replaced by `None`.  

![if else](screenshots/if_2.png)

If-Else are chainables, just connect `output` to `send_if_false`.  
⚠️ Always simply test `input` with `compare_with`, and connect the desired value to `send_if_true`. ⚠️  
Here a simple example with 2 If-Else nodes (choose between 3 different resolutions).  
❗ Notice that the same write text node is connected to both If-Else nodes input :  

![if else](screenshots/if_3.png)

Let's take a similar example but let's use my Write loop text node to display all 3 types once :  

![if else](screenshots/if_4.png)

If you understood the previous examples, here is a complete example that will create 3 images, landscape, portrait and square :  

![if else](screenshots/if_5.png)

Workflow is hidden for simplicity, but is very basic, just connect latent to Ksampler, nothing special.)  
You can also connect the same advanced loop write text node with my save folder node to save the images (landscape/portrait/square) in separate folders, but you do you...  

### 46 - 🖼🔍 Image Details

**Description:**  
Display the details of an image. (width, height, has_transparency, orientation, type)  
`RGBA` is considered as having transparency, `RGB` is not.  
`orientation` can be `landscape`, `portrait` or `square`.  

![image details](screenshots/image_details_1.png)

### 47 - 🖼🔗 Combine Images

**Description:**  
Combine multiple images (A single image or a list of images.)  

There are two types of logic to "combine images". With "all_in_one" enabled, it will combine all the images into one tensor.  
Otherwise it will send the images one by one. (check examples below) :  

This is an example of the "all_in_one" option disabled :  

![combine images](screenshots/combine_images_1.png)

But for example, if you want to use my node `select an image, pick`, you need to enable `all_in_one` and the images must all have the same resolution.  

![combine images](screenshots/combine_images_2.png)

You can notice that there is no visible difference when you use `all_in_one` with `preview image` node. (this is why I added the `show text` node, note that show text will make it blue, because it's an image/tensor.)  

When you use `combine image` node, you can actually also send many images at once, it will combine them all.  
Here is an example with `Load images from folder` node, `Image details` node and `Combine images` node. (Of course it can't have `all_in_one` set to True in this situation because the images have different resolutions) :  

![combine images](screenshots/combine_images_3.png)

Here another simple example taking a few selected images from a folder and combining them (For later processing for example) :  

![combine images](screenshots/combine_images_4.png)

### 48 - 🔀🎲 Text scrambler (🧑 Character)

![scrambler character](screenshots/scrambler_character.png)

**Description:**  
Take text as input and scramble (randomize) the text by using the file `scrambler/character_scrambler.json` in the comfyui custom nodes folder.  

### 49 - 📹👁 Video Preview

![video preview](screenshots/video_preview.png)

**Description:**  
This node takes a video path as input and displays the video.  

### 50 - 🖼➜📹 Images to Video path (tmp video)

![image to video path](screenshots/image_to_video_path.png)

**Description:**  
This node will take a list of images and convert them to a temporary video file.  

### 51 - 📹➜🖼 Video Path to Images

![video path to image](screenshots/video_path_to_image.png)

**Description:**  
This node will take a video path as input and convert it to a list of images.  
In the above example, I also take half of the frames by setting `frame_interval` to 2.  
Note that i had 16 frames, on the top right preview you can see 8 images.  

### 52 - 🔊📹 Audio Video Sync

**Description:**  

This node will basically synchronize the duration of an audio file with a video file by adding silence to the audio file if it's too short, or demultiply the video file if too long. (Video ideally need to be a loop, check my ping pong video node.)  
It is good like for example with MuseTalk <https://github.com/chaojie/ComfyUI-MuseTalk>, If you want to chain up videos (Let's say sentence by sentence) it will always go back to the last frame. (Making the video transition smoother.)  

Here is an example without `Audio Video Sync` node (The duration of the video is shorter than the audio, so after playing it will not go back to the last frame, ideally i want to have a loop where the first frame is the same as the last frame. -See my node loop video ping pong if needed-) :

![audio sync video](screenshots/audio_sync_video_without.png)

Here is an example with `Audio Video Sync` node, notice that it is also convenient to recover the frames per second of the video, and send that to other nodes. :

![audio sync video](screenshots/audio_sync_video_with.png)

### 53 - ♻ Loop Load checkpoint (Model Selector)

![loop model selector](screenshots/loop_model_selector.png)

**Description:**  
This is the loop version of node 41. (check there for similar details)  
It will loop over all the selected checkpoints.  

❗ The big difference with 41 is that checkpoints are preloaded in memory. You can run them all faster all at once.  
It is a good way to test multiple checkpoints quickly.  

### 54 - ♻ Loop Lora Selector

![loop lora selector](screenshots/loop_lora_selector.png)

**Description:**  
Loop over all the selected Loras.  
Above is an example with Pony and several styles of Lora.  

Below is another example, here with flux, to test if your Lora training was undertrained, overtrained or just right :  

![loop lora selector](screenshots/loop_lora_selector_flux.png)

### 55 - 🎲 Random Lora Selector

![random lora selector](screenshots/random_lora_selector.png)

**Description:**  
Just take a single Lora at random from a list of Loras.  