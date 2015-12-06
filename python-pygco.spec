%global modname pygco

Name:           python-%{modname}
Version:        0.0.6
Release:        1%{?dist}
Summary:        Python wrappers for GCO alpha-expansion and alpha-beta-swaps

License:        BSD
URL:            https://pypi.python.org/pypi/pygco
Source0:        https://github.com/mjirik/gco_python/archive/%{version}/%{modname}-%{version}.tar.gz
Patch0:         0001-use-system-gco.patch

BuildRequires:  gco-devel

%description
Python wrappers for GCO alpha-expansion and alpha-beta-swaps. These wrappers
provide a high level interface for graph cut inference for multi-label
problems.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel Cython
%if 0%{?fedora} > 23
BuildRequires:  python2-numpy
Requires:       python2-numpy
%else
BuildRequires:  numpy
Requires:       numpy
%endif

%description -n python2-%{modname}
Python wrappers for GCO alpha-expansion and alpha-beta-swaps. These wrappers
provide a high level interface for graph cut inference for multi-label
problems.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-Cython
BuildRequires:  python3-numpy
Requires:       python3-numpy

%description -n python3-%{modname}
Python wrappers for GCO alpha-expansion and alpha-beta-swaps. These wrappers
provide a high level interface for graph cut inference for multi-label
problems.

Python 3 version.

%prep
%autosetup -n gco_python-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{modname}
%doc README.md example.py
%{python2_sitearch}/%{modname}*

%files -n python3-%{modname}
%doc README.md example.py
%{python3_sitearch}/%{modname}*

%changelog
* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.6-1
- Initial package
