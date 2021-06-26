
const hotpTotpGenerator = require('hotp-totp-generator');

const MyTOTP = hotpTotpGenerator.totp({
  key: sharedSecret,
  T0: 0,
  X: 30,
  algorithm: 'sha512',
  digits: 10,
});
console.log(MyTOTP)
