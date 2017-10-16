import React from 'react';
import PropTypes from 'prop-types';
import apiUrls from '../constants/apiUrls';


class PostForm extends React.Component {

    state = {
        title: '',
        photo: '',
        isLoading: false,
    };

    onChange = (e) => {
        if (e.target.name === "photo"){
            e.preventDefault();
            let reader = new FileReader();
            let photo = e.target.files[0];
            let key = e.target.name;
            console.log(photo);
            console.log(reader.result);
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
        console.log(this.state);
        console.log(JSON.stringify(this.state));
        if (this.state.isLoading) {
            return;
        }
        this.setState({ isLoading: true });
        fetch(apiUrls.posts, {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify(this.state),
            headers: {
                'content-type': 'application/json',
            }
        }).then(
            body => body.json(),
        ).then(
            (json) => {
                this.setState({ isLoading: false });
                return this.props.onCreate(json);
            },
        )
    };


    render() {
        let $imagePreview = null;
        if (this.state.photo) {
          $imagePreview = (<img src={this.state.photo} />);
        } else {
          $imagePreview = (<div className="previewText">Please select an Image for Preview</div>);
        }
        return (
            <div className="b-create-form">
                <h2>Форма добавления</h2>
                <form>
                    <div className="b-form-field-wrapper">
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


PostForm.propTypes = {
    onCreate: PropTypes.func.isRequired,
};

export default PostForm;