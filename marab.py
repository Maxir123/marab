import os
try:
    import pymupdf as fitz
except ImportError:
    import fitz

# Resolve PDF path (check current folder, then wood-site folder)
pdf_path = "MERAB PROFILE 1.pdf"
if not os.path.exists(pdf_path):
    pdf_path = os.path.join("wood-site", "MERAB PROFILE 1.pdf")

if not os.path.exists(pdf_path):
    raise FileNotFoundError(f"Could not find PDF file at '{pdf_path}'")

print(f"Reading: {pdf_path}")
d = fitz.open(pdf_path)

os.makedirs("extract/images", exist_ok=True)
os.makedirs("extract/pages", exist_ok=True)

print(f"Total pages: {len(d)}")
for i, p in enumerate(d, 1):
    p.get_pixmap(dpi=60).save(f"extract/pages/page_{i:02d}.png")
    for n, x in enumerate(p.get_images(full=True), 1):
        pix = fitz.Pixmap(d, x[0])
        if pix.width < 400 or pix.height < 300:
            continue
        if pix.n - pix.alpha >= 4:
            pix = fitz.Pixmap(fitz.csRGB, pix)
        pix.save(f"extract/images/p{i:02d}_{n}.png")

print("Done! Extracted pages and images into 'extract/' directory.")
