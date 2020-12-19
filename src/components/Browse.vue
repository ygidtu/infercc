<template>
    <div>
        <el-tabs type="border-card">
            <el-tab-pane label="Create">
                <Create />
            </el-tab-pane>
            <el-tab-pane label="Query">
                <Query />
            </el-tab-pane>
        </el-tabs>
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