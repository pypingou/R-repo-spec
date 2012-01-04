%global packname  lifecontingencies
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.6
Release:          1%{?dist}
Summary:          Package to perform actuarial evaluation of life contingencies

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Financial and actuarial functions to evaluate life contingencies.

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
%doc %{rlibdir}/lifecontingencies/CITATION
%doc %{rlibdir}/lifecontingencies/doc
%doc %{rlibdir}/lifecontingencies/NEWS
%doc %{rlibdir}/lifecontingencies/DESCRIPTION
%doc %{rlibdir}/lifecontingencies/html
%{rlibdir}/lifecontingencies/INDEX
%{rlibdir}/lifecontingencies/NAMESPACE
%{rlibdir}/lifecontingencies/help
%{rlibdir}/lifecontingencies/data
%{rlibdir}/lifecontingencies/R
RPM build errors:
%{rlibdir}/lifecontingencies/Meta
%{rlibdir}/lifecontingencies/demo

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.6-1
- initial package for Fedora