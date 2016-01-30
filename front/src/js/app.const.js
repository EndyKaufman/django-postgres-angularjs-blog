app.factory('AppConst', function(AuthConst, TagConst, NoteConst, BookmarkConst, ProjectConst, SearchConst, NavbarConst){

    var service={
        brand:{
            title: 'MY BLOG',
            name: 'MY_BLOG',
            url: '#/home',
            image: '//2.gravatar.com/avatar/767fc9c115a1b989744c755db47feb60?s=132&d=wavatar'
        },
        templates:{
            navbar: 'views/navbar.html',
            footer:'views/footer.html'
        },
        navbar: NavbarConst,
        search: SearchConst,
        auth: AuthConst,
        tag: TagConst,
        note: NoteConst,
        bookmark: BookmarkConst,
        project: ProjectConst
    };

    return service;
  });