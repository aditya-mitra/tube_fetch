import axios from "axios";
import { ApiResultType } from "../types";

const results_url = "http://127.0.0.1:9000" + "/api/v1";

export default async function fetchResults(
    offset: number,
    search: string
): Promise<ApiResultType> {
    return axios
        .get(results_url, { params: { limit: 10, offset, search } })
        .then((response) => response.data)
        .catch((_e) => {
            // toast error
            return [];
        });
}
