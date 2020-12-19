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
                    "As an emerging powerful technical method, single-cell RNA sequencing provides the expression profiles of individual cells and provide an opportunity to understand the cell composition in different tissue or tumors. But the technical difficulties and expensive costs limits its promotion. Thereby, we developed a deconvolution workflow inferCC (infer cellular composition based on scRNA-seq expression signatures) to evaluate the relative fractions of diverse cell types. We take the raw counts of scRNA-seq with log2 transformed were used to calculate the specificity index (tau value). Then the raw expression of most cell type-specific genes (tau > 0.9) combined with our cell markers was used as a reference, and a deconvolution algorithm from MuSiC (Wang et al., 2019a) or dtangle  (Hunt et al., 2019) was used to evaluate the proportion of different cell types in each sample. And the similar cell composition was retrieved based on results."
                ]
            }
        }
    }
</script>

<style scoped>

</style>