import React from 'react';
import PropTypes from 'prop-types';
import currentPage from '../constants/currentPage';


class Layout extends React.Component {

    state = {

    };


    render() {
        return(
            <div>
                <div className="b-side-menu">
                    <button onClick={ this.props.onSelect } className="b-side-menu-button"
                            name={ currentPage.myPage }>Моя страница</button>
                    <button onClick={ this.props.onSelect } className="b-side-menu-button"
                            name={ currentPage.feedPage }>Новости</button>
                    <button onClick={ this.props.onSelect } className="b-side-menu-button"
                            name={ currentPage.profilePage }>Профиль</button>
                </div>
                <div>{ this.props.child }</div>
            </div>
            )

    }
}


Layout.propTypes = {
    onSelect: PropTypes.func.isRequired,
};

export default Layout;