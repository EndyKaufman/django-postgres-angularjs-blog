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
                return (AppConfig.userId!=false)
            }
        },
        {
            name: 'profile',
            parent:'auth',
            hiddenHandler: function(){
                return (AppConfig.userId==false)
            }
        },
        {
            name:'logout',
            parent:'auth',
            hiddenHandler: function(){
                return (AppConfig.userId==false)
            }
        }
    ]
});