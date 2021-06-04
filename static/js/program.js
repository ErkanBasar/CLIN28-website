// eslint-disable-next-line no-unused-vars
(function (window, document, $, moment, globaldict, undefined) {

  function makeid(text) {
    text = text ? text : '';
    var possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    for (var i = 0; i < 5; i++)
      text += possible.charAt(Math.floor(Math.random() * possible.length));
    return text;
  }

  function urlExists(url) {
    var http = new XMLHttpRequest();
    http.open('HEAD', url, false);
    http.send();
    return http.status!=404;
  }

  /************************************************************/
  /* Initialize: called after program is loaded               */
  /************************************************************/

  function initialize (hideProgram) {
    $('.program-talk').click(function () {
      $('#talk-title').html($(this).data('title'));
      $('#talk-authors').html($(this).data('authors'));
      $('#talk-abstract').html($(this).data('abstract'));
      var abstractURL = globaldict.urls.abstractURL.replace(/123456/, $(this).attr('id'));
      $('#copy-abstract-url').html('<i class="fa fa-link"></i>' + abstractURL);
      $('#copy-abstract-url').attr('href', abstractURL);
      var pdfURL = globaldict.urls.PDFPath.replace(/123456/, $(this).attr('id'));
      $('#show-presentation').attr('href', pdfURL);
      if (urlExists(pdfURL)) {
        $('#show-presentation').show();
      } else {
        $('#show-presentation').hide();
      }
      $('#abstract-popup').show();
    });
    $('.close').click(function (event) {
      event.stopImmediatePropagation();
      var divId = $(this).data('divid');
      $('#' + divId).hide();
    });
    $('.collapse-button').each(function () {
      var divId = $(this).data('divid');
      if ($(this).hasClass('collapsed')) {
        $('#' + divId).hide();
      } else {
        $('#' + divId).show();
      }
      $(this).click(function () {
        if ($(this).hasClass('collapsed')) {
          $('#' + divId).show();
          $(this).removeClass('collapsed');
        } else {
          $('#' + divId).hide();
          $(this).addClass('collapsed');
        }
      });
    });
    if(window.location.href.match(/#abstract-/)) {
      var talkId = window.location.href.split('/')[3].split('-')[1];
      $('#' + talkId).click();
    }
    if (hideProgram) {
      $('#program').css('display', 'none');
    }
  }

  /************************************************************/
  /* Load the Program                                         */
  /************************************************************/

  $.getJSON(globaldict.urls.program, function (data) {

    data.forEach(function (slot) {
      slot.uniqueId = data.indexOf(slot).toString() + makeid();
      var slotHTML = $('<div>', {
        class: 'program-table container'
      });

      // Header
      var slotHeader = $('<div>', {
        class: 'row slot-header'
      }).append($('<div>', {
        id: 'slot-' + slot.uniqueId + '-time',
        class: 'col-md-1',
        text: slot.start + ' - ' + slot.end
      }));

      var slotTitle = $('<div>', {
        class: 'col-md-11',
        text: slot.title
      }).append($('<small>', {
        html: slot.location ? ' Loc: ' + slot.location + '' : ''
      }));

      if (slot.subslots) {
        var slotContent = $('<div>', {
          class: 'slot-body',
          id: slot.uniqueId
        });
      }

      slot.columnWidth = 3;
      slot.columnWidthCustom = '';

      // Session Titles
      if(slot.sessions) {
        slot.columnWidth = Math.floor(12/slot.sessions.length);
        slot.columnWidthCustom = (12/slot.sessions.length).toFixed(1).toString().replace('.', '').replace(',', '');
        var tableRow = $('<div>', {
          class: 'row sessions-row'
        });
        var timeColumn = $('<div>', {
          class: 'col-md-1'
        });
        tableRow.append(timeColumn);
        // var infoColumns = $('<div>', {
        //   class: 'col-md-11'
        // });
        // slot.sessions.forEach(function (session) {
        //   var talkColumn = $('<div>', {
        //     class: 'col-md-' + slot.columnWidth + ' col-md-' + slot.columnWidthCustom,
        //     html: '<h4>' + session.title + '</h4><p>' + (session.chair ? 'Chair: ' + session.chair + '<br>' : '') + 'Loc: ' + session.location + '</p>'
        //   });
        //   infoColumns.append(talkColumn);
        // });
        // tableRow.append(infoColumns);
        slotContent.append(tableRow);
      }

      // Talks
      var time = '';
      if(slot.subslots) {
        slot.subslots.forEach(function (subslot, index) {
          // if (slot.sessions) {
          //   var mins = 20*index;
          //   time = moment('26 January 2018 ' + slot.start).add(mins, 'm').format('HH:mm');
          // } else {
          //   slot.columnWidth = Math.floor(12/subslot.length);
          //   slot.columnWidthCustom = (12/subslot.length).toFixed(1).toString().replace('.', '').replace(',', '');
          // }
          var tableRow = $('<div>', {
            class: 'row subslot-row'
          });
          var timeColumn = $('<div>', {
            class: 'col-md-1 subslot-time',
            text: time
          });
          tableRow.append(timeColumn);
          var infoColumns = $('<div>', {
            class: 'col-md-11'
          });
          subslot.forEach(function (talk) {
            var talkColumn = $('<div>', {
              class: 'program-talk col-md-' + slot.columnWidth + ' col-md-' + slot.columnWidthCustom,
              id: talk.id,
              html: '<b>' + talk.title + '</b>' + (talk.title ? '<br>' : '') + '<i>' + (talk.authors ? talk.authors : '') + '</i>',
              'data-title': talk.title,
              'data-authors': talk.authors,
              'data-abstract': talk.abstract,
            });
            if (globaldict.availablePDFs.indexOf(talk.id.toString()) >= 0) {
              talkColumn.append($('<div>', {
                class: 'pdf-available',
                id: 'pdf-' + talk.id,
              }).append($('<a>', {
                html: '<i class="fa fa-file-pdf-o"></i> PDF available',
                'data-fancybox': '',
                'data-type': 'pdf',
                href: globaldict.urls.PDFPath.replace(/123456/, talk.id),
              })));
            }
            infoColumns.append(talkColumn);
          });
          tableRow.append(infoColumns);
          slotContent.append(tableRow);
        });
      }

      if (slotContent) {
        var collapseButton = $('<span>', {
          class: 'fa collapse-button pull-right',
          'data-divid': slot.uniqueId
        });
        slotTitle.append(collapseButton);
      }

      slotHeader.append(slotTitle);
      slotHTML.append(slotHeader);
      slotHTML.append(slotContent);
      $('#program-table-wrapper').append(slotHTML);
      if (time && !slot.end) {
        time = moment('26 January 2018 ' + time).add(20, 'm').format('HH:mm');
        $('#slot-' + slot.uniqueId + '-time').text(slot.start + ' - ' + time);
      }
    });

    initialize(false);
  });

})(window, window.document, window.jQuery, window.moment, window.globaldict);
