describe('Project API:', function() {
  var mytools = require('./../tools.js');

  var item = undefined, listbysearch = undefined, listbytag = undefined, list = undefined;

  beforeEach(function(done){
    browser.get(browser.baseUrl).then(function(){
        mytools.getJson('/project/list', function(response){
            list = response.data;

            mytools.getJson('/project/item/project1', function(response){
                item = response.data;

                mytools.getJson('/project/listbytag/tag1', function(response){
                    listbytag = response.data;

                    mytools.getJson('/project/search/search_text', function(response){
                        listbysearch = response.data;

                        done();
                    })
                })
            })
        })
    });
  });

  it('get /project/list and check structure', function() {
    expect(typeof list).toEqual('object');
    var record = list.records[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    expect(typeof list.pageNumber).toEqual('number');
    expect(typeof list.countRecordsOnPage).toEqual('number');
    expect(typeof list.countAllRecords).toEqual('number');
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });

  it('get /project/item/:project_name and check structure', function() {
    expect(typeof item).toEqual('object');
    var record = item;
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });

  it('get /project/listbytag/:tag_text and check structure', function() {
    expect(typeof listbytag).toEqual('object');
    var record = listbytag.records[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    expect(typeof listbytag.pageNumber).toEqual('number');
    expect(typeof listbytag.countRecordsOnPage).toEqual('number');
    expect(typeof listbytag.countAllRecords).toEqual('number');
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });

  it('get /project/search/:search_text and check structure', function() {
    expect(typeof listbysearch).toEqual('object');
    var record = listbysearch.records[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    expect(typeof listbysearch.pageNumber).toEqual('number');
    expect(typeof listbysearch.countRecordsOnPage).toEqual('number');
    expect(typeof listbysearch.countAllRecords).toEqual('number');
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]] != undefined ? true : false).toEqual(true);
  });

});