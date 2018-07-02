var DATATABLES_CONSTANT = {  
          
    // datatables常量  
    DATA_TABLES : {  
        DEFAULT_OPTION : { // DataTables初始化选项  
        	oLanguage : {  
                sProcessing : "处理中...",  
                sLengthMenu : "每页 _MENU_ 项",//"显示 _MENU_ 项结果,",  
                sZeroRecords : "没有匹配结果",  
                sInfo : "显示第 _START_ 至 _END_ 项结果（共 _TOTAL_ 项）",  
                sInfoEmpty : "显示第 0 至 0 项结果，共 0 项",  
                sInfoFiltered :"",// "(由 _MAX_ 项结果过滤)",  
                sInfoPostFix : "",  
                sSearch : "搜索:",  
                sUrl : "",  
                sEmptyTable : "表中数据为空",  
                sLoadingRecords : "载入中...",  
                sInfoThousands : ",",                
                oPaginate : {  
                    sFirst : "首页",  
                    sPrevious : "上页",  
                    sNext : "下页",  
                    sLast : "末页"  
                },  
                "oAria" : {  
                    "sSortAscending" : ": 以升序排列此列",  
                    "sSortDescending" : ": 以降序排列此列"  
                }  
            },  
            //bStateSave : true,
            bStateSave : true,
            // 禁用自动调整列宽  
            autoWidth : false,  
            // 为奇偶行加上样式，兼容不支持CSS伪类的场合  
            stripeClasses : [ "odd", "even" ],  
            // 取消默认排序查询,否则复选框一列会出现小箭头  
            //order : [],  
            // 隐藏加载提示,自行处理  
            processing : false,  
            // 启用服务器端分页  
            serverSide : true,  
            // 禁用原生搜索  
            searching : false,
            //自定义布局
            sDom:'rt<"bottom"lpfi<"clear">>',//定义分页等 的布局 f:过滤 p 分页 i 信息 l 每页数据量
        },  
        COLUMN : {  
            // 复选框单元格  
            CHECKBOX : {  
                className: "td-checkbox",  
                orderable : false,  
                bSortable : false,  
                width:"30px",
                data : "id",  
                render : function(data, type, row, meta) {  
                    var content = '<input type="checkbox" name="checkList" class="group-checkable" value="' + data + '" />';                       
                    return content;  
                }  
            }  
        },  
        // 常用render可以抽取出来，如日期时间、头像等  
        RENDER : {  
            ELLIPSIS : function(data, type, row, meta) {  
                data = data || "";  
                return '<span title="' + data + '">' + data + '</span>';  
            }  
        }  
    }  
      
  
};