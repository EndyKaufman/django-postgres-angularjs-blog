app.constant('ProjectConst', {
    strings:{
        title: 'My project',
        description: 'Projects descriptions'
    },
    urls:{
        url: '#/project',
        getData: '/project',
        action: '/project'
    },
    types:[
        {id:1,title:'Text'},
        {id:2,title:'Html'},
        {id:3,title:'Url'},
        {id:4,title:'Markdown'}
    ],
    templates:{
        inputs:{
            central: 'views/project/inputs/central.html',
            right: 'views/project/inputs/right.html'
        },
        list:{
            item: 'views/project/list-item.html',
            tags: 'views/project/list-tags.html'
        },
        item:{
            view: 'views/project/item-view.html'
        }
    },
    message:{
        'project/remove/confirm':'Do you really want to remove project <strong>%s</strong>?'
    }
});