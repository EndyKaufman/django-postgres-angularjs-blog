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
            parent:'auth',
            hiddenHandler: function(){
                return (AppConfig.user.id!=undefined)
            }
        },
        {
            name: 'profile',
            parent:'auth',
            hiddenHandler: function(){
                return (AppConfig.user.id==undefined)
            }
        },
        {
            name:'logout',
            parent:'auth',
            hiddenHandler: function(){
                return (AppConfig.user.id==undefined)
            }
        }
    ]
});