app.factory('TagSvc', function ($routeParams, $http, $q, $rootScope, AppConst, TagRes, ProjectRes, NavbarSvc) {
    var service={};

    service.list=false;
    service.allList=false;

    service.countItemsOnRow=3;

    service.title=AppConst.tag.strings.title;

    $rootScope.$on('navbar.change',function(event, eventRoute, current, previous){
        if (current.params!=undefined && current.params.navId!='tag'){
            service.tagText='';
        }
    });

    service.init=function(reload){
        NavbarSvc.init('tag');

        service.tagText=$routeParams.tagText;

        if ($routeParams.tagText!=undefined){
            service.allList=[];
            $q.all([
                service.load(),
                ProjectRes.getListByTag($routeParams.tagText)
            ]).then(function(responseList) {
                for (var i=1;i<responseList.length;i++){
                    if (i==1)
                        service.allList.push({
                            name: 'project',
                            list: responseList[i].data.data
                        });
                }
            });
        }
    }

    service.searchTag=function(query){
        var list=[];
        for (var i=0;i<service.list.length;i++){
            if (service.list[i].text.indexOf(query)!=-1)
                list.push(service.list[i]);
        }
        return list;
    }

    service.load=function(reload){
        var deferred = $q.defer();
        if (service.list===false || reload===true)
            TagRes.getList().then(function (response) {
                service.list=angular.copy(response.data.data);
                deferred.resolve(service.list);
                $rootScope.$broadcast('tag.load', service.list);
            },
            function (response) {
                service.list=[];
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    MessageSvc.error(response.data.code, response.data);
                deferred.resolve(service.list);
            })
        else
            deferred.resolve(service.list);
        return deferred.promise;
    }
    return service;
  });