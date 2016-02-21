app.constant('AccountConst',{
    reg:{
        title: 'Reg',
        name: 'reg'
    },
    login:{
        title: 'Login',
        name: 'login'
    },
    logout:{
        title: 'Logout',
        name: 'logout'
    },
    profile:{
        title: 'Profile',
        name: 'profile'
    },
    recovery:{
        name: 'Recovery',
        name: 'recovery'
    },
    message:{
        'account/exists':'User with email <strong>%s</strong> is exists!',
        'account/noemail':'Email is empty!',
        'account/nopassword':'Password is empty!',
        'account/wrongemail':'Email is incorrect!',
        'account/usernotfound':'User not founded!',
        'account/wrongpassword':'Wrong password!',
        'account/notactive':'User not activated!',
        'account/younotactive':'You not activated!',
        'account/login/success':'You authorizing!',
        'account/logout/success':'Bye-Bye!',
        'account/logout/confirm':'Do you really want to leave?',
        'account/usernotfound':'User with email <strong>%s</strong> not found!',
        'account/recovery/checkemail':'Check email <strong>%s</strong> for code to reset password',
        'account/delete/confirm':'Do you really want to delete account?'
    }
});