import React from 'react';
import Post from './Post';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import {loadPosts} from '../actions/posts';
import apiUrls from "../constants/apiUrls";
import {bindActionCreators} from "redux";


class PostList extends React.Component {

    componentDidMount = () => {
        if (!this.props.isLoaded){
            this.props.loadPosts(apiUrls.posts);
        }
    };

    render() {
        const load_src = require("../images/load.gif");
        if (this.props.isLoading) {
            return <img src={ load_src } alt="Загрузка..."/>
        }
        const posts = this.props.postList.map(
            item => {
                return (<Post key = {item} id={ item }/>);

            });

        return (
            <div className="b-post-list">
                { posts }
            </div>
        );
    }
}


PostList.propTypes = {
    postList: PropTypes.arrayOf(PropTypes.number),
    isLoading: PropTypes.bool,
    loadPosts: PropTypes.func.isRequired,
};

PostList.defaultProps= {
    postList: [],
    isLoading: false,
};


const mapStateToProps = ({posts}) => {
    return {
        postList: posts.postList,
        isLoading: posts.isLoading,
        isLoaded: posts.isLoaded,
    }
};

const mapDispatchToProps = (dispatch) => {
    return bindActionCreators({loadPosts}, dispatch)
};

export default connect(mapStateToProps, mapDispatchToProps)(PostList);

