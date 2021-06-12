// const axios = require('axios');
// const base64 = require('base-64');
// const utf8 = require('utf8');
const hotpTotpGenerator = require('hotp-totp-generator');

const ReqJSON = {
  github_url: 'https://gist.github.com/manisaiprasad/bcde82c08f0958a1a49d0c3aac6d9093',
  contact_email: 'manisaiprasadam@gmail.com"',
};

// const stringData = JSON.stringify(ReqJSON);
// const URL = 'https://api.challenge.hennge.com/challenges/003';
const sharedSecret = ReqJSON.contact_email + 'HENNGECHALLENGE003';

const MyTOTP = hotpTotpGenerator.totp({
  key: sharedSecret,
  T0: 0,
  X: 30,
  algorithm: 'sha512',
  digits: 10,
});
console.log(MyTOTP)
// const authStringUTF = ReqJSON.contact_email + ':' + MyTOTP;
// const bytes = utf8.encode(authStringUTF);
// const encoded = base64.encode(bytes);

// const createReq = async () => {
//   try {
//     const config = {
//       withCredentials: true,
//       headers: {
//         'Content-Type': 'application/json',
//          Authorization: 'Basic ' + encoded,
//       },
//     };

//     console.log('Making request', { URL, ReqJSON, config });

//     const response = await axios.post(URL, stringData, config);
//     console.log(response.data);
//   } catch (err) {
//     console.error(err.response.data);
//   }
// };

// createReq();