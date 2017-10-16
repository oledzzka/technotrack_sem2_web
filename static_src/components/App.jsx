import React from 'react';
import MyPage from './MyPage'
import Layout from "./Layout";
import '../styles/base.scss';
import currentPage from '../constants/currentPage';


class App extends React.Component {
    state = {
        currentPage: currentPage.myPage,
    };

    onLayoutSelect = (e) => {
        this.setState({ currentPage: e.target.name });
    };

    render() {
        let childPage;
        switch (this.state.currentPage) {
            case currentPage.feedPage:
                childPage = <h1>FEEEEEEED</h1>;
                break;
            case currentPage.myPage:
                childPage =  <MyPage />;
                break;
            default:
                childPage = <h1>NO profilePage</h1>;
                break;
        }
        return (
            <div className="b-wrapper">
                <h1>Посты</h1>
                <Layout child={ childPage } onSelect={ this.onLayoutSelect }/>
            </div>
        )
    }
}

export default App;