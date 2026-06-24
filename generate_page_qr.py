"""
QR code generator for your hosted contact-card PWA.

1. Host the contact-pwa/ folder somewhere (GitHub Pages, Netlify, Vercel,
   Cloudflare Pages -- all have a free tier and just need you to drag the
   folder in or push it to a repo).
2. Put the resulting URL below.
3. Run:  pip install "qrcode[pil]" --break-system-packages
         python generate_page_qr.py
4. Print/share page_qr.png.

First scan on each NEW device needs internet (to download the page once).
After that, the service worker caches it, and it works with no connection
on that device from then on.
"""

import qrcode

PAGE_URL = "https://yourname.github.io/contact-card/"  # <-- put your real URL here

qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)
qr.add_data(PAGE_URL)
qr.make(fit=True)
img = qr.make_image(fill_color="#10182B", back_color="#F4EFE3")
img.save("page_qr.png")
print("Saved page_qr.png ->", PAGE_URL)
