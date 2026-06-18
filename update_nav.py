import os
base = r'C:\Users\emely\OneDrive\Documents\projects\UniBridge'
files = ['index.html', 'contact.html', 'Register.html', 'student-dashboard.html', 'lecturer-dashboard.html', 'admin-dashboard.html']

old = '<a href="signin.html"><i class="fas fa-sign-in-alt"></i> Sign In</a>'
new = '<a href="signin.html" class="signin-btn"><i class="fas fa-sign-in-alt"></i> Sign In</a>'

for f in files:
    path = os.path.join(base, f)
    content = open(path, encoding='utf-8').read()
    if 'signin-btn' not in content:
        content = content.replace(old, new)
        open(path, 'w', encoding='utf-8').write(content)
        print(f'Updated {f}')
    else:
        print(f'{f} already done')
