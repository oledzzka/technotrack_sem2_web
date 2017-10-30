import React from 'react';
import PropTypes from 'prop-types';
import apiUrls from '../constants/apiUrls';
import {connect} from "react-redux";
import {bindActionCreators} from "redux";
import {setDataToServer} from "../actions/common";


class PostForm extends React.Component {

     state = {
         title: '',
         photo: '',
     };

    onChange = (e) => {
        if (e.target.name === "photo"){
            e.preventDefault();
            let reader = new FileReader();
            let photo = e.target.files[0];
            let key = e.target.name;
            if (photo){
                reader.onloadend = () => {
                    this.setState({
                    [key]: reader.result
                    });
                };
                reader.readAsDataURL(photo);
            }

        } else {
            this.setState({ [e.target.name]: e.target.value });
        }
    };

    onClick = (e) => {
        e.preventDefault();
        this.props.setDataToServer(apiUrls.posts, JSON.stringify(this.state));
    };


    render() {
        let $imagePreview = null;
        if (this.state.photo) {
          $imagePreview = (<img src={this.state.photo} />);
        } else {
          $imagePreview = (<div className="previewText">Please select an Image for Preview</div>);
        }
        return (
            <div>
                <h2>Форма добавления</h2>
                <form>
                    <div>
                        <input onChange={ this.onChange } value={ this.state.title } className="b-form-field"
                               type="text" name="title" placeholder="Заголовок"/>
                    </div>
                    <input className="fileInput" onChange={ this.onChange } type="file" name="photo"/>
                    <div className="imgPreview"> {$imagePreview} </div>
                    <div className="b-form-field-wrapper">
                        <button onClick={ this.onClick }>Создать</button>
                    </div>
                </form>
            </div>
        );
    }
}

PostForm.propTypes={
    setDataToServer: PropTypes.func,
};

const mapStateToProps = () => {
    return {}
};

const mapDispatchToProps = (dispatch) => {
    return bindActionCreators({setDataToServer}, dispatch)
};

export default connect(mapStateToProps, mapDispatchToProps)(PostForm);
