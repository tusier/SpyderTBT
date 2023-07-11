var o0o0 = CryptoJS.enc.Utf8.parse("1234123412ABCDEF");
var o00o = CryptoJS.enc.Utf8.parse('ABCDEF1234123412');

function _OOIio(data) {
    const encryptedHexStr = CryptoJS.enc.Base64.parse(data);
    const srcs = CryptoJS.enc.Base64.stringify(encryptedHexStr);
    const decrypt = CryptoJS.AES.decrypt(srcs, o0o0, {
        iv: o00o,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    });
    let decryptedStr = decrypt.toString(CryptoJS.enc.Utf8);
    return JSON.parse(decryptedStr.toString());
}

