%global packname  gee
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          4.13.17
Release:          1%{?dist}
Summary:          Generalized Estimation Equation solver

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.13-17.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Generalized Estimation Equation solver

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
%doc %{rlibdir}/gee/html
%doc %{rlibdir}/gee/DESCRIPTION
%{rlibdir}/gee/INDEX
%{rlibdir}/gee/help
%{rlibdir}/gee/NAMESPACE
%{rlibdir}/gee/R
%{rlibdir}/gee/Meta
%{rlibdir}/gee/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.13.17-1
- initial package for Fedora