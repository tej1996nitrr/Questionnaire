import { CSRF_TOKEN } from "./csrf_token.js"

async function getJSON(response){
    if(response.status===204) return '';
    return response.json();
}
//for creating http requests
function apiService(endpoint, method, data){
    const config = {
        method: method || GET,
        body: data !== undefined? JSON.stringify(data):null,
        headers:{
            'content-type':'application/json',
            'X-CSRFTOKEN': CSRF_TOKEN
        }
    }
    return fetch(endpoint, config).then(getJON).catch(error => {console.log(error)})
}
export {apiService};