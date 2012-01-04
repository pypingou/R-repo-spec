%global packname  DWD
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.10
Release:          1%{?dist}
Summary:          DWD implementation based on A IPM SOCP solver

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Matrix R-methods 

BuildRequires:    R-devel tex(latex) R-Matrix R-methods 

%description
This package provides the implementation of distance weighted
discrimination (DWD) using an interior point method for the solution of
second order cone programming problems, originally described by K.C. Toh,
M.J. Todd, R.H. Tutuncu (1999).

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
%doc %{rlibdir}/DWD/DESCRIPTION
%doc %{rlibdir}/DWD/doc
%doc %{rlibdir}/DWD/html
%{rlibdir}/DWD/INDEX
%{rlibdir}/DWD/help
%{rlibdir}/DWD/NAMESPACE
%{rlibdir}/DWD/R
%{rlibdir}/DWD/Meta
%{rlibdir}/DWD/data
%{rlibdir}/DWD/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.10-1
- initial package for Fedora