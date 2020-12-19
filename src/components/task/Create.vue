<template>
    <div>
        <el-row :gutter="20">
            <el-col :span="24">
                <el-form>
                    <el-row :gutter="20">
                        <el-col :span="8">
                            <el-form-item label="Species">
                                <el-select 
                                v-loading="task.species.length === 0" 
                                v-model="task.data.species" 
                                filterable 
                                placeholder="Please select species" 
                                @change="load_tissues"
                                clearable>
                                    <el-option
                                    v-for="item in task.species"
                                    :key="item"
                                    :label="item"
                                    :value="item">
                                    </el-option>
                                </el-select>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="Tissue">
                                <el-select  
                                v-model="task.data.tissue" 
                                :disabled="task.data.species === ''"
                                filterable 
                                placeholder="Please select tissue" 
                                clearable>
                                    <el-option
                                    v-for="item in task.tissues"
                                    :key="item"
                                    :label="item"
                                    :value="item">
                                    </el-option>
                                </el-select>
                            </el-form-item>
                        </el-col>
                        <el-col :span="8">
                            <el-form-item label="Software">
                                <el-select v-loading="task.softwares.length === 0" v-model="task.data.software" filterable placeholder="Please select software" clearable>
                                    <el-option
                                    v-for="item in task.softwares"
                                    :key="item"
                                    :label="item"
                                    :value="item">
                                    </el-option>
                                </el-select>
                            </el-form-item>
                        </el-col>
                    </el-row>
                    <el-row :gutter="20">
                        <el-col :span="8">
                            <span class="demonstration">Tau value</span>
                            <el-slider
                                v-model="task.data.tau"
                                :min="0.5"
                                :step="0.1"
                                :max="0.9"
                                :marks="marks"
                                show-stops>
                            </el-slider>
                        </el-col>
                        <el-col :span="7">
                            <el-upload
                                class="upload-demo"
                                ref="upload"
                                accept=".csv"
                                name="file"
                                method="post"
                                :action="this.urls.file"
                                :on-success="uploadSuccess"
                                :on-error="uploadFailed"
                                :before-upload="beforeUpload"
                                :auto-upload="true">
                                    <el-button size="small" type="primary">
                                        Upload
                                    </el-button>
                                    <div class="el-upload__tip" slot="tip">
                                        Only support csv format，and no more than {{ this.filesize }}mb
                                    </div>
                                </el-upload>
                        </el-col>
                        <el-col :span="3">
                            <el-form-item>
                                <el-button 
                                type="success" 
                                :icon="task.data.name !== '' ? 'el-icon-check' : 'el-icon-close'" 
                                :disabled="task.data.name === '' || task.data.species === '' || task.data.tissue === '' || task.data.software === ''"
                                @click="create"
                                plain
                                >
                                    Create
                                </el-button>
                            </el-form-item>
                        </el-col>
                        <el-col :span="3">
                            <el-form-item>
                                <el-button type="danger" icon="el-icon-search" 
                                @click="reset"
                                plain
                                >Reset</el-button>
                            </el-form-item>
                        </el-col>
                        <el-col :span="3">
                            <el-form-item>
                                <el-tooltip class="item" effect="dark" content="Please upload example.csv file" placement="top-start">
                                    <el-button 
                                    icon="el-icon-search" 
                                    @click="example"
                                    plain
                                    >
                                    example
                                    </el-button>
                                </el-tooltip>
                            </el-form-item>
                        </el-col>
                    </el-row>
                </el-form>
            </el-col>
        </el-row>

        <el-row :gutter="20" v-show="created.uuid !== ''">
            <el-divider />
            <el-col :span="24">
                <el-alert
                    title="Note"
                    description="Please save uuid for query results."
                    type="info" show-icon />
                <el-divider />
                <note :data="this.created" />
            </el-col>
        </el-row>
    </div>
</template>


<script>
    import urls from "../../utils/const"
    import note from "./note"

    export default {
        name: "Create",
        components: {note},
        data() {
            return {
                filesize: 50,
                urls: urls,
                marks: {
                    0.5: "0.5", 0.6: "0.6", 
                    0.7: "0.7", 0.8: "0.8", 
                    0.9: "0.9"
                },
                task: {
                    species: [],
                    tissues: [],
                    softwares: [],
                    data: {
                        name: "",
                        species: "",
                        tissue: "",
                        software: "",
                        tau: 0.9,
                    },
                },
                created: {
                    uuid: "",
                    name: "",
                    species: "",
                    tissue: "",
                    software: "",
                    tau: 0.9,
                    status: "",
                    note: ""
                }
            }
        },
        methods: {
            // eslint-disable-next-line no-unused-vars
            uploadSuccess (response, file, fileList) {
                this.task.data.name = response.md5;
            },
            beforeUpload (file) {
                const isCSV = file.type === 'text/csv';
                 if (!isCSV) {
                  this.$message.error('The upload file should be csv format!');
                }

                const isLt2M = file.size / 1024 / 1024 < this.filesize;

                if (!isLt2M) {
                  this.$message.error(`The upload file should small than ${this.filesize}MB!`);
                }
                return isCSV && isLt2M
            },
            // eslint-disable-next-line no-unused-vars
            uploadFailed(err, file, fileList) {
                this.$message.error(err.message);
            },
            example() {
                this.task.data = {
                    species: "human",
                    tissue: "AdultLung",
                    software: "MuSiC",
                    tau: 0.9,
                }

                window.open(`${this.urls.data}/example.csv`)
            },
            reset() {
                this.task.data = {
                    uuid: "",
                    species: "",
                    tissue: "",
                    software: "",
                    tau: 0.9,
                    file: ""
                }
                this.created = {
                    uuid: "",
                    species: "",
                    tissue: "",
                    software: "",
                    tau: 0.9,
                    status: "",
                    note: ""
                }
            },
            create() {
                const self = this
                this.axios.get(this.urls.create, {
                    params: this.task.data
                }).then(response => {
                    self.created = response.data
                }).catch(error => {
                    self.$notify({
                        showClose: true,
                        type: 'error',
                        title: `Error Status: ${error.response.status}`,
                        message: error.response.data["message"]
                    });
                })
            },
            load_species() {
                const self = this
                this.axios.get(this.urls.support, {
                    params: {source: "species"}
                }).then(response => {
                    self.task.species = response.data
                }).catch(error => {
                    self.$notify({
                        showClose: true,
                        type: 'error',
                        title: `Error Status: ${error.response.status}`,
                        message: error.response.data["message"]
                    });
                })
            },
            load_software() {
                const self = this
                this.axios.get(this.urls.support, {
                    params: {source: "software"}
                }).then(response => {
                    self.task.softwares = response.data
                }).catch(error => {
                    self.$notify({
                        showClose: true,
                        type: 'error',
                        title: `Error Status: ${error.response.status}`,
                        message: error.response.data["message"]
                    });
                })
            },
            load_tissues() {
                const self = this
                this.axios.get(this.urls.support, {
                    params: {source: "tissue", species: this.task.data.species}
                }).then(response => {
                    self.task.tissues = response.data
                }).catch(error => {
                    self.$notify({
                        showClose: true,
                        type: 'error',
                        title: `Error Status: ${error.response.status}`,
                        message: error.response.data["message"]
                    });
                })
            },
        },
        mounted() {
            this.load_species()
            this.load_software()
        },
    }
</script>

<style scoped>

</style>