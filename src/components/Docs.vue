<template>
    <div>
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
            <el-breadcrumb-item>Statistics</el-breadcrumb-item>
        </el-breadcrumb>

        <el-divider />

        <h2>Statistics</h2>
        <el-row>
            <el-radio-group v-model="choose.sel" @change="select_choose">
                <el-radio-button v-for="key in data.source" :label="key" :key="key"  />
            </el-radio-group>
        </el-row>
        <el-divider />
        <el-row>
            <StatBar :data="choose.data" />
        </el-row>
        <el-divider />
        <el-row>
            <el-table stripe :data="choose.data" height="500" style="width: 100%">
                <el-table-column
                    prop="source"
                    label="Source"
                    width="180">
                    <template slot-scope="scope">
                        <span>{{ scope.row.source }}<sup>[{{scope.row.ref}}]</sup></span>
                    </template>
                </el-table-column>
                <el-table-column
                    prop="tissue"
                    label="Tissue"
                    width="180">
                </el-table-column>
                <el-table-column
                    prop="num"
                    label="Number">
                </el-table-column>
            </el-table>
        </el-row>
        <el-divider />
        <h2>Reference</h2>
        <el-row :gutter="20" >
            <el-divider >Datasets</el-divider>
            <el-col :span="24">
                <el-card >
                    <div style="padding: 14px;">
                        <ol>
                            <li v-for="ref in datasets" :key="ref">
                                {{ ref }}
                            </li>
                        </ol>
                    </div>
                </el-card>
            </el-col>
        </el-row>
        <el-row :gutter="20" >
            <el-divider >Softwares</el-divider>
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
    </div>
</template>

<script>
    import urls from '../utils/const'
    import StatBar from './StatsBar'
    export default {
        name: "Docs",

        components: {StatBar},
 
        data() {
            return {
                page: "",
                reference: [
                    'Wang, X., Park, J., Susztak, K., Zhang, N. R., & Li, M. (2019). Bulk tissue cell type deconvolution with multi-subject single-cell expression reference. Nature communications, 10(1), 1-9.',
                    'Hunt, G. J., Freytag, S., Bahlo, M., & Gagnon-Bartsch, J. A. (2019). dtangle: accurate and robust cell type deconvolution. Bioinformatics, 35(12), 2093-2099.',
                ],
                datasets: [
                    'Lonsdale, J., Thomas, J., Salvatore, M., Phillips, R., Lo, E., Shad, S., ... & Foster, B. (2013). The genotype-tissue expression (GTEx) project. Nature genetics, 45(6), 580-585.',
                    'Han, X., Zhou, Z., Fei, L., Sun, H., Wang, R., Chen, Y., ... & Zhou, Y. (2020). Construction of a human cell landscape at single-cell level. Nature, 581(7808), 303-309.',
                    'processing, Library, p., sequencing, Computational data, a., Cell type, a., Writing, g. (2018). Single-cell transcriptomics of 20 mouse organs creates a Tabula Muris. Nature, 562, 367-372.',
                ],
                choose: {
                    sel: "GTEx",
                    data: []
                },
                data: {source: [], data: []},
                urls: urls
            }
        },
        methods: {
            select_choose () {
                let res = []

                for (let i of this.data.data) {
                    if (i.source === this.choose.sel) {
                        res.push(i)
                    }
                }
                this.choose.data = res
            }
        },
        mounted() {
            const self = this

            this.axios.get(`${urls.static}/num.json`).
            then(response => { this.data = response.data }).
            finally(() => {
                this.select_choose()
            })
        }
    }
</script>

<style>
    #area {
        background-color: #F2F6FC
    }

    strong {
        color: #F56C6C;
    }

    li {
        margin-left: 10px;
    }

    li li {
        margin-left: 20px;
    }

    ul {list-style-position: inside;}

    code {
        background-color: #E4E7ED;
    }
</style>