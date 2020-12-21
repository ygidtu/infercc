<template>
    <div>
        <el-row :gutter="20">
            <h2>Methods</h2>
            <el-row :gutter="20" v-for="m in methods" :key="m.title">
                <el-col :span="24">
                    <el-card >
                        <div slot="header" class="clearfix">
                            <h4>{{ m.title }}</h4>
                        </div>
                        <div style="padding: 14px;">
                            <div v-for="v in m.content" :key=v style="padding: 14px;" v-html="v" />
                        </div>
                    </el-card>
                </el-col>
            </el-row>

            <h2>User guide</h2>
            <el-row :gutter="20" v-for="key in images" :key="key.img">
                <el-col :span="24">
                    <el-card :body-style="{ padding: '0px' }">
                        <el-image :src="key.img" class="image" style="width: 80%"/>
                        <div v-for="v in key.desc" :key=v style="padding: 14px;">
                            {{ v }}
                        </div>
                    </el-card>
                </el-col>
            </el-row>

            <el-divider>Example</el-divider>
            <el-row :gutter="20">
                <el-col :span="24">
                    <el-card :body-style="{ padding: '0px' }" v-for="e in example" :key="e.img">
                        <div v-if="e.title !== ''" slot="header" class="clearfix">
                        <h4>{{ e.title }}</h4>
                    </div>
                    <div style="padding: 14px;">
                        <el-image :src="e.img" style="width:50%" />
                        <div v-for="v in e.desc" :key=v style="padding: 14px;" v-html="v" />
                    </div>
                    </el-card>
                </el-col>
            </el-row>
            <el-divider />
            <h2>Code availability</h2>
            <el-row :gutter="20">
                <el-col :span="24">
                    <el-card >
                        Github repo: <el-link type="primary" href="https://github.com/ygidtu/infercc">ygidtu/infercc</el-link>
                    </el-card>
                </el-col>
            </el-row>
            <el-divider />
            <h2>Reference</h2>
            <el-row :gutter="20" >
                <el-col :span="24">
                    <el-card >
                        <div style="padding: 14px;">
                            <ol>
                                <li v-for="ref in reference" :key="ref">
                                    {{ ref }}
                                </li>
                            </ol>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </el-row>
    </div>
</template>

