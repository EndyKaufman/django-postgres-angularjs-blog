app.factory('ProjectSvc', function ($routeParams, $rootScope, $http, $q, $timeout, $location, AppConst, ProjectRes, TagSvc, NavbarSvc, MessageSvc) {
    var service={};

    $rootScope.$on('project.delete',function(item){
        MessageSvc.info('project/delete/success', {values:item});
        ProjectSvc.goList();
    });

    $rootScope.$on('project.create',function(item){
        MessageSvc.info('project/create/success', {values:item});
    });

    $rootScope.$on('project.update',function(item){
        MessageSvc.info('project/update/success', {values:item});
    });

    service.item={};
    service.list=false;

    service.TagSvc=TagSvc;

    service.countItemsOnRow=2;

    service.title=AppConst.project.strings.title;

    service.init=function(reload){
        NavbarSvc.init('project');

        $q.all([
            TagSvc.load(),
            service.load()
        ]).then(function(responseList) {

        });
    }

    service.goList=function(){
        $location.path(AppConst.project.urls.url.replace('#',''));
    }
	service.doCreate=function(item){
		 ProjectRes.actionCreate(item).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    service.list.push(angular.copy(response.data.data));
                    $rootScope.$broadcast('project.create', service.item);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    MessageSvc.error(response.data.code, {
                        object: item
                    });
            }
        );
    }
	service.doUpdate=function(item){
		 ProjectRes.actionUpdate(item).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    service.item=angular.copy(response.data.data);
                    $rootScope.$broadcast('project.update', service.item);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    MessageSvc.error(response.data.code, {
                        object: item
                    });
            }
        );
    }
	service.doDelete=function(item){
		 ProjectRes.actionDelete(item).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    for (var i=0;i<service.list.length;i++){
                        if (service.list[i].id==item.id){
                            service.list.splice(i, 1);
                            break;
                        }
                    }
                    service.item={};
                    $rootScope.$broadcast('project.delete', item);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    MessageSvc.error(response.data.code, {
                        object: item
                    });
            }
        );
    }

    service.doDeleteImage=function(index){
        service.item.images.splice(index, 1);
    }
    service.doAppendImage=function(text){
        if (text===undefined)
            text='';
        service.item.images.push({
            id: chance.guid(),
            title: text
        });
    }

    service.load=function(){
        var deferred = $q.defer();
        if ($routeParams.projectName!=undefined){
            if (service.item.name!==$routeParams.projectName)
                ProjectRes.getItem($routeParams.projectName).then(
                    function (response) {
                        service.item=angular.copy(response.data.data);
                        deferred.resolve(service.item);
                        $rootScope.$broadcast('project.item.load', service.item);
                    },
                    function (response) {
                        service.item={};
                        if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                            MessageSvc.error(response.data.code, {
                                values:
                                    [
                                        $routeParams.projectName
                                    ]
                            });
                        deferred.resolve(service.item);
                    }
                );
        }else{
            if (service.list===false){
                ProjectRes.getList().then(function (response) {
                    var data=angular.copy(response.data.data);
                    service.list=data.records;
                    service.pageNumber=data.pageNumber;
                    service.countRecordsOnPage=data.countRecordsOnPage;
                    service.countAllRecords=data.countAllRecords;
                    deferred.resolve(service.list);
                    $rootScope.$broadcast('project.load', service.list);
                }, function (response) {
                    service.list=[];
                    if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                        MessageSvc.error(response.data.code, {
                            object: service
                        });
                    deferred.resolve(service.list);
                });
            }else
                deferred.resolve(service.list);
        }
        return deferred.promise;
    }
    return service;
  });