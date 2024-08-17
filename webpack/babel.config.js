const {plugins} = require("./webpack.config");
module.exports = {
    presets: [ '@babel/preset-env' ],
    plugins: [ '@babel/plugin-proposal-class-properties', '@babel/plugin-transform-runtime' ]
}