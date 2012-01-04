%global packname  wccsom
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          SOM networks for comparing patterns with peak shifts

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-class R-MASS 

BuildRequires:    R-devel tex(latex) R-class R-MASS 

%description
SOM networks for comparing patterns with peak shifts.

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
%doc %{rlibdir}/wccsom/DESCRIPTION
%doc %{rlibdir}/wccsom/html
%{rlibdir}/wccsom/NAMESPACE
%{rlibdir}/wccsom/INDEX
%{rlibdir}/wccsom/Meta
%{rlibdir}/wccsom/R
%{rlibdir}/wccsom/help
%{rlibdir}/wccsom/libs
%{rlibdir}/wccsom/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.4-1
- initial package for Fedora