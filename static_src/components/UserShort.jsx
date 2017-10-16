import React from 'react';
import PropTypes from 'prop-types';


class UserShort extends React.Component {
    render() {
        const no_ava_src = require("../images/no-avatars.png");
        let src_ava = no_ava_src;
        if (  this.props.user.avatar !=="" ){
            src_ava =  this.props.user.avatar ;
        }
        return (
            <div>
                <img className="b-avatar" src={ src_ava } alt="No photo" />
                <div className="b-user-name">{ this.props.user.first_name + ' ' + this.props.user.last_name }</div>
                <div className="b-user-name">{ this.props.user.username }</div>
            </div>
        );
    }

}
//
// UserShort.propTypes = {
//     user: PropTypes.shape({
//         avatar: PropTypes.string,
//         first_name: PropTypes.string,
//         last_name: PropTypes.string,
//         user_name: PropTypes.string,
//     })
//
// };
//
// UserShort.defaultProps = {
//     user:{
//         avatar: null,
//         last_name: "",
//         first_name: "",
//         user_name: '',
//     }
// };
//

export default UserShort;