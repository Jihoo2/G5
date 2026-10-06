"""기본 화면에 필요한 제목·색상·클래스·상태 표시 설정."""

APP_TITLE = "교과 7 - 조각김치 이물검출 라벨링 도구"

CLASSES = [
    (0, "나뭇잎·종이류", "#2E9E3F", True),
    (1, "플라스틱류·돌·금속류", "#E53935", True),
    (2, "나뭇가지류", "#1E6FE8", True),
    (3, "벌레류", "#9C3FE0", True),
    (4, "고무장갑 (사용 안 함)", "#9E9E9E", False),
    (5, "병해·갈변", "#FB8C00", True),
    (6, "파·고추", "#00897B", True),
]

CLASS_NAMES = {cid: name for cid, name, _, _ in CLASSES}

CLASS_COLORS = {cid: color for cid, _, color, _ in CLASSES}

ENABLED_CLASSES = [cid for cid, _, _, enabled in CLASSES if enabled]

NUM_CLASSES = len(CLASSES)

STATUSES = ["PASS", "EDITED", "REVIEW", "REVIEWED"]

STATUS_DESC = {
    "PASS": "[2단계] 기존 BBox·Class 확인, 누락 없음 → 검수자/pass (TXT만)\n"
            "수정했거나 Class 4가 있으면 선택 불가",
    "EDITED": "[2단계] 오류 발견 → BBox/Class 수정 → 검수자/edited\n"
              "수정 이유를 Issue/Note에 기록 필수 → Cross Review 대상",
    "REVIEW": "[2단계] 애매함 → 추측하지 않음 → 검수자/review\n"
              "애매한 점을 Issue/Note에 기록 필수 → 다른 작업자와 재확인",
    "REVIEWED": "[3단계] Cross Review 결과 정상 → 검수자/reviewed (TXT만)\n"
                "Cross Review 대상만, 직전 처리자와 다른 검수자만 가능",
}

REVIEWER_ONLY_STATUSES = ("PASS", "REVIEW", "REVIEWED")

SCENE_TYPES = [
    ("kimchi_with_target", "김치+대상"),
    ("normal_kimchi", "정상 김치"),
    ("object_only", "객체 단독"),
    ("need_check", "기타 확인 필요"),
]

ROLE_WORKER = "worker"

ROLE_REVIEWER = "reviewer"

ROLE_LABELS = {ROLE_WORKER: "작업자", ROLE_REVIEWER: "검수자"}

THUMB_W, THUMB_H = 150, 100

COLOR_BG = "#EEF1F6"

COLOR_PANEL = "#FFFFFF"

COLOR_BORDER = "#D8DEE8"

COLOR_ACCENT = "#1E6FE8"

COLOR_ACCENT_DARK = "#1757BD"

COLOR_TEXT = "#1F2937"

COLOR_MUTED = "#6B7280"

COLOR_CANVAS = "#2B2F36"

COLOR_DANGER = "#D93025"

COLOR_SUCCESS = "#22A33A"

FONT_CANDIDATES = ["NanumGothic", "NanumBarunGothic", "Noto Sans CJK KR",
                   "Noto Sans KR", "Malgun Gothic", "UnDotum", "DejaVu Sans"]

MONO_CANDIDATES = ["D2Coding", "NanumGothicCoding", "DejaVu Sans Mono", "Monospace"]
