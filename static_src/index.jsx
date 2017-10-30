import React from 'react';
import ReactDOM from 'react-dom';
import App from "./components/App.jsx";
import './styles/base.scss';
import { Provider } from 'react-redux';
import initStore from './utils/store';
import createHistory from 'history/createBrowserHistory';
import { ConnectedRouter, routerMiddleware } from 'react-router-redux';
import MyPage from "./page/MyPage";

const history = createHistory();
const middleware = routerMiddleware(history);

ReactDOM.render(
    <Provider store={ initStore([middleware]) }>
        <ConnectedRouter history={ history }>
            <App />
        </ConnectedRouter>
    </Provider>,
    document.getElementById('index')
);
