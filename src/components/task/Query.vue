<template>
    <div>
        <el-row :gutter="20">
            <el-col :span="24">
                <el-form label-width="80px">
                    <el-col :span="12">
                        <el-form-item label="UUID">
                            <el-input v-model="uuid" placeholder="Please input your uuid" clearable />
                        </el-form-item>
                    </el-col>
                    <el-col :span="4">
                        <el-col :span="4">
                            <el-form-item>
                                <el-button 
                                type="success" plain
                                :icon="uuid !== '' ? 'el-icon-check' : 'el-icon-close'" 
                                :disabled="uuid === ''"
                                @click="query">
                                    Query
                                </el-button>
                            </el-form-item>
                        </el-col>
                    </el-col>
                    <el-col :span="4">
                        <el-form-item>
                            <el-button 
                            type="primary" plain
                            @click="example">
                                Example
                            </el-button>
                        </el-form-item>
                    </el-col>
                </el-form>
            </el-col>
        </el-row>

        <el-row :gutter="20" v-if="uuid !== '' && task.uuid !== ''">
            <el-divider />
            <el-col :span="24">
            <note v-if="this.tag !== ''" :data="this.task" />
            </el-col>
        </el-row>
    </div>
</template>

<script>
    import urls from "../../utils/const"
    import note from "./note"

    export default {
        name: "Query",
        components: {note},
        data() {
            return {
                filesize: 50,
                urls: urls,
                uuid: "",
                task: {
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
            reset() {
                this.uuid = ""
                this.task = {
                    uuid: "",
                    name: "",
                    species: "",
                    tissue: "",
                    software: "",
                    tau: 0.9,
                    status: "",
                    note: ""
                }
            },
            example() {
                this.uuid = "3e723599-515b-410c-9911-4e83a5f63ba4"
                this.query()
            },
            query() {
                const self = this
                this.axios.get(this.urls.task, {
                    params: {uuid: this.uuid}
                }).then(response => {
                    self.task = response.data
                }).catch(error => {
                    self.$notify({
                        showClose: true,
                        type: 'error',
                        title: `Error Status: ${error.response.status}`,
                        message: error.response.data["message"]
                    });
                })
            }
        }
    }
</script>

<style scoped>

</style>