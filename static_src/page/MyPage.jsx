import React from 'react';

import Layout from "../components/Layout";
import PostList from "../components/PostList";
import SearchForm from "../components/SearchForm";
import apiUrls from "../constants/apiUrls";

class MyPage extends React.Component {

    render(){
        return (
            <Layout>
                <SearchForm  url={apiUrls.posts} />
                <PostList />
            </Layout>
        );
    }
}

export default MyPage;