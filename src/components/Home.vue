<template>
    <div>
        <el-row :gutter="20">
            <el-card v-for="o in content" :key="o"  class="box-card">
                <div class="text item">
                    {{ o }}
                </div>
            </el-card>
            <el-image :src="urls.static + '/infercc.svg'" style="width:100%"/> 
        </el-row>
    </div>
</template>

<script>
    import urls from "../utils/const";
    export default {
        name: "Home",
        data () {
            return {
                urls: urls,
                content: [
                    "RNA sequencing (RNA-seq) is a powerful tool to explore transcriptional diversity and heterogeneity at bulk and single-cell level. Single-cell RNA-seq while powerful in providing cell composition and gene expression at single-cell level, is currently costly and with limited sample sizes. Therefore, combining scRNA-seq results from a limited number of representative samples and the existing bulk RNA-seq from large cohorts can gain better insights into healthy and diseased samples.",
                    "Here we developed a deconvolution workflow inferCC (infer cellular composition based on single-cell expression signatures) to provide robust estimation of the relative cellular fractions using multiple state-of-the-art algorithms (such as MuSiC or dtangle). We first identified cell-type specific signatures from public scRNA-seq including the Human Cell Atlas with 599,926 cells from 52 tissues, the Mouse Cell Atlas with 405,796 cells from 51 tissues and Tabula muris with 100,605 cells from 20 mouse organs. Using our derived single-cell signatures and deconvolution methods, we processed (a) the GTEx cohort including 11688 samples from 53 healthy human tissues, (b) 10,486 tumor samples from TCGA and published RNA-seq of cancerous samples, (c) 553 mouse samples from 18 tissues and 14 developmental stages; and provide deconvolution for (d) user-provided healthy and tumor bulk RNA-seq data. Using non-small cell lung cancer (NSCLC) as an example, we found that cellular compositions were highly consistent despite different sources (Pearson correlation > 0.8). Notably, this information can distinguish two subtypes of NSCLC, namely lung adenocarcinoma and squamous carcinoma and the adjacent healthy tissue. Lastly, we adapted machine learning methods that (a) classify the user-provided sample as a high or low concordance with the cell type or tissue of interest, and (b) distinguish the cancer subtypes (with an accuracy of AUC = 0.89 in NSCLC), and (c) associate the patient groups with a certain high cellular composition with patient survival."
                ]
            }
        }
    }
</script>

<style scoped>

</style>