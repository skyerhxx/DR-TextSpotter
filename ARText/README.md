
# ARText

ARText is the first Chinese Artistic Dataset focus on the font diversity and shape variance of characters in text spotting/text detection/text recognition. ARText consists of 33,000 Chinese artistic images (with 3,535 characters) collected from the Internet, which is randomly divided into training set (30,000 images)
and testing set (3,000 images) for model development.

<div align=center>
    <img src="../resources/ARText_examples.jpg" width="780" height="504" />
</div>



## Download

Download ARText dataset from:

https://pan.baidu.com/s/1gJtAMCnnQAh_OTrafln94Q    code: zvll



## Data Resource

We collect our ARText images all from the Internet, trying to cover a wide content range. Then we impose data cleaning manually on them, removing images with low-resolution or inappropriate content. Finally, we category these images into different types as **UGC (User Generated Content), Movies, TV series, Children, Comic, Variety Show and Documentary**.



## Annotation Details

The annotation format in ARText is similar to [ICDAR19-ReCTS](https://rrc.cvc.uab.es/?ch=12).

In each annotation, we provide text-level and character-level annotations, including the bounding boxes and the corresponding content, which can be utilized in text detection, text recognition and text spotting tasks.  

The format of the bounding box includes four corner points of the orientated bounding box. In one image, there may be multiple texts in different font size, but we only focus on the main part and ignore some small texts.  

<div align=center>
    <img src="../resources/annotation_example_img.jpg" />
</div>

<div align=center>
    <img src="../resources/annotation_example.jpg" width="816" height="185" />
</div>



## Dataset Analysis

The whole dataset includes 33, 000 images with 3,563 different kinds of Chinese characters. The dataset statistics can be seen below. 

<div align=center>
    <img src="../resources/ARText_statistics.jpg" width="816" height="185" />
</div>

We label dataset images into three categories (Simple, Medium, Hard) manually, according to the recognition difficulty standard (as described below). There are some image category examples

<div align=center>
    <img src="../resources/ARText_classification_standard.jpg" width="534" height="202" />
</div>



<img src="../resources/ARText_category_examples.jpg" style="zoom:50%;" />

Moreover, we calculate the occurrence frequency of each character in both training set and testing set. The top-30 characters are presented here, and the character frequency distribution of training and testing set basically remains the same. 

<img src="../resources/character-frequency.jpg" style="zoom:67%;" />

The text length distribution of the whole dataset is presented below. Note that there might be multiple text instances in one image, so the image counts can be larger than ARText image number.  

<div align=center>
    <img src="../resources/calculate_text_length.jpg" width="420" height="294" />
</div>




## Citation

If you find this dataset helpful, please cite:

```
@article{hao2023deformdrt,
  author = {Xixuan Hao and Aozhong Zhang and Xianze Meng and Bin Fu},
  title = {Deformation Robust Text Spotting with Geometric Prior},
  year = {2023},
  journal = {arXiv preprint arXiv:2308.16404},
}
```

