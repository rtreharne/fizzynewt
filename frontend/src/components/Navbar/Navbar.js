import React, { useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom'
import { Menu, Segment } from 'semantic-ui-react';

import './Navbar.css'

export default function Navbar(){


    // Bit of a hacky way for react to know the current route.    
    const currentRoute = useLocation()
    let activeItem = currentRoute.pathname.slice(1);


    useEffect(() => {
        activeItem = currentRoute.pathname.slice(1);
    }, [currentRoute])

    return (

        <nav>
            <Segment inverted className='navbar' >
                <Menu inverted pointing secondary size='large'>
                    <Menu.Item header>
                        FizzyNewt
                    </Menu.Item>
                    <Link to="">

                        <Menu.Item
                            name = ''
                            active = {activeItem === ''}
                            className = {'menuItem'}
                        >
                            Home
                        </Menu.Item>
                    </Link>
                    <Link to="create">
                        <Menu.Item 
                            name = 'create' 
                            active={activeItem === 'create'}
                            className = {'menuItem'}
                        >Create
                        </Menu.Item> 
                    </Link>
                </Menu>
            </Segment>
        </nav>
    )
}

