import React from 'react';
import {Switch, Route} from 'react-router-dom';
import '../styles/base.scss';
import CreatePostPage from "../page/CreatePostPage";
import MyPage from "../page/MyPage";
import ListPostPage from "../page/ListPostPage";


class App extends React.Component {

    render() {
        return (
            <Switch>
                <Route exact path="/" component={ () => <h2>Start</h2> }/>
                {/*<Route exact path="/index/create" render={ (props) => <PostForm { ...props } />}/>*/}
                <Route exact path="/index/create" component={ CreatePostPage }/>
                <Route exact path="/index/postlist" component={ ListPostPage }/>
                <Route exact path="/index/mypage" component={ MyPage }/>
            </Switch>

        )
    }
}

export default App;