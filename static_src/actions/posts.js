import {post} from "../schemas";
import {getFromServer, setDataToServer} from "./common";

export const START_POST_LOADING = 'START_POST_LOADING';
export const SUCCESS_POST_LOADING = 'SUCCESS_POST_LOADING';
export const ERROR_POST_LOADING = 'ERROR_POST_LOADING';

export const loadPosts = (url) => {
    return getFromServer(url, [post], [START_POST_LOADING, SUCCESS_POST_LOADING, ERROR_POST_LOADING]);
};


export const START_SETTING_POST = 'START_SETTING_POST';
export const SUCCESS_SETTING_POST = 'SUCCESS_SETTING_POST';
export const ERROR_SETTING_POST = 'ERROR_SETTING_POST';

export const setPost = (url, data) => {
    return setDataToServer (url,data,[post],[START_SETTING_POST, SUCCESS_SETTING_POST, ERROR_SETTING_POST], '')
};