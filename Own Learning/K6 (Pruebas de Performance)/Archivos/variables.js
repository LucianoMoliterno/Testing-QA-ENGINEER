import http from 'k6/http'

const hostname = `http://${__ENV.DOMAIN}`

export default function(){
    let response = http.post(hostname,"hola mundo");
}
