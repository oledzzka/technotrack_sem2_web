import React from 'react';
import Post from './Post';
import PropTypes from 'prop-types';


class PostList extends React.Component {
    render() {
        const load_src = require("../images/load.gif");
        if (this.props.isLoading) {
            return <img src={ load_src } alt="Загрузка..."/>
        }
        const posts = this.props.postList.map(
            item => {
                return (<Post key = {item.id} owner= {item.author}
                        title = {item.title} photo = {item.photo} likes = {item.likes_count}/>);

            });

        return (
            <div className="b-post-list">
                { posts }
            </div>
        );
    }
}
//
// PostList.propTypes = {
//     postList: PropTypes.arrayOf(PropTypes.shape({
//         id: PropTypes.number.isRequired,
//         owner : PropTypes.shape({
//             first_name: PropTypes.string.isRequired,
//             last_name: PropTypes.string.isRequired,
//             user_name: PropTypes.string.isRequired,
//             avatar: PropTypes.string,
//         }),
//         photo: PropTypes.string,
//         likes_count: PropTypes.number.isRequired
//     })),
//     isLoading: PropTypes.bool,
// };

PostList.defaultProps= {
    PostList: [],
    isLoading: false,
};

export default PostList;