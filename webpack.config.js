const webpack           = require( 'webpack' );
const ExtractTextPlugin = require( 'extract-text-webpack-plugin' );
const path              = require( 'path' ); // This resolves into the absolute path of the theme root.
const env               = process.env.NODE_ENV;

const postCss = {
    loader: 'postcss-loader',
    options: {
        sourceMap: true
    }
};

const cssLoader = {
    loader: 'css-loader',
    options: {
        sourceMap: true,
        minimize: true
    }
};

const sassLoader = {
    loader: 'sass-loader',
    options: {
        sourceMap: true
    }
};

const config = {
    devtool: 'source-map',
    entry: {
        main: './assets/scripts/main.js'
    },
    output: {
        path: path.resolve( './assets/dist' ),
        filename: '[name].js'
    },

    // webpack-dev-server configuration
    devServer: {
      // Can be omitted unless you are using 'docker' 
      //   host: '0.0.0.0',
      // This is where webpack-dev-server serves your bundle
      // which is created in memory.
      // To use the in-memory bundle,
      // your <script> 'src' should point to the bundle
      // prefixed with the 'publicPath', e.g.:
      //   <script src='http://localhost:9001/assets/bundle.js'>
      //   </script>
      publicPath: '/assets/dist/',
      // The local filesystem directory where static html files
      // should be placed.
      // Put your main static html page containing the <script> tag
      // here to enjoy 'live-reloading'
      // E.g., if 'contentBase' is '../views', you can
      // put 'index.html' in '../views/main/index.html', and
      // it will be available at the url:
      //   https://localhost:9001/main/index.html
      contentBase: path.resolve(__dirname, "./"),
      // 'Live-reloading' happens when you make changes to code
      // dependency pointed to by 'entry' parameter explained earlier.
      // To make live-reloading happen even when changes are made
      // to the static html pages in 'contentBase', add 
      // 'watchContentBase'
      watchContentBase: true,
      compress: true,
      port: 9001,
      watchOptions: {
        // Delay the rebuild after the first change
        aggregateTimeout: 300,

        // Poll using interval (in ms, accepts boolean too)
        poll: 1000,
      },
      open: true, // Open the page in browser
      hot: true
    },

    plugins: [

        // Extract all css into one file.
        new ExtractTextPlugin( '[name].css', {
            allChunks: true
        }),

        new webpack.HotModuleReplacementPlugin()
    ],
    module: {
        rules: [
            {
                test: /\.js$/,
                include: [
                    path.resolve( __dirname, 'assets/script' )
                ],
                use: {
                    loader: 'babel-loader',
                    options: {

                        // Removes unneeded whitespace
                        compact: true,

                        // Do not use the .babelrc configuration file.
                        babelrc: false,

                        // The loader will cache the results of the loader in node_modules/.cache/babel-loader.
                        cacheDirectory: true,

                        // List enabled ECMAScript feature sets.
                        presets: [ 'env', 'stage-0' ],

                        // The 'transform-runtime' plugin tells babel to require the runtime instead of inlining it.
                        plugins: [ 'transform-runtime' ]
                    }
                }
            },
            {
                test: /\.css$/,
                use: ExtractTextPlugin.extract({
                    use: [ cssLoader, postCss ]
                })
            },
            {
                test: /\.scss$/,
                use: ExtractTextPlugin.extract({
                    use: [ cssLoader, postCss, sassLoader ]
                })
            },
            {
                test: /\.(woff(2)?|eot|ttf|otf)(\?[a-z0-9=\.]+)?$/,
                use: {
                    loader: 'url-loader?name=../fonts/[name].[ext]',
                    options: {
                        limit: 4096
                    }
                }
            },
            {
                test: /\.(svg|gif|png|jpeg|jpg)(\?[a-z0-9=\.]+)?$/,
                use: {
                    loader: 'url-loader?name=../images/[name].[ext]',
                    options: {
                        limit: 4096
                    }
                }
            }
        ]
    },
    watchOptions: {
        poll: 500
    }
};

if ( env === 'production' ) {
    config.plugins.push(

        // Minify for the production environment.
        new webpack.optimize.UglifyJsPlugin({
            sourceMap: true,
            parallel: true,
            mangle: false,
            compress: {
                unused: false
            }
        })
    );
}

module.exports = config;
