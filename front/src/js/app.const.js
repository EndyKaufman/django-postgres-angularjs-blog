app.factory('AppConst', function(AccountConst, TagConst, NoteConst, BookmarkConst, ProjectConst, SearchConst, NavbarConst){

    var service={
        homeUrl:'/project',
        brand:{
            title: 'MY BLOG',
            name: 'MY_BLOG',
            image: '//2.gravatar.com/avatar/767fc9c115a1b989744c755db47feb60?s=132&d=wavatar'
        },
        navbar: NavbarConst,
        search: SearchConst,
        account: AccountConst,
        tag: TagConst,
        note: NoteConst,
        bookmark: BookmarkConst,
        project: ProjectConst
    };

    return service;
  });