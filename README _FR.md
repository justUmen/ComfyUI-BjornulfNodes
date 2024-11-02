# 🔗 Comfyui : Bjornulf_custom_nodes v0.48 🔗

In English : [README.md](README.md)  

Une liste de 55 nœuds personnalisés pour Comfyui : Afficher, manipuler et éditer du texte, des images, des vidéos, des loras et plus encore.  
Vous pouvez gérer des opérations de boucle, générer du contenu aléatoire, déclencher des conditions logiques, faire des pauses et contrôler manuellement vos workflows, et même travailler avec des outils d'IA externes comme Ollama ou synthèse vocale.  

# Café : ☕☕☕☕☕ 5/5

❤️❤️❤️ <https://ko-fi.com/bjornulf> ❤️❤️❤️

# ☘ Ce projet fait partie de mon trio IA. ☘

1 - 📝 IA - Génération Text/Chat : [Bjornulf Lobe Chat Fork](https://github.com/justUmen/Bjornulf_lobe-chat)  
2 - 🔊 IA - Génération vocale : [Bjornulf Text To Speech](https://github.com/justUmen/Bjornulf_XTTS)  
<u>**3 - 🎨 IA - Génération d'images :** [Bjornulf Comfyui custom nodes](https://github.com/justUmen/ComfyUI-BjornulfNodes) (vous êtes ici)</u>  

# 📋 Menu des nœuds par catégorie

## 👁 Afficher / Montrer 👁
`1.` Afficher (Texte, Nombre entier/flottant) [👁 Show (Text, Int, Float)](#1----show-text-int-float)  
`49.` Aperçu Vidéo [📹👁 Video Preview](#49----video-preview)  

## ✒ Texte ✒
`2.` Écrire du texte [✒ Write Text](#2----write-text)  
`3.` 🗔 Écrire du texte "avancé" (+ 🎲 sélection aléatoire et 🅰️ variables) [✒🗔 Advanced Write Text (+ 🎲 random selection and 🅰️ variables)](#3----advanced-write-text---random-selection-and-🅰%EF%B8%8F-variables)  
`4.` Combiner des textes [🔗 Combine Texts](#4----combine-texts)  
`15.` Sauvegarder du texte [💾 Save Text](#15----save-text)  
`26.` Ligne aléatoire à partir de l'entrée [🎲 Random line from input](#26----random-line-from-input)  
`28.` Texte avec Seed aléatoire [🔢🎲 Text with random Seed](#28----text-with-random-seed)  
`32.` Générateur de description de personnage [🧑📝 Character Description Generator](#32----character-description-generator)  
`48.` Scrambleur de texte (Personnage) [🔀🎲 Text scrambler (🧑 Character)](#48----text-scrambler--character)  

## ♻ Boucle ♻
`6.` Boucle [♻ Loop](#6----loop)  
`7.` Boucle de textes [♻ Loop Texts](#7----loop-texts)  
`8.` Boucle nombre entier [♻ Loop Integer](#8----loop-integer)  
`9.` Boucle nombre flottant [♻ Loop Float](#9----loop-float)  
`10.` Boucle de tous les samplers [♻ Loop All Samplers](#10----loop-all-samplers)  
`11.` Boucle de tous les schedulers [♻ Loop All Schedulers](#11----loop-all-schedulers)  
`12.` Boucle combo [♻ Loop Combos](#12----loop-combos)  
`27.` Boucle (Toutes les lignes de l'entrée) [♻ Loop (All Lines from input)](#27----loop-all-lines-from-input)  
`33.` Boucle (Toutes les lignes de l'entrée 🔗 combinées par lignes) [♻ Loop (All Lines from input 🔗 combine by lines)](#33----loop-all-lines-from-input--combine-by-lines)  
`38.` Boucle (Images) [♻🖼 Loop (Images)](#38----loop-images)  
`39.` Boucle (Écrire du texte "avancé" + variables) [♻ Loop (✒🗔 Advanced Write Text + 🅰️ variables)](#39----loop--advanced-write-text)  
`42.` Boucle (Modèle+Clip+Vae) - Checkpoint [♻ Loop (Model+Clip+Vae) - aka Checkpoint / Model](#42----loop-modelclipvae---aka-checkpoint--model)  
`53.` Boucle Charger le checkpoint (Sélecteur de modèle) [♻ Loop Load checkpoint (Model Selector)](#53----loop-load-checkpoint-model-selector)  
`54.` Boucle Sélecteur de Lora [♻ Loop Lora Selector](#54----loop-lora-selector)  

## 🎲 Aléatoire 🎲
`3.` Écrire du texte avancé (+ sélection aléatoire et variables) [✒🗔 Advanced Write Text (+ 🎲 random selection and 🅰️ variables)](#3----advanced-write-text---random-selection-and-🅰%EF%B8%8F-variables)  
`5.` Aléatoire (Textes) [🎲 Random (Texts)](#5----random-texts)  
`26.` Ligne aléatoire à partir de l'entrée [🎲 Random line from input](#26----random-line-from-input)  
`28.` Texte avec Seed aléatoire [🔢🎲 Text with random Seed](#28----text-with-random-seed)  
`37.` Image aléatoire [🎲🖼 Random Image](#37----random-image)  
`40.` Aléatoire (Modèle+Clip+Vae) - Checkpoint [🎲 Random (Model+Clip+Vae) - aka Checkpoint / Model](#40----random-modelclipvae---aka-checkpoint--model)  
`41.` Charger un checkpoint aléatoire (Sélecteur de modèle) [🎲 Random Load checkpoint (Model Selector)](#41----random-load-checkpoint-model-selector)  
`48.` Scrambleur de texte (Personnage) [🔀🎲 Text scrambler (🧑 Character)](#48----text-scrambler--character)  
`55.` Sélecteur de Lora aléatoire [🎲 Random Lora Selector](#55----random-lora-selector)  

## 🖼💾 Sauvegarde d'image 💾🖼
`16.` Sauvegarder une image pour Bjornulf LobeChat [💾🖼💬 Save image for Bjornulf LobeChat](#16----save-image-for-bjornulf-lobechat-for-my-custom-lobe-chat)  
`17.` Sauvegarder une image (tmp_api.png) API Temporaire [💾🖼 Save image as `tmp_api.png` Temporary API](#17----save-image-as-tmp_apipng-temporary-api-%EF%B8%8F)  
`18.` Sauvegarder une image dans un dossier choisi [💾🖼📁 Save image to a chosen folder name](#18----save-image-to-a-chosen-folder-name)  
`14.` Sauvegarder sous un nom exact [💾🖼 Save Exact name](#1314------resize-and-save-exact-name-%EF%B8%8F)  

## 🖼📥 Charger une image 📥🖼
`29.` Charger une image avec transparence [📥🖼 Load Image with Transparency ▢](#29----load-image-with-transparency-)  
`43.` Charger des images depuis le dossier de sortie [📥🖼📂 Load Images from output folder](#43----load-images-from-output-folder)  

## 🖼 Image - autres 🖼
`13.` Redimensionner l'image [📏 Resize Image](#1314------resize-and-save-exact-name-%EF%B8%8F)  
`22.` Supprimer la transparence de l'image (alpha) [🔲 Remove image Transparency (alpha)](#22----remove-image-transparency-alpha)  
`23.` Image en niveaux de gris (noir & blanc) [🔲 Image to grayscale (black & white)](#23----image-to-grayscale-black--white)  
`24.` Superposer deux images (Fond + premier plan) [🖼+🖼 Stack two images (Background + Overlay)](#24----stack-two-images-background--overlay)  
`25.` Écran vert en transparence [🟩➜▢ Green Screen to Transparency](#25----green-screen-to-transparency)  
`29.` Charger une image avec transparence [⬇️🖼 Load Image with Transparency ▢](#29----load-image-with-transparency-)  
`30.` Couper une image avec un masque [🖼✂ Cut image with a mask](#30----cut-image-with-a-mask)  
`37.` Image aléatoire [🎲🖼 Random Image](#37----random-image)  
`38.` Boucle (Images) [♻🖼 Loop (Images)](#38----loop-images)  
`43.` Charger des images depuis le dossier output [⬇️📂🖼 Load Images from output folder](#43----load-images-from-output-folder)  
`44.` Sélectionner une image, Choisir [🖼👈 Select an Image, Pick](#44----select-an-image-pick)  
`46.` Détails de l'image [🖼🔍 Image Details](#46----image-details)  
`47.` Combiner des images [🖼 Combine Images](#47----combine-images)  

## 🚀 Charger des checkpoints 🚀
`40.` Aléatoire (Modèle+Clip+Vae) - Checkpoint [🎲 Random (Model+Clip+Vae) - aka Checkpoint / Model](#40----random-modelclipvae---aka-checkpoint--model)  
`41.` Charger un checkpoint aléatoire (Sélecteur de modèle) [🎲 Random Load checkpoint (Model Selector)](#41----random-load-checkpoint-model-selector)  
`42.` Boucle (Modèle+Clip+Vae) - Checkpoint [♻ Loop (Model+Clip+Vae) - aka Checkpoint / Model](#42----loop-modelclipvae---aka-checkpoint--model)  
`53.` Boucle Charger le checkpoint (Sélecteur de modèle) [♻ Loop Load checkpoint (Model Selector)](#53----loop-load-checkpoint-model-selector)

## 🚀 Charger des loras 🚀
`54.` Boucle Sélecteur de Lora [♻ Loop Lora Selector](#54----loop-lora-selector)  
`55.` Sélecteur de Lora aléatoire [🎲 Random Lora Selector](#55----random-lora-selector)  

## 📹 Video 📹
`20.` Ping Pong Vidéo [📹 Video Ping Pong](#20----video-ping-pong)  
`21.` Images en Vidéo (FFmpeg) [📹 Images to Video (FFmpeg)](#21----images-to-video)  
`49.` Aperçu Vidéo [📹👁 Video Preview](#49----video-preview)  
`50.` Images en Vidéo (vidéo temporaire) [🖼➜📹 Images to Video path (tmp video)](#50----images-to-video-path-tmp-video)  
`51.` Chemin/path de Vidéo en Images [📹➜🖼 Video Path to Images](#51----video-path-to-images)  
`52.` Synchronisation Audio Vidéo [🔊📹 Audio Video Sync](#52----audio-video-sync)  

## 🤖 IA 🤖
`19.` Ollama [🦙 Ollama](#19----ollama)  
`31.` Texte en Parole [🔊 TTS - Text to Speech](#31----tts---text-to-speech-100-local-any-voice-you-want-any-language)  

## 🔊 Audio 🔊
`31.` Texte en Parole [🔊 TTS - Text to Speech](#31----tts---text-to-speech-100-local-any-voice-you-want-any-language)  
`52.` Synchronisation Audio Vidéo [🔊📹 Audio Video Sync](#52----audio-video-sync)  

## 💻 System 💻
`34.` Libération de VRAM [🧹 Free VRAM hack](#34----free-vram-hack)  

## 🧍 Contrôle manuel de l'utilisateur 🧍
`35.` En pause. Reprendre ou arrêter, Choisir [⏸️ Paused. Resume or Stop, Pick 👇](#35---%EF%B8%8F-paused-resume-or-stop-)  
`36.` En pause. Sélectionner l'entrée, Choisir [⏸️ Paused. Select input, Pick 👇](#36---%EF%B8%8F-paused-select-input-pick-one)  

## 🧠 Logique / Opérations conditionnelles 🧠
`45.` Si-Sinon If-Else (comparer) [🔀 If-Else (input / compare_with)](#45----if-else-input--compare_with)  

# ☁ Utilisation en cloud :

Comfyui est excellent pour une utilisation locale, mais j'ai parfois besoin de plus de puissance que ce que j'ai...  
J'ai un ordinateur avec une 4070 super avec 12 Go et le flux fp8 simple prend environ ~40 secondes. Avec une 4090 dans le cloud, je peux exécuter le flux fp16 en ~12 secondes. (Il y a bien sûr aussi des workflows que je ne peux même pas exécuter localement.)  

Mon lien de parrainage pour Runpod : <https://runpod.io?ref=tkowk7g5> (Si vous utilisez cela, je recevrai une commission, sans frais supplémentaires pour vous.)  
Si vous voulez utiliser mes nœuds et comfyui dans le cloud (et que vous pouvez installer plus de choses), je gère un template optimisé prêt à l'emploi sur runpod : <https://runpod.io/console/deploy?template=r32dtr35u1&ref=tkowk7g5>  
Nom du template : `bjornulf-comfyui-allin-workspace`, opérationnel en ~3 minutes. (Cela dépend de votre pod, de la configuration et du téléchargement de modèles/checkpoints supplémentaires ou de tout autre élément non inclus.)  
Vous devez créer et sélectionner un volume réseau avant d'utiliser cela, la taille dépend de vous, j'ai 50 Go de stockage car je n'utilise le cloud que pour Flux ou l'entraînement de lora sur une 4090. (~0,7$/heure)  
⚠️ Lorsque le pod est prêt, vous devez ouvrir un terminal dans le navigateur (après avoir cliqué sur `connect` depuis votre pod) et utiliser ceci pour lancer ComfyUI manuellement : `cd /workspace/ComfyUI && python main.py --listen 0.0.0.0 --port 3000` (Il est bien meilleur de le contrôler avec un terminal, vérifier les logs, etc...)  
Ensuite, vous pouvez simplement cliquer sur le bouton `Connect to port 3000`.  
Comme gestionnaire de fichiers, vous pouvez utiliser le `JupyterLab` inclus sur le port 8888.  
Si vous avez des problèmes avec cela, faites-le moi savoir.  
Tout sera géré dans le stockage réseau Runpod (`/workspace/ComfyUI`), vous pouvez donc arrêter et redémarrer le GPU cloud sans rien perdre, changer de GPU ou autre.  
Zone : Je recommande `EU-RO-1`, mais à vous de choisir.  
Rechargez votre compte Runpod avec un minimum de 10$ pour commencer.  
⚠️ Attention, vous paierez à la minute, donc ce n'est pas recommandé pour tester ou apprendre comfyui. Faites-le localement !!!  
Exécutez le GPU cloud uniquement lorsque vous avez déjà votre workflow prêt à être exécuté.  
Conseil : prenez un GPU bon marché pour tester, télécharger des modèles/checkpoint ou configurer les choses.  
Pour télécharger des checkpoints ou autre, vous devez utiliser le terminal.  
Pour télécharger depuis Huggingface (obtenez le token ici <https://huggingface.co/settings/tokens>).  
Voici un exemple de tout ce dont vous avez besoin pour flux dev :  

```
huggingface-cli login --token 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
huggingface-cli download black-forest-labs/FLUX.1-dev flux1-dev.safetensors --local-dir /workspace/ComfyUI/models/unet
huggingface-cli download comfyanonymous/flux_text_encoders clip_l.safetensors --local-dir /workspace/ComfyUI/models/clip
huggingface-cli download comfyanonymous/flux_text_encoders t5xxl_fp16.safetensors --local-dir /workspace/ComfyUI/models/clip
huggingface-cli download black-forest-labs/FLUX.1-dev ae.safetensors --local-dir /workspace/ComfyUI/models/vae
```
Pour utiliser Flux, vous pouvez simplement glisser-déposer dans votre interface comfyui le .json de mon repo github : `workflows/FLUX_dev_troll.json`, lien direct : <https://github.com/justUmen/ComfyUI-BjornulfNodes/blob/main/workflows/FLUX_dev_troll.json>.  

Pour télécharger depuis civitai (obtenez le token ici <https://civitai.com/user/account>), il suffit de copier/coller le lien du checkpoint que vous souhaitez télécharger et d'utiliser quelque chose comme ça, avec votre token dans l'URL :  
```
CIVITAI="8b275fada679ba5812b3da2bf35016f6"
wget --content-disposition -P /workspace/ComfyUI/models/checkpoints "https://civitai.com/api/download/models/272376?type=Model&format=SafeTensor&size=pruned&fp=fp16&token=$CIVITAI"
```
Si vous avez des problèmes avec ce template Runpod, faites-le moi savoir, je suis là pour vous aider. 😊   

# 🏗 Dépendances (rien à faire pour mon runpod ☁)

## 🪟🐍 Windows : Installer des dépendances sur Windows avec Python intégré (version portable)

Vous devez d'abord trouver ce `python.exe` intégré à Python, puis vous pouvez faire un clic droit ou un shift + clic droit à l'intérieur du dossier dans votre gestionnaire de fichiers pour ouvrir un terminal.

Voici où je l'ai, avec la commande dont vous avez besoin :  
`H:\ComfyUI_windows_portable\python_embeded> .\python.exe -m pip install pydub ollama`  

Lorsque vous devez installer quelque chose, vous pouvez reprendre le même code et installer la dépendance que vous voulez :  
`.\python.exe -m pip install whateveryouwant`  

Vous pouvez ensuite exécuter comfyui.  

## 🐧🐍 Linux : Installer des dépendances (sans venv, non recommandé)

- `pip install ollama` (vous pouvez aussi installer ollama si vous le souhaitez :  https://ollama.com/download) - Vous n'avez pas vraiment besoin de l'installer si vous ne voulez pas utiliser mon nœud ollama. (MAIS vous devez exécuter `pip install ollama`)
- `pip install pydub` (pour le nœud TTS)

## 🐧🐍 Linux : Installer des dépendances avec un environnement virtuel python (venv)

Si vous voulez utiliser un environnement virtuel Python uniquement pour comfyUI, ce que je recommande, vous pouvez le faire par exemple (en pré-installant pip également) :  

```
sudo apt-get install python3-venv python3-pip
python3 -m venv /the/path/you/want/venv/bjornulf_comfyui
```

Une fois votre environnement installé dans ce nouveau dossier, vous pouvez l'activer et installer des dépendances à l'intérieur :  

```
source /the/path/you/want/venv/bjornulf_comfyui/bin/activate
pip install ollama pydub
```

Ensuite, vous pouvez démarrer comfyui avec cet environnement (notez que vous devez le réactiver chaque fois que vous voulez lancer comfyui) :  

```
cd /where/you/installed/ComfyUI && python main.py
```

# 📝 Changements / versions

- **v0.2** : Amélioration du nœud ollama avec invite système + sélection de modèle.  
- **v0.3** : Ajout d'un nouveau nœud : Sauvegarder l'image dans un dossier choisi.  
- **v0.3** : Ajout des métadonnées comfyui / workflow à tous mes nœuds liés aux images.  
- **v0.4** : Prise en charge de l'option de transparence avec le format webm, encodeurs d'options. Et ajout d'une entrée pour le flux audio.  
- **v0.5** : Nouveau nœud : Supprimer la transparence de l'image (alpha) - Remplir le canal alpha avec une couleur unie.  
- **v0.5** : Nouveau nœud : Image en niveaux de gris (noir & blanc) - Convertir une image en niveaux de gris.  
- **v0.6** : Nouveau nœud : Combiner des images (Fond + Overlay) - Combiner deux images en une seule.  
- **v0.7** : Remplacement du nœud API Sauvegarder par le nœud Sauvegarder Bjornulf Lobechat. (Pour mon lobe-chat personnalisé)  
- **v0.8** : Combiner des images : ajout d'une option pour placer l'image en haut, en bas ou au centre.  
- **v0.8** : Combiner des textes : ajout de l'option pour les barres obliques /  
- **v0.8** : Ajout d'un nœud basique pour transformer l'écran vert en transparence.  
- **v0.9** : Ajout d'un nouveau nœud : Retourner une ligne aléatoire à partir de l'entrée.  
- **v0.10** : Ajout d'un nouveau nœud : Boucle (Toutes les lignes de l'entrée) - Itérer sur toutes les lignes d'un texte d'entrée.  
- **v0.11** : Ajout d'un nouveau nœud : Texte avec Seed aléatoire - Générer une seed aléatoire, avec du texte.  
- **v0.12** : Combiner des images : ajout d'une option pour déplacer verticalement et horizontalement. (de -50% à 150%)  
- **v0.13** : Ajout d'un nouveau nœud : Charger une image avec transparence (alpha) - Charger une image avec transparence.  
- **v0.14** : Ajout d'un nouveau nœud : Couper une image à partir d'un masque.  
- **v0.15** : Ajout de deux nouveaux nœuds : TTS - Texte en Parole et Générateur de Description de Personnage.  
- **v0.16** : Gros changements sur le Générateur de Description de Personnage.  
- **v0.17** : Nouveau nœud de boucle, combiner par lignes.  
- **v0.18** : Nouveau nœud de boucle, Hack de libération de VRAM.  
- **v0.19** : Changements pour le nœud de sauvegarde vers un dossier : ignorer les noms d'images manquants, utilisera le nombre le plus élevé trouvé + 1.  
- **v0.20** : Changements pour la sauvegarde lobechat de l'image : inclure le code du hack de libération de VRAM + ignorer les noms d'images manquants.  
- **v0.21** : Ajout d'un nouveau nœud d'écriture de texte qui affiche également le texte dans la console comfyui (pratique pour déboguer).  
- **v0.22** : Autoriser le nœud d'écriture de texte à utiliser une sélection aléatoire comme ceci {capuche|casque} choisira au hasard entre capuche ou casque.  
- **v0.23** : Ajout d'un nouveau nœud : Pause, reprendre ou arrêter le workflow.  
- **v0.24** : Ajout d'un nouveau nœud : Pause, sélectionner l'entrée, en choisir une.  
- **v0.25** : Deux nouveaux nœuds : Boucle d'images et Image aléatoire.  
- **v0.26** : Nouveau nœud : Boucle écrire du texte. Augmenter également le nombre d'entrées autorisées pour la plupart des nœuds. (+ mise à jour de quelques changements majeurs)  
- **v0.27** : Deux nouveaux nœuds : Boucle (Modèle+Clip+Vae) et Aléatoire (Modèle+Clip+Vae) - aka Checkpoint / Modèle.  
- **v0.28** : Correction des textes aléatoires et ajout de nombreux exemples de captures d'écran pour plusieurs nœuds.  
- **v0.29** : Correction des problèmes de points flottants avec le nœud de boucle flottante.  
- **v0.30** : Mise à jour du nœud de boucle basique avec une entrée optionnelle.  
- **v0.31** : ❗Désolé, modifications majeures pour les nœuds d'écriture/affichage de texte, système plus propre : 1 simple nœud d'écriture de texte et un autre avancé avec console et syntaxe spéciale. Afficher peut maintenant gérer INT, FLOAT, TEXTE.  
- **v0.32** : Renommage rapide pour éviter de casser le nœud loop_text.  
- **v0.33** : Contrôle aléatoire sur les nœuds en pause, correction du bug de son pydub sous Windows.  
- **v0.34** : Deux nouveaux nœuds : Charger des images depuis le dossier de sortie et Sélectionner une image, Choisir.  
- **v0.35** : Grandes améliorations du nœud TTS 31. Il enregistrera également le fichier audio dans le dossier "ComfyUI/Bjornulf_TTS/". - Pas encore testé sous Windows -  
- **v0.36** : Correction du modèle aléatoire.  
- **v0.37** : Nouveau nœud : Chargement aléatoire du checkpoint (Sélecteur de modèle). Alternative au nœud de checkpoint aléatoire. (Ne précharge pas tous les checkpoints en mémoire, plus lent pour changer de checkpoint, mais plus de sorties pour décider où stocker vos résultats.)  
- **v0.38** : Nouveau nœud : Logique Si-Sinon. (entrée == comparer_avec), exemples avec différentes tailles d'espace latent. + correction de quelques problèmes de désérialisation.  
- **v0.39** : Ajout de la gestion des variables au nœud d'écriture de texte avancé.  
- **v0.40** : Ajout de la gestion des variables au nœud de boucle d'écriture de texte avancé. Ajout d'un menu pour tous les nœuds au README.  
- **v0.41** : Deux nouveaux nœuds : détails de l'image et combiner des images. Aussi ❗ Gros changements pour le nœud Si-Sinon. (+ beaucoup de petits changements)  
- **v0.42** : Meilleure README avec nœuds par catégorie, modifications de certains titres de nœuds.  
- **v0.43** : Ajout de control_after_generate à Ollama et possibilité de conserver en VRAM pendant 1 minute si besoin. (Pour enchaîner des générations rapides.) Ajout de fallback à 0.0.0.0.  
- **v0.44** : Autoriser ollama à avoir une url personnalisée dans le fichier `ollama_ip.txt` dans le dossier des nœuds personnalisés de comfyui. Changements mineurs, ajout de détails/mises à jour au README.  
- **v0.45** : Ajout d'un nouveau nœud : Scrambleur de texte (Personnage), changement aléatoire du texte en utilisant le fichier `scrambler/scrambler_character.json` dans le dossier des nœuds personnalisés de comfyui.  
- **v0.46** : ❗ De nombreux changements pour les nœuds vidéo. Sauvegarder en vidéo utilise désormais des FLOAT pour les fps, pas des INT. (Beaucoup d'autres nœuds personnalisés font ça aussi...) Ajout d'un nœud pour prévisualiser la vidéo, ajouter un nœud pour convertir un chemin vidéo en liste d'images, ajouter un nœud pour convertir une liste d'images en vidéo temporaire + chemin vidéo. ajout d'un nœud pour synchroniser la durée de l'audio avec la vidéo. (utile pour MuseTalk) modification du nœud TTS avec de nombreuses nouvelles sorties ("audio_path", "full_path", "duration") à réutiliser avec d'autres nœuds comme MuseTalk, aussi TTS renommé input en "connect_to_workflow", pour éviter les erreurs d'envoi de texte.  
- **v0.47** : Nouveau nœud : Boucle Charger le checkpoint (Sélecteur de modèle).  
- **v0.48** : Deux nouveaux nœuds pour les loras : Sélecteur de Lora aléatoire et Boucle Sélecteur de Lora.  

# 📝 Nodes descriptions

## 1 - 👁 Show (Text, Int, Float)

![Show Text](screenshots/show.png)

**Description:**  
Le nœud d'affichage ne fera que montrer du texte ou une liste de plusieurs textes. (nœud en lecture seule)  
3 types sont gérés : le vert est pour les chaînes de caractères (STRING), l'orange pour les nombres flottants (FLOAT) et le bleu pour les entiers (INT). J'ai mis des couleurs pour que vous (ou moi) n'essayiez pas de les modifier. 🤣  

## 2 - ✒ Write Text

![write Text](screenshots/write.png)

**Description:**  
Nœud simple pour écrire du texte.  

## 3 - ✒🗔 Advanced Write Text (+ 🎲 random selection and 🅰️ variables)

![write Text Advanced](screenshots/write_advanced.png)

**Description:**  
Le nœud "Écrire du texte avancé" permet une syntaxe spéciale pour accepter des variantes aléatoires, comme {capuche|casque} qui choisira au hasard entre capuche ou casque.  
Vous avez également seed et control_after_generate pour gérer l'aléatoire.  
Il affiche aussi le texte dans la console de ComfyUI. (Utile pour le débogage)  
Exemple de logs dans la console :  
```
Raw text: photo of a {green|blue|red|orange|yellow} {cat|rat|house}
Picked text: photo of a green house
```

Vous pouvez aussi créer et réutiliser des variables avec cette syntaxe : `<nom>`.
Usage example :  

![variables](screenshots/variables.png)

## 4 - 🔗 Combine Texts
![Combine Texts](screenshots/combine_texts.png)

**Description:**  
Combine plusieurs entrées de texte en une seule sortie. (peut avoir une séparation avec : virgule, espace, nouvelle ligne ou rien.)  

## 5 - 🎲 Random (Texts)
![Random Text](screenshots/random_text.png)

**Description:**  
Génère et affiche un texte aléatoire à partir d'une liste prédéfinie. Idéal pour créer des propositions aléatoires.  
Vous avez également `control_after_generate` pour gérer l'aléatoire.  

## 6 - ♻ Loop
![Loop](screenshots/loop.png)

**Description:**  
Nœud de boucle à usage général, vous pouvez le connecter entre n'importe quels éléments.  
Il possède une entrée optionnelle, si aucune entrée n'est donnée, il bouclera sur la valeur de la chaîne "if_no_input" (que vous pouvez modifier).  
❗ Attention, ce nœud accepte tout type d'entrée et de sortie, vous pouvez donc l'utiliser avec des textes, des entiers, des images, des masques, etc. Mais assurez-vous que vos entrées/sorties soient cohérentes.  
N'utilisez pas cette Boucle si vous pouvez faire autrement.  

Voici un exemple avec mon nœud 28, pour forcer une seed différente à chaque itération :  
![Loop](screenshots/loop4.png)

## 7 - ♻ Loop Texts
![Loop Texts](screenshots/loop_texts.png)

**Description:**  
Parcourez une liste d'entrées de texte.  

Voici un exemple d'utilisation avec la combinaison de textes et "flux" :  
![Loop Texts example](screenshots/loop_text_example.png)

## 8 - ♻ Loop Integer
![Loop Integer](screenshots/loop_integer.png)
![Loop Int + Show Text](screenshots/loop_int+show_text.png)

**Description:**  
Itérer à travers une plage de valeurs entières, utile pour les `steps` dans ksampler, etc...  

❗ N'oubliez pas que vous pouvez convertir les widgets de ksampler en entrée en faisant un clic droit sur le nœud ksampler :  
![Widget to Input](screenshots/widget-to-input.png)

Voici un exemple d'utilisation avec ksampler (Remarquez qu'avec "steps", ce nœud n'est pas optimisé, mais suffisant pour un test rapide) :  
![Widget to Input](screenshots/example_loop_integer.png)

## 9 - ♻ Loop Float
![Loop Float + Show Text](screenshots/loop_float+show_text.png)
![Loop Float](screenshots/loop_float.png)

**Description:**  
Bouclez à travers une plage de nombres à virgule flottante, utile pour cfg, denoise, etc...  

Voici un exemple avec controlnet, en essayant de créer un chat rouge basé sur un lapin bleu :  
![Loop All Samplers](screenshots/loop_float_example.png)

## 10 - ♻ Loop All Samplers
![Loop All Samplers](screenshots/loop_all_samplers.png)

**Description:**  
Itérer sur tous les samplers disponibles pour les appliquer de manière séquentielle. Idéal pour les tests.  

Voici un exemple de boucle sur tous les samplers avec le scheduler "normal" :  
![Loop All Samplers](screenshots/example_loop_all_samplers.png)

## 11 - ♻ Loop All Schedulers
![Loop All Schedulers](screenshots/loop_all_schedulers.png)

**Description:**  
Itérer sur tous les schedulers disponibles pour les appliquer de manière séquentielle. Idéal pour les tests. (même idée que pour les samplers ci-dessus, mais pour les schedulers)  

## 12 - ♻ Loop Combos
![Loop Combos](screenshots/loop_combos.png)

**Description:**  
Générer une boucle à partir d'une liste de mes propres combinaisons personnalisées (scheduler + sampler), ou sélectionner manuellement une combinaison.
Utile pour les tests.  

Exemple d'utilisation pour voir les différences entre différentes combinaisons :  
![example combos](screenshots/example_combos.png)

## 13/14 - 📏 + 🖼 Resize and Save Exact name ⚠️💣
![Resize and Save Exact](screenshots/resize_save_exact.png)

**Description:**  
Redimensionner une image aux dimensions exactes. L'autre nœud enregistrera l'image à l'emplacement exact.  
⚠️💣 Avertissement : L'image sera écrasée si elle existe déjà.  


## 15 - 💾 Save Text
![Save Text](screenshots/save_text.png)

**Description:**  
Sauvegarder l'entrée de texte donnée dans un fichier. Utile pour la journalisation et le stockage des données textuelles.  

## 16 - 💾🖼💬 Save image for Bjornulf LobeChat (❗For my custom [lobe-chat](https://github.com/justUmen/Bjornulf_lobe-chat)❗)
![Save Bjornulf Lobechat](screenshots/save_bjornulf_lobechat.png)

**Description:**  
❓ J'ai créé ce nœud pour mon lobe-chat personnalisé afin d'envoyer+recevoir des images via l'API de Comfyui : [lobe-chat](https://github.com/justUmen/Bjornulf_lobe-chat)  
Il enregistrera l'image dans le dossier `output/BJORNULF_LOBECHAT/`.  
Le nom commencera par `api_00001.png`, puis `api_00002.png`, etc...  
Il créera également un lien vers la dernière image générée à l'emplacement `output/BJORNULF_API_LAST_IMAGE.png`.  
Ce lien sera utilisé par mon lobe-chat personnalisé pour copier l'image dans le projet lobe-chat.  


## 17 - 💾🖼 Save image as `tmp_api.png` Temporary API ⚠️💣
![Save Temporary API](screenshots/save_tmp_api.png)

**Description:**  
Sauvegarder une image pour une utilisation à court terme : ./output/tmp_api.png ⚠️💣

## 18 - 💾🖼📁 Save image to a chosen folder name
![Save Temporary API](screenshots/save_image_to_folder.png)

**Description:**  
Sauvegarder une image dans un dossier spécifique : `my_folder/00001.png`, `my_folder/00002.png`, etc...  
Permet également plusieurs dossiers imbriqués, comme par exemple : `animal/dog/small`.  

## 19 - 🦙 Ollama
![Ollama](screenshots/ollama_1.png)

**Description:**  
Générera un texte détaillé basé sur ce que vous lui donnez.  
Je recommande d'utiliser `mistral-nemo` si vous pouvez le faire tourner, mais c'est à vous de décider. (Il faudra peut-être ajuster légèrement l'invite système)  

Vous avez également `control_after_generate` pour forcer le nœud à se relancer à chaque exécution du workflow. (Même s'il n'y a pas de modification du nœud ou de ses entrées.)  

Vous avez l'option de le garder en VRAM pendant une minute avec `keep_1min_in_vram`. (Si vous prévoyez de générer plusieurs fois avec le même prompt)  
Chaque exécution sera significativement plus rapide, mais ne libérera pas la VRAM pour autre chose.  

![Ollama](screenshots/ollama_2.png) 

⚠️ Avertissement : L'utilisation de `keep_1min_in_vram` peut être un peu gourmande en VRAM. Réfléchissez bien si vous en avez vraiment besoin. La plupart du temps, lorsque vous utilisez `keep_1min_in_vram`, vous ne voudrez pas générer une image ou autre chose en même temps.  

⚠️ Vous pouvez créer un fichier appelé `ollama_ip.txt` dans mon dossier de nœuds personnalisés de ComfyUI si vous avez une IP spéciale pour votre serveur Ollama, la mienne est : `http://192.168.1.37:11434`.  

## 20 - 📹 Video Ping Pong
![Video Ping Pong](screenshots/video_pingpong.png)

**Description:**  
Créer un effet ping-pong à partir d'une liste d'images (d'une vidéo) en inversant la direction de lecture lorsque la dernière image est atteinte. Idéal pour un effet de boucle infinie.  

## 21 - 📹 Images to Video
![Images to Video](screenshots/imgs2video.png)

**Description:**  
Combiner une séquence d'images en un fichier vidéo.  
❓ J'ai créé ce nœud car il prend en charge la transparence avec le format webm. (Nécessaire pour rembg)  
Les images temporaires sont stockées dans le dossier `ComfyUI/temp_images_imgs2video/`, ainsi que le fichier audio wav.  

## 22 - 🔲 Remove image Transparency (alpha)
![Remove Alpha](screenshots/remove_alpha.png)

**Description:**  
Supprimer la transparence d'une image en remplissant le canal alpha avec une couleur unie. (noir, blanc ou écran vert)  
Bien sûr, cela fonctionne avec une image ayant de la transparence, comme celles provenant des nœuds rembg.  
Nécessaire pour certains nœuds qui ne prennent pas en charge la transparence.  

## 23 - 🔲 Image to grayscale (black & white)
![Image to Grayscale](screenshots/grayscale.png)

**Description:**  
Convertir une image en niveaux de gris (noir et blanc)  
Exemple : Je l'utilise parfois avec Ipadapter pour désactiver l'influence des couleurs.  
Mais parfois, vous pouvez aussi vouloir avoir une image en noir et blanc...  

## 24 - 🖼+🖼 Stack two images (Background + Overlay)
![Superpose Images](screenshots/combine_background_overlay.png)

**Description:**  
Superposer deux images en une seule : une image de fond et une (ou plusieurs) superpositions transparentes. (permet d'avoir une vidéo, il suffit d'envoyer toutes les images et de les recombiner ensuite.)  
Mise à jour 0.11 : Ajout d'une option pour déplacer verticalement et horizontalement. (de -50% à 150%)  
❗ Avertissement : Pour l'instant, `background` est une image statique. (J'ajouterai la possibilité d'y mettre une vidéo plus tard.)  
⚠️ Avertissement : Si vous souhaitez charger directement une image avec transparence, utilisez mon nœud `🖼 Load Image with Transparency ▢` au lieu du nœud `Load Image`.  


## 25 - 🟩➜▢ Green Screen to Transparency
![Greenscreen to Transparency](screenshots/greeenscreen_to_transparency.png)

**Description:**  
Transformer l'écran vert en transparence.  
Nécessite bien sûr un écran vert propre. (Le seuil peut être ajusté, mais c'est un nœud très basique.)

## 26 - 🎲 Random line from input
![Random line from input](screenshots/random_line_from_input.png)

**Description:**  
Prend une ligne aléatoire à partir d'un texte d'entrée. (Lorsque l'utilisation de plusieurs nœuds "Écrire Texte" devient fastidieuse, vous pouvez simplement copier/coller une liste de l'extérieur.)  
Vous pouvez changer entre fixe/aléatoire (fixed/randomized) avec `control_after_generate` pour obtenir un texte différent à chaque exécution du workflow. (ou pas)

## 27 - ♻ Loop (All Lines from input)
![Loop input](screenshots/loop_all_lines.png)

**Description:**  
Itérer sur toutes les lignes d'un texte d'entrée. (Utile pour tester plusieurs lignes de texte.)

## 28 - 🔢 Text with random Seed

**Description:**  

❗ Ce nœud est utilisé pour forcer la génération d'une seed aléatoire avec du texte.  
Mais qu'est-ce que cela signifie ???  
Lorsque vous utilisez une boucle (♻), la boucle utilise la même seed pour chaque itération. (Le but est de conserver la même seed pour comparer les résultats.)  
Même avec `randomize` pour `control_after_generate`, il utilise toujours la même seed pour chaque boucle, et elle ne change qu'à la fin du workflow.

![Text with random Seed 1](screenshots/random_seed_1.png)

Donc, si vous souhaitez forcer l'utilisation d'une autre seed à chaque itération, vous pouvez utiliser ce nœud au milieu.
Par exemple, si vous souhaitez générer une image différente à chaque fois. (c'est-à-dire : vous utilisez des nœuds de boucle non pas pour comparer ou tester des résultats, mais pour générer plusieurs images.)  
Utilisez-le ainsi par exemple : (Les deux images ont des prompts différents ET des seeds différentes)

![Text with random Seed 2](screenshots/random_seed_2.png)

Voici un exemple des similarités que vous souhaitez éviter avec FLUX avec des prompts différents (capuche/casque) mais la même seed :

![Text with random Seed 3](screenshots/random_seed_3_flux.png)

Voici un exemple des similarités que vous souhaitez éviter avec SDXL avec des prompts différents (bleu/rouge) mais la même seed :

![Text with random Seed 4](screenshots/random_seed_4_sdxl.png)

FLUX : Voici un exemple de 4 images sans le nœud Random Seed à gauche, et à droite 4 images avec le nœud Random Seed :

![Text with random Seed 5](screenshots/result_random_seed.png)

## 29 - 🖼 Load Image with Transparency ▢
![Load image Alpha](screenshots/load_image_alpha.png)

**Description:**  
Charge une image avec transparence.  
Le nœud `Load Image` par défaut ne chargera pas la transparence.  

## 30 - 🖼✂ Cut image with a mask
![Cut image](screenshots/image_mask_cut.png)

**Description:**  
Découpe une image à partir d'un masque.  

## 31 - 🔊 TTS - Text to Speech (100% local, any voice you want, any language)
![TTS](screenshots/tts.png)

**Description:**  
[Listen to the audio example](https://github.com/user-attachments/assets/5a4a67ff-cf70-4092-8f3b-1ccc8023d8c6)

❗ Nœud jamais testé sur Windows, uniquement sur Linux pour le moment. ❗  

Utilisez mon serveur TTS pour générer de la parole à partir de texte, basé sur XTTS v2.  
❗ Bien sûr, pour utiliser ce nœud comfyui (frontend), vous devez utiliser mon serveur TTS (backend) : <https://github.com/justUmen/Bjornulf_XTTS>  
J'ai créé ce backend pour <https://github.com/justUmen/Bjornulf_lobe-chat>, mais vous pouvez également l'utiliser avec comfyui via ce nœud.  
Après avoir installé `Bjornulf_XTTS`, vous DEVEZ créer un lien dans mon dossier de nœuds personnalisés Comfyui appelé `speakers` : `ComfyUI/custom_nodes/Bjornulf_custom_nodes/speakers`  
Ce lien doit pointer vers le dossier où vous avez installé/storé les échantillons de voix que vous utilisez pour mon TTS, comme `default.wav`.  
Si mon serveur TTS fonctionne sur le port 8020 (vous pouvez tester dans votre navigateur avec le lien <http://localhost:8020/tts_stream?language=en&speaker_wav=default&text=Hello>) et que les échantillons de voix sont bons, vous pouvez utiliser ce nœud pour générer de la parole à partir du texte.

**Détails**  
Ce nœud doit toujours être connecté à un nœud principal : `Preview audio`.  

Mon nœud générera et enregistrera les fichiers audio dans le dossier `ComfyUI/Bjornulf_TTS/`, en fonction de la langue sélectionnée, du nom de l'échantillon de voix et du texte.  
Exemple de fichier audio à partir de la capture d'écran ci-dessus : `ComfyUI/Bjornulf_TTS/Chinese/default.wav/你吃了吗.wav`  
Vous remarquerez que vous n'avez PAS besoin de sélectionner une voix chinoise pour parler en chinois. Oui, cela fonctionne, vous pouvez vous enregistrer et vous faire parler dans la langue que vous voulez.  
De plus, lorsque vous sélectionnez une voix avec ce format `fr/fake_Bjornulf.wav`, il créera évidemment un dossier supplémentaire `fr` : `ComfyUI/Bjornulf_TTS/English/fr/fake_Bjornulf.wav/hello_im_me.wav`. Facile de voir que vous utilisez un échantillon de voix française pour un enregistrement en anglais.

`control_after_generate` comme d'habitude, il est utilisé pour forcer le nœud à s'exécuter à chaque exécution du workflow. (Même s'il n'y a aucune modification du nœud ou de ses entrées.)  
`overwrite` est utilisé pour écraser le fichier audio s'il existe déjà. (Par exemple, si vous n'aimez pas la génération, définissez simplement `overwrite` sur True et exécutez à nouveau le workflow, jusqu'à obtenir un bon résultat. Ensuite, vous pouvez remettre la valeur à False. (En résumé : sans `overwrite` défini sur True, il ne régénérera pas le fichier audio s'il existe déjà dans le dossier `Bjornulf_TTS`.)  
`autoplay` est utilisé pour jouer le fichier audio dans le nœud lorsqu'il est exécuté. (La lecture manuelle ou l'enregistrement se fait dans le nœud `preview audio`.)

Donc... notez que si vous savez que vous avez déjà un fichier audio prêt à être joué, vous pouvez toujours utiliser mon nœud, mais vous n'avez PAS besoin que mon serveur TTS soit en cours d'exécution.  
Mon nœud jouera simplement le fichier audio s'il le trouve, il n'essaiera pas de se connecter au serveur backend TTS.  
Disons que vous avez déjà utilisé ce nœud pour créer un fichier audio disant `workflow is done` avec la voix d'Attenborough :  

![TTS](screenshots/tts_end.png)  

Tant que vous gardez exactement les mêmes paramètres, il n'utilisera pas mon serveur pour jouer le fichier audio ! Vous pouvez éteindre le serveur TTS en toute sécurité, donc il n'utilisera pas votre précieuse VRAM. (Le serveur TTS devrait utiliser environ 3 Go de VRAM.)

De plus, `connect_to_workflow` est optionnel, cela signifie que vous pouvez créer un workflow avec SEULEMENT mon nœud TTS pour pré-générer les fichiers audio avec les phrases que vous souhaitez utiliser plus tard, exemple :  
![TTS](screenshots/tts_preload.png)  

Si vous voulez exécuter mes nœuds TTS en même temps que la génération d'images, je vous recommande d'utiliser mon nœud PAUSE afin que vous puissiez arrêter manuellement le serveur TTS après l'exécution de mon nœud TTS. Une fois la VRAM libérée, vous pouvez cliquer sur le bouton RESUME pour continuer le workflow.  
Si vous pouvez vous permettre d'exécuter les deux en même temps, tant mieux pour vous, mais localement, je ne peux pas faire fonctionner mon serveur TTS et FLUX en même temps, donc j'utilise cette astuce :  

![TTS](screenshots/tts_preload_2.png)  

### 32 - 🧑📝 Character Description Generator
![characters](screenshots/characters.png)
![characters](screenshots/characters2.png)

**Description:**  
Génère une description de personnage basée sur un fichier json dans le dossier `characters` : `ComfyUI/custom_nodes/Bjornulf_custom_nodes/characters`  
Créez votre propre fichier json avec vos propres personnages, et utilisez ce nœud pour générer une description.  
❗ Pour l'instant, c'est un nœud très basique, beaucoup de choses vont être ajoutées et modifiées !!!  
Certains détails sont inutilisables pour certains checkpoints, c'est un travail en cours, la structure du json n'est pas encore définitive.  
Certains personnages sont déjà inclus.  

### 33 - ♻ Loop (All Lines from input 🔗 combine by lines)

![loop combined](screenshots/loop_combined.png)

**Description:**  
Parfois, vous voulez boucler sur plusieurs entrées, mais vous souhaitez également séparer différentes lignes de votre sortie.  
Avec ce nœud, vous pouvez définir le nombre d'entrées et de sorties que vous voulez. Voir l'exemple pour l'utilisation.  

### 34 - 🧹 Free VRAM hack
![free vram](screenshots/free_vram_hack1.png)
![free vram](screenshots/free_vram_hack2.png)

**Description:**  
Voici ma tentative pour libérer de la VRAM après utilisation, je vais essayer d'améliorer cela.  
Pour moi, au lancement, ComfyUI utilise 180MB de VRAM, après l'utilisation de mon nœud de nettoyage de VRAM, cela peut redescendre à 376MB.  
Je ne pense pas qu'il existe un moyen propre de le faire, donc j'utilise une méthode un peu "bricolée".  
Ce n'est donc pas parfait, mais c'est mieux que d'être bloqué avec 6GB de VRAM utilisés si je sais que je ne vais plus en avoir besoin...  
Il suffit de connecter ce nœud à votre workflow, il prend une image en entrée et renvoie la même image sans aucun changement.  
❗ ComfyUI utilise du cache pour fonctionner plus rapidement (comme ne pas recharger les checkpoints), donc utilisez ce nœud de libération de VRAM seulement quand vous en avez besoin.  
❗ Pour que ce nœud fonctionne correctement, vous devez activer le mode dev/api dans ComfyUI. (Vous pouvez le faire dans les paramètres)

### 35 - ⏸️ Paused. Resume or Stop ?

![pause resume stop](screenshots/pause1.png)
![pause resume stop](screenshots/pause2.png)
![pause resume stop](screenshots/pause3.png)

**Description:**  
Interrompt automatiquement le workflow et fait sonner une cloche quand c'est le cas. (joue le fichier audio `bell.m4a` fourni)  
Vous pouvez ensuite reprendre ou arrêter manuellement le workflow en cliquant sur les boutons du nœud.  
Je fais cela, par exemple, si j'ai un processus de suréchantillonnage très long, je peux vérifier si l'entrée est correcte avant de continuer. Parfois, je peux arrêter le workflow et le redémarrer avec une autre seed.  
Vous pouvez connecter n'importe quel type de nœud au nœud de pause, ci-dessus un exemple avec du texte, mais vous pouvez envoyer une IMAGE ou autre chose, dans le nœud `input = output`. (Bien sûr, vous devez envoyer la sortie vers quelque chose qui a le bon format...)  

### 36 - ⏸️🔍 Paused. Select input, Pick one

![pick input](screenshots/pick.png)

**Description:**  
Interrompt automatiquement le workflow et fait sonner une cloche quand c'est le cas. (joue le fichier audio `bell.m4a` fourni)  
Vous pouvez ensuite sélectionner manuellement l'entrée que vous souhaitez utiliser, puis reprendre le workflow avec celle-ci.  
Vous pouvez connecter ce nœud à tout ce que vous voulez, ci-dessus un exemple avec une IMAGE. Mais vous pouvez choisir ce que vous voulez, dans le nœud `input = output`.  

### 37 - 🎲🖼 Random Image

![random image](screenshots/random_image.png)

**Description:**  
Prend simplement une image aléatoire à partir d'une liste d'images.  

### 38 - ♻🖼 Loop (Images)

![loop images](screenshots/loop_images.png)

**Description:**  
Boucle sur une liste d'images.  
Exemple d'utilisation : Vous avez une liste d'images, et vous voulez appliquer le même processus à chacune d'entre elles.  
Ci-dessus un exemple du nœud de boucle d'images les envoyant à un workflow Ipadapter. (Même seed bien sûr.)  

### 39 - ♻ Loop (✒🗔 Advanced Write Text)

![loop write text](screenshots/loop_write_text.png)

**Description:**  
Si vous avez besoin d'une boucle rapide mais que vous ne voulez pas quelque chose de trop complexe avec un nœud de boucle, vous pouvez utiliser ce nœud combiné d'écriture de texte + boucle.  
Il acceptera la même syntaxe spéciale que le nœud Advanced write text `{blue|red}`, mais il bouclera sur TOUTES les possibilités au lieu d'en prendre une au hasard.  
Version 0.40 : Vous pouvez également utiliser des variables `<name>` dans la boucle.  

### 40 - 🎲 Random (Model+Clip+Vae) - aka Checkpoint / Model

![random checkpoint](screenshots/random_checkpoint.png)

**Description:**  
Prend simplement un trio aléatoire à partir d'un nœud de chargement de checkpoint.  
Notez qu'il utilise le nœud principal Load checkpoint. Cela signifie que tous les checkpoints seront préchargés en mémoire.

Détails :  
- Cela prendra plus de VRAM, mais il sera plus rapide de passer d'un checkpoint à l'autre.  
- Il ne peut pas vous donner le nom du checkpoint actuellement chargé.

Consultez le nœud numéro 41 avant de décider lequel utiliser.  

### 41 - 🎲 Random Load checkpoint (Model Selector)

![pick input](screenshots/random_load_checkpoint.png)

**Description:**  
Ceci est une autre façon de sélectionner un nœud de chargement de checkpoint aléatoirement.  
Il ne préchargera pas tous les checkpoints en mémoire, donc il sera plus lent de passer d'un checkpoint à l'autre.  
Mais vous pouvez utiliser plus de sorties pour décider où stocker vos résultats. (`model_folder` renvoie le dernier nom de dossier du checkpoint.)  
Je stocke toujours mes checkpoints dans un dossier avec le type de modèle comme `SD1.5`, `SDXL`, etc... Donc c'est un bon moyen de récupérer rapidement cette information.

Détails :  
- Notez qu'en comparaison avec le nœud 40, vous ne pouvez pas avoir de configuration séparée selon le checkpoint sélectionné. (Par exemple, un nœud `CLIP Set Last Layer` réglé à -2 pour un modèle spécifique, ou un vae ou clip séparé.) C'est-à-dire que tous les modèles vont partager exactement le même workflow.

Consultez le nœud numéro 40 avant de décider lequel utiliser.  
Le nœud 53 est la version boucle de ce nœud.  

### 42 - ♻ Loop (Model+Clip+Vae) - aka Checkpoint / Model

![pick input](screenshots/loop_checkpoint.png)

**Description:**  
Boucle sur tous les trios à partir de plusieurs nœuds de checkpoint.  

### 43 - 📥🖼📂 Load Images from output folder

![pick input](screenshots/load_images_folder.png)

**Description:**  
Sélectionnez rapidement toutes les images d'un dossier à l'intérieur du dossier de sortie. (Non récursif.)  
Donc... Comme vous pouvez le voir sur la capture d'écran, les images sont réparties en fonction de leur résolution.  
Il n'est pas possible de modifier dynamiquement le nombre de sorties, donc j'ai choisi un nombre : 4.  
Le nœud séparera les images en fonction de leur résolution, donc avec ce nœud, vous pouvez avoir 4 résolutions différentes par dossier. (Si vous en avez plus, vous devriez peut-être créer un autre dossier...)  
Pour éviter les erreurs ou les crashs si vous avez moins de 4 résolutions dans un dossier, le nœud générera simplement des tenseurs blancs. (une image carrée blanche.)  
Ce nœud est donc un peu bricolé pour l'instant, mais je peux sélectionner mes différents personnages en moins d'une seconde.  
Si vous voulez savoir comment je sauvegarde personnellement mes images pour un personnage spécifique, voici une partie de mon workflow (Remarquez que j'utilise personnellement / pour les dossiers car je suis sous Linux) :  
![pick input](screenshots/character_save.png)  
Dans cet exemple, j'ai mis "character/" comme chaîne et ensuite combiné avec "nothing". Mais c'est pareil si vous faites "character" et ensuite combinez avec "/". (J'aime simplement avoir un / à la fin du nom de mes dossiers...)

Si vous êtes satisfait de cette logique, vous pouvez ensuite sélectionner tous ces nœuds, faire un clic droit et `Convert to Group Node`, vous pouvez alors avoir votre propre nœud personnalisé "save character" :  
![pick input](screenshots/bjornulf_save_character_group.png)

Voici un autre exemple du même principe mais sans le nœud de sauvegarde de dossier :  
![pick input](screenshots/bjornulf_save_character_group2.png)

⚠️ Si vous souhaitez vraiment regrouper toutes les images en un seul flux, vous pouvez utiliser mon nœud 47 `Combine images` pour les rassembler.  

### 44 - 🖼👈 Select an Image, Pick

![pick input](screenshots/select_image.png)

**Description:**  
Sélectionnez une image à partir d'une liste d'images.  
Utile en combinaison avec mes nœuds Load images from folder et preview image.

Vous pouvez bien sûr créer un nœud de groupe, comme celui-ci, qui est le même que sur la capture d'écran ci-dessus :  
![pick input](screenshots/select_image_group.png)

### 45 - 🔀 If-Else (input / compare_with)

![if else](screenshots/if_0.png)


**Description:**  
Si l'`input` donné est égal à `compare_with` dans le widget, il enverra vers `send_if_true`, sinon il enverra vers `send_if_false`. (Si `send_if_false` n'est pas connecté, il renverra `None`.)  
Vous pouvez transférer n'importe quoi, ci-dessous un exemple d'envoi d'une taille d'espace latent différente en fonction de si c'est SDXL ou non.  

![if else](screenshots/if_0_1.png)

Voici un exemple du nœud avec toutes les sorties affichées à l'aide des nœuds Show text :  

![if else](screenshots/if_1.png)

`send_if_false` est optionnel, si non connecté, il sera remplacé par `None`.  

![if else](screenshots/if_2.png)

Les If-Else sont chaînables, connectez simplement `output` à `send_if_false`.  
⚠️ Testez toujours simplement `input` avec `compare_with`, et connectez la valeur désirée à `send_if_true`. ⚠️  
Voici un simple exemple avec 2 nœuds If-Else (choisir entre 3 résolutions différentes).  
❗ Remarquez que le même nœud write text est connecté aux deux entrées des nœuds If-Else :  

![if else](screenshots/if_3.png)

Prenons un exemple similaire, mais en utilisant mon nœud Write loop text pour afficher les 3 types une fois :  

![if else](screenshots/if_4.png)

Si vous avez compris les exemples précédents, voici un exemple complet qui créera 3 images : paysage, portrait et carré :  

![if else](screenshots/if_5.png)

Le workflow est caché pour plus de simplicité, mais il est très basique, connectez simplement latent à Ksampler, rien de spécial.)  
Vous pouvez également connecter le même nœud advanced loop write text avec mon nœud save folder pour enregistrer les images (paysage/portrait/carré) dans des dossiers séparés, mais faites comme vous voulez...

### 46 - 🖼🔍 Image Details

**Description:**  
Affiche les détails d'une image. (largeur, hauteur, has_transparency, orientation, type)  
`RGBA` est considéré comme ayant de la transparence, `RGB` non.  
L'`orientation` peut être `paysage`, `portrait` ou `carré`.

![image details](screenshots/image_details_1.png)

### 47 - 🖼🔗 Combine Images

**Description:**  
Combine plusieurs images (Une seule image ou une liste d'images.)  

Il existe deux logiques pour "combiner les images". Avec l'option "all_in_one" activée, toutes les images seront combinées en un seul tensor.  
Sinon, il enverra les images une par une. (voir les exemples ci-dessous) :  

Voici un exemple avec l'option "all_in_one" désactivée :  

![combine images](screenshots/combine_images_1.png)

Mais par exemple, si vous voulez utiliser mon nœud `select an image, pick`, vous devez activer "all_in_one" et les images doivent toutes avoir la même résolution.  

![combine images](screenshots/combine_images_2.png)

Vous pouvez remarquer qu'il n'y a pas de différence visible lorsque vous utilisez "all_in_one" avec le nœud preview image. (c'est pourquoi j'ai ajouté le nœud `show text`, notez que `show text` sera en bleu, car c'est une image/tensor.)  

Lorsque vous utilisez le nœud `combine image`, vous pouvez en fait envoyer plusieurs images à la fois, et elles seront toutes combinées.  
Voici un exemple avec le nœud `Load images from folder`, le nœud `Image details` et le nœud `Combine images`. (Bien sûr, "all_in_one" ne peut pas être activé dans cette situation car les images ont des résolutions différentes) :  

![combine images](screenshots/combine_images_3.png)

Voici un autre exemple simple où quelques images sélectionnées d'un dossier sont combinées (pour un traitement ultérieur par exemple) :  

![combine images](screenshots/combine_images_4.png)

### 48 - 🔀🎲 Text scrambler (🧑 Character)

![scrambler character](screenshots/scrambler_character.png)

**Description:**  
Prend du texte en entrée et mélange (randomise) le texte en utilisant le fichier `scrambler/character_scrambler.json` dans le dossier des nœuds personnalisés de ComfyUI.  

### 49 - 📹👁 Video Preview

![video preview](screenshots/video_preview.png)

**Description:**  
Ce nœud prend un chemin vidéo en entrée et affiche la vidéo.  

### 50 - 🖼➜📹 Images to Video path (tmp video)

![image to video path](screenshots/image_to_video_path.png)

**Description:**  
Ce nœud prendra une liste d'images et les convertira en un fichier vidéo temporaire.  

### 51 - 📹➜🖼 Video Path to Images

![video path to image](screenshots/video_path_to_image.png)

**Description:**  
Ce nœud prendra un chemin vidéo en entrée et le convertira en une liste d'images.  
Dans l'exemple ci-dessus, j'ai également pris la moitié des images en définissant `frame_interval` à 2.  
Notez que j'avais 16 images, et dans l'aperçu en haut à droite, vous pouvez voir 8 images.  

### 52 - 🔊📹 Audio Video Sync

**Description:**  

Ce nœud synchronisera essentiellement la durée d'un fichier audio avec un fichier vidéo en ajoutant du silence au fichier audio s'il est trop court, ou en démultipliant le fichier vidéo s'il est trop long. (La vidéo doit idéalement être en boucle, consultez mon nœud de vidéo ping-pong.)

Cela fonctionne bien par exemple avec MuseTalk <https://github.com/chaojie/ComfyUI-MuseTalk>. Si vous voulez enchaîner des vidéos (par exemple phrase par phrase), elles reviendront toujours à la dernière image. (Rendant la transition vidéo plus fluide.)

Voici un exemple sans le nœud `Audio Video Sync` (La durée de la vidéo est plus courte que l'audio, donc après lecture, elle ne reviendra pas à la dernière image. Idéalement, je voudrais avoir une boucle où la première image est la même que la dernière. -Voir mon nœud loop video ping pong si nécessaire-) :

![audio sync video](screenshots/audio_sync_video_without.png)

Voici un exemple avec le nœud `Audio Video Sync`. Notez qu'il est également pratique de récupérer les images par seconde de la vidéo et de les envoyer à d'autres nœuds. :  

![audio sync video](screenshots/audio_sync_video_with.png)

### 53 - ♻ Loop Load checkpoint (Model Selector)

![loop model selector](screenshots/loop_model_selector.png)

**Description:**  
Ceci est la version boucle du nœud 41. (consultez-le pour des détails similaires)  
Il bouclera sur tous les points de contrôle sélectionnés.

❗ La grande différence avec le nœud 41 est que les points de contrôle sont préchargés en mémoire. Vous pouvez tous les exécuter plus rapidement d'un coup.  
C'est un bon moyen de tester plusieurs points de contrôle rapidement.

### 54 - ♻ Loop Lora Selector

![loop lora selector](screenshots/loop_lora_selector.png)

**Description:**  
Boucle sur tous les Loras sélectionnés.  
Ci-dessus, un exemple avec Pony et plusieurs styles de Lora.

Ci-dessous, un autre exemple, ici avec flux, pour tester si votre entraînement Lora est sous-entraîné, surentraîné ou juste correct :  

![loop lora selector](screenshots/loop_lora_selector_flux.png)

### 55 - 🎲 Random Lora Selector

![random lora selector](screenshots/random_lora_selector.png)

**Description:**  
Prenez simplement un seul Lora au hasard dans une liste de Loras.  