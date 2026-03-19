
# Mini-Omni

<p align="center"><strong style="font-size: 18px;">
Mini-Omni: Language Models Can Hear, Talk While Thinking in Streaming
</strong>
</p>

<p align="center">
🤗 <a href="https://huggingface.co/gpt-omni/mini-omni">Hugging Face</a>   | 📖 <a href="https://github.com/gpt-omni/mini-omni">Github</a> 
|     📑 <a href="https://arxiv.org/abs/2408.16725">Technical report</a> |
🤗 <a href="https://huggingface.co/datasets/gpt-omni/VoiceAssistant-400K">Datasets</a>
</p>

Mini-Omni is an open-source multimodal large language model that can **hear, talk while thinking**. Featuring real-time end-to-end speech input and **streaming audio output** conversational capabilities.

<p align="center">
    <img src="data/figures/frameworkv3.jpg" width="100%"/>
</p>


## Updates

- **2024.10:** We released [Mini-Omni2](https://github.com/gpt-omni/mini-omni2) with vision and audio capabilities. 
- **2024.09:** Amazing online [interactive gradio demo](https://huggingface.co/spaces/gradio/omni-mini) by 🤗 gradio team.
- **2024.09:** **VoiceAssistant-400K** is uploaded to [Hugging Face](https://huggingface.co/datasets/gpt-omni/VoiceAssistant-400K).

## Features

✅ **Real-time speech-to-speech** conversational capabilities. No extra ASR or TTS models required.

✅ **Talking while thinking**, with the ability to generate text and audio at the same time.

✅ **Streaming audio output** capabilities.

✅ With "Audio-to-Text" and "Audio-to-Audio" **batch inference** to further boost the performance.

## Demo

NOTE: need to unmute first.

https://github.com/user-attachments/assets/03bdde05-9514-4748-b527-003bea57f118


## Install

Create a new conda environment and install the required packages:

```sh
conda create -n omni python=3.10
conda activate omni

git clone https://github.com/gpt-omni/mini-omni.git
cd mini-omni
pip install -r requirements.txt
```

## Quick start / Pornire rapidă

**1. Start Server / Pornire Server**

You need to start the server before running the streamlit or gradio demo.
Trebuie să pornești serverul înainte de a rula demo-ul Streamlit sau Gradio.

```sh
# Activate virtual environment / Activare mediu virtual
source venv/bin/activate

# Run on GPU (Recommended) / Rulare pe GPU (Recomandat)
python3 server.py --ip '0.0.0.0' --port 60808 --device cuda:0

# OR Run on CPU / SAU Rulare pe CPU
python3 server.py --ip '0.0.0.0' --port 60808 --device cpu
```

**2. Run Web UI / Rulare Interfață Web**

Choose one of the interfaces below / Alege una dintre interfețele de mai jos:

- **Streamlit Demo (Recommended / Recomandat)**
```sh
source venv/bin/activate
export PYTHONPATH=./
API_URL=http://0.0.0.0:60808/chat streamlit run webui/omni_streamlit.py
```

- **Gradio Demo**
```sh
source venv/bin/activate
export PYTHONPATH=./
API_URL=http://0.0.0.0:60808/chat python3 webui/omni_gradio.py
```

example:

NOTE: need to unmute first. Gradio seems can not play audio stream instantly, so the latency feels a bit longer.

https://github.com/user-attachments/assets/29187680-4c42-47ff-b352-f0ea333496d9


**Local test**

```sh
conda activate omni
cd mini-omni
# test run the preset audio samples and questions
python inference.py
```

## FAQ

**1. Does the model support other languages?**

No, the model is only trained on English. However, as we use whisper as the audio encoder, the model can understand other languages which is supported by whisper (like chinese), but the output is only in English.

**2. What is `post_adapter` in the code? does the open-source version support tts-adapter?**

The `post_adapter` is `tts-adapter` in the model.py, but the open-source version does not support `tts-adapter`.

**3. Error: `ModuleNotFoundError: No module named 'utils.xxxx'`**

Run `export PYTHONPATH=./` first. No need to run `pip install utils`, or just try: `pip uninstall utils`

**4. Error: can not run streamlit in local browser, with remote streamlit server**, issue: https://github.com/gpt-omni/mini-omni/issues/37
    
You need start streamlit **locally** with PyAudio installed.


## Acknowledgements 

- [Qwen2](https://github.com/QwenLM/Qwen2/) as the LLM backbone.
- [litGPT](https://github.com/Lightning-AI/litgpt/) for training and inference.
- [whisper](https://github.com/openai/whisper/)  for audio encoding.
- [snac](https://github.com/hubertsiuzdak/snac/)  for audio decoding.
- [CosyVoice](https://github.com/FunAudioLLM/CosyVoice) for generating synthetic speech.
- [OpenOrca](https://huggingface.co/datasets/Open-Orca/OpenOrca) and [MOSS](https://github.com/OpenMOSS/MOSS/tree/main) for alignment.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=gpt-omni/mini-omni&type=Date)](https://star-history.com/#gpt-omni/mini-omni&Date)
