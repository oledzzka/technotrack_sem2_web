import React from 'react';
import PropTypes from 'prop-types';
import {connect} from "react-redux";
import {bindActionCreators} from "redux";
import {loadPosts} from '../actions/posts';


class SearchForm extends React.Component {

     state = {
         query: '',
     };

    onChange = (e) => {
        this.setState({ [e.target.name]: e.target.value });
    };

    onClick = (e) => {
        e.preventDefault();
        const url = `${this.props.url}?query=${this.state.query}`;
        this.props.loadPosts(url);
    };


    render(){
        return (
            <div>
                <h2>Форма поиска</h2>
                <form>
                    <div>
                        <input onChange={ this.onChange } value={ this.state.query } className="b-form-field"
                               type="text" name="query" placeholder="Заголовок"/>
                    </div>
                    <div className="b-form-field-wrapper">
                        <button onClick={ this.onClick }>Найти</button>
                    </div>
                </form>
            </div>
        );
    }
}

SearchForm.propTypes={
    loadPosts: PropTypes.func,
    url: PropTypes.string.isRequired,
};

const mapStateToProps = () => {
    return {}
};

const mapDispatchToProps = (dispatch) => {
    return bindActionCreators({loadPosts}, dispatch)
};

export default connect(mapStateToProps, mapDispatchToProps)(SearchForm);
