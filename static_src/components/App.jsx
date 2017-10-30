import React from 'react';
import {Switch, Route} from 'react-router-dom';
import '../styles/base.scss';
import PostList from "./PostList";
import PostForm from "./PostForm";
import MyPage from "../page/MyPage";

class App extends React.Component {

    render() {
        return (
            <Switch>
                <Route exact path="/" component={ () => <h2>Start</h2> }/>
                <Route exact path="/index/create" render={ (props) => <PostForm { ...props } />}/>
                <Route exact path="/index/postlist" component={ PostList }/>
                <Route exact path="/index/mypage" component={ MyPage }/>
            </Switch>

        )
    }
}

export default App;