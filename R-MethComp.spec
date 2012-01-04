%global packname  MethComp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Functions for analysis of method comparison studies.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-nlme 

BuildRequires:    R-devel tex(latex) R-nlme 

%description
Methods (standard and advanced) for comparison of measurement methods.

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
%doc %{rlibdir}/MethComp/html
%doc %{rlibdir}/MethComp/doc
%doc %{rlibdir}/MethComp/DESCRIPTION
%{rlibdir}/MethComp/R
%{rlibdir}/MethComp/NAMESPACE
%{rlibdir}/MethComp/INDEX
%{rlibdir}/MethComp/Meta
%{rlibdir}/MethComp/data
%{rlibdir}/MethComp/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora