# Colorizer
# Image Colorizer using GANs

A deep learning application that colorizes grayscale images using Generative Adversarial Networks (GANs) with a U-Net generator and PatchGAN discriminator.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![PyTorch](https://img.shields.io/badge/PyTorch-1.9+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Overview

This project implements an automatic image colorization system using conditional GANs. The model takes grayscale (L channel) images as input and predicts the color channels (ab channels) in the LAB color space, producing realistic colorized images.

## Features

- **GAN-based Architecture**: Uses U-Net generator with ResNet18 backbone and PatchGAN discriminator
- **User-friendly GUI**: Built with Tkinter for easy image selection and visualization
- **Pre-trained Models**: Includes pre-trained weights for immediate use
- **Save Functionality**: Export colorized images in various formats

## Architecture

### Generator
- **Base Model**: ResNet18 + U-Net (DynamicUnet from fastai)
- **Input**: Grayscale image (L channel, 1 channel)
- **Output**: Color channels (ab channels, 2 channels)
- **Image Size**: 256x256 pixels

### Discriminator
- **Type**: PatchGAN (70x70 patches)
- **Input**: 3-channel concatenated image (L + ab)
- **Layers**: 3 downsampling layers with batch normalization

### Loss Functions
- **Generator Loss**: Combination of adversarial loss (BCE) and L1 loss
  - L1 loss weight (lambda): 100
- **Discriminator Loss**: Binary cross-entropy for real/fake classification

## Requirements

```
python>=3.8
torch>=1.9.0
torchvision>=0.10.0
fastai==2.4
numpy
pillow
matplotlib
scikit-image
tqdm
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/image-colorizer.git
cd image-colorizer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download pre-trained weights:
   - Due to file size limitations, pre-trained model weights are not included in this repository
   - Contact: vishnutalwar02@gmail.com to request the weight files:
     - `colorizer.pt` (pre-trained generator)
     - `final_model_weights_2.pt` (final GAN model)
   - Place the weight files in the project root directory

## Project Structure

```
image-colorizer/
│
├── backend.py              # Core model architecture and training code
├── file_ui.py             # Initial UI for image selection
├── file_ui_2.py           # Results display UI
├── file1.py               # Threading utilities for progress bar
│
├── colorizer.pt           # Pre-trained generator weights (not included)
├── final_model_weights_2.pt  # Final model weights (not included)
├── wheel.ico              # Application icon
│
├── unlabeled2017_subsample/  # Training data directory (not included)
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## Usage

### Running the Application

1. Start the application:
```bash
python backend.py
```

2. The GUI will open with two steps:
   - **Step 1**: Select a grayscale or color image using the Browse button
   - **Step 2**: View the original and colorized images side by side

3. Save the colorized image using the "Save As" button

### Training Your Own Model

If you want to train the model from scratch:

1. Prepare your dataset in the `unlabeled2017_subsample/` directory
2. Uncomment the training code in `backend.py`
3. Run the training:
```bash
python backend.py
```

Training parameters:
- Batch size: 16
- Image size: 256x256
- Learning rate (G): 2e-4
- Learning rate (D): 2e-4
- Beta1: 0.5
- Beta2: 0.999
- Lambda L1: 100

## Dataset

The model was trained on a subset of the COCO 2017 dataset (unlabeled images). For training your own model:

- Dataset size: 10,000 images
- Train/Val split: 8,000/2,000
- Image preprocessing: Resize to 256x256, random horizontal flip

**Note**: Training data is not included due to size constraints. Contact vishnutalwar02@gmail.com for sample data or use your own dataset.

## Model Performance

The model converts images from RGB to LAB color space, predicts the ab channels, and reconstructs the full color image. Results show realistic colorization for various image types including landscapes, objects, and scenes.

## Technical Details

### Color Space
- Input: LAB color space (L channel only)
- Output: LAB color space (ab channels)
- Conversion: Automatic RGB ↔ LAB conversion

### Normalization
- L channel: Normalized to [-1, 1] from [0, 100]
- ab channels: Normalized to [-1, 1] from [-110, 110]

## Known Limitations

- Works best with 256x256 images (automatically resized)
- May struggle with unusual color combinations
- Requires GPU for reasonable inference speed (CPU supported but slower)

## Future Improvements

- [ ] Add support for batch processing
- [ ] Implement video colorization
- [ ] Add multiple model checkpoints
- [ ] Improve GUI with real-time preview
- [ ] Add color adjustment controls

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Model architecture inspired by pix2pix and U-Net papers
- Built using PyTorch and fastai frameworks
- GUI built with Tkinter

## Contact

For pre-trained weights, training samples, or questions:
- Email: vishnutalwar02@gmail.com

## Citation

If you use this project in your research, please cite:

```bibtex
@software{image_colorizer,
  author = {Vishnu Talwar},
  title = {Image Colorizer using GANs},
  year = {2025},
  url = {https://github.com/yourusername/image-colorizer}
}
```

## References

- [Image-to-Image Translation with Conditional Adversarial Networks (pix2pix)](https://arxiv.org/abs/1611.07004)
- [U-Net: Convolutional Networks for Biomedical Image Segmentation](https://arxiv.org/abs/1505.04597)
- [Colorful Image Colorization](https://arxiv.org/abs/1603.08511)
