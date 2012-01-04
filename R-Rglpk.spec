%global packname  Rglpk
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          R/GNU Linear Programming Kit Interface

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-slam 

BuildRequires:    R-devel tex(latex) R-slam 

%description
R interface to the GNU Linear Programing Kit (GLPK version 4.42). GLPK is
open source software for solving large-scale linear programming (LP),
mixed integer linear programming (MILP) and other related problems.

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
%doc %{rlibdir}/Rglpk/DESCRIPTION
%doc %{rlibdir}/Rglpk/html
%{rlibdir}/Rglpk/R
%{rlibdir}/Rglpk/help
%{rlibdir}/Rglpk/INDEX
%{rlibdir}/Rglpk/Meta
%{rlibdir}/Rglpk/CHANGELOG
%{rlibdir}/Rglpk/NAMESPACE
%{rlibdir}/Rglpk/libs

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.5-1
- initial package for Fedora