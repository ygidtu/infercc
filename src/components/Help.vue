<template>
    <div>
        <el-row :gutter="20">
            <el-tabs tab-position="left">
                <el-tab-pane label="Help">
                    <el-row :gutter="20" v-for="key in images" :key="key.img">
                        <el-col :span="24">
                            <el-card :body-style="{ padding: '0px' }">
                                <el-image :src="key.img" class="image" />
                                <div v-for="v in key.desc" :key=v style="padding: 14px;">
                                    {{ v }}
                                </div>
                            </el-card>
                        </el-col>
                    </el-row>
                </el-tab-pane>
                <!-- <el-tab-pane label="Methods">
                    <el-row :gutter="20">
                        <el-col :span="24">
                            <h2>Bioinformatics and statistical methods</h2>
                        </el-col>
                    </el-row>
                    <el-divider />
                    <el-row :gutter="20" v-for="key in methods" :key="key.title">
                        
                        <el-col :span=24>
                            <el-card class="box-card">
                            <div slot="header" class="clearfix">
                                <strong>{{ key.title }}</strong>  
                            </div>
                            <div class="text item">
                                {{ key.content }}
                            </div>
                            
                            <el-col :span="23" :offset="1">
                                <div class="text item">
                                    <ol><li v-for="v in key.ul" :key="v">{{v}}</li></ol>
                                </div>
                            </el-col>
                            
                            </el-card>
                            
                            <el-divider />
                        </el-col>
                    </el-row>
                </el-tab-pane> -->
            </el-tabs>
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
                            "We provide multiple deconvolution algorithms for human and mouse. Users could customized the basic params and upload the raw expression matrix in csv format.",
                            "The first column of csv file should be official geen symbol, and first row should be the sample id. An example file could be downlod by click the example button.",
                            "Once click on create button, a task uuid will return, please carefully keep the uuid to reterive results."
                        ]
                    },
                    {
                        img: urls.static + "/infercc_02.png",
                        desc: [
                            "This tab is used to query task status, and download results file and running log.",
                            "If users have any issue with webservice usage please feel free to contact with us, and uuid and running log will be required."
                        ]
                    },
                ],
                methods: [
                    
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