from .images_to_video import imagesToVideo
from .write_text import WriteText
from .write_text_console import WriteTextInConsole
from .write_image_environment import WriteImageEnvironment
from .write_image_characters import WriteImageCharacters
from .write_image_character import WriteImageCharacter
from .write_image_allinone import WriteImageAllInOne
from .combine_texts import CombineTexts
from .loop_texts import LoopTexts
from .random_texts import RandomTexts
from .random_model_clip_vae import RandomModelClipVae
from .video_pingpong import VideoPingPong
from .loop_float import LoopFloat
from .loop_integer import LoopInteger
from .loop_basic_batch import LoopBasicBatch
from .loop_samplers import LoopSamplers
from .loop_schedulers import LoopSchedulers
from .ollama import ollamaLoader
from .show_text import ShowText
from .show_int import ShowInt
from .show_float import ShowFloat
from .save_text import SaveText
from .save_tmp_image import SaveTmpImage
from .save_image_path import SaveImagePath
# from .save_api_image import SaveApiImage
from .save_img_to_folder import SaveImageToFolder
from .resize_image import ResizeImage
from .loop_my_combos_samplers_schedulers import LoopCombosSamplersSchedulers
from .remove_transparency import RemoveTransparency
from .image_to_grayscale import GrayscaleTransform
from .combine_background_overlay import CombineBackgroundOverlay
from .save_bjornulf_lobechat import SaveBjornulfLobeChat
from .green_to_transparency import GreenScreenToTransparency
from .random_line_from_input import RandomLineFromInput
from .loop_lines import LoopAllLines
from .random_seed_with_text import TextToStringAndSeed
from .load_image_alpha import LoadImageWithTransparency
from .image_mask_cutter import ImageMaskCutter
from .character_description import CharacterDescriptionGenerator
from .text_to_speech import TextToSpeech
from .loop_combine_texts_by_lines import CombineTextsByLines
from .free_vram_hack import FreeVRAM
# from .pause_resume import PauseResume
# from .check_black_image import CheckBlackImage
# from .clear_vram import ClearVRAM

# from .CUSTOM_STRING import CustomStringType

