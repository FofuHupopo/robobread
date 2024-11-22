import axios, {AxiosError, CreateAxiosDefaults} from "axios";

export const API_URL = "http://127.0.0.1:8000/api/";
export const API_URL_CLIENT = "http://127.0.0.1:8000/api/";

// export const API_URL = "http://192.168.114.11/api/";
// export const API_URL_CLIENT = "http://192.168.114.11/api/";

const getContentType = () => ({
    "Content-Type": "application/json"
});


const axiosOptions: CreateAxiosDefaults = {
    baseURL: API_URL_CLIENT,
    headers: getContentType(),
    withCredentials: true
};

export const $api = axios.create(axiosOptions);


export type ErrorType<Error> = AxiosError<Error>;

export type BodyType<BodyData> = BodyData;

export default $api;
