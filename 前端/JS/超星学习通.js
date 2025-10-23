// 使用加密模块
const CryptoJS = require('crypto-js');

// 补齐参数
t = 1754404120036
function _0x11dbad() {
    //var _0x5c52a4 = _0x2e675c;
    for (var _0x55977e = [], _0x12474f = '0123456789abcdef', _0x33c6e8 = 0x0; _0x33c6e8 < 0x24; _0x33c6e8++)
        _0x55977e[_0x33c6e8] = _0x12474f['substr'](Math['floor'](0x10 * Math['random']()), 0x1);
    return _0x55977e[0xe] = '4',
    _0x55977e[0x13] = _0x12474f['substr'](0x3 & _0x55977e[0x13] | 0x8, 0x1),
    _0x55977e[0x8] = _0x55977e[0xd] = _0x55977e[0x12] = _0x55977e[0x17] = '-',
    _0x55977e['join']('');
}
_0x3fedba = 'qDG21VMg9qS5Rcok4cfpnHGnpf5LhcAv'
_0x589b78 = 'slide'

function GetSign(_0x4e0309){
    _0x422ded = CryptoJS.MD5(_0x4e0309 + _0x11dbad()).toString()
    //console.log(_0x422ded)
    _0x4e0309 = CryptoJS.MD5(_0x4e0309 + _0x3fedba + _0x589b78 + _0x422ded).toString() + ':' + (parseInt(_0x4e0309) + 0x493e0) || ''
    //console.log(_0x4e0309)
    _0x4015b8 = CryptoJS.MD5(_0x3fedba + _0x589b78 + Date['now']() + _0x11dbad()).toString()
    //console.log(_0x4015b8)
    return {
        'captchaKey' : _0x422ded,
        'token' : _0x4e0309,
        'iv' : _0x4015b8
}
}
// console.log(GetSign(t))

// 所需参数
// captchaKey = _0x422ded,
// token = _0x4e0309,
// iv = _0x4015b8

function GetIV(nowTime){
    _0x4015b8 = CryptoJS.MD5(_0x3fedba + _0x589b78 + nowTime + _0x11dbad()).toString()
    return _0x4015b8
}