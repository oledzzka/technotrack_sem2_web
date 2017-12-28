import {CALL_API, getJSON} from 'redux-api-middleware';
import {normalize} from "normalizr";

export const START_GET_FROM_SERVER = 'START_GET_FROM_SERVER';
export const SUCCESS_GET_FROM_SERVER = 'SUCCESS_GET_FROM_SERVER';
export const ERROR_GET_FROM_SERVER = 'ERROR_GET_FROM_SERVER';

export const getFromServer = (url, schema, types=[START_GET_FROM_SERVER,
                                            SUCCESS_GET_FROM_SERVER,
                                            ERROR_GET_FROM_SERVER]) => {
    return {
        [CALL_API]: {
            credentials: 'include',
            endpoint: url,
            method: 'GET',
            types: [
                types[0],
                {
                    type: types[1],
                    payload: (action, state, res) => {
                        return getJSON(res).then(
                            (json) => {
                                console.log(json);
                                const normalizeData = normalize(json, schema);
                                return Object.assign({}, normalizeData);
                            },
                        );
                    },
                },
                types[2]],
        }
    };
};



export const START_SETTING_TO_SERVER = 'START_SETTING_TO_SERVER';
export const SUCCESS_SETTING_TO_SERVER = 'SUCCESS_SETTING_TO_SERVER';
export const ERROR_SETTING_TO_SERVER = 'ERROR_SETTING_TO_SERVER';

export const setDataToServer = (url, data, schema,  types=[START_SETTING_TO_SERVER,
                                            SUCCESS_SETTING_TO_SERVER,
                                            ERROR_SETTING_TO_SERVER],
                                content_type = 'application/json') => {
    console.log('postPublishing');
    const header_dict = {
        'X-CSRFToken': document.cookie.match(/csrftoken=([^ ;]+)/)[1]
    };

    if (content_type) {
        header_dict['content-type'] = content_type;
    }
    return {
        [CALL_API]: {
            credentials: 'include',
            endpoint: url,
            method: 'POST',
            body: data,
            headers: header_dict,
            types: [
                types[0],
                {
                    type: types[1],
                    payload: (action, state, res) => {
                        return getJSON(res).then(
                            (json) => normalize(json, schema),
                        );
                    },
                },
                types[2],
            ],
        },
    };
};