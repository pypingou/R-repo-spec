%global packname  wild1
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.09
Release:          1%{?dist}
Summary:          R Tools for Wildlife Research and Management

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-chron R-survival R-sp R-maptools R-spatstat R-ICSNP R-ks 


BuildRequires:    R-devel tex(latex) R-chron R-survival R-sp R-maptools R-spatstat R-ICSNP R-ks



%description
Provides classes, methods, and examples for use in wildlife research and

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
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.09-1
- initial package for Fedora