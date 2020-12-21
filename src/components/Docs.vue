<template>
    <div>
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
            <el-breadcrumb-item>Statistics</el-breadcrumb-item>
        </el-breadcrumb>

        <el-divider />

        <h2>Statistics</h2>
        <!-- <el-row>
            <el-radio-group v-model="choose.sel" @change="select_choose">
                <el-radio-button v-for="key in data.source" :label="key" :key="key"  />
            </el-radio-group>
        </el-row> -->
        <el-cascader-panel :options="data.source" v-model="choose.sel" @change="select_choose" />
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
                        <span>{{ scope.row.source }}</span>
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
        <!-- <el-divider />
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
        </el-row> -->
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
                choose: {
                    sel: ["human", "rna-seq", "GTEx"],
                    data: []
                },
                // data: {source: [], data: []},
                urls: urls,
                data: {source: {}, data: []}
            }
        },
        methods: {
            select_choose () {
                let res = []
                for (let i of this.data.data) {
                    if (i.source === this.choose.sel[2]) {
                        res.push(i)
                    }
                }
                this.choose.data = res
            },
        },
        mounted() {
            const self = this
            this.axios.get(`${urls.static}/num_v2.json`).
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