NODE_CLASS_MAPPINGS = {
    # "Bjornulf_CustomStringType": CustomStringType,
    "Bjornulf_ollamaLoader": ollamaLoader,
    # "Bjornulf_PauseResume": PauseResume,
    "Bjornulf_FreeVRAM": FreeVRAM,
    "Bjornulf_CombineTextsByLines": CombineTextsByLines,
    "Bjornulf_TextToSpeech": TextToSpeech,
    "Bjornulf_CharacterDescriptionGenerator": CharacterDescriptionGenerator,
    "Bjornulf_ImageMaskCutter": ImageMaskCutter,
    "Bjornulf_LoadImageWithTransparency": LoadImageWithTransparency,
    "Bjornulf_LoopAllLines": LoopAllLines,
    "Bjornulf_TextToStringAndSeed": TextToStringAndSeed,
    "Bjornulf_GreenScreenToTransparency": GreenScreenToTransparency,
    "Bjornulf_RandomLineFromInput": RandomLineFromInput,
    # "Bjornulf_CheckBlackImage": CheckBlackImage,
    # "Bjornulf_ClearVRAM": ClearVRAM,
    "Bjornulf_SaveBjornulfLobeChat": SaveBjornulfLobeChat,
    "Bjornulf_WriteText": WriteText,
    "Bjornulf_WriteTextInConsole": WriteTextInConsole,
    "Bjornulf_RemoveTransparency": RemoveTransparency,
    "Bjornulf_GrayscaleTransform": GrayscaleTransform,
    "Bjornulf_CombineBackgroundOverlay": CombineBackgroundOverlay,
    # "Bjornulf_WriteImageEnvironment": WriteImageEnvironment,
    # "Bjornulf_WriteImageCharacters": WriteImageCharacters,
    # "Bjornulf_WriteImageCharacter": WriteImageCharacter,
    # "Bjornulf_WriteImageAllInOne": WriteImageAllInOne,
    "Bjornulf_ShowText": ShowText,
    "Bjornulf_ShowInt": ShowInt,
    "Bjornulf_ShowFloat": ShowFloat,
    "Bjornulf_SaveText": SaveText,
    "Bjornulf_ResizeImage": ResizeImage,
    "Bjornulf_SaveImageToFolder": SaveImageToFolder,
    "Bjornulf_SaveTmpImage": SaveTmpImage,
    "Bjornulf_SaveImagePath": SaveImagePath,
    # "Bjornulf_SaveApiImage": SaveApiImage,
    "Bjornulf_CombineTexts": CombineTexts,
    "Bjornulf_LoopTexts": LoopTexts,
    "Bjornulf_RandomTexts": RandomTexts,
    "Bjornulf_RandomModelClipVae": RandomModelClipVae,
    "Bjornulf_imagesToVideo": imagesToVideo,
    "Bjornulf_VideoPingPong": VideoPingPong,
    "Bjornulf_LoopFloat": LoopFloat,
    "Bjornulf_LoopInteger": LoopInteger,
    "Bjornulf_LoopBasicBatch": LoopBasicBatch,
    "Bjornulf_LoopSamplers": LoopSamplers,
    "Bjornulf_LoopSchedulers": LoopSchedulers,
    "Bjornulf_LoopCombosSamplersSchedulers": LoopCombosSamplersSchedulers,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # "Bjornulf_CustomStringType": "!!! CUSTOM STRING TYPE !!!",
    "Bjornulf_ollamaLoader": "🦙 Ollama (Description)",
    # "Bjornulf_PauseResume": "⏸️ Pause/Resume",
    "Bjornulf_FreeVRAM": "🧹 Free VRAM hack",
    "Bjornulf_CombineTextsByLines": "♻ Loop (All Lines from input 🔗 combine by lines)",
    "Bjornulf_TextToSpeech": "🔊 TTS - Text to Speech",
    "Bjornulf_CharacterDescriptionGenerator": "🧑📝 Character Description Generator",
    "Bjornulf_ImageMaskCutter": "🖼✂ Cut Image with Mask",
    "Bjornulf_LoadImageWithTransparency": "🖼 Load Image with Transparency ▢",
    "Bjornulf_GreenScreenToTransparency": "🟩➜▢ Green Screen to Transparency",
    # "Bjornulf_CheckBlackImage": "🔲 Check Black Image (Empty mask)",
    "Bjornulf_SaveBjornulfLobeChat": "🖼💬 Save image for Bjornulf LobeChat",
    "Bjornulf_TextToStringAndSeed": "🔢 Text with random Seed",
    # "Bjornulf_ClearVRAM": "🧹 Clear VRAM",
    "Bjornulf_RandomLineFromInput": "🎲 Random line from input",
    "Bjornulf_ShowText": "👁 Show (Text)",
    "Bjornulf_ShowInt": "👁 Show (Int)",
    "Bjornulf_ShowFloat": "👁 Show (Float)",
    "Bjornulf_CombineBackgroundOverlay": "🖼+🖼 Combine images (Background+Overlay alpha)",
    "Bjornulf_GrayscaleTransform": "🖼➜🔲 Image to grayscale (black & white)",
    "Bjornulf_RemoveTransparency": "▢➜⬛ Remove image Transparency (alpha)",
    # "🔲➜⬛ Transparency to color",
    "Bjornulf_ResizeImage": "📏 Resize Image",
    "Bjornulf_SaveImagePath": "🖼 Save Image (exact path, exact name) ⚠️💣",
    "Bjornulf_SaveImageToFolder": "🖼📁 Save Image(s) to a folder",
    "Bjornulf_SaveTmpImage": "🖼 Save Image (tmp_api.png) ⚠️💣",
    # "Bjornulf_SaveApiImage": "🖼 Save Image (./output/api_00001.png...)",
    "Bjornulf_SaveText": "💾 Save Text", #Make SaveCharacter, SaveLocation, SaveCamera, SaveAction, SaveClothes, SaveEmotion...
    "Bjornulf_LoadText": "📥 Load Text", #Make LoadCharacter, LoadLocation, LoadCamera, LoadAction, LoadClothes, LoadEmotion...
    "Bjornulf_WriteText": "✒ Write Text",
    "Bjornulf_WriteTextInConsole": "✒🗔 Write Text (Console too) ",
    # "Bjornulf_WriteImageEnvironment": "✒ Write Image Environment",
    # "Bjornulf_WriteImageCharacters": "✒ Write Image Characters",
    # "Bjornulf_WriteImageCharacter": "✒ Write Image Character",
    # "Bjornulf_WriteImageAllInOne": "✒ Write Image All-in-one",
    "Bjornulf_CombineTexts": "🔗 Combine (Texts)",
    "Bjornulf_LoopTexts": "♻ Loop (Texts)",
    "Bjornulf_RandomTexts": "🎲 Random (Texts)",
    "Bjornulf_RandomModelClipVae": "🎲 Random (Model+Clip+Vae)",
    "Bjornulf_imagesToVideo": "📹 images to video (FFmpeg)",
    "Bjornulf_VideoPingPong": "📹 video PingPong",
    "Bjornulf_LoopFloat": "♻ Loop (Float)",
    "Bjornulf_LoopInteger": "♻ Loop (Integer)",
    "Bjornulf_LoopBasicBatch": "♻ Loop",
    "Bjornulf_LoopAllLines": "♻ Loop (All Lines from input)",
    "Bjornulf_LoopSamplers": "♻ Loop (All Samplers)",
    "Bjornulf_LoopSchedulers": "♻ Loop (All Schedulers)",
    "Bjornulf_LoopCombosSamplersSchedulers": "♻ Loop (My combos Sampler⚔Scheduler)",
}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']