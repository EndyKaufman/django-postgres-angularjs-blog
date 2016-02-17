app.constant('AccountConst',{
    reg:{
        title: 'Reg',
        name: 'reg',
        url: '#/reg',
        action: '/account/reg'
    },
    login:{
        title: 'Login',
        name: 'login',
        url: '#/login',
        action: '/account/login'
    },
    logout:{
        title: 'Logout',
        name: 'logout',
        url: '#/logout',
        action: '/account/logout'
    },
    profile:{
        title: 'Profile',
        name: 'profile',
        url: '#/profile',
        action: '/account/profile'
    },
    update:{
        action: '/account/update'
    },
    delete:{
        action: '/account/delete'
    },
    recovery:{
        name: 'Recovery',
        name: 'recovery',
        url: '#/recovery',
        action: '/account/recovery'
    },
    message:{
        'account/exists':'User with email <strong>%s</strong> is exists!',
        'account/noemail':'Email is empty!',
        'account/nopassword':'Password is empty!',
        'account/wrongemail':'Email is incorrect!',
        'account/usernofound':'User not founded!',
        'account/wrongpassword':'Wrong password!',
        'account/notactive':'User not activated!',
        'account/younotactive':'You not activated!',
        'account/login/success':'You authorizing!',
        'account/logout/success':'Bye-Bye!',
        'account/logout/confirm':'Do you really want to leave?',
        'account/usernofound':'User with email <strong>%s</strong> not found!',
        'account/recovery/checkemail':'Check email <strong>%s</strong> for link to reset password',
        'account/delete/confirm':'Do you really want to delete account?'
    }
});