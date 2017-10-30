import React from 'react';

import Layout from "../components/Layout";
import PostForm from "../components/PostForm";
import PostList from "../components/PostList";

class MyPage extends React.Component {

    render(){
        return (
            <Layout>
                <PostForm  />
                <PostList />
            </Layout>
        );
    }
}

export default MyPage;