describe('Project Admin API:', function() {
  var helpers = require('./../helpers.js');

  var listResponse = undefined, createResponse = undefined, updateResponse = undefined, deleteResponse = undefined;

  beforeEach(function(done){
    browser.driver.manage().window().setSize(1280, 1024);
    browser.get(browser.baseUrl).then(function(){
        helpers.getJson('/project/list', function(response){
            listResponse = response;
            var record = listResponse.data[0];

            helpers.postJson('/project/create', record, function(response){
                createResponse = response;

                helpers.postJson('/project/update/'+record.id, record, function(response){
                    updateResponse = response;

                    helpers.postJson('/project/delete/'+record.tags[0].id, {}, function(response){
                        deleteResponse = response;

                        done();
                    })
                })
            })
        })
    });
  });

  it('POST /project/create & check structure', function() {
    expect(typeof createResponse).toEqual('object');
    expect(createResponse.code).toEqual('ok');
    var record = createResponse.data[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]]).toBeDefined();
  });

  it('GET /project/list & check structure', function() {
    expect(typeof listResponse).toEqual('object');
    expect(listResponse.code).toEqual('ok');
    var record = listResponse.data[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]]).toBeDefined();
  });

  it('POST /project/update/:project_id & check structure', function() {
    expect(typeof updateResponse).toEqual('object');
    expect(updateResponse.code).toEqual('ok');
    var record = updateResponse.data[0];
    var fields = ['id', 'title', 'description', 'name', 'images', 'url', 'type', 'html', 'markdown', 'text', 'tags'];
    for (var i=0; i<fields.length; i++)
        expect(record[fields[0]]).toBeDefined();
  });

  it('POST /project/delete/:project_id & check structure', function() {
    expect(typeof deleteResponse).toEqual('object');
    expect(deleteResponse.code).toEqual('ok');
  });


});