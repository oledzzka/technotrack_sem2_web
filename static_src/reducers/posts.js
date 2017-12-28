import update from 'react-addons-update'
import {
    SUCCESS_POST_LOADING, START_POST_LOADING, ERROR_POST_LOADING, SUCCESS_SETTING_POST,
    START_SETTING_POST
} from '../actions/posts';

const initialState = {
    postList: [],
    posts: {},
    isLoading: false,
    isLoaded: false,
    isCreate: false,
};


export default function posts(store=initialState, action) {
    switch (action.type){
        case START_POST_LOADING: {
            return update(store, {
                isLoading: { $set: true },
            });
        }
        case SUCCESS_POST_LOADING: {
            return update(store, {
                isLoaded: {$set: true },
                isLoading: { $set: false },
                postList: { $set: action.payload.result },
                posts: {$merge: action.payload.entities.posts}
            });
        }
        case ERROR_POST_LOADING: {
            return update(store, {
                isLoading: { $set: false },
            });
        }

        case START_SETTING_POST: {
            return update(store, {
                isCreate: {$set: false},
            })
        }

        case SUCCESS_SETTING_POST: {
            return update(store, {
                isCreate: {$set: true},
                }
            )
        }
        default:
            return store;
    }
}