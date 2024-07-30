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
from .show_int import ShowInt
from .show_float import ShowFloat
from .save_text import SaveText
from .save_tmp_image import SaveTmpImage
from .save_image_path import SaveImagePath
from .save_api_image import SaveApiImage
from .save_img_to_folder import SaveImageToFolder
from .resize_image import ResizeImage
from .loop_my_combos_samplers_schedulers import LoopCombosSamplersSchedulers

# from .CUSTOM_STRING import CustomStringType

NODE_CLASS_MAPPINGS = {
    # "Bjornulf_CustomStringType": CustomStringType,
    "Bjornulf_ollamaLoader": ollamaLoader,
    "Bjornulf_WriteText": WriteText,
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
    "Bjornulf_SaveApiImage": SaveApiImage,
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
    "Bjornulf_ShowText": "👁 Show (Text)",
    "Bjornulf_ShowInt": "👁 Show (Int)",
    "Bjornulf_ShowFloat": "👁 Show (Float)",
    "Bjornulf_ResizeImage": "📏 Resize Image",
    "Bjornulf_SaveImagePath": "🖼 Save Image (exact path, exact name) ⚠️💣",
    "Bjornulf_SaveImageToFolder": "🖼📁 Save Image to a folder",
    "Bjornulf_SaveTmpImage": "🖼 Save Image (tmp_api.png) ⚠️💣",
    "Bjornulf_SaveApiImage": "🖼 Save Image (./output/api_00001.png...)",
    "Bjornulf_SaveText": "💾 Save Text", #Make SaveCharacter, SaveLocation, SaveCamera, SaveAction, SaveClothes, SaveEmotion...
    "Bjornulf_LoadText": "📥 Load Text", #Make LoadCharacter, LoadLocation, LoadCamera, LoadAction, LoadClothes, LoadEmotion...
    "Bjornulf_WriteText": "✒ Write Text",
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
    "Bjornulf_LoopSamplers": "♻ Loop (All Samplers)",
    "Bjornulf_LoopSchedulers": "♻ Loop (All Schedulers)",
    "Bjornulf_LoopCombosSamplersSchedulers": "♻ Loop (My combos Sampler⚔Scheduler)",
}

WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']