<template>
    <div>
        <el-row :gutter="20">
            <el-row :gutter="20">
                <el-col :span="8" v-for="p in stu" :key="p.Email">
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span>{{ p.Name }} <sup>{{ p.Afiliation }}</sup></span>
                        </div>
                        <div><strong>Email</strong>: {{ p.Email }}</div>
                        </el-card>
                </el-col>
            </el-row>
            <el-divider />
            <el-row :gutter="20">
                <el-col :span="8" v-for="p in prof" :key="p.Email">
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span>{{ p.Name }} <sup>{{ p.Afiliation }}</sup></span>
                        </div>
                        <div>{{ p.Description }}</div>
                        <el-divider />
                        <div><strong>Email</strong>: {{ p.Email }}</div>
                        </el-card>
                </el-col>
            </el-row>

            <el-divider />
            <el-row>
                <el-timeline>
                    <el-timeline-item
                    v-for="m in maintainer"
                    :key="m.name">
                    If you have any question with <strong>{{ m.desc }}</strong>, please contact 
                    <el-popover
                        placement="top-start"
                        title="Email"
                        width="200"
                        trigger="hover"
                        :content="m.Email">
                        <el-button plain slot="reference" type="success" size="medium">{{ m.name }}</el-button>
                    </el-popover>
                    </el-timeline-item>
                </el-timeline>
            </el-row>

            <el-divider />
            <el-card>
                <div slot="header" class="clearfix">
                    <h4>Affiliation:</h4>
                </div>
                <span v-for="(a, idx) in affiliation" :key="idx">
                    <sup>{{ idx + 1 }}</sup> {{ a }} <br />
                </span>
                <el-divider />
                <span><sup>*</sup> To whom correspondence should be addressed. Email: luchen@scu.edu.cn (LC)</span><br />
                <span><sup>#</sup> The authors wish it to be known that, in their opinion, the first authors should be regarded as joint First Authors.</span>
            </el-card>
        </el-row>

        
    </div>
</template>

<script>
    export default {
        name: "Home",
        data () {
            return {
                prof: [
                    {
                        Name: "Dr. Lu Chen",
                        Description: "Department of Laboratory Medicine, State Key Laboratory of Biotherapy, West China Second Hospital, Sichuan University",
                        Email: "luchen@scu.edu.cn",
                        Afiliation: "1*"
                    }
                ],
                stu: [
                    {Name: "Yiming Zhang", Email: "ygidtu@gmail.com", Afiliation: "1#"}
                ],
                maintainer: [
                    {name: "Yiming Zhang", Email: "ygidtu@gmail.com", desc: "website usage or bug report"}
                ],
                affiliation: [
                    "Key Laboratory of Birth Defects and Related Diseases of Women and Children of MOE, State Key Laboratory of Biotherapy, West China Second Hospital, Sichuan University, Chengdu 610041, China",
                ],
            }
        }
    }
</script>

<style scoped>
    strong {
        color: #F56C6C;
    }
</style>