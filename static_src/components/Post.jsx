import React from 'react';
import UserShort from './UserShort';


class Post extends React.Component {
    render() {
        return(
            <div className="b-post">
                <UserShort user={ this.props.owner }/>
                <div className="b-post__title">{ this.props.title }</div>
                <img width="30%" height="10%" src={ this.props.photo } alt="no photo"/>
            </div>
        );
    }
}
//
// Post.propTypes = {
//     owner : PropTypes.shape({
//         first_name: PropTypes.string.isRequired,
//         last_name: PropTypes.string.isRequired,
//         user_name: PropTypes.string.isRequired,
//         avatar: PropTypes.string,
//     }),
//     photo: PropTypes.string,
//     likes_count: PropTypes.number.isRequired
// };
//
// Post.defaultProps = {
//     owner: {
//         first_name: '',
//         last_name: '',
//         user_name: '',
//         avatar: '',
//     },
//     photo: '',
//     likes_count: '',
// };

export default Post;
