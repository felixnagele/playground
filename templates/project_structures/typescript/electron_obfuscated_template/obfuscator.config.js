module.exports = {
  compact: true,

  controlFlowFlattening: true,
  controlFlowFlatteningThreshold: 0.75,

  deadCodeInjection: true,
  deadCodeInjectionThreshold: 0.4,

  debugProtection: false,
  debugProtectionInterval: 0,

  disableConsoleOutput: false,

  identifierNamesGenerator: 'hexadecimal',

  identifiersDictionary: [],

  identifiersPrefix: '',

  inputFileName: '',

  log: false,

  numbersToExpressions: true,

  optionsPreset: 'default',

  renameGlobals: false, // Keep false for Electron/Node.js compatibility

  renameProperties: false, // Keep false for compatibility

  rotateStringArray: true,

  seed: 0, // 0 = random

  selfDefending: true,

  simplify: true,

  sourceMap: false,
  sourceMapBaseUrl: '',
  sourceMapFileName: '',
  sourceMapMode: 'separate',

  splitStrings: true,
  splitStringsChunkLength: 10,

  stringArray: true,
  stringArrayCallsTransform: true,
  stringArrayCallsTransformThreshold: 0.75,
  stringArrayEncoding: ['base64'],
  stringArrayIndexesType: ['hexadecimal-number'],
  stringArrayIndexShift: true,
  stringArrayRotate: true,
  stringArrayShuffle: true,
  stringArrayWrappersCount: 2,
  stringArrayWrappersChainedCalls: true,
  stringArrayWrappersParametersMaxCount: 4,
  stringArrayWrappersType: 'function',
  stringArrayThreshold: 0.75,

  target: 'node', // Important for Electron!

  transformObjectKeys: false, // Keep false for compatibility

  unicodeEscapeSequence: false, // Keep false for better performance
};
