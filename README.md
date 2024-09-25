This repository is a school project as a part of the subject "Projects on recent advances in Machine Learning", IMT Atlantique, France. 

It is the result of the combined efforts of : Houda Ghallab, Noé Getuirrez and Mohamed Salim Arifa.

Managed and tutored by Mr. Mohamed Lansari.
                                                    

<div align="center">
    <h1>Watermarking for Neural Networks</h1>
</div>

## Overview:
The goal was to explore different methods to embed a watermark into neural networks:

- **White-Box, Uchida et al.**: https://arxiv.org/pdf/1701.04082
- **Black-Box, Zhang et al.**: https://www.researchgate.net/profile/Zhongshu-Gu/publication/325480419_Protecting_Intellectual_Property_of_Deep_Neural_Networks_with_Watermarking/links/5c1cfcd4a6fdccfc705f2cd4/Protecting-Intellectual-Property-of-Deep-Neural-Networks-with-Watermarking.pdf
- **Additional ressources**: https://www.frontiersin.org/articles/10.3389/fdata.2021.729663/pdf

Check Presentation.pdf for a quick summary and explanation.

## Implementation:
The code aims to be as clear and readable as possible with every part explained. we use jupyter notebooks to separate codes into cells with explanations linked to each cell for an ease of access.
Throughout the code you will find #TOMOD these are lines of code that you are asked to modify in order for the code to function properly or to set the preference of the user. They are generally save paths / data directories/ coefficients etc.

Proof of concept is a simple implementation of the papers on the MNIST dataset and a very simple model. Applications on Unet contains the implementation the papers on the BRATS dataset and a 3D U-net.


## Data tainting:
Methods to add differents types of noise to training data in order to prepare the trigger set.
Tainting methods are present in the tainting_methods Modify the #TOMODS before running the cells. the code will create folders with tainted data that you can use 

--------------------------------------------
Some of the art used in the project was generously provided by : -Mohamed Attia (@pope.art)
