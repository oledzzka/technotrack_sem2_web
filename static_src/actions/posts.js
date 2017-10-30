import {post} from "../schemas";
import {getFromServer} from "./common";

export const START_POST_LOADING = 'START_POST_LOADING';
export const SUCCESS_POST_LOADING = 'SUCCESS_POST_LOADING';
export const ERROR_POST_LOADING = 'ERROR_POST_LOADING';

export const loadPosts = (url) => {
    return getFromServer(url, post, [START_POST_LOADING, SUCCESS_POST_LOADING, ERROR_POST_LOADING]);
};
