import requests
def show_menu(title, options):
    """统一显示菜单，避免重复代码"""
    print("="*40)
    print(title)
    print("="*40)
    for key, value in options.items():
        print(f"{key}.{value}")
    print("="*40)

def get_int_input(prompt):
    """确保用户输入的是整数"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("\033[31m输入错误，请输入一个整数。\033[0m")

def get_float_input(prompt):
    """确保用户输入的是数字"""
    while True:
        try:
            return float(input(prompt)) 
        except ValueError:
            print("\033[31m输入错误，请输入一个数字。\033[0m")

def calculation_four_arithmetic():
    """
    四则运算
    """
    show_menu("四则运算",{1:"加法",2:"减法",3:"乘法",4:"除法",5:"2次",6:"3次",7:"n次",8:"返回"})
    choose = get_int_input("选择：")
    if choose == 1:
        a = get_float_input("加数：")
        print("按Enter输出/输入结果")
        while True:
            try:
                b = float(input("加数："))
                a += b
            except:
                break
        print("结果：",a)
    elif choose == 2:
        a = get_float_input("被减数：")
        print("按Enter输出/输入结果")
        while True:
            try:
                b = float(input("减数："))
                a -= b
            except:
                break
        print("结果：",a)
    elif choose == 3:
        a = get_float_input("乘数：")
        print("按Enter输出/输入结果")
        while True:
            try:
                b = float(input("乘数:"))
                a *= b
            except:
                break
        print("结果：",a)
    elif choose == 4:
        a = get_float_input("被除数：")
        print("按Enter输出/输入结果")
        while True:
            try:
                b = float(input("除数："))
                try:
                    a /= b
                except ZeroDivisionError:
                    print("\033[31m除数不可为0！\033[0m")
            except:
                break
        print("结果：", a)
    elif choose == 5:
        a = get_float_input("数：")
        print("结果：", a**2)
    elif choose == 6:
        a = get_float_input("数：")
        print("结果：", a**3)
    elif choose == 7:
        a = get_float_input("乘数：")
        n = get_float_input("n:")
        print("结果：", a ** n)
    elif choose == 8:
        pass
    else:
        print("\033[31m注意：不要输错选择\033[0m")

def calculation_plane_figure():
    """
    平面图形计算
    """
    show_menu("平面图形运算",{1:"矩形（平行四边）",2:"三角形",3:"圆",4:"返回"})
    choose = get_int_input("选择：")
    if choose ==1:
        a = get_float_input("长（底）：")
        b = get_float_input("宽（高）：")
        print("周长:",2*(a+b),"面积：",a*b)
    elif choose == 2:
        print("如果仅计算周长，请随便填底和高")
        a = get_float_input("底：")
        b = get_float_input("高：")
        try:
            print("没有则空，按Enter继续")
            a1 = float(input("边1："))
            b1 = float(input("边2："))
            c1 = float(input("边3："))
            
            # 改进的勾股定理判断
            sides = [a1, b1, c1]
            sides.sort()  # 从小到大排序
            eps = 1e-6  # 允许的误差
            
            # 判断最长边的平方是否等于两短边的平方和
            if abs(sides[2]**2 - (sides[0]**2 + sides[1]**2)) < eps:
                print(f"周长:{a1+b1+c1} 面积:{a*b/2} (直角三角形)")
            else:
                print(f"周长:{a1+b1+c1} 面积:{a*b/2} (非直角三角形)")
                
        except:
            print("条件不足，无周长；面积：", a*b/2)
    elif choose == 3:
        r = get_float_input("半径：")
        try:
            Π = float(input("Π（如果没有就空）："))
            print("周长：",2*Π*r,"面积：",Π*(r**2))
        except:
            print("周长：",r*2,"Π；面积：",r**2,"Π")
    elif choose == 4:
        pass
    else:
        print("\033[31m注意：不要输错选择\033[0m")

def calculation_three_dimensional_shapes():
    """
    立体图形计算
    """
    show_menu("立体图形运算",{1:"长方体",2:"圆柱",3:"圆锥",4:"返回"})
    choose = get_int_input("选择：")
    if choose ==1:
        try:
            print("如是底面积留空")
            a = float(input("长："))
            b = float(input("宽："))
            c = float(input("高："))
            print("体积:",a*b*c,"表面积：",(a*b+a*c+b*c)*2)
        except:
            s = get_float_input("底面积：")
            h = get_float_input("高：")
            print("体积：",s*h,"表面积（正方体）：",s*6)
    elif choose == 2:
        print("如是底面积留空")
        try:
            h = float(input("高："))
            r = float(input("底面半径：",))
            try:
                Π = float(input("Π（没有则留空）："))
                print("体积:",Π*(r**2)*h,"表面积：",Π*(r**2)*2+2*Π*r*h,"侧面积：",Π*2*r*h)
            except:
                print("体积:",(r**2)*h,"Π","表面积：",2*r*(r+h),"Π","侧面积：",2*r*h,"Π")
        except:
            s = get_float_input("底面积：")
            h = get_float_input("高：")
            print("体积：",s*h,"上下表面积：",2*s)
    elif choose == 3:
        print("如是底面积留空")
        try:
            h = float(input("高："))
            r = float(input("底面半径：",))
            l = float(input("母线："))
            try:
                Π = float(input("Π（没有则留空）："))
                print("体积:",Π*(r**2)*h/3,"表面积：",Π*(r**2)+Π*r*l,"侧面积：",Π*r*l)
            except:
                print("体积:",(r**2)*h,"Π","表面积：",r*(r+l),"Π","侧面积：",r*l,"Π")
        except:
            s = get_float_input("底面积：")
            h = get_float_input("高：")
            print("体积：",s*h/3)
    elif choose == 4:
        pass
    else:
        print("\033[31m注意：不要输错选择\033[0m")

def linear_function(a, x, b):
    """
    计算一次函数的值
    y = ax + b
    参数:
    a -- 一次项系数
    x -- 自变量
    b -- 常数项
    返回:
    y -- 函数值
    """
    return a * x + b


def quadratic_function(a, x, b, c):
    """
    计算二次函数的值
    y = ax² + bx + c
    参数:
    a -- 二次项系数
    x -- 自变量
    b -- 一次项系数
    c -- 常数项
    返回:
    y -- 函数值
    """
    return a * (x**2) + b * x + c


def inverse_proportion_function(x, k):
    """
    计算反比例函数的值
    y = k/x
    参数:
    x -- 自变量 (x ≠ 0)
    k -- 比例系数
    返回:
    y -- 函数值
    """
    if x == 0:
        raise ValueError("\033[31m除数不可为0！\033[0m")
    return k / x

def unit_conversion():
    show_menu("单位换算",{1:"长度",2:"面积",3:"体积",4:"重量",5:"温度",6:"进制",7:"返回"})
    choose = get_int_input("选择：")
    if choose == 1:
        length_conversion()
    elif choose == 2:
        area_conversion()
    elif choose == 3:
        volume_conversion()
    elif choose == 4:
        weight_conversion()
    elif choose == 5:
        temperature_conversion()
    elif choose == 6:
        show_menu("进制转换",{1:"十进制"})
        print("目前仅支持十进制转2，8，16进制")
        a = get_int_input("输入十进制数:")
        print("二进制：",bin(a),"八进制:",oct(a),"十六进制:",hex(a))
    elif choose == 7:
        return
    else:
        print("\033[31m注意：不要输错选择\033[0m")

def length_conversion():
    """长度单位转换"""
    units = {
        1: ("米", "m", 1.0),
        2: ("厘米", "cm", 0.01),
        3: ("毫米", "mm", 0.001),
        4: ("千米", "km", 1000.0),
        5: ("英寸", "in", 0.0254),
        6: ("英尺", "ft", 0.3048),
        7: ("码", "yd", 0.9144),
        8: ("英里", "mi", 1609.344)
    }
    
    show_menu("长度单位转换", {k: v[0] for k, v in units.items()})
    
    from_unit = get_int_input("转换自（输入编号）：")
    to_unit = get_int_input("转换到（输入编号）：")
    value = get_float_input("数值：")
    
    result = value * units[from_unit][2] / units[to_unit][2]
    print(f"{value} {units[from_unit][0]} = {result:.6f} {units[to_unit][0]}")

def area_conversion():
    """面积单位转换"""
    units = {
        1: ("平方米", "m²", 1.0),
        2: ("平方厘米", "cm²", 0.0001),
        3: ("平方毫米", "mm²", 0.000001),
        4: ("平方千米", "km²", 1000000.0),
    }
    
    show_menu("面积单位转换", {k: v[0] for k, v in units.items()})
    
    from_unit = get_int_input("转换自（输入编号）：")
    to_unit = get_int_input("转换到（输入编号）：")
    value = get_float_input("数值：")
    
    result = value * units[from_unit][2] / units[to_unit][2]
    print(f"{value} {units[from_unit][0]} = {result:.6f} {units[to_unit][0]}")

def temperature_conversion():
    """温度单位转换"""
    units = {
        1: ("摄氏度", "℃", 1.0),
        2: ("华氏度", "℉", -17.2222222222),
    }
    
    show_menu("温度单位转换", {k: v[0] for k, v in units.items()})
    
    from_unit = get_int_input("转换自（输入编号）：")
    to_unit = get_int_input("转换到（输入编号）：")
    value = get_float_input("数值：")
    
    result = value * units[from_unit][2] / units[to_unit][2]
    print(f"{value} {units[from_unit][0]} = {result:.6f} {units[to_unit][0]}")

def volume_conversion():
    """立体单位转换"""
    units = {
        1: ("立方米", "m³", 1.0),
        2: ("立方厘米", "cm³", 0.000001),
        3: ("立方毫米", "mm³", 0.000000001),
    }
    
    show_menu("立体单位转换", {k: v[0] for k, v in units.items()})
    
    from_unit = get_int_input("转换自（输入编号）：")
    to_unit = get_int_input("转换到（输入编号）：")
    value = get_float_input("数值：")
    
    result = value * units[from_unit][2] / units[to_unit][2]
    print(f"{value} {units[from_unit][0]} = {result:.6f} {units[to_unit][0]}")

def weight_conversion():
    """重量单位转换"""
    units = {
        1: ("千克", "kg", 1.0),
        2: ("克", "g", 0.001),
        3: ("毫克", "mg", 0.000001),
        4: ("斤","1/2kg",2),
    }
    
    show_menu("重量单位转换", {k: v[0] for k, v in units.items()})
    
    from_unit = get_int_input("转换自（输入编号）：")
    to_unit = get_int_input("转换到（输入编号）：")
    value = get_float_input("数值：")
    
    result = value * units[from_unit][2] / units[to_unit][2]
    print(f"{value} {units[from_unit][0]} = {result:.6f} {units[to_unit][0]}")

def Calculation_function():
    show_menu("函数计算",{1:"一次函数 (y = ax + b)",2:"二次函数 (y = ax² + bx + c)",3:"反比例函数 (y = k/x)",4:"返回"})
    
    choose = get_int_input("\n选择: ")
    
    if choose == 1:
        a = get_float_input("a (一次项系数): ")
        b = get_float_input("b (常数项): ")
        x = get_float_input("x: ")
        result = linear_function(a, x, b)
        print(f"\n当x={x}时，y = {a}*{x} + {b} = {result}")
        
    elif choose == 2:
        a = get_float_input("a (二次项系数): ")
        b = get_float_input("b (一次项系数): ")
        c = get_float_input("c (常数项): ")
        x = get_float_input("x: ")
        result = quadratic_function(a, x, b, c)
        print(f"\n当x={x}时，y = {a}*{x}² + {b}*{x} + {c} = {result}")
        
    elif choose == 3:
        k = get_float_input("k (比例系数): ")
        
        # 特殊处理：x不能为0
        while True:
            x = get_float_input("x值 (x≠0): ")
            if abs(x) < 1e-10:  # 检查是否为0（考虑浮点数精度）
                print("\033[31m错误：x不能为0！\033[0m")
            else:
                break
        
        result = k / x
        print(f"\n当x={x}时，y = {k}/{x} = {result}")
        
    elif choose == 4:
        pass  # 返回
    else:
        print("\033[31m注意：不要输错选择\033[0m")

def ultra_simple_update_check():
    """
    检查更新
    """
    VERSION = "2.0.1"
    
    print("\n" + "="*40)
    print("检查更新")
    print("="*40)
    
    owner = "honglin114514"
    repo = "LAZY"

    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/releases/latest"
        response = requests.get(url)
        
        # 检查响应状态码
        if response.status_code != 200:
            print(f"\033[31m请求失败，状态码: {response.status_code}\033[0m")
            input("\n按 Enter 键返回主菜单...")
            return
        
        data = response.json()
        
        latest_version = data.get("tag_name", "")
        release_url = data.get("html_url", "")
        
        print(f"当前版本: {VERSION}")
        print(f"最新版本: {latest_version}")
        print(f"更新页面: {release_url}")
        
        if latest_version:
            from packaging import version
            
            try:
                current_ver = version.parse(str(VERSION))
                latest_ver = version.parse(latest_version.replace("v", ""))
                
                if latest_ver > current_ver:
                    print("\033[32m有可用更新。\033[0m")
                else:
                    print("\033[34m当前已是最新版本。\033[0m")
            except Exception as e:
                print(f"\033[33m版本比较失败: {str(e)}\033[0m")
        else:
            print("\033[33m无法获取最新版本信息。\033[0m")
            
    except requests.exceptions.RequestException:
        print("\033[31m网络连接失败，请检查网络。\033[0m")
        try:
            p = int(input("输入1打开下载网页手动更新，留空返回："))
            if p == 1:
                import webbrowser
                webbrowser.open('https://github.com/Honglin114514/LAZY/releases/tag/v2.0') 
        except:
            pass
    except Exception as e:
        print(f"\033[31m检查失败: {str(e)}\033[0m")

while True:
    show_menu("Calculation Tool v2.1.0",{1:"四则运算",2:"平面图形计算",3:"立体图形计算",4:"函数计算",5:"单位换算",6:"检查更新(Github)",7:"关于",8:"退出"})
    choose = get_int_input("选择：")
    if choose == 1:
        calculation_four_arithmetic()
    elif choose == 2:
        calculation_plane_figure()
    elif choose == 3:
        calculation_three_dimensional_shapes()
    elif choose ==4:
        Calculation_function()
    elif choose ==5:
        unit_conversion()
    elif choose ==6:
        ultra_simple_update_check()
    elif choose ==7:
        print("=" * 40)
        print("关于")
        print("=" * 40)
        print("#         # ######### ##")
        print("#        # #            ##")
        print("#        # #              ##")
        print("#       #####             ##")
        print("#       #   #           ##")
        print("###### #     # ###### ##    ")
        print("使用即代表同意我们的用户协议，最终解释权归作者所有。")
        print("仅用于学习交流，请在下载后24小时内删除，不可用于其他用途！")
        print("用户使用此程序产生的所有后果由使用者承担.")
        print("-LAZY-")
        print("LAZY CT v2.1.0")
        print("开发：起懒了的cat")
        print("email:honglin114514@outlook.com")
        print("="*16,"更新日志","="*16)
        print("添加单位换算（长面体重温进制）")
        try:
            v = int(input("输入1查看用户协议，留空返回主菜单："))
            if v == 1:
                print("\n" + "="*16 + " 用户协议 " + "="*16)
                print("1. 使用声明：")
                print("   - 本软件为免费工具，仅供学习、教育和合法计算使用")
                print("   - 禁止用于任何非法、违规、侵权或危害国家安全的活动")
                print("   - 禁止用于商业考试作弊、学术不端等不当用途")
                print("   - 禁止用于破解、攻击、篡改其他系统或数据")
                
                print("\n2. 责任限制：")
                print("   - 用户应对使用本软件产生的所有后果承担全部责任")
                print("   - 作者不对软件功能的准确性、完整性或适用性作任何担保")
                print("   - 作者不对因使用本软件导致的任何直接、间接损失负责")
                print("   - 对于计算结果，用户应自行验证其正确性和适用性")
                
                print("\n3. 数据隐私：")
                print("   - 本软件完全在本地运行，不收集、不上传任何用户数据")
                print("   - 所有计算过程均在用户设备上完成，无网络传输(检查更新除外)")
                
                print("\n4. 其他条款：")
                print("   - 本软件选择性提供技术支持和维护承诺")
                print("   - 作者保留随时修改、终止提供软件的权利")
                print("   - 如有软件功能与法律法规冲突，以法律法规为准")
                
                print("\n5. 同意条款：")
                print("   - 继续使用本软件即表示您已阅读、理解并同意上述所有条款")
                print("   - 如不同意本协议，请立即停止使用并卸载本软件")
        except:
            pass
    elif choose == 8:
        exit()
    else:
        print("\033[31m注意：不要输错选择\033[0m")