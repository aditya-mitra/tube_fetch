import axios from "axios";
import { ApiResultType } from "../types";

const BASE_URL = "http://127.0.0.1:9000";

export default async function fetchResults(): Promise<ApiResultType> {
    return axios
        .get(BASE_URL + "/api/v1")
        .then((response) => response.data)
        .catch((_e) => {
            // toast error
            return [];
        });
}
