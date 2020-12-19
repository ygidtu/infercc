<template>
    <el-row>
        <el-col :span="8" :offset="8">
            <el-card class="box-card">
                <div slot="header" class="clearfix">
                    <span><strong>ID: </strong>{{ data["uuid"] }}</span>
                </div>
                <div v-for="(v, k) in this.columns" :key="k" class="text item">
                    <span v-if="k === 'Status'">
                        <strong>{{ k }}: </strong>
                        <el-tag :type="tag">{{ data[v] }}</el-tag>
                    </span>
                    <span v-else>
                        <strong>{{ k }}: </strong>{{ data[v] }}
                    </span>
                </div>

                <div id="download" v-if="this.tag === 'success'">
                    <el-divider>Results</el-divider>

                    <div v-for="f in this.files" :key="f">
                        <el-link 
                        :href="`${urls.data}/${data['name']}/${f}`"
                        type="primary"
                        >{{ f }}</el-link>
                    </div>
                </div>
            </el-card>
        </el-col>
    </el-row>
</template>

<script>
import urls from "../../utils/const"

export default {
    name: "note",
    props: {
        data: { required: true},
    },
    data() {
        return {
            columns: {
                "Create Time": "create_time",
                "File MD5": "name",
                "Status":  "status",
                "Species": "species",
                "Tissue": "tissue",
                "Tau": "tau",
                "Software": "software",
                "Note": "note"
            },
            tag: null,
            urls: urls,
            files: []
        }
    },

    methods: {
        get_files() {
            const self = this
            this.axios.get(urls.file, {params: { name: this.$props.data["name"] }}).then(response => {
                self.files = response.data
            }).catch(error => {
                self.$notify({
                    showClose: true,
                    type: 'error',
                    title: `Error Status: ${error.response.status}`,
                    message: error.response.data["message"]
                });
            })
        },
        get_tag() {
            let data = this.$props.data
            let status = data["status"];

            if (status === "Failed") {
                this.tag = "danger"
            }
            if (status === "Created") {
                this.tag = "info"
            }

            if (status === "Finished") {
                this.tag = "success"
                this.get_files()
            }
        }
    },

    mounted () {
        this.get_tag()
    }
}
</script>