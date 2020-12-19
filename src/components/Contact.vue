<template>
    <div>
        <el-row :gutter="20">
            <h3>Prof.</h3>

            <el-row :gutter="20">
                <el-col :span="8" v-for="p in prof" :key="p.Email">
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span>{{ p.Name }}</span>
                        </div>
                        <div>{{ p.Description }}</div>
                        <el-divider />
                        <div><strong>Email</strong>: {{ p.Email }}</div>
                        </el-card>
                </el-col>
            </el-row>

            <el-divider />

            <h3>Students</h3>
            <el-row :gutter="20">
                <el-col :span="8" v-for="p in stu" :key="p.Email">
                    <el-card class="box-card">
                        <div slot="header" class="clearfix">
                            <span>{{ p.Name }}</span>
                        </div>
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
                        Name: "Lu Chen, Ph.D. Professor",
                        Description: "Department of Laboratory Medicine, State Key Laboratory of Biotherapy, West China Second Hospital, Sichuan University",
                        Email: "luchen@scu.edu.cn"
                    },
                    {
                        Name: "Jing-wen Lin, Ph.D. Professor",
                        Description: "Department of Laboratory Medicine, State Key Laboratory of Biotherapy, West China Second Hospital, Sichuan University",
                        Email: "lin.jingwen@scu.edu.cn"
                    }
                ],
                stu: [
                    {Name: "Yiming Zhang", Email: "ygidtu@gmail.com"},
                ],
                maintainer: [
                    {name: "Yiming Zhang", Email: "ygidtu@gmail.com", desc: "website usage or bug report"}
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