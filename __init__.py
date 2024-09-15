from .images_to_video import imagesToVideo
from .write_text import WriteText
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
# from .show_int import ShowInt
# from .show_float import ShowFloat
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
from .pause_resume_stop import PauseResume
from .pick_input import PickInput
from .loop_images import LoopImages
from .random_image import RandomImage
# from .random_checkpoint import RandomCheckpoint
from .loop_model_clip_vae import LoopModelClipVae
from .write_text_advanced import WriteTextAdvanced
from .loop_write_text import LoopWriteText
# from .load_images_from_folder import LoadImagesFromSelectedFolder
# from .show import ShowWhatever

# from .pass_preview_image import PassPreviewImage
# from .check_black_image import CheckBlackImage
# from .clear_vram import ClearVRAM

# from .CUSTOM_STRING import CustomStringType

NODE_CLASS_MAPPINGS = {
    # "Bjornulf_CustomStringType": CustomStringType,
    "Bjornulf_ollamaLoader": ollamaLoader,
    "Bjornulf_WriteText": WriteText,
    # "Bjornulf_LoadImagesFromSelectedFolder": LoadImagesFromSelectedFolder,
    # "Bjornulf_ShowWhatever": ShowWhatever,
    "Bjornulf_LoopModelClipVae": LoopModelClipVae,
    # "Bjoenulf_RandomCheckpoint": RandomCheckpoint,
    "Bjornulf_LoopWriteText": LoopWriteText,
    "Bjornulf_LoopImages": LoopImages,
    "Bjornulf_RandomImage": RandomImage,
    # "Bjornulf_PassPreviewImage": PassPreviewImage,
    "Bjornulf_PickInput": PickInput,
    "Bjornulf_PauseResume": PauseResume,
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
    "Bjornulf_WriteTextAdvanced": WriteTextAdvanced,
    "Bjornulf_RemoveTransparency": RemoveTransparency,
    "Bjornulf_GrayscaleTransform": GrayscaleTransform,
    "Bjornulf_CombineBackgroundOverlay": CombineBackgroundOverlay,
    # "Bjornulf_WriteImageEnvironment": WriteImageEnvironment,
    # "Bjornulf_WriteImageCharacters": WriteImageCharacters,
    # "Bjornulf_WriteImageCharacter": WriteImageCharacter,
    # "Bjornulf_WriteImageAllInOne": WriteImageAllInOne,
    "Bjornulf_ShowText": ShowText,
    # "Bjornulf_ShowInt": ShowInt,
    # "Bjornulf_ShowFloat": ShowFloat,
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
    "Bjornulf_WriteText": "✒ Write Text",
    "Bjornulf_WriteTextAdvanced": "✒🗔 Advanced Write Text",
    "Bjornulf_LoopWriteText": "♻ Loop (✒🗔 Advanced Write Text)",
    "Bjornulf_LoopModelClipVae": "♻ Loop (Model+Clip+Vae)",
    "Bjornulf_LoopImages": "♻🖼 Loop (Images)",
    "Bjornulf_CombineTextsByLines": "♻ Loop (All Lines from input 🔗 combine by lines)",
    "Bjornulf_LoopTexts": "♻ Loop (Texts)",
    "Bjornulf_LoopFloat": "♻ Loop (Float)",
    "Bjornulf_LoopInteger": "♻ Loop (Integer)",
    "Bjornulf_LoopBasicBatch": "♻ Loop",
    "Bjornulf_LoopAllLines": "♻ Loop (All Lines from input)",
    "Bjornulf_LoopSamplers": "♻ Loop (All Samplers)",
    "Bjornulf_LoopSchedulers": "♻ Loop (All Schedulers)",
    "Bjornulf_LoopCombosSamplersSchedulers": "♻ Loop (My combos Sampler⚔Scheduler)",
    "Bjornulf_RandomImage": "🎲🖼 Random Image",
    "Bjornulf_RandomLineFromInput": "🎲 Random line from input",
    "Bjornulf_RandomTexts": "🎲 Random (Texts)",
    "Bjornulf_RandomModelClipVae": "🎲 Random (Model+Clip+Vae)",
    # "Bjornulf_PassPreviewImage": "🖼⮕ Pass Preview Image",
    "Bjornulf_CharacterDescriptionGenerator": "🧑📝 Character Description Generator",
    "Bjornulf_GreenScreenToTransparency": "🟩➜▢ Green Screen to Transparency",
    # "Bjornulf_CheckBlackImage": "🔲 Check Black Image (Empty mask)",
    "Bjornulf_SaveBjornulfLobeChat": "🖼💬 Save image for Bjornulf LobeChat",
    "Bjornulf_TextToStringAndSeed": "🔢 Text with random Seed",
    # "Bjornulf_ClearVRAM": "🧹 Clear VRAM",
    # "Bjornulf_ShowWhatever": "👁 Show Anything",
    "Bjornulf_ShowText": "👁 Show (Text, Int, Float)",
    # "Bjornulf_ShowInt": "👁 Show (Int)",
    # "Bjornulf_ShowFloat": "👁 Show (Float)",
    "Bjornulf_ImageMaskCutter": "🖼✂ Cut Image with Mask",
    "Bjornulf_LoadImageWithTransparency": "🖼 Load Image with Transparency ▢",
    "Bjornulf_CombineBackgroundOverlay": "🖼+🖼 Combine images (Background+Overlay alpha)",
    "Bjornulf_GrayscaleTransform": "🖼➜🔲 Image to grayscale (black & white)",
    "Bjornulf_RemoveTransparency": "▢➜⬛ Remove image Transparency (alpha)",
    "Bjornulf_ResizeImage": "📏 Resize Image",
    "Bjornulf_SaveImagePath": "🖼 Save Image (exact path, exact name) ⚠️💣",
    "Bjornulf_SaveImageToFolder": "🖼📁 Save Image(s) to a folder",
    "Bjornulf_SaveTmpImage": "🖼 Save Image (tmp_api.png) ⚠️💣",
    # "Bjornulf_SaveApiImage": "🖼 Save Image (./output/api_00001.png...)",
    "Bjornulf_SaveText": "💾 Save Text",
    # "Bjornulf_LoadText": "📥 Load Text",
    "Bjornulf_CombineTexts": "🔗 Combine (Texts)",
    "Bjornulf_imagesToVideo": "📹 images to video (FFmpeg)",
    "Bjornulf_VideoPingPong": "📹 video PingPong",
    "Bjornulf_ollamaLoader": "🦙 Ollama (Description)",
    "Bjornulf_FreeVRAM": "🧹 Free VRAM hack",
    "Bjornulf_TextToSpeech": "🔊 TTS - Text to Speech",
    "Bjornulf_PickInput": "⏸️🔍 Paused. Select input, Pick one",
    "Bjornulf_PauseResume": "⏸️ Paused. Resume or Stop ?",
    # "Bjornulf_LoadImagesFromSelectedFolder": "📂🖼 Load Images from folder",
}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']