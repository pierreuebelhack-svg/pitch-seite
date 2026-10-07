# Baut den Upload-Ordner aus index.html: nur genutzte Medien, Link-Vorschau (og:) für LinkedIn & Co., optional GoatCounter.
# Aufruf: python3 bauen.py <öffentliche-url> [goatcounter-name]
#   z. B. python3 bauen.py https://mein-format.netlify.app meinkonto
import re, os, shutil, sys
W = os.path.dirname(os.path.abspath(__file__)); Z = os.path.join(W, '_upload')
URL = (sys.argv[1] if len(sys.argv) > 1 else '').rstrip('/')
gc = sys.argv[2] if len(sys.argv) > 2 else ''
html = open(os.path.join(W, 'index.html'), encoding='utf-8').read()
# Platzhalter-Bilder ohne Datei entfernen (vermeidet Fehlabrufe)
html = re.sub(r'<img [^>]*src="((?:clips|bilder)/[^"]+)"[^>]*>', lambda m: m.group(0) if os.path.exists(os.path.join(W, m.group(1))) else '', html)
dateien = sorted(set(d for d in re.findall(r'(?:clips|bilder)/[A-Za-z0-9_.-]+\.(?:mp4|jpg|jpeg|png|webp)', html) if os.path.exists(os.path.join(W, d))))
if os.path.isdir(Z): shutil.rmtree(Z, ignore_errors=True)
os.makedirs(Z, exist_ok=True)
for d in dateien:
    os.makedirs(os.path.join(Z, os.path.dirname(d)), exist_ok=True); shutil.copyfile(os.path.join(W, d), os.path.join(Z, d))
meta = ''
titel = re.search(r'<title>(.*?)</title>', html).group(1)
m = re.search(r'<p class="logline">(.*?)</p>', html, re.S); beschreibung = re.sub('<[^>]+>', '', m.group(1)).strip() if m else ''
bild = next((d for d in dateien if d.endswith(('.jpg', '.jpeg', '.png'))), '')
if URL:
    vorschau = ''
    if bild:
        try:
            from PIL import Image  # Vorschaubild 1200 x 627
            im = Image.open(os.path.join(W, bild)).convert('RGB'); z = 1200 / im.width
            im = im.resize((1200, round(im.height * z))); o = max(0, (im.height - 627) // 2)
            im.crop((0, o, 1200, o + 627)).save(os.path.join(Z, 'vorschau.jpg'), quality=86); vorschau = 'vorschau.jpg'
        except ImportError:
            vorschau = bild
    meta += ('<meta property="og:type" content="website">\n<meta property="og:url" content="%s/">\n'
             '<meta property="og:title" content="%s">\n<meta property="og:description" content="%s">\n'
             '<meta name="description" content="%s">\n<meta name="twitter:card" content="summary_large_image">\n'
             % (URL, titel, beschreibung, beschreibung))
    if vorschau: meta += '<meta property="og:image" content="%s/%s">\n' % (URL, vorschau)
if gc:
    meta += '<script data-goatcounter="https://%s.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>\n' % gc
open(os.path.join(Z, 'index.html'), 'w', encoding='utf-8').write(html.replace('</head>', meta + '</head>', 1))
for r, _, fs in os.walk(Z):
    for f in fs:
        if f.startswith('._'): os.remove(os.path.join(r, f))
print(len(dateien), 'Medien ->', Z, '| Vorschau:', 'ja' if URL else 'nein (keine URL)', '| Zähler:', gc or 'aus')
