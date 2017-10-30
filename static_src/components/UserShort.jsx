import React from 'react';
import PropTypes from 'prop-types';
import {connect} from "react-redux";


class UserShort extends React.Component {
    render() {
        const no_ava_src = require("../images/no-avatars.png");
        let src_ava = no_ava_src;
        if (  this.props.avatar ){
            src_ava =  this.props.avatar ;
        }
        return (
            <div>
                <img className="b-avatar" src={ src_ava } alt="No photo" />
                <div className="b-user-name">{ this.props.first_name + ' ' + this.props.last_name }</div>
                <div className="b-user-name">{ this.props.username }</div>
            </div>
        );
    }

}

UserShort.propTypes = {
    id: PropTypes.number.isRequired,
};


const mapStateToProps = ({ users }, ownProps) => {
    return {
        ...users.users[ownProps.id],
    }
};

export default connect(mapStateToProps)(UserShort);
