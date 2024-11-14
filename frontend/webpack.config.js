// project/frontend/webpack.config.js

const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
  mode: 'development', // 개발 모드
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/, // .js, .jsx 파일을 처리
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.css$/, // CSS 파일을 처리
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  resolve: {
    extensions: ['.js', '.jsx'], // import 시 확장자 생략 가능
  },
  devServer: {
    static: {
      directory: path.join(__dirname, 'public'), // contentBase를 static으로 변경
    },
    compress: true,
    port: 3000,
    historyApiFallback: true, // React Router를 사용할 때 필요
  },
};