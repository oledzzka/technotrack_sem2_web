import React from 'react';
import UserShort from './UserShort';
import PropTypes from 'prop-types';
import {connect} from "react-redux";


class Post extends React.Component {
    render() {
        return(
            <div className="b-post">
                <UserShort id={ this.props.author }/>
                <div className="b-post__title">{ this.props.title }</div>
                <img width="30%" height="10%" src={ this.props.photo } alt="no photo"/>
            </div>
        );
    }
}

Post.propTypes = {
    id: PropTypes.number.isRequired,
};

const mapStateToProps = ({ posts }, ownProps) => {
    return {
        ...posts.posts[ownProps.id],
    }
};

export default connect(mapStateToProps)(Post);
