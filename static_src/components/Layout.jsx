import React from 'react';
import PropTypes from 'prop-types';
import {Link} from 'react-router-dom';
import 'grommet/grommet.min.css';

import Split from 'grommet/components/Split';
import Box from 'grommet/components/Box'
import Sidebar from 'grommet/components/Sidebar'
import Header from 'grommet/components/Header'
import Title from 'grommet/components/Title'
import Section from 'grommet/components/Section'
import Menu from 'grommet/components/Menu'
import Footer from 'grommet/components/Footer'
import Button from 'grommet/components/Button'

import Article from 'grommet/components/Article'
import User from 'grommet/components/icons/base/User'


class Layout extends React.Component {

    render() {
        return (

            <Article>
                <Section pad="none">
                    <Split flex='right' fixed={true}>
                            <Box  justify='start'>

                            <Sidebar colorIndex='neutral-1'  fixed={true}>
                                    <Header colorIndex="brand">
                                        <Title>Insta</Title>
                                    </Header>
                                    <Menu>
                                        <Link to="/index/create">Создать</Link>
                                        <Link to="/index/postlist">Список</Link>
                                        <Link to="/index/mypage">Моя страница</Link>
                                    </Menu>
                        </Sidebar>
                            </Box>

                        <Box colorIndex='light-2'
                             justify='center'
                             align='center'
                             pad='medium'>
                            {this.props.children}
                        </Box>
                    </Split>
                </Section>
                {/*<Footer pad='medium'>*/}
                    {/*<Button icon={<User />}/>*/}
                {/*</Footer>*/}
            </Article>
        )
    }
}


Layout.propTypes = {
    children: PropTypes.arrayOf(PropTypes.object).isRequired,
};

export default Layout;