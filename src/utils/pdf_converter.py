import os
import re
from typing import List
import fitz

from src.config.settings import PDF_IMAGES_DIR, DEFAULT_DPI


class PDFConverter:
    """Handles PDF to image conversion for display purposes."""
    
    def __init__(self):
        self.output_folder = PDF_IMAGES_DIR
    
    def convert_pdf_to_images(self, pdf_path: str, dpi: int = DEFAULT_DPI) -> List[str]:
        """Convert PDF pages to images."""
        doc = fitz.open(pdf_path)
        image_paths = []
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            
            zoom = dpi / 72  # 72 is default DPI
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat)
            
            image_path = self.output_folder / f"page_{page_num + 1}.png"
            pix.save(str(image_path))
            image_paths.append(str(image_path))
        
        doc.close()
        return image_paths
    
    @staticmethod
    def natural_sort_key(s: str):
        """Natural sorting key for file names."""
        return [int(text) if text.isdigit() else text for text in re.split(r'(\d+)', s)]
    
    def get_sorted_images(self) -> List[str]:
        """Get sorted list of image paths."""
        if not self.output_folder.exists():
            return []
        
        images = sorted(
            [f for f in self.output_folder.iterdir() if f.suffix == '.png'],
            key=lambda x: self.natural_sort_key(x.name)
        )
        return [str(img) for img in images] 