%global packname  LogicReg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.11
Release:          1%{?dist}
Summary:          Logic Regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Routines for Logic Regression

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/LogicReg/html
%doc %{rlibdir}/LogicReg/DESCRIPTION
%{rlibdir}/LogicReg/NAMESPACE
%{rlibdir}/LogicReg/libs
%{rlibdir}/LogicReg/Meta
%{rlibdir}/LogicReg/data
%{rlibdir}/LogicReg/INDEX
%{rlibdir}/LogicReg/R
%{rlibdir}/LogicReg/help
%{rlibdir}/LogicReg/condlogic.ff

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.11-1
- initial package for Fedora