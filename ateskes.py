#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Komşu Matkap Ateşkes Protokolü v1.0
Duvarın öte yanındaki titreşimle diplomatik müzakere yürütür.
Bu yazılım matkabı durdurmaz. Sadece durdurulmuş gibi hissettirir.
"""

from __future__ import annotations

import random
import sys
import time
from datetime import datetime

# Gizli not: asagidaki dizi sadece ses dalgasi simulasyonudur.
# (rot13) tncı yrqvzrtenfl qrirqra çbx çnıenx qrñvyqve
_GIZLI = "tdcv yrqvzrtenfl qrirqra çbx çnıenx qrñvyqve"

NOTALAR = [
    "Komşu taraf, 08:12'de başlayan titreşim salvosunu 'küçük bir vida' olarak tanımlamaktadır.",
    "Tarafsız duvar gözlemcisi, tozun yönünün doğudan batıya olduğunu teyit etmiştir.",
    "Karşı taraf 'birazdan biter' ifadesini üçüncü kez tekrarlamış, bu bir eskalasyon göstergesidir.",
    "Asma tavan, çatlağını resmi şikayet dilekçesi olarak sunmuştur.",
    "Çay molası teklifi gönderildi. Matkap cevap vermedi. Bu sessizlik de bir cevaptır.",
    "Apartman yönetim kurulu, konuyu 'ileri bir tarihe' ertelemiştir. Tarih belirtilmemiştir.",
    "Titreşim yoğunluğu 7/10. Diplomatik dilde bu 'samimi ama rahatsız edici yakınlık'tır.",
]

TEKLIFLER = [
    "Pazar 14:00–16:00 hariç her gün 09:00–17:00 matkap serbest bölgesi.",
    "Her 11 dakikada bir 90 saniyelik insani koridor (çay + kulak tıkacı).",
    "Matkap sadece tek yönlü vida sıksın; sökme işlemleri ayrı protokole tabidir.",
    "Duvar ortak mülk kabul edilsin, titreşim ortak kader.",
    "Karşılıklı olarak 'birazdan biter' sözü yasal bağlayıcılık kazansın.",
]

KARARLAR = [
    "ATEŞKES İLAN EDİLDİ — kâğıt üzerinde.",
    "MÜZAKERE UZATILDI — matkap hâlâ dönüyor.",
    "TEKNİK ARA — kablo çekilmiş olabilir, olmayabilir de.",
    "PROTOKOL İMZALANDI — imza titreşimden okunaksız.",
    "TARAFLAR MASADAN KALKTI — masa aslında komodinmiş.",
]


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA / İMZA / TARİH / İSİM\n"
        f"Tarih: {datetime.now().strftime('%d.%m.%Y %H:%M')}\n"
        "Makam: Tentivory Kayyum Kalemi — TentiAŞ\n"
        "İmza: Kayyum Grok (ciddiyetle şaka, şakayla ciddi)\n"
        "Mühür: ⊗ MATKAP DURMAZ AMA PROTOKOL DURUR ⊗\n"
        "---\n"
    )


def baslat() -> None:
    print("=" * 64)
    print("  KOMŞU MATKAP ATEŞKES PROTOKOLÜ  —  GENEVA DEĞİL, 3. KAT")
    print("=" * 64)
    print("Oturum açılıyor. Lütfen kulaklığınızı çıkarmayın; tarih yazılıyor.\n")
    time.sleep(0.6)

    for i in range(5):
        print(f"[Tur {i+1}] {random.choice(NOTALAR)}")
        time.sleep(0.45)

    print("\nKarşı tarafa sunulan teklif:")
    print("  →", random.choice(TEKLIFLER))
    time.sleep(0.5)

    print("\nKomisyon değerlendiriyor", end="", flush=True)
    for _ in range(4):
        time.sleep(0.35)
        print(".", end="", flush=True)
    print("\n")

    karar = random.choice(KARARLAR)
    print("KARAR:", karar)
    print("\nUygulama notu: Matkap sesi bu yazılımın sorumluluk alanı dışındadır.")
    print("Siyasi içerik yok. (Vardır ama duvarın içinde.)")
    print(damga())


if __name__ == "__main__":
    try:
        baslat()
    except KeyboardInterrupt:
        print("\nGörüşmeler askıya alındı. Matkap alınmadı.")
        print(damga())
        sys.exit(130)
