app.constant('NavbarConst', {
    left:[
        {
            name: 'project'
        },
        {
            name: 'note',
        },
        {
            name: 'bookmark',
        }
    ],
    search:{
        placeholder: ''
    },
    right:[
        {
            name:'login',
            parent:'account',
            hiddenHandler: function(){
                return (AppConfig.user.id!=undefined)
            }
        },
        {
            name: 'profile',
            parent:'account',
            hiddenHandler: function(){
                return (AppConfig.user.id==undefined)
            }
        },
        {
            name:'logout',
            parent:'account',
            hiddenHandler: function(){
                return (AppConfig.user.id==undefined)
            }
        }
    ]
});