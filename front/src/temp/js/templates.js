angular.module("app").run(['$templateCache', function(a) { a.put('views/widjets/carusel/content.html', '<div class="jumbotron-photo" ng-if="item.images.length>0">\n' +
    '    <div id="{{\'carousel-\'+item.name}}" class="carousel slide" data-ride="carousel">\n' +
    '        <ol class="carousel-indicators" ng-if="item.images.length>1">\n' +
    '            <li ng-repeat="image in item.images" data-target="{{\'#carousel-\'+item.name}}"\n' +
    '                data-slide-to="{{$index}}" ng-class="$index==0?\'active\':\'\'"></li>\n' +
    '        </ol>\n' +
    '        <div class="carousel-inner">\n' +
    '            <div ng-repeat="image in item.images" class="item" ng-class="$index==0?\'active\':\'\'"><img\n' +
    '                    ng-src="{{image}}"></div>\n' +
    '        </div>\n' +
    '        <a ng-click="CaruselSvc.prev(\'#carousel-\'+item.name)" class="left carousel-control"\n' +
    '           data-slide="prev" ng-if="item.images.length>1">\n' +
    '            <span class="glyphicon glyphicon-chevron-left"></span>\n' +
    '        </a>\n' +
    '        <a ng-click="CaruselSvc.next(\'#carousel-\'+item.name)" class="right carousel-control"\n' +
    '           data-slide="next" ng-if="item.images.length>1">\n' +
    '            <span class="glyphicon glyphicon-chevron-right"></span>\n' +
    '        </a>\n' +
    '    </div>\n' +
    '</div>');
	a.put('views/widjets/anonce/content.html', '<div class="jumbotron-contents" ng-if="item.type==1">\n' +
    '    <h2 ng-bind-html="item.title | unsafe"></h2>\n' +
    '    <p ng-bind-html="item.text | unsafe"></p>\n' +
    '</div>\n' +
    '<div class="jumbotron-contents" ng-if="item.type==2">\n' +
    '    <h2 ng-bind-html="item.title | unsafe"></h2>\n' +
    '    <p ng-bind-html="item.html | unsafe"></p>\n' +
    '</div>\n' +
    '<div class="jumbotron-contents" ng-if="item.type==3">\n' +
    '    <h2 ng-bind-html="item.title | unsafe"></h2>\n' +
    '    <p ng-bind-html="item.url | unsafe"></p>\n' +
    '</div>\n' +
    '<div class="jumbotron-contents" ng-if="item.type==4">\n' +
    '    <h2 ng-bind-html="item.title | unsafe"></h2>\n' +
    '    <p ng-bind-html="item.markdown | unsafe"></p>\n' +
    '</div>');
	a.put('views/tag/list.html', '<div class="container">\n' +
    '    <div class="page-header">\n' +
    '        <h1>Tag: <span ng-bind-html="TagSvc.tagText | unsafe"></span></h1>\n' +
    '    </div>\n' +
    '    <div ng-repeat="allItem in TagSvc.allList">\n' +
    '    <p class="lead">Place: <a ng-bind-html="allItem.title | unsafe" ng-href="{{allItem.url}}"></a></p>\n' +
    '    <div class="row">\n' +
    '        <div ng-class="\'col-md-\'+(12/TagSvc.countItemsOnRow)" ng-repeat="item in allItem.list">\n' +
    '            <div class="jumbotron">\n' +
    '                <div ng-include="AppConst.widjets.carusel.template"></div>\n' +
    '                <div ng-include="AppConst.widjets.anonce.template"></div>\n' +
    '\n' +
    '                <div class="jumbotron-contents">\n' +
    '                    <div class="row">\n' +
    '                        <div class="col-md-8">\n' +
    '                            <span ng-repeat="tag in item.tags">\n' +
    '                                <a ng-href="{{TagSvc.tagUrl+\'/\'+tag}}" class="btn btn-default btn-xs"\n' +
    '                                   ng-bind-html="tag | unsafe"></a>\n' +
    '                            </span>\n' +
    '                        </div>\n' +
    '                        <div class="col-md-4">\n' +
    '                            <a ng-href="{{allItem.url+\'/\'+item.name}}" class="btn btn-link pull-right">Detail...</a>\n' +
    '                        </div>\n' +
    '                    </div>\n' +
    '                </div>\n' +
    '            </div>\n' +
    '        </div>\n' +
    '    </div>\n' +
    '\n' +
    '</div>');
	a.put('views/search/list.html', '<div class="container">\n' +
    '    <div class="page-header">\n' +
    '        <h1>Search result for text "<span ng-bind-html="SearchSvc.searchText | unsafe"></span>"</h1>\n' +
    '    </div>\n' +
    '    <div ng-repeat="allItem in SearchSvc.allList">\n' +
    '    <p class="lead">Place: <a ng-bind-html="allItem.title | unsafe" ng-href="{{allItem.url}}"></a></p>\n' +
    '    <div class="row">\n' +
    '        <div ng-class="\'col-md-\'+(12/SearchSvc.countItemsOnRow)" ng-repeat="item in allItem.list">\n' +
    '            <div class="jumbotron">\n' +
    '                <div ng-include="AppConst.widjets.carusel.template"></div>\n' +
    '                <div ng-include="AppConst.widjets.anonce.template"></div>\n' +
    '\n' +
    '                <div class="jumbotron-contents">\n' +
    '                    <div class="row">\n' +
    '                        <div class="col-md-8">\n' +
    '                            <span ng-repeat="tag in item.tags">\n' +
    '                                <a ng-href="{{SearchSvc.tagUrl+\'/\'+tag}}" class="btn btn-default btn-xs"\n' +
    '                                   ng-bind-html="tag | unsafe"></a>\n' +
    '                            </span>\n' +
    '                        </div>\n' +
    '                        <div class="col-md-4">\n' +
    '                            <a ng-href="{{allItem.url+\'/\'+item.name}}" class="btn btn-link pull-right">Detail...</a>\n' +
    '                        </div>\n' +
    '                    </div>\n' +
    '                </div>\n' +
    '            </div>\n' +
    '        </div>\n' +
    '    </div>\n' +
    '\n' +
    '</div>');
	a.put('views/project/list.html', '<div class="container">\n' +
    '    <div class="page-header">\n' +
    '        <h1>My projects</h1>\n' +
    '    </div>\n' +
    '    <p class="lead">Description of projects</p>\n' +
    '    <div class="row">\n' +
    '        <div ng-class="\'col-md-\'+(12/ProjectSvc.countItemsOnRow)" ng-repeat="item in ProjectSvc.list">\n' +
    '            <div class="jumbotron">\n' +
    '                <div ng-include="AppConst.widjets.carusel.template"></div>\n' +
    '                <div ng-include="AppConst.widjets.anonce.template"></div>\n' +
    '\n' +
    '                <div class="jumbotron-contents">\n' +
    '                    <div class="row">\n' +
    '                        <div class="col-md-8">\n' +
    '                            <span ng-repeat="tag in item.tags">\n' +
    '                                <a ng-href="{{ProjectSvc.tagUrl+\'/\'+tag}}" class="btn btn-default btn-xs"\n' +
    '                                   ng-bind-html="tag | unsafe"></a>\n' +
    '                            </span>\n' +
    '                        </div>\n' +
    '                        <div class="col-md-4">\n' +
    '                            <a ng-href="{{ProjectSvc.projectUrl+\'/\'+item.name}}" class="btn btn-link pull-right">Detail...</a>\n' +
    '                        </div>\n' +
    '                    </div>\n' +
    '                </div>\n' +
    '            </div>\n' +
    '        </div>\n' +
    '    </div>\n' +
    '\n' +
    '</div>');
	a.put('views/project/item.html', '<div class="container">\n' +
    '    <div class="page-header">\n' +
    '        <h1 ng-bind-html="ProjectSvc.item.title | unsafe" class="hidden-sm hidden-md hidden-lg"></h1>\n' +
    '        <div class="pull-right">\n' +
    '            <span ng-repeat="tag in ProjectSvc.item.tags">\n' +
    '                <a ng-href="{{ProjectSvc.tagUrl+\'/\'+tag}}" class="btn btn-default btn-xs"\n' +
    '                   ng-bind-html="tag | unsafe"></a>\n' +
    '            </span>\n' +
    '            <>\n' +
    '        </div>\n' +
    '        <h1 ng-bind-html="ProjectSvc.item.title | unsafe" class="hidden-xs"></h1>\n' +
    '    </div>\n' +
    '    <p class="lead" ng-bind-html="ProjectSvc.item.description | unsafe"></p>\n' +
    '    <div class="row">\n' +
    '        <div class="col-md-12">\n' +
    '            <div class="jumbotron">\n' +
    '                <div class="jumbotron-photo">\n' +
    '                    <div class="row">\n' +
    '                        <div ng-class="\'col-md-\'+(12/ProjectSvc.item.images.length)" ng-repeat="image in ProjectSvc.item.images">\n' +
    '                            <img ng-src="{{image}}"/>\n' +
    '                        </div>\n' +
    '                    </div>\n' +
    '                </div>\n' +
    '\n' +
    '                <div ng-include="ProjectSvc.anonceTemplate"></div>\n' +
    '\n' +
    '                <div class="jumbotron-contents">\n' +
    '                    <div class="row">\n' +
    '                        <div class="col-md-8">\n' +
    '                            <span ng-repeat="tag in ProjectSvc.item.tags">\n' +
    '                                <a ng-href="{{ProjectSvc.tagUrl+\'/\'+tag}}" class="btn btn-default btn-xs"\n' +
    '                                   ng-bind-html="tag | unsafe"></a>\n' +
    '                            </span>\n' +
    '                        </div>\n' +
    '                    </div>\n' +
    '                </div>\n' +
    '            </div>\n' +
    '        </div>\n' +
    '    </div>\n' +
    '</div>');
	a.put('views/home/content.html', '<div class="container">\n' +
    '    <div class="page-header">\n' +
    '        <h1>Page header</h1>\n' +
    '    </div>\n' +
    '    <p class="lead">Description of page <code>source code</code> and others text.</p>\n' +
    '    <p>Text for link <a href="http://google.com">i am link</a> others text.</p>\n' +
    '</div>');
	a.put('views/auth/login.html', '<div class="container">\n' +
    '    <div class="page-header">\n' +
    '        <h1>Login on site</h1>\n' +
    '    </div>\n' +
    '    <p class="lead">Please enter you email address and password for login on site <code>(admin@email.com, user@email.com, author@email.com)</code></p>\n' +
    '    <p>\n' +
    '    <div class="row">\n' +
    '        <div class="col-sm-4">\n' +
    '            <form ng-submit="AuthSvc.doLogin(email,password)" novalidate class="css-form">\n' +
    '                <div class="form-group">\n' +
    '                    <label for="email">Email:</label>\n' +
    '                    <input type="email" class="form-control" id="email" placeholder="email" ng-model="email" required>\n' +
    '                </div>\n' +
    '                <div class="form-group">\n' +
    '                    <label for="password">Password:</label>\n' +
    '                    <input type="password" class="form-control" id="password" placeholder="password"\n' +
    '                           ng-model="password" >\n' +
    '                </div>\n' +
    '                <button type="submit" class="btn btn-primary">Login</button>\n' +
    '            </form>\n' +
    '        </div>\n' +
    '    </div>\n' +
    '    </p>\n' +
    '    <p>If you lose password please click to <a ng-href="{{AuthSvc.recovery.url}}">recovery password</a></p>\n' +
    '    <p>For registration on site use <a ng-href="{{AuthSvc.reg.url}}">registration form</a></p>\n' +
    '</div>');
	a.put('views/navbar.html', '<nav class="navbar navbar-inverse navbar-fixed-top" ng-controller="NavbarCtrl">\n' +
    '    <div class="container">\n' +
    '        <div class="navbar-header">\n' +
    '            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar"\n' +
    '                    aria-expanded="false" aria-controls="navbar">\n' +
    '                <span class="sr-only">Toggle navigation</span>\n' +
    '                <span class="icon-bar"></span>\n' +
    '                <span class="icon-bar"></span>\n' +
    '                <span class="icon-bar"></span>\n' +
    '            </button>\n' +
    '            <a class="navbar-brand" ng-href="{{NavbarSvc.brand.url}}"\n' +
    '               ng-if="!NavbarSvc.brand.hidden" ng-bind-html="NavbarSvc.brand.title | unsafe"></a>\n' +
    '        </div>\n' +
    '        <div id="navbar" class="collapse navbar-collapse">\n' +
    '            <ul class="nav navbar-nav" ng-if="NavbarSvc.items.left.length>0">\n' +
    '                <li ng-repeat="item in NavbarSvc.items.left" ng-if="!item.hidden"\n' +
    '                    ng-class="item.active==true ? \'active\' : \'\'">\n' +
    '                    <a ng-href="{{item.url}}" ng-bind-html="item.title | unsafe"></a>\n' +
    '                </li>\n' +
    '            </ul>\n' +
    '            <form class="navbar-form navbar-right" role="search" ng-if="!NavbarSvc.items.search.hidden"\n' +
    '                  novalidate>\n' +
    '                <div class="form-search search-only">\n' +
    '                    <i class="search-icon glyphicon glyphicon-search"></i>\n' +
    '                    <input type="text" class="form-control search-query"\n' +
    '                           placeholder="{{NavbarSvc.items.search.placeholder}}" ng-model="searchText"\n' +
    '                           ng-enter="NavbarSvc.doSearch(searchText)">\n' +
    '                </div>\n' +
    '            </form>\n' +
    '            <ul class="nav navbar-nav navbar-right" ng-if="NavbarSvc.items.right.length>0">\n' +
    '                <li ng-repeat="item in NavbarSvc.items.right" ng-if="!item.hidden"\n' +
    '                    ng-class="item.active==true ? \'active\' : \'\'">\n' +
    '                    <a ng-href="{{item.url}}" ng-bind-html="item.title | unsafe"></a>\n' +
    '                </li>\n' +
    '            </ul>\n' +
    '        </div><!--/.nav-collapse -->\n' +
    '    </div>\n' +
    '</nav>');
	a.put('views/footer.html', '<footer class="footer">\n' +
    '    <div class="container">\n' +
    '        <p class="text-muted">Footer text</p>\n' +
    '    </div>\n' +
    '</footer>');
	 }]);