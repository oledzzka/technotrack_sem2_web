import { createStore, applyMiddleware, compose } from "redux";
import initReduce from '../reducers';
import middleWares from '../middlewares';

function initStore(additionalMiddleWares = []) {
    const initialStore = {};
    return createStore(
        initReduce,
        initialStore,
        compose(applyMiddleware(...additionalMiddleWares, ...middleWares), window.__REDUX_DEVTOOLS_EXTENSION__()));

}
export default initStore;