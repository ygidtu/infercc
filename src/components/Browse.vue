<template>
    <div>
        <el-card class="box-card">
            <div slot="header" class="clearfix">
                <span>Create</span>
            </div>
            <Create />
        </el-card>
        <el-card class="box-card">
            <div slot="header" class="clearfix">
                <span>Query</span>
            </div>
            <Query />
        </el-card>
    </div>
</template>

<script>
    import Create from "./task/Create"
    import Query from "./task/Query"

    export default {
        name: "MainLayout",
        components: {Create, Query}
    }
</script>

<style scoped>

</style>