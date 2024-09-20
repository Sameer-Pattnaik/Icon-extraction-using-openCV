## Documentation for Icon Extraction Script

### Overview
This Python script extracts icons from an image (`Equity Portfolio.png`) by applying image processing techniques using OpenCV. It converts the image to grayscale, applies thresholding, detects contours, and filters rectangular shapes (representing icons) based on aspect ratios. Each extracted icon is saved as an image file, and the details of the extracted icons are saved in a JSON file.

### Dependencies
Ensure you have the following dependencies installed:
- OpenCV: `cv2`
- NumPy: `numpy`

You can install these packages using pip:
```bash
pip install opencv-python numpy
```

### Code Walkthrough

1. **Image Loading**: 
   The image `Equity Portfolio.png` is loaded using OpenCV's `cv2.imread()` function.
   ```python
   image = cv2.imread('Equity Portfolio.png')
   ```

2. **Grayscale Conversion**: 
   The loaded image is converted to grayscale for easier processing and thresholding.
   ```python
   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   ```

3. **Thresholding**: 
   Otsu's binarization is applied to the grayscale image to create a binary (black-and-white) version of the image, which helps in segmenting the icons from the background.
   ```python
   _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
   ```

4. **Contour Detection**: 
   Contours (edges of shapes in the image) are detected from the thresholded image using the `cv2.findContours()` function. These contours are used to find the bounding rectangles of the icons.
   ```python
   contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
   ```

5. **Icon Extraction**: 
   The contours are iterated over, and for each contour, a bounding rectangle is created using `cv2.boundingRect()`. Icons are extracted if they meet an aspect ratio criterion (to filter out non-rectangular shapes). The extracted icons are saved as separate image files.
   ```python
   for contour in contours:
       x, y, w, h = cv2.boundingRect(contour)
       aspect_ratio = float(w)/h
       if aspect_ratio > 0.5 and aspect_ratio < 2.0:
           icon = image[y:y+h, x:x+w]
           icon_path = f'icon_{len(icons)+1}.png'
           cv2.imwrite(icon_path, icon)
           icons.append({'image_path': icon_path, 'bounds': [x, y, w, h]})
   ```

6. **JSON Output**: 
   Details of the extracted icons, such as the file path and bounding box coordinates (`x`, `y`, `width`, `height`), are saved in a JSON file named `icons.json`.
   ```python
   with open('icons.json', 'w') as f:
       json.dump(icons, f, indent=4)
   ```

7. **Completion Message**: 
   A message is printed indicating that the icons have been extracted and saved.
   ```python
   print('Icons extracted and saved to icons.json')
   ```

### JSON Structure
The resulting `icons.json` file contains details of each extracted icon:
```json
[
    {
        "image_path": "icon_1.png",
        "bounds": [x, y, width, height]
    },
    {
        "image_path": "icon_2.png",
        "bounds": [x, y, width, height]
    }
]
```
Each entry represents an icon, with its saved image path and bounding box coordinates.

### Key Functions
- **`cv2.imread()`**: Loads an image from a file.
- **`cv2.cvtColor()`**: Converts an image from one color space to another.
- **`cv2.threshold()`**: Applies a threshold to an image to convert it to binary.
- **`cv2.findContours()`**: Finds contours in a binary image.
- **`cv2.boundingRect()`**: Calculates the bounding rectangle for a contour.
- **`cv2.imwrite()`**: Saves an image to a file.

### Use Cases
This script is useful for:
- Automatically detecting and extracting icons or symbols from an image.
- Saving the extracted icons for further analysis or use in another application.

### Customization
- **Aspect Ratio Filtering**: You can adjust the aspect ratio threshold to target specific types of shapes.
- **File Paths**: Modify the file paths for the input image or the saved icon images as needed.

### Output Files
1. Extracted icons as `.png` files.
2. A `icons.json` file containing metadata for the icons (file paths and bounding box coordinates).

This script helps in automating the extraction of icons from images, making it a useful tool for image processing tasks.
