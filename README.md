# **National ID Information Extraction Using OCR**
The "National ID Extract Information Using OCR" project is an automated solution that uses Optical Character Recognition (OCR) technology to extract essential data from National ID cards. This project simplifies the extraction of information, such as the cardholder's name, date of birth, and address, from a variety of National ID cards.

The "National ID Extract Information Using OCR" project is a cutting-edge solution designed to streamline and simplify the process of extracting critical information from National ID cards. Leveraging advanced Optical Character Recognition (OCR) technology, this project offers a robust and automated approach to digitizing data from a variety of National ID cards, enhancing efficiency and accuracy in the handling of personal identification documents.


## Project Workflow

- [Loading Image](#Loading-Image-using-EasyGui)
- [Preprocssing](#Preprocessing)
- [Warping Perspective](#Warping-Perspective)
- [OCR using tesseract](#Information-Extraction-Using-Tesseract-OCR)
- [Conclusion](#Conclusion)



# Loading Image using EasyGui
Before you begin, ensure that you have the EasyGUI library installed. You can install it using pip:

```bash
pip install easygui
```
EasyGUI is a module for very simple, very easy GUI programming in Python. EasyGui provides an easy-to-use interface for simple GUI interaction with a user.      
Now, You can easily load your image using Dialog Box.


# Preprocessing
After loading the image, We need to apply some preprocessing operations to prepare our image.
These operations are:
- **RESIZE IMAGE**
- **CONVERT TO GRAYSCALE**
- **APPLY GAUSSIAN BLURRING**
- **APPLY THRESHOLODING**
- **MORPHOLOGICAL OPERATIONS**


# Warping Perspective
In this project, I apply perspective warping to the image to correct for distortions or to achieve specific visual effects. This technique involves transforming the image in such a way that it appears to have been viewed from a different perspective, creating a new, transformed version of the original image.

the process typically involves defining key points or regions in the image and specifying the desired perspective transformation. The result is a visually altered image that can be useful for various applications, such as image correction, virtual reality, or creative artwork.

For more information:
https://www.computervision.zone/courses/document-scanner


- ### Image before Warping
<img src="/Images/test_NID_1.jpg" alt="before warping" width="600" height="400">

- ### 4-Key Points
<img src="/Images/test_NID_2.jpg" alt="after Warping" width="600" height="400">

- ### Image After Warping
<img src="/Images/test_NID_3.jpg" alt="after Warping2" width="600" height="400">


# Information Extraction Using Tesseract OCR

This project leverages the power of [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for extracting text information from National ID cards. Tesseract is an open-source OCR engine developed by Google that provides accurate and efficient text recognition capabilities.

### Why Tesseract OCR?

Tesseract OCR is a well-established and widely used OCR engine known for its ability to recognize text from various image formats and complex layouts. It supports multiple languages, making it suitable for projects involving National ID cards from different regions and languages.

To ensure optimal OCR results, it is essential to configure Tesseract for your specific use case. You may need to fine-tune language settings and preprocessing steps to adapt Tesseract to the National ID card formats you are working with. Please refer to the project's documentation for details on configuring Tesseract for this project.

# Example1
## The Original Image
<img src="/Images/test_NID_4.jpg" alt="before warping" width="600" height="400">

## Image After Applying Threshold
<img src="/Images/test_NID_5.jpg" alt="before warping" width="600" height="400">

## National ID Card Information
| Index  | surname | name | sex | nationality | identity number | date | country          | status       |
|-------|-----|--------|----------|------------|-----------|---------|----------------|---------------|
| 0 | amari  | sumsub | m | rsa   | 0123456789012   | 22 jul 1980 | rsa | citizen    |


--- 

# Example1
## The Original Image
<img src="/Images/test_NID_4.jpg" alt="before warping" width="600" height="400">

## Image After Applying Threshold
<img src="/Images/test_NID_5.jpg" alt="before warping" width="600" height="400">

## National ID Card Information
| Index  | surname | name | sex | nationality | identity number | date | country          | status       |
|-------|-----|--------|----------|------------|-----------|---------|----------------|---------------|
| 0 | amari  | sumsub | m | rsa   | 0123456789012   | 22 jul 1980 | rsa | citizen    |




# Conclusion
National ID cards are crucial documents used worldwide for a wide range of purposes, including identification, access control, and official transactions. Extracting information such as the cardholder's name, date of birth, address, and other pertinent details can be a time-consuming and error-prone task when done manually. This project alleviates these challenges by automating the extraction process, making it faster, more reliable, and less prone to human error.
