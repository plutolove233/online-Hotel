'use strict';

const path = require('path');

module.exports = {
  dev: {
    // Paths
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',
    proxyTable: {
      '/api_1_0': {
        target: '120.79.200.146:8000',
        changeOrigin: true,
        pathRewrite: { '^/api': '/api_1_0' },
      },
    },

   
    host: 'localhost',
    port: 8080, 
    autoOpenBrowser: true,
    errorOverlay: true,
    notifyOnErrors: true,
    disableHostCheck: true,
    https: false,
    hotOnly: false,
    poll: false, 
    showEslintErrorsInOverlay: false,
    devtool: 'cheap-module-eval-source-map',
    cacheBusting: true,
    cssSourceMap: true,
  },

  build: {
    //主界面
    index: path.resolve(__dirname, '../dist/index.html'),

    // 路径
    assetsRoot: path.resolve(__dirname, '../dist'),
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',

    /**
     * Source Maps
     */

    productionSourceMap: true,
    
    devtool: '#source-map',

   
    productionGzip: false,
    productionGzipExtensions: ['js', 'css'],

   
    bundleAnalyzerReport: process.env.npm_config_report,
  },
};
