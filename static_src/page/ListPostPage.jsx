import React from 'react';

import Layout from "../components/Layout";
import PostList from "../components/PostList";

class ListPostPage extends React.Component {

    render(){
        return (
            <Layout>
                <PostList />
            </Layout>
        );
    }
}

export default ListPostPage;