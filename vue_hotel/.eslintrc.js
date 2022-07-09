module.exports = {
  env: {
    browser: true,
    // eslint-disable-next-line
    es2021: true,
  },
  extends: ['plugin:vue/essential', 'airbnb-base', 'prettier'],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module',
    parser: 'babel-eslint',
  },
  settings: {
    'import/resolver': {
      webpack: {
        config: 'build/webpack.base.conf.js',
      },
    },
  },
  plugins: ['vue'],
  // add your custom rules here
  rules: {
    eqeqeq: 2,
    quotes: [1, 'single'],
    'vue/no-parsing-error': [2, { 'x-invalid-end-tag': false }],
    'arrow-parens': [2, 'always'],
    semi: [2, 'always'], // 语句强制分号结尾
    'comma-dangle': 'off',
    'space-before-function-paren': [0, 'always'], //函数定义时括号前面要不要有空格
    'nonblock-statement-body-position': [2, 'any'],
    'no-return-assign': [2, 'except-parens'],
    'spaced-comment': [2, 'always'],
    'no-plusplus': [2, { allowForLoopAfterthoughts: true }],
    'no-multi-assign': 0,
    'no-lonely-if': 'error',
    'no-underscore-dangle': [
      2,
      {
        allow: [
          '_this',
          '__cacheCommonROIVis',
          '__cacheAnnotationRoiVis',
          '_lastMsgHeaderLen',
          '_lastMsgHeader',
          '_tcpPacketEnd',
          '_socket',
          '_msgCmdID',
          '_msgCellID',
          '_msgOpID ',
          '_msgRestDataLen',
          '_buffer',
          '_joint',
          '_msgOpID',
          '_msgSenderPID',
          '_socketio',
          '_cmdHandlers',
          '_icons',
          '_eventHandlers',
          '_focusCellCallback',
        ],
      },
    ],
    'class-methods-use-this': 0,
    indent: 'off',
    'space-before-function-paren': 0,
    // don't require .vue extension when importing
    // 'import/extensions': [
    //   'error',
    //   'always',
    //   {
    //     js: 'never',
    //     vue: 'never',
    //   },
    // ],
    // allow optionalDependencies
    'import/no-extraneous-dependencies': [
      'error',
      {
        optionalDependencies: ['test/unit/index.js'],
      },
    ],
    // allow debugger during development
    'no-console': process.env.NODE_ENV === 'production' ? 1 : 0,
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-param-reassign': [
      'error',
      {
        props: true,
        ignorePropertyModificationsFor: [
          'e', // for e.returnvalue
          'ctx', // for Koa routing
          'req', // for Express requests
          'request', // for Express requests
          'res', // for Express responses
          'response', // for Express responses
          'state', // for vuex state
          'err',
          'fmt',
          'date',
          'lib',
          'win',
          'parseInt',
        ],
      },
    ],
  },
};
