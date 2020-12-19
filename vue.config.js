module.exports = {
    lintOnSave: false, //禁用eslint
    publicPath: 'static',  // static
    outputDir: "./dist",
    runtimeCompiler: true,
    productionSourceMap: true,
    configureWebpack:{
        performance: {
            hints: false
        }
    },
    devServer: {
        disableHostCheck: true,
    }
};