// '게시하기' 버튼에 클릭 이벤트 리스너 추가
document.getElementById('submit').addEventListener('click', function() {
  // 제목과 내용을 가져옴
  const title = document.getElementById('title').value;
  const content = document.getElementById('content').value;

  // 제목이나 내용이 비어있는지 확인
  if (!title || !content) {
      alert('제목과 내용을 입력하세요.'); // 경고 메시지
      return; // 함수 종료
  }

  // 게시물이 추가될 컨테이너 요소 선택
  const postContainer = document.getElementById('posts');

  // 새로운 게시물 요소 생성
  const postDiv = document.createElement('div');
  postDiv.className = 'post'; // 클래스 이름 설정

  // 제목 요소 생성
  const postTitle = document.createElement('h2');
  postTitle.textContent = title; // 제목 텍스트 설정

  // 내용 요소 생성
  const postContent = document.createElement('p');
  postContent.textContent = content; // 내용 텍스트 설정

  // 제목과 내용을 게시물 요소에 추가
  postDiv.appendChild(postTitle);
  postDiv.appendChild(postContent);

  // 게시물 요소를 게시물 컨테이너에 추가
  postContainer.appendChild(postDiv);

  // 입력 필드 초기화
  document.getElementById('title').value = '';
  document.getElementById('content').value = '';
});