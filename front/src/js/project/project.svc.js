app.factory('ProjectSvc', function ($routeParams, $rootScope, $http, $q, $location, AppConst, ProjectRes, TagSvc, NavbarSvc) {
    var service={};

    service.item=false;
    service.list=false;

    service.TagSvc=TagSvc;

    service.types=AppConst.project.types;
    service.projectUrl=AppConst.project.urls.url;
    service.tagUrl=AppConst.tag.urls.url;

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
        $location.path(service.projectUrl.replace('#',''));
    }
	service.doCreate=function(item){
		 ProjectRes.actionCreate(item).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    service.list.push(response.data.data);
                    $rootScope.$broadcast('project.create', service.item);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    alert(response.data.code);
            }
        );
    }
	service.doUpdate=function(item){
		 ProjectRes.actionUpdate(item).then(
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined && response.data.code=='ok'){
                    service.item=response.data.data;
                    $rootScope.$broadcast('project.update', service.item);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    alert(response.data.code);
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
                    service.item=false;
                    $rootScope.$broadcast('project.delete', item);
                }
            },
            function (response) {
                if (response!=undefined && response.data!=undefined && response.data.code!=undefined)
                    alert(response.data.code);
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
                        service.item=response.data.data;
                        deferred.resolve(service.item);
                        $rootScope.$broadcast('project.item.load', service.item);
                    },
                    function (response) {
                        service.item={};
                        console.log('error', response);
                        deferred.resolve(service.item);
                    }
                );
        }else{
            if (service.list===false){
                ProjectRes.getList().then(function (response) {
                    service.list=response.data.data.records;
                    service.pageNumber=response.data.data.pageNumber;
                    service.countRecordsOnPage=response.data.data.countRecordsOnPage;
                    service.countAllRecords=response.data.data.countAllRecords;
                    deferred.resolve(service.list);
                    $rootScope.$broadcast('project.load', service.list);
                }, function (response) {
                    service.list=[];
                    console.log('error', response);
                    deferred.resolve(service.list);
                });
            }else
                deferred.resolve(service.list);
        }
        return deferred.promise;
    }
    return service;
  });