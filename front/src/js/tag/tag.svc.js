app.factory('TagSvc', function ($routeParams, $http, $q, AppConst, NavbarSvc, ProjectSvc) {
    var service={};

    service.allList=false;

    service.tagUrl=AppConst.tag.urls.url;

    service.countItemsOnRow=3;

    service.title=AppConst.tag.strings.title;

    service.init=function(reload){
        NavbarSvc.init('tag');

        service.tagText=$routeParams.tagText;

        if ($routeParams.tagText!=undefined){
            service.allList=[];
            $q.all([
                ProjectSvc.getListByTag($routeParams.tagText)
            ]).then(function(responseList) {
                for (var i=0;i<responseList.length;i++){
                    service.allList.push({
                        title: AppConst.project.strings.title,
                        url: AppConst.project.urls.url,
                        list: responseList[i].data.data.records
                    });
                }
            });
        }
    }
    return service;
  });