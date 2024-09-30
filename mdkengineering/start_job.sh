#!bin/bash/ -l

#$ -P ds549

#$ -l h_rt=240:00:00

#$ -N WikiDocSpider

#$ -l mem_per_core=28
#$ -pe omp 32
#$ -l cpu_arch=icelake
#$ -l cpu_type=X8358

#$ -m ea
#$ -M wycheng@bu.edu

module load python3


python3 -m pip install bs4
python3 -m pip install google-cloud-storage
python3 -m pip install google-cloud-logging
python3 -m pip install scrapy

scrapy crawl wikiDocSpider
