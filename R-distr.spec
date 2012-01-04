%global packname  distr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.3.3
Release:          1%{?dist}
Summary:          Object oriented implementation of distributions

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-graphics R-startupmsg R-sfsmisc R-SweaveListingUtils 

BuildRequires:    R-devel tex(latex) R-methods R-graphics R-startupmsg R-sfsmisc R-SweaveListingUtils 

%description
S4 Classes and Methods for distributions

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.3-1
- initial package for Fedora