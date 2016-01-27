app.constant('AuthConst',{
    reg:{
        title: 'Reg',
        name: 'reg',
        url: '#/reg',
        action: '/auth/reg'
    },
    login:{
        title: 'Login',
        name: 'login',
        url: '#/login',
        action: '/auth/login'
    },
    logout:{
        title: 'Logout',
        name: 'logout',
        url: '#/logout',
        action: '/auth/logout'
    },
    profile:{
        title: 'Profile',
        name: 'profile',
        url: '#/profile',
        action: '/auth/profile'
    },
    recovery:{
        name: 'Recovery',
        name: 'recovery',
        url: '#/recovery',
        action: '/auth/recovery'
    },
    message:{
        'auth/login/invalidform':'Error in email or password field!',
        'auth/login/success':'You authorizing!',
        'auth/logout/success':'Bye-Bye!',
        'auth/logout/confirm':'Do you really want to leave?',
        'auth/usernofound':'User with email %s not found!'
    }
});