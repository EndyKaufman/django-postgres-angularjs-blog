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
    update:{
        action: '/auth/update'
    },
    recovery:{
        name: 'Recovery',
        name: 'recovery',
        url: '#/recovery',
        action: '/auth/recovery'
    },
    message:{
        'auth/noemail':'Email is empty!',
        'auth/nopassword':'Password is empty!',
        'auth/wrongemail':'Email is incorrect!',
        'auth/usernofound':'User not founded!',
        'auth/wrongpassword':'Wrong password!',
        'auth/notactive':'User not activated!',
        'auth/login/success':'You authorizing!',
        'auth/logout/success':'Bye-Bye!',
        'auth/logout/confirm':'Do you really want to leave?',
        'auth/usernofound':'User with email <strong>%s</strong> not found!'
    }
});