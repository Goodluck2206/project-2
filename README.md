# Contact Card PWA

A custom, installable "tap a button to connect" card — the dressed-up version
of the vCard QR. This is a real webpage with your own icon buttons, not the
phone's plain native contact screen.

## 1. Customize

Open `index.html`, find the `CONFIG` block near the top of the `<script>`
section, and fill in your real name, phone, email, and links. Set any link's
`url` to `""` to hide that button entirely.

## 2. Test it locally

```
cd contact-pwa
python3 -m http.server 8000
```
Open `http://localhost:8000` in your browser to preview it.

## 3. Host it (pick one, all free)

- **GitHub Pages** — push this folder to a repo, enable Pages in repo
  settings, you get a URL like `https://yourname.github.io/contact-card/`.
- **Netlify / Vercel / Cloudflare Pages** — drag-and-drop the folder in their
  dashboard, get a URL instantly, no git required.

## 4. Generate the QR code

Edit `PAGE_URL` in `generate_page_qr.py` to your real hosted URL, then:
```
pip install "qrcode[pil]" --break-system-packages
python generate_page_qr.py
```
This makes `page_qr.png` — print or share that.

## How the offline part works

- **First scan, per device**: needs internet, to download the page once.
- **Service worker** (`sw.js`) then caches the page on that device.
- **Every scan after that, on that same device**: works with zero connection.
- The big "Save Contact" button always works offline (even on first visit,
  once the page itself has loaded) — it builds a `.vcf` file entirely in the
  browser, no server involved.

If you only need the truly-offline-from-the-very-first-scan, no-server
guarantee (e.g. for strangers scanning a printed flyer), that's what the
plain vCard QR code from earlier does — this page trades a little of that
for a much nicer, fully custom look.

## Updating later

Bump `CACHE_NAME` in `sw.js` (e.g. `contact-card-v2`) whenever you change
`index.html` and re-deploy — that forces devices to fetch the fresh version
the next time they're online, instead of serving the old cached copy forever.
