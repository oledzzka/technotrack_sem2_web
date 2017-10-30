import update from 'react-addons-update'

const initialState = {
    users: {},
};

export default function users(store=initialState, action) {
    if (action && action.payload && action.payload.entities && action.payload.entities.users) {
        return update(store,{
            users: {$merge : action.payload.entities.users}
        });
    } else return store;
}