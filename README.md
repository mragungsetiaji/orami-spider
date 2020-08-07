# orami-spider
Spider for crawl orami product

This code used the specific category on orami. I choose **takoyakids** as example. This code may not works for other category.

## Installation

Install core library in your env:
```python
pip install scrapy==2.3.0
```

## How to use
Run the following command on terminal:
```bash
scrapy crawl spider
```

This command will generate csv output with name *spider.csv". If open it with pandas you will get like shown below:

```bash
(py38) ➜ orami-spider git:(master) ✗ python
Python 3.8.3 (default, Jul  2 2020, 11:26:31) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> pd.set_option('display.max_columns', None)
>>> pd.read_csv("spider.csv").head()
                                                 url  \
0  https://www.orami.co.id/takoyakids-petra-vest-...   
1  https://www.orami.co.id/takoyakids-remi-harem-...   
2  https://www.orami.co.id/takoyakids-aoki-pyjama...   
3  https://www.orami.co.id/takoyakids-naomi-chain...   
4  https://www.orami.co.id/coco-comfy-sheep-set-b...   

                                           title       price      seller  \
0           Takoyakids Petra Vest Girl Sets Navy  Rp 139.000  Takoyakids   
1               Takoyakids Remi Jumpsuit Mustard   Rp 95.000  Takoyakids   
2  Takoyakids Aoki Pyjama Sets Mustard 4-5 Years  Rp 129.000  Takoyakids   
3         Takoyakids Naomi Chain Girl Dress Navy         NaN  Takoyakids   
4           Takoyakids Comfy Sheep Set Boys Mint   Rp 89.000  Takoyakids   

                                           highlight  
0  . Set Vest dan Celana Pendek ( +inner). \r \r ...  
1  . Yuk  lengkapi koleksi pakaian buah hati Anda...  
2  . Yuk  lengkapi koleksi pakaian buah hati Anda...  
3  . Dress. \r \r . Bermotif. \r \r . Detail pita...  
4  . Pakaian . Takoyakids . sangat adem dan nyama...
```

