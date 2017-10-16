import React from 'react';
import PostForm from './PostForm';
import PostList from './PostList';
import apiUrls from '../constants/apiUrls';


class MyPage extends React.Component {

    state= {
        postList: [],
        isLoading: false,
    };

    onPostCreate = (post) => {
        this.setState({
            postList: [post, ...this.state.postList],
        });
    };

    componentDidMount = () => {
        this.setState({ isLoading: true});
        fetch(apiUrls.posts, {
            credentials: 'include',
        }).then(
            (body) => body.json()
        ).then(
            (json) => this.setState({ postList: json, isLoading: false })
        );
    };

    render() {
        return(
            <div>
                <PostForm onCreate={ this.onPostCreate } />
                <PostList isLoading={this.state.isLoading} postList={this.state.postList} />
            </div>
        );
    }
}

export default MyPage;