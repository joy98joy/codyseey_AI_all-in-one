import math


MARS_GRAVITY_FACTOR = 0.38

DENSITIES = {
    '유리': 2.4,
    '알루미늄': 2.7,
    '탄소강': 7.85,
    'glass': 2.4,
    'aluminum' : 2.7,
    'carbon_steel':7.85
    }
# 화성 중력 계수 (지구 중력의 약 0.38배)

def sphere_area(diameter, material, thickness=1.0):
    """
    반구체 돔의 표면적과 무게를 계산하는 함수.

    Args:
        diameter (float): 돔의 지름 (단위: m).
        material (str): 돔의 재질 ('유리', '알루미늄', '탄소강' 중 하나).
        thickness (float): 돔의 두께 (단위: cm).

    Returns:
        tuple: (면적, 무게) 튜플을 반환합니다.
        계산 실패 시 (None, None)을 반환합니다.
    """
    
    # 유효성 검사
    if diameter <= 0 or thickness <= 0:
        print("오류: 지름과 두께는 0보다 커야 합니다.")
        return None, None
    if material not in DENSITIES:
        print(f"오류: '{material}'은 지원하지 않는 재질입니다.")
        return None, None
    
    # 단위 통일: m -> cm
    radius_m = diameter / 2 #반지름
    radius_cm = radius_m * 100
    thickness_cm = thickness

    # 1. 반구의 표면적 계산 (구의 표면적 공식: 4 * pi * r^2)
    # 돔의 표면적은 구의 절반 면적 + 바닥 면적
    surface_area_cm2 = 2 * math.pi * (radius_cm ** 2) + math.pi * (radius_cm ** 2)
    surface_area_m2 = surface_area_cm2 / (100**2) # cm^2 -> m^2 변환

    # 2. 돔의 부피 계산
    # 부피 = 표면적 * 두께
    volume_cm3 = surface_area_cm2 * thickness_cm

    # 3. 돔의 무게 계산
    density_g_per_cm3 = DENSITIES[material]
    mass_g = volume_cm3 * density_g_per_cm3
    mass_kg = mass_g / 1000

    # 4. 화성 중력 반영
    weight_mars_kg = mass_kg * MARS_GRAVITY_FACTOR

    return surface_area_m2, weight_mars_kg

def main():
    
    while True:
        print("\n--- 화성 기지 돔 계산기 ---")
        try:
            diameter_input = input("지름 (m)을 입력하세요 (예: 10). 종료하려면 'q'를 입력하세요: ")
            
            if diameter_input.lower() == 'q':
                print("프로그램을 종료합니다.")
                break

            diameter = float(diameter_input)
            if diameter <= 0:
                print('1 이상의 숫자를 입력하세요')
                continue
            
            material = input("재질을 선택하세요 (유리, 알루미늄, 탄소강). 종료하려면 'q'를 입력하세요:  ")
            if material.lower() == 'q':
                print("프로그램을 종료합니다.")
                break
            thickness = 1

            area, weight = sphere_area(diameter, material, thickness)
            
            if area is not None and weight is not None:
                print(f"\n재질 => {material}, 지름 => {diameter}, 두께 => {thickness}, "
                      f"면적 => {area:.3f} m², 무게 => {weight:.3f} kg")

        except ValueError:
            print("오류: 올바른 숫자 또는 재질을 입력해주세요.")
        except Exception as e:
            print(f"예상치 못한 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    main()
