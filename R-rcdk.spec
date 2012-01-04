%global packname  rcdk
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.1.4
Release:          1%{?dist}
Summary:          rcdk - Interface to the CDK Libraries

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rJava R-rcdklibs R-fingerprint R-methods R-png R-iterators 

BuildRequires:    R-devel tex(latex) R-rJava R-rcdklibs R-fingerprint R-methods R-png R-iterators 

%description
This package allows the user to access functionality in the CDK, a Java
framework for cheminformatics. This allows the user to load molecules,
evaluate fingerprints, calculate molecular descriptors and so on. In
addition the CDK API allows the user to view structures in 2D.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.1.4-1
- initial package for Fedora