<script>
    import urls from '../utils/const'
    export default {
        name: "Home",
        data () {
            return {
                images: [
                    {
                        img: urls.static + "/infercc_01.png",
                        desc: [
                            "We provide multiple deconvolution algorithms for human and mouse. First, Users could select the species and tissues corresponding to their expression matrix. Then, users could choose which software to run through the 3rd dropdown selector. By selecting the tau value, user could customized the different sets of cell type-specific genes to use. Finally, click on the “upload” button, to upload a raw expression matrix in csv format. The first column of csv file should be official gene symbol, and first row should be the sample id. An example file could be download by click the example button. Once click on create button, a task universally unique identifier (UUID) will return, please carefully keep the UUID to retrieve results."
                        ]
                    },
                    {
                        img: urls.static + "/infercc_02.png",
                        desc: [
                            "This query tab is used to query task status, and download results file and running log. Once task is finished, the result files e.g. dtangle.csv and music.csv will listed at bottom. Users could retrieve these files by click on the download links. The result file format were displayed on the right. If users have any issue with webservice usage please feel free to contact with us, and UUID and running log will be required."
                        ]
                    },
                    {
                        img: urls.static + "/composition.svg",
                        desc: [
                            "Line plots showed the cell composition of 17 cells deconvoluted from different sources of bulk RNA-seq. The correlations were calculated using Pearson correlation."
                        ]
                    },
                ],
                methods: [
                    {
                        title: "Pipeline",
                        description: "Overview of the inferCC workflow.",
                        content: [
                            '<img src="static/infercc.svg" class="el-image__inner">',
                            'For user-provided or public bulk RNA-seq, we processed (a) the GTEx cohort including 11688 samples from 53 healthy human tissues, (b) 10,486 tumor samples from TCGA and published RNA-seq of cancerous samples, (c) 49 NSCLC patients from WCH, (d) 260 samples of Each asians LUAD patients, (e) 427 samples from chinese NSCLC patients, (f) 553 mouse samples from 18 tissues and 14 developmental stages. We next identified cell-type specific signatures from public scRNA-seq including the Human Cell Atlas with 599,926 cells from 52 tissues, the Mouse Cell Atlas with 405,796 cells from 51 tissues and Tabula muris with 100,605 cells from 20 mouse organs. Next, we provide robust estimation of the relative cellular fractions using multiple state-of-the-art algorithms (such as MuSiC or dtangle). The resulted cellular compositions were used for follow-up analyses including the clustering, classification based on machine learning methods, and association with patient survival.'
                        ]
                    },
                    {
                        title: "Integrations of public datasets",
                        description: "Single cell RNA-seq Datasets",
                        content: [
                            'The Human Cell Atlas with 599,926 cells from 52 tissues (Han et al., 2020)',
                            'The Mouse Cell Atlas with 405,796 cells from 51 tissues (Han et al., 2018)',
                            'The Tabula muris with 100,605 cells from 20 mouse organs (Tabula Muris et al., 2018)'
                        ]
                    },
                    {
                        title: "",
                        description: "Bulk RNA-seq Datasets.",
                        content: [
                            "<h4>Human:</h4>",
                            '•	GTEx. The raw counts of normal tissue (release v7) were downloaded from the GTEx portal (https://gtexportal.org/home/) (Carithers et al., 2015). ', 
                            '•	TCGA',
                            '•	East Asians of lung cancer. The raw counts of East Asians (n = 260) were downloaded from OncoSG (https://src.gisapps.org/OncoSG_public/datasets) under data set “Lung Adenocarcinoma (GIS, 2019)”(Chen et al., 2020).',
                            '•	CHOICE of lung cancer. The RNA-seq FPKM data from CHOICE (n = 427) were retrieved from figureshare (https://doi.org/10.6084/m9.figshare.7306364.v1) (Zhang et al., 2019).',
                            "<h4>Mouse:</h4>",
                            "All samples were retrieved from NCBI-SRA (https://www.ncbi.nlm.nih.gov/sra/) ",
                            "including:",
                            '•	Samples of Embryonic heart from project PRJDB5724 (Umemura et al., 2017).',
                            '•	Samples of 7 organs (brain, cerebellum, heart, kidney, liver, ovary and testis) from embryonic day 10.5 to adulthood from project PRJEB26869 (Cardoso-Moreira et al., 2019).',
                            '•	Samples of whole testis from juvenile mice between post-natal day 6 and 35 from project PRJEB27404 (Ernst et al., 2019)',
                            '•	Circadian samples of mouse tissue from project PRJNA237293 (Zhang et al., 2014).',
                            '•	Samples of 12 organs from PRJNA143627 (Brawand et al., 2011), PRJNA381064 (Marin et al., 2017), PRJNA176589 (Barbosa-Morais et al., 2012), PRJNA177791 (Merkin et al., 2012), PRJNA186646 (Necsulea et al., 2014), and PRJNA470431 (Carelli et al., 2018).'
                        ]
                    },
                    {
                      title:"Identification of cell-type specific genes from scRNA-seq.",
                      content: [
                          "For each scRNA-seq dataset, the matrix of log2 transformed raw reads count of scRNA-seq were used to calculate the specificity index (tau value) for each gene. Cell type-specific index tau was defined previously (Yanai et al., 2005) as:",
                          '<img src="static/math.png" class="el-image__inner" style="width: 100px">',
                          "Where N is the number of cell types, and xi is the target gene expression of cell type i normalized by the maximal normalized expression value of all cell types. We considered that those genes with tau > 0.9 as highly cell type-specific genes. Then, those genes combined with our cell markers was used as a reference"
                      ]
                    },
                    {
                        title: "Deconvolution",
                        content: [
                            'A deconvolution algorithm from MuSiC (v0.1.1) (Wang et al., 2019) was used to evaluate the proportion of different cell types in each sample. And the similar cell composition was retrieved based on dtangle (v0.3.1) (Hunt et al., 2019) results.'
                        ]
                    },
                    {
                        title: "Cellular composition estimation.",
                        content: [
                            'To estimate the cellular composition robustly, we utilized two deconvolution algorithms based on  MuSiC (v0.1.1) (Wang et al., 2019a) and dtangle (v0.3.1) (Hunt et al., 2019). We found the results were comparable. For example, a user-provided bulk RNA-seq from healthy human tissue will be deconvoluted based on single cell signatures from human cell atlas. We are also incorporating more scRNA-seq from tumor and are planning to build tumor-specific signatures. Other deconvolution methods will be further added to increase the robustness.'
                        ]
                    },
                    {
                        title: "Clustering module",
                        content: [
                            'To conduct the cell compositions comparison between different samples, we correlated the calculated cellular composition using the Pearson correlation. The correlation coefficients were then used to cluster with other relevant samples. For example, a user-provided bulk RNA-seq from healthy human tissue can be clustered with the results from GTEx.'
                        ]
                    },
                    {
                        title: "Classification based on Machine learning and association with patient survival.",
                        content: [
                            'Given each tissue or cancer type/subtype has its cellular compositions, we used the large cohorts bulk RNA-seq to train our machine learning model such as SVM from scikit-learn (v0.22.2) (Pedregosa et al., 2011), aiming to classify the tissue or cancer type/subtype. In non-small cell lung cancer (NSCLC), we found that cellular compositions were highly consistent despite different sources (Pearson correlation > 0.8). Notably, this information can distinguish two subtypes of NSCLC, namely lung adenocarcinoma and squamous carcinoma and the adjacent healthy tissue. Lastly, we adapted machine learning methods that (a) classify the user-provided sample as a high or low concordance with the cell type or tissue of interest, and (b) distinguish the cancer subtypes (with an accuracy of AUC = 0.89 in NSCLC), and (c) associate the patient groups with a certain high cellular composition with patient survival through TCGABiolinks (Colaprico et al., 2016; Mounir et al., 2019). For survival analyses, the Log-rank test was used to determine the differences between Kaplan-Meier survival curves. P < 0.05 was considered statistically significant. All statistical analyses were performed using R (v3.6.0).'
                        ]
                    }
                ],
                reference: [
                    'Barbosa-Morais, N. L., Irimia, M., Pan, Q., Xiong, H. Y., Gueroussov, S., Lee, L. J., Slobodeniuc, V., Kutter, C., Watt, S., Çolak, R., et al. (2012). The Evolutionary Landscape of Alternative Splicing in Vertebrate Species. Science 338, 1587.',
                    'Brawand, D., Soumillon, M., Necsulea, A., Julien, P., Csárdi, G., Harrigan, P., Weier, M., Liechti, A., Aximu-Petri, A., Kircher, M., et al. (2011). The evolution of gene expression levels in mammalian organs. Nature 478, 343.',
                    'Cardoso-Moreira, M., Halbert, J., Valloton, D., Velten, B., Chen, C., Shao, Y., Liechti, A., Ascenção, K., Rummel, C., Ovchinnikova, S., et al. (2019). Gene expression across mammalian organ development. Nature 571, 505-509.',
                    'Carelli, F. N., Liechti, A., Halbert, J., Warnefors, M., and Kaessmann, H. (2018). Repurposing of promoters and enhancers during mammalian evolution. Nat Commun 9, 4066.',
                    'Carithers, L. J., Ardlie, K., Barcus, M., Branton, P. A., Britton, A., Buia, S. A., Compton, C. C., DeLuca, D. S., Peter-Demchok, J., and Gelfand, E. T. (2015). A novel approach to high-quality postmortem tissue procurement: the GTEx project. Biopreservation and biobanking 13, 311-319.',
                    'Chen, J., Yang, H., Teo, A. S. M., Amer, L. B., Sherbaf, F. G., Tan, C. Q., Alvarez, J. J. S., Lu, B., Lim, J. Q., and Takano, A. (2020). Genomic landscape of lung adenocarcinoma in East Asians. Nature Genetics, 1-10.',
                    'Colaprico, A., Silva, T. C., Olsen, C., Garofano, L., Cava, C., Garolini, D., Sabedot, T. S., Malta, T. M., Pagnotta, S. M., Castiglioni, I., et al. (2016). TCGAbiolinks: an R/Bioconductor package for integrative analysis of TCGA data. Nucleic Acids Res 44, e71.',
                    'Ernst, C., Eling, N., Martinez-Jimenez, C. P., Marioni, J. C., and Odom, D. T. (2019). Staged developmental mapping and X chromosome transcriptional dynamics during mouse spermatogenesis. Nat Commun 10, 1251.',
                    'Han, X., Wang, R., Zhou, Y., Fei, L., Sun, H., Lai, S., Saadatpour, A., Zhou, Z., Chen, H., Ye, F., et al. (2018). Mapping the Mouse Cell Atlas by Microwell-Seq. Cell 172, 1091-1107 e1017.',
                    'Han, X., Zhou, Z., Fei, L., Sun, H., Wang, R., Chen, Y., Chen, H., Wang, J., Tang, H., Ge, W., et al. (2020). Construction of a human cell landscape at single-cell level. Nature 581, 303-309.',
                    'Hunt, G. J., Freytag, S., Bahlo, M., and Gagnon-Bartsch, J. A. (2019). dtangle: accurate and robust cell type deconvolution. Bioinformatics 35, 2093-2099.',
                    'Marin, R., Cortez, D., Lamanna, F., Pradeepa, M. M., Leushkin, E., Julien, P., Liechti, A., Halbert, J., Brüning, T., Mössinger, K., et al. (2017). Convergent origination of a Drosophila-like dosage compensation mechanism in a reptile lineage. Genome Res 27, 1974-1987.',
                    'Merkin, J., Russell, C., Chen, P., and Burge, C. B. (2012). Evolutionary dynamics of gene and isoform regulation in Mammalian tissues. Science 338, 1593-1599.',
                    'Mounir, M., Lucchetta, M., Silva, T. C., Olsen, C., Bontempi, G., Chen, X., Noushmehr, H., Colaprico, A., and Papaleo, E. (2019). New functionalities in the TCGAbiolinks package for the study and integration of cancer data from GDC and GTEx. PLoS Comput Biol 15, e1006701.',
                    'Necsulea, A., Soumillon, M., Warnefors, M., Liechti, A., Daish, T., Zeller, U., Baker, J. C., Grützner, F., and Kaessmann, H. (2014). The evolution of lncRNA repertoires and expression patterns in tetrapods. Nature 505, 635.',
                    'Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., and Dubourg, V. (2011). Scikit-learn: Machine learning in Python. the Journal of machine Learning research 12, 2825-2830.',
                    'Tabula Muris, C., Overall, c., Logistical, c., Organ, c., processing, Library, p., sequencing, Computational data, a., Cell type, a., Writing, g., et al. (2018). Single-cell transcriptomics of 20 mouse organs creates a Tabula Muris. Nature 562, 367-372.',
                    'Umemura, Y., Koike, N., Ohashi, M., Tsuchiya, Y., Meng, Q. J., Minami, Y., Hara, M., Hisatomi, M., and Yagita, K. (2017). Involvement of posttranscriptional regulation of Clock in the emergence of circadian clock oscillation during mouse development. Proc Natl Acad Sci U S A 114, E7479-e7488.',
                    'Wang, X., Park, J., Susztak, K., Zhang, N. R., and Li, M. (2019a). Bulk tissue cell type deconvolution with multi-subject single-cell expression reference. Nat Commun 10, 380.',
                    'Wang, Z., Tu, K., Xia, L., Luo, K., Luo, W., Tang, J., Lu, K., Hu, X., He, Y., Qiao, W., et al. (2019b). The Open Chromatin Landscape of Non-Small Cell Lung Carcinoma. Cancer Res.',
                    'Yanai, I., Benjamin, H., Shmoish, M., Chalifa-Caspi, V., Shklar, M., Ophir, R., Bar-Even, A., Horn-Saban, S., Safran, M., Domany, E., et al. (2005). Genome-wide midrange transcription profiles reveal expression level relationships in human tissue specification. Bioinformatics 21, 650-659.',
                    'Zhang, R., Lahens, N. F., Ballance, H. I., Hughes, M. E., and Hogenesch, J. B. (2014). A circadian gene expression atlas in mammals: implications for biology and medicine. Proc Natl Acad Sci U S A 111, 16219-16224.',
                    'Zhang, X.-C., Wang, J., Shao, G.-G., Wang, Q., Qu, X., Wang, B., Moy, C., Fan, Y., Albertyn, Z., and Huang, X. (2019). Comprehensive genomic and immunological characterization of Chinese non-small cell lung cancer patients. Nature communications 10, 1-12.'
                ],
                example: [
                    {
                        title: "1.	Check the concordance of cellular compositions with large cohorts in human lung and lung cancer",
                        img: urls.static + "/composition.svg",
                        desc: [
                            "Figure E1 Line plots showed the cell composition of 17 cells deconvoluted from different sources of bulk RNA-seq. The correlations were calculated using Pearson correlation.",
                            "To tested our pipeline, we used a bulk RNA-seq from an WCH cohort of 45 non-small cell lung cancer (NSCLC) patients (Wang et al., 2019b). Lung adenocarcinoma (LUAD) and squamous carcinoma (LUSC) are two major subtypes of NSCLC with distinct pathologic features and treatment paradigms.",
                            "We assessed the cell compositions from large cohorts with tumorous and normal lung bulk RNA-seq, including TCGA (n = 1,116), WCH RNA-seq (n = 49), East Asians group (n = 260), CHOICE (n = 490) and GTEx (n = 427). We found that the cell compositions were highly consistent despite different sources of bulk RNA-seq in LUAD, LUSC and normal lung (Pearson correlation r > 0.8, Figure E1)."
                        ]
                    },
                    {
                        title: "2.	Classification based on distinct cellular compositions in two sub-types of non-small cell lung cancer",
                        img: urls.static + "/tcga_cor.svg",
                        desc: [
                            "The Pearson correlation between cell weights of samples from TCGA. LUAD and LUSC tended to be clustered together. The proportions of different disease types were labels on the right.",
                            "The cell composition can distinguish the LUAD and LUSC in WCH (Figure E2), TCGA (Figure E3)."
                        ]
                    },
                    {
                        title: "",
                        img: urls.static + "/ml.svg",
                        desc: [
                            "Based on these cell compositions, we were able to correctly classify the lung cancer subtypes with high accuracy using support vector machine (SVM) (Figure E4, AUC = 0.89, SD = 0.01), suggesting the cellular compositions deconvoluted by inferCC could be used to classify the lung cancer patients."
                        ]
                    },
                    {
                        title: "3.	Identification of sub-groups and their association with patient survival",
                        img: urls.static + "/tcga_cluster.svg",
                        desc: [
                            "Heatmap of the deconvoluted weights of non-immune cells based on bulk RNA-seq data from LUAD patients. Patients could be separated into 4 groups, including NE-high (1), AT1-high (2), AT2-high (3) and Fib-high (4). (Figure E5)",
                            "Notably, the patients classified as fib-high were related to poor prognosis in LUAD in TCGA (p = 0.016, Log-rank test, Figure E6), while other groups were not related to the survival."
                        ]
                    },
                    {
                        title: "",
                        img: urls.static + "/tcga_surv.svg",
                        desc: [
                            "Kaplan-Meier survival curves for patients with LUAD (n = 513), stratified for the Fib-high group and the rest. P-value was calculated using the log-rank test."
                        ]
                    },
                ]
            }
        }
    }
</script>

<style scoped>
    strong {
        color: #F56C6C;
    }
</style>