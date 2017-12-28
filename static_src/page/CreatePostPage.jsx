import React from 'react';

import Layout from "../components/Layout";
import PostForm from "../components/PostForm"

class CreatePostPage extends React.Component {

    render(){
        return (
            <Layout>
                <PostForm/>
            </Layout>
        );
    }
}

export default CreatePostPage;