#!/usr/bin/env python3
"""
Script de test Mini-Omni pe CPU.
Forțează device=cpu și măsoară latența de inferență.
"""
import os
import sys
import time
import soundfile as sf
import torch

# Asigurăm că importurile litgpt găsesc modulele din mini-omni
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["PYTHONPATH"] = os.path.dirname(os.path.abspath(__file__))

from inference import OmniInference, download_model

DEVICE = "cpu"
CKPT_DIR = "./checkpoint"
SAMPLE_AUDIO = "./data/samples/output1.wav"
OUTPUT_FILE = "./test_output_cpu.wav"

def main():
    print(f"🖥️  Torch version: {torch.__version__}")
    print(f"🖥️  Device: {DEVICE}")
    print()

    # Descarcă modelul dacă nu există
    if not os.path.exists(CKPT_DIR):
        print(f"📥 Descărc modelul gpt-omni/mini-omni de pe HuggingFace (~4GB)...")
        download_model(CKPT_DIR)
        print("✅ Model descărcat!")
    else:
        print(f"✅ Model găsit în {CKPT_DIR}")

    # Verificăm că există un fișier audio de test
    if not os.path.exists(SAMPLE_AUDIO):
        print(f"⚠️ Fișierul de test {SAMPLE_AUDIO} nu există.")
        samples = [f for f in os.listdir("./data/samples") if f.endswith(".wav")]
        if samples:
            SAMPLE_AUDIO_USE = os.path.join("./data/samples", samples[0])
            print(f"   Folosesc: {SAMPLE_AUDIO_USE}")
        else:
            print("❌ Nu există fișiere WAV în ./data/samples/ !")
            sys.exit(1)
    else:
        SAMPLE_AUDIO_USE = SAMPLE_AUDIO

    print(f"\n🔊 Audio de intrare: {SAMPLE_AUDIO_USE}")
    print("⏳ Inițializez modelul (prima dată poate dura 1-2 min)...")

    t0 = time.time()
    model = OmniInference(ckpt_dir=CKPT_DIR, device=DEVICE)
    t_load = time.time() - t0
    print(f"✅ Model inițializat în {t_load:.1f}s\n")

    # Warm-up
    print("🔥 Warm-up (primul run e mai lent)...")
    t1 = time.time()
    audio_chunks = []
    for chunk in model.run_AT_batch_stream(SAMPLE_AUDIO_USE):
        audio_chunks.append(chunk)
    t_warmup = time.time() - t1
    print(f"⏱️ Warm-up finalizat în {t_warmup:.1f}s\n")

    # Test real
    print("🎙️ Test inferență reală...")
    t2 = time.time()
    audio_chunks = []
    for chunk in model.run_AT_batch_stream(SAMPLE_AUDIO_USE):
        audio_chunks.append(chunk)
        t_first = time.time() - t2
        if len(audio_chunks) == 1:
            print(f"   ⏱️ Primul chunk audio: {t_first:.2f}s")
    t_total = time.time() - t2
    print(f"   ⏱️ Timp total inferență: {t_total:.1f}s")
    print(f"   📦 Chunks audio generate: {len(audio_chunks)}")

    # Salvăm output-ul
    if audio_chunks:
        import numpy as np
        # audio_chunks sunt bytes (int16) conform utils/snac_utils.py
        all_bytes = b"".join(audio_chunks)
        combined = np.frombuffer(all_bytes, dtype=np.int16)
        sf.write(OUTPUT_FILE, combined, 24000)
        duration = len(combined) / 24000
        print(f"\n✅ Output salvat: {OUTPUT_FILE} ({duration:.1f}s audio)")
        print(f"   Viteză: {t_total:.1f}s pentru {duration:.1f}s audio")
    else:
        print("❌ Niciun chunk generat!")

    print("\n📊 REZUMAT:")
    print(f"   Încărcare model: {t_load:.1f}s")
    print(f"   Latență inferență: {t_total:.1f}s")


if __name__ == "__main__":
    main